from fastapi import APIRouter

router = APIRouter()

@router.get('/api/docs')
def read_docs():
    return {
        'message': 'API documentation'
    }


@router.post('/api/{process_name}', name='start')
def start_proc(process_name: str):
    return {
        'message': 'process started'
    }


@router.post('/api/{process_name}', name='stop')
def stop_proc(process_name: str):
    return {
        'message': 'process stopped'
    }


@router.get('/api/{process_name}')
def get_status(process_name: str):
    return {
        'status': 'running'
    }


@router.get('/api/{process_name}/result')
def get_result(process_name: str):
    return {
        'result': 'some result'
    }