import time
import os
import threading
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    time.sleep(5)
    process_id = os.getpid()
    thread_id = threading.get_ident()
    return {"message": "Hello, World!", "process_id": process_id, "thread_id": thread_id}
@app.get('/health')
def health():
    return {'message': 'I am working'}
    
