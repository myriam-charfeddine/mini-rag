from fastapi import FastAPI
# from dotenv import load_dotenv
# load_dotenv(".env")
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup the db when the app is launched
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)  # Connect to MongoDB  (we associated the connection to the app : app.mongo_db (.mongo_db is not an already existing attribute))
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]  # Access the database (we associated the db to the app : app.db_client (.db_client is not an already existing attribute))
    print("Database connected.")

    yield  # Pass control to the app

    #shutdown the db once app closed
    app.mongo_conn.close()
    print("Database connection closed.")

app = FastAPI(lifespan=lifespan)


# #startup the db when the app is launched
# @app.on_event("startup")
# async def startup_db_client():
#     settings = get_settings()
#     app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL) #connect to MONGODB
#     app.db_client = app.mongo_conn[settings.MONGODB_DATABASE] #access the db in question

# #shutdown the db once app closed
# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongo_conn.close()



app.include_router(base.base_router)
app.include_router(data.data_router)

