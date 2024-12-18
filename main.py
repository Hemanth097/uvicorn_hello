import time
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    time.sleep(5)
    return {'message': 'Hello, World!'}"
@app.get('/health')
def read_root():
    return {'message': 'I am working'}"
