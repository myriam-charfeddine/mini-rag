from fastapi import FastAPI
# from dotenv import load_dotenv
# load_dotenv(".env")
from routes import base, data, nlp
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from contextlib import asynccontextmanager
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory



@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup the db when the app is launched
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)  # Connect to MongoDB  (we associated the connection to the app : app.mongo_db (.mongo_db is not an already existing attribute))
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]  # Access the database (we associated the db to the app : app.db_client (.db_client is not an already existing attribute))
    print("Database connected.")
    
    llm_provider_factory = LLMProviderFactory(settings)
    vectordb_provider_factory = VectorDBProviderFactory(settings)

    # defining the app attribute : generation client
    app.generation_client = llm_provider_factory.create(provider = settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)

    # defining the app attribute : embedding client
    app.embedding_client = llm_provider_factory.create(provider = settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)
    
    # vector db client
    app.vectordb_client = vectordb_provider_factory.create(provider=settings.VECTOR_DB_BACKEND)
    
    # connect to vector db
    app.vectordb_client.connect()

    yield  # Pass control to the app...

    #shutdown the db once app closed
    app.mongo_conn.close()
    print("Database connection closed.")

    # disconnect from vector db
    app.vectordb_client.disconnect()

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
app.include_router(nlp.nlp_router)

