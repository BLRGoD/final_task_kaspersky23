from fastapi import FastAPI
from app.main import app



@app.get('/api/docs')
def read_docs():
    return {
        'message': 'API documentation'
    }


@app.post('/api/{process_name}', name='start')
def start_proc(process_name: str):
    return {
        'message': 'process started'
    }


@app.post('/api/{process_name}', name='stop')
def stop_proc(process_name: str):
    return {
        'message': 'process stopped'
    }


@app.get('/api/{process_name}')
def get_status(process_name: str):
    return {
        'status': 'running'
    }


@app.get('/api/{process_name}/result')
def get_result(process_name: str):
    return {
        'result': 'some result'
    }