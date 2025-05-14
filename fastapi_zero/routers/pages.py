
# fastapi_zero/routers/pages.py
from datetime import datetime
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Templates
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "FastAPI Zero", "message": "Olá Mundo!"}
    )

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "message": "Bem-vindo ao Dashboard!",
            "description": "Visualize estatísticas e informações do sistema",
            "stats": {"users": 1250, "active": 847, "requests": 12345},
            "version": "0.1.0",
            "environment": "Development",
            "current_date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        },
    )

# Adicione outras rotas de páginas conforme necessário

