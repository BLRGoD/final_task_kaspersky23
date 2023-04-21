from fastapi import FastAPI

app = FastAPI()


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
