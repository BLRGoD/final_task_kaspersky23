from fastapi import APIRouter
from app.process import proc
from multiprocessing import Process

router = APIRouter()
process = Process(target=proc)


@router.get('/api/docs', name='documentation')
def read_docs():
    return {
        'message': 'API documentation'
    }


@router.post('/api/{process_name}/start', name='start')
def start_proc(process_name: str):
    if process_name == 'process':
        process.start()
        return {
            'message': 'process started'
        }
    else:
        return {
            'message': 'process not found'
        }


@router.post('/api/{process_name}/stop', name='stop')
def stop_proc(process_name: str):
    if process_name == 'process':
        process.terminate()
        return {
            'message': 'process terminated'
        }
    else:
        return {
            'message': 'process not found'
        }


@router.get('/api/{process_name}', name='status')
def get_status(process_name: str):
    return {
        'status': 'running'
    }


@router.get('/api/{process_name}/result', name='result')
def get_result(process_name: str):
    return {
        'result': 'some result'
    }