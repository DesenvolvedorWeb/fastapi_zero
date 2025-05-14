# fastapi_zero/app.py
from datetime import datetime
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader, select_autoescape

from fastapi_zero.schemas import Message

# Use FileSystemLoader em vez de PackageLoader
env = Environment(loader=FileSystemLoader('templates'), autoescape=select_autoescape())

app = FastAPI(title='FastAPI Zero')

# Montar arquivos estáticos
app.mount('/static', StaticFiles(directory='static'), name='static')

# Mantenha esta linha como está
Templates = Jinja2Templates(directory='templates')
template = env.get_template('index.html')


@app.get(
    '/',
    response_class=HTMLResponse,
    response_model=Message,
    status_code=HTTPStatus.OK,
)
async def read_root(request: Request):
    # passa o objeto request e outras variáveis para o template
    return Templates.TemplateResponse(
        'index.html', {'request': request, 'message': 'Olá Mundo!'}
    )


@app.get(
    '/dashboard',
    response_class=HTMLResponse,
)
async def dashboard(request: Request):
    return Templates.TemplateResponse(
        'dashboard.html',
        {
            'request': request,
            'message': 'Bem-vindo ao Dashboard!',
            'description': 'Visualize estatísticas e informações do sistema',
            'stats': {'users': 1250, 'active': 847, 'requests': 12345},
            'version': '0.1.0',
            'environment': 'Development',
            'current_date': datetime.now().strftime('%d/%m/%Y %H:%M'),
        },
    )


@app.get(
    '/api/stats',
    status_code=HTTPStatus.OK,
)
async def api_stats():
    """Retorna estatísticas do sistema em formato JSON."""
    return {
        'success': True,
        'data': {
            'users': 1250,
            'active': 847,
            'requests': 12345
        }
    }
