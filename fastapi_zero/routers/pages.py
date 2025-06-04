# fastapi_zero/routers/pages.py
from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()


# Templates
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {'request': request, 'title': 'FastAPI Zero', 'message': 'Olá Mundo!'},
    )


@router.get('/dashboard', response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
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


@router.get('/login', response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse(
        'login.html',
        {
            'request': request,
            'message': 'Faça login para acessar o sistema',
            'description': 'Entre com seu usuário e senha',
        },
    )


@router.post('/login', response_class=HTMLResponse)
async def login(request: Request):
    form_data = await request.form()
    username = form_data.get('username')
    password = form_data.get('password')

    if username == 'admin' and password == 'fastapizero':
        return templates.TemplateResponse(
            'index.html',
            {
                'request': request,
                'message': 'Login bem-sucedido!',
                'description': 'Você está logado no sistema',
            },
        )
    else:
        return templates.TemplateResponse(
            'login.html',
            {
                'request': request,
                'message': 'Credenciais inválidas. Tente novamente.',
                'description': 'Faça login para acessar o sistema',
            },
        )


@router.get('/logout', response_class=HTMLResponse)
async def logout(request: Request):
    return templates.TemplateResponse(
        'logout.html',
        {
            'request': request,
            'message': 'Você está saindo do sistema',
            'description': 'Obrigado por utilizar o FastAPI Zero',
        },
    )


@router.post('/create_user', response_class=HTMLResponse)
async def create_user(request: Request):
    return templates.TemplateResponse(
        'create_user.html',
        {
            'request': request,
            'message': 'Criar Novo Usuário',
            'description': 'Preencha os dados para criar um novo usuário',
        },
    )


@router.get('/listar_usuarios', response_class=HTMLResponse)
async def listar_usuarios(request: Request):
    return templates.TemplateResponse(
        'listar_usuarios.html',
        {
            'request': request,
            'message': 'Lista de Usuários',
            'description': 'Visualize todos os usuários cadastrados no sistema',
            'users': [
                {'username': 'admin', 'role': 'admin', 'email': 'admin@example.com'},
                {'username': 'user', 'role': 'user', 'email': 'user@example.com'},
            ],
        },
    )


@router.get('/editar_usuario/{username}', response_class=HTMLResponse)
async def editar_usuario(request: Request, username: str):
    return templates.TemplateResponse(
        'editar_usuario.html',
        {
            'request': request,
            'message': f'Editar Usuário: {username}',
            'description': 'Altere os dados do usuário',
            'username': username,
        },
    )


@router.get('/deletar_usuario/{username}', response_class=HTMLResponse)
async def deletar_usuario(request: Request, username: str):
    return templates.TemplateResponse(
        'deletar_usuario.html',
        {
            'request': request,
            'message': f'Deletar Usuário: {username}',
            'description': 'Confirme a exclusão do usuário',
            'username': username,
        },
    )


@router.get('/consultar_usuario/{username}', response_class=HTMLResponse)
async def consultar_usuario(request: Request, username: str):
    return templates.TemplateResponse(
        'consultar_usuario.html',
        {
            'request': request,
            'message': f'Consultar Usuário: {username}',
            'description': 'Veja os detalhes do usuário',
            'username': username,
            'user_details': {
                'username': username,
                'role': 'user',
                'email': 'user@example.com',
                'created_at': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'last_login': datetime.now().strftime('%d/%m/%Y %H:%M'),
            },
        },
    )
