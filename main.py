from fastapi import FastAPI
app = FastAPI()

def hi():
    return(
        'message': 'hello world!'
    )