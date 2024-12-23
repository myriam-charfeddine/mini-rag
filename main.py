from fastapi import FastAPI
app = FastAPI()

#uvicorn main:app --reload --host 0.0.0.0 --port 5000

@app.get('/hi')
def hi():
    return{
        'message': 'hello world!'
    }