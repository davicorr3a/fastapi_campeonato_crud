# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.postgres_crud import *

from app.mongo_crud import (
    listar_ligas_mongo, inserir_liga_mongo, buscar_liga_mongo,
    atualizar_liga_mongo, deletar_liga_mongo,
    listar_times_mongo, inserir_time_mongo, buscar_time_mongo,
    atualizar_time_mongo, deletar_time_mongo,
    listar_estadios_mongo, inserir_estadio_mongo, buscar_estadio_mongo,
    atualizar_estadio_mongo, deletar_estadio_mongo,
    listar_partidas_mongo, inserir_partida_mongo, buscar_partida_mongo,
    atualizar_partida_mongo, deletar_partida_mongo
)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/assets"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---------------------- LIGA ----------------------
@app.get("/ligas", response_class=HTMLResponse)
def listar_ligas(request: Request):
    ligas = listar_ligas_pg()
    return templates.TemplateResponse("ligas/listar.html", {"request": request, "ligas": ligas})

@app.get("/ligas/novo", response_class=HTMLResponse)
def form_nova_liga(request: Request):
    return templates.TemplateResponse("ligas/form.html", {"request": request})

@app.post("/ligas/novo")
def criar_liga(nome: str = Form(...), divisao: str = Form(...)):
    criar_liga_pg(nome, divisao)
    return RedirectResponse("/ligas", status_code=303)

@app.get("/ligas/deletar/{liga_id}")
def deletar_liga(liga_id: int):
    deletar_liga_pg(liga_id)
    return RedirectResponse("/ligas", status_code=303)

@app.get("/ligas/editar/{liga_id}", response_class=HTMLResponse)
def editar_liga_form(request: Request, liga_id: int):
    liga = buscar_liga_pg(liga_id)
    return templates.TemplateResponse("ligas/form.html", {"request": request, "liga": liga})

@app.post("/ligas/editar/{liga_id}")
def atualizar_liga(liga_id: int, nome: str = Form(...), divisao: str = Form(...)):
    atualizar_liga_pg(liga_id, nome, divisao)
    return RedirectResponse("/ligas", status_code=303)

# ---------------------- TIME ----------------------
@app.get("/times", response_class=HTMLResponse)
def listar_times(request: Request):
    times = listar_times_pg()
    return templates.TemplateResponse("times/listar.html", {"request": request, "times": times})

@app.get("/times/novo", response_class=HTMLResponse)
def form_novo_time(request: Request):
    ligas = listar_ligas_pg()
    return templates.TemplateResponse("times/form.html", {"request": request, "ligas": ligas})

@app.post("/times/novo")
def criar_time(
    nome: str = Form(...),
    nome_time: str = Form(...),
    temporada: str = Form(...),
    categoria: str = Form(...),
    total_jogadores: int = Form(...),
    liga_id: int = Form(...)
):
    criar_time_pg(nome, nome_time, temporada, categoria, total_jogadores, liga_id)
    return RedirectResponse("/times", status_code=303)

@app.get("/times/deletar/{time_id}")
def deletar_time(time_id: int):
    deletar_time_pg(time_id)
    return RedirectResponse("/times", status_code=303)

@app.get("/times/editar/{time_id}", response_class=HTMLResponse)
def editar_time_form(request: Request, time_id: int):
    time = buscar_time_pg(time_id)
    ligas = listar_ligas_pg()
    return templates.TemplateResponse("times/form.html", {"request": request, "time": time, "ligas": ligas})

@app.post("/times/editar/{time_id}")
def atualizar_time(
    time_id: int,
    nome: str = Form(...),
    nome_time: str = Form(...),
    temporada: str = Form(...),
    categoria: str = Form(...),
    total_jogadores: int = Form(...),
    liga_id: int = Form(...)
):
    atualizar_time_pg(time_id, nome, nome_time, temporada, categoria, total_jogadores, liga_id)
    return RedirectResponse("/times", status_code=303)

# ---------------------- ESTADIO ----------------------
@app.get("/estadios", response_class=HTMLResponse)
def listar_estadios(request: Request):
    estadios = listar_estadios_pg()
    return templates.TemplateResponse("estadios/listar.html", {"request": request, "estadios": estadios})

@app.get("/estadios/novo", response_class=HTMLResponse)
def form_novo_estadio(request: Request):
    return templates.TemplateResponse("estadios/form.html", {"request": request})

@app.post("/estadios/novo")
def criar_estadio(
    nome: str = Form(...),
    localizacao: str = Form(...),
    capacidade: int = Form(...),
    tipo_de_gramado: str = Form(...),
    patrocinadores: str = Form(...)
):
    criar_estadio_pg(nome, localizacao, capacidade, tipo_de_gramado, patrocinadores)
    return RedirectResponse("/estadios", status_code=303)

@app.get("/estadios/deletar/{estadio_id}")
def deletar_estadio(estadio_id: int):
    deletar_estadio_pg(estadio_id)
    return RedirectResponse("/estadios", status_code=303)

@app.get("/estadios/editar/{estadio_id}", response_class=HTMLResponse)
def editar_estadio_form(request: Request, estadio_id: int):
    estadio = buscar_estadio_pg(estadio_id)
    return templates.TemplateResponse("estadios/form.html", {"request": request, "estadio": estadio})

@app.post("/estadios/editar/{estadio_id}")
def atualizar_estadio(
    estadio_id: int,
    nome: str = Form(...),
    localizacao: str = Form(...),
    capacidade: int = Form(...),
    tipo_de_gramado: str = Form(...),
    patrocinadores: str = Form(...)
):
    atualizar_estadio_pg(estadio_id, nome, localizacao, capacidade, tipo_de_gramado, patrocinadores)
    return RedirectResponse("/estadios", status_code=303)

# ---------------------- PARTIDAS ----------------------
@app.get("/partidas", response_class=HTMLResponse)
def listar_partidas(request: Request):
    partidas = listar_partidas_pg()
    return templates.TemplateResponse("partidas/listar.html", {"request": request, "partidas": partidas})

@app.get("/partidas/novo", response_class=HTMLResponse)
def form_nova_partida(request: Request):
    estadios = listar_estadios_pg()
    times = listar_times_pg()
    return templates.TemplateResponse("partidas/form.html", {"request": request, "estadios": estadios, "times": times})

@app.post("/partidas/novo")
def criar_partida(
    codigo: str = Form(...),
    data: str = Form(...),
    horario: str = Form(...),
    estadio_id: int = Form(...),
    time_casa_id: int = Form(...),
    time_visitante_id: int = Form(...)
):
    criar_partida_pg(codigo, data, horario, estadio_id, time_casa_id, time_visitante_id)
    return RedirectResponse("/partidas", status_code=303)

@app.get("/partidas/deletar/{partida_id}")
def deletar_partida(partida_id: int):
    deletar_partida_pg(partida_id)
    return RedirectResponse("/partidas", status_code=303)

@app.get("/partidas/editar/{partida_id}", response_class=HTMLResponse)
def editar_partida_form(request: Request, partida_id: int):
    partida = buscar_partida_pg(partida_id)
    estadios = listar_estadios_pg()
    times = listar_times_pg()
    return templates.TemplateResponse("partidas/form.html", {"request": request, "partida": partida, "estadios": estadios, "times": times})

@app.post("/partidas/editar/{partida_id}")
def atualizar_partida(
    partida_id: int,
    codigo: str = Form(...),
    data: str = Form(...),
    horario: str = Form(...),
    estadio_id: int = Form(...),
    time_casa_id: int = Form(...),
    time_visitante_id: int = Form(...)
):
    atualizar_partida_pg(partida_id, codigo, data, horario, estadio_id, time_casa_id, time_visitante_id)
    return RedirectResponse("/partidas", status_code=303)

@app.get("/relacional", response_class=HTMLResponse)
def relacional_menu(request: Request):
    return templates.TemplateResponse("relacional.html", {"request": request})

@app.get("/nao_relacional", response_class=HTMLResponse)
def nao_relacional_menu(request: Request):
    return templates.TemplateResponse("nao_relacional.html", {"request": request})

#Parte não relacional
# -------------------- LIGAS --------------------
@app.get("/ligas_mongo", response_class=HTMLResponse)
def listar_ligas_mongo_view(request: Request):
    try:
        ligas = listar_ligas_mongo()
        return templates.TemplateResponse("ligas_mongo/listar.html", {"request": request, "ligas": ligas})
    except Exception as e:
        return HTMLResponse(f"<h1>Erro ao carregar ligas</h1><pre>{e}</pre>", status_code=500)

@app.get("/ligas_mongo/novo", response_class=HTMLResponse)
def form_nova_liga(request: Request):
    return templates.TemplateResponse("ligas_mongo/form.html", {"request": request})

@app.post("/ligas_mongo/novo")
def criar_liga(nome: str = Form(...), divisao: str = Form(...)):
    inserir_liga_mongo(nome, divisao)
    return RedirectResponse("/ligas_mongo", status_code=303)

@app.get("/ligas_mongo/deletar/{liga_id}")
def deletar_liga(liga_id: str):
    deletar_liga_mongo(liga_id)
    return RedirectResponse("/ligas_mongo", status_code=303)

@app.get("/ligas_mongo/editar/{liga_id}", response_class=HTMLResponse)
def editar_liga_form(request: Request, liga_id: str):
    liga = buscar_liga_mongo(liga_id)
    return templates.TemplateResponse("ligas_mongo/form.html", {"request": request, "liga": liga})

@app.post("/ligas_mongo/editar/{liga_id}")
def atualizar_liga(liga_id: str, nome: str = Form(...), divisao: str = Form(...)):
    atualizar_liga_mongo(liga_id, nome, divisao)
    return RedirectResponse("/ligas_mongo", status_code=303)

# -------------------- TIMES --------------------
@app.get("/times_mongo", response_class=HTMLResponse)
def listar_times_mongo_view(request: Request):
    times = listar_times_mongo()
    return templates.TemplateResponse("times_mongo/listar.html", {"request": request, "times": times})

@app.get("/times_mongo/novo", response_class=HTMLResponse)
def form_novo_time(request: Request):
    ligas = listar_ligas_mongo()
    return templates.TemplateResponse("times_mongo/form.html", {"request": request, "ligas": ligas})

@app.post("/times_mongo/novo")
def criar_time(
    nome: str = Form(...), nome_time: str = Form(...), temporada: str = Form(...),
    categoria: str = Form(...), total_jogadores: int = Form(...), liga_nome: str = Form(...)
):
    inserir_time_mongo(nome, nome_time, temporada, categoria, total_jogadores, liga_nome)
    return RedirectResponse("/times_mongo", status_code=303)

@app.get("/times_mongo/deletar/{time_id}")
def deletar_time(time_id: str):
    deletar_time_mongo(time_id)
    return RedirectResponse("/times_mongo", status_code=303)

@app.get("/times_mongo/editar/{time_id}", response_class=HTMLResponse)
def editar_time_form(request: Request, time_id: str):
    time = buscar_time_mongo(time_id)
    ligas = listar_ligas_mongo()
    return templates.TemplateResponse("times_mongo/form.html", {"request": request, "time": time, "ligas": ligas})

@app.post("/times_mongo/editar/{time_id}")
def atualizar_time(
    time_id: str,
    nome: str = Form(...), nome_time: str = Form(...), temporada: str = Form(...),
    categoria: str = Form(...), total_jogadores: int = Form(...), liga_nome: str = Form(...)
):
    atualizar_time_mongo(time_id, nome, nome_time, temporada, categoria, total_jogadores, liga_nome)
    return RedirectResponse("/times_mongo", status_code=303)

# -------------------- ESTÁDIOS --------------------
@app.get("/estadios_mongo", response_class=HTMLResponse)
def listar_estadios_mongo_view(request: Request):
    estadios = listar_estadios_mongo()
    return templates.TemplateResponse("estadios_mongo/listar.html", {"request": request, "estadios": estadios})

@app.get("/estadios_mongo/novo", response_class=HTMLResponse)
def form_novo_estadio(request: Request):
    return templates.TemplateResponse("estadios_mongo/form.html", {"request": request})

@app.post("/estadios_mongo/novo")
def criar_estadio(
    nome: str = Form(...), localizacao: str = Form(...), capacidade: int = Form(...),
    tipo_de_gramado: str = Form(...), patrocinadores: str = Form(...)
):
    inserir_estadio_mongo(nome, localizacao, capacidade, tipo_de_gramado, patrocinadores)
    return RedirectResponse("/estadios_mongo", status_code=303)

@app.get("/estadios_mongo/deletar/{estadio_id}")
def deletar_estadio(estadio_id: str):
    deletar_estadio_mongo(estadio_id)
    return RedirectResponse("/estadios_mongo", status_code=303)

@app.get("/estadios_mongo/editar/{estadio_id}", response_class=HTMLResponse)
def editar_estadio_form(request: Request, estadio_id: str):
    estadio = buscar_estadio_mongo(estadio_id)
    return templates.TemplateResponse("estadios_mongo/form.html", {"request": request, "estadio": estadio})

@app.post("/estadios_mongo/editar/{estadio_id}")
def atualizar_estadio(
    estadio_id: str,
    nome: str = Form(...), localizacao: str = Form(...), capacidade: int = Form(...),
    tipo_de_gramado: str = Form(...), patrocinadores: str = Form(...)
):
    atualizar_estadio_mongo(estadio_id, nome, localizacao, capacidade, tipo_de_gramado, patrocinadores)
    return RedirectResponse("/estadios_mongo", status_code=303)

# -------------------- PARTIDAS --------------------
@app.get("/partidas_mongo", response_class=HTMLResponse)
def listar_partidas_mongo_view(request: Request):
    partidas = listar_partidas_mongo()
    return templates.TemplateResponse("partidas_mongo/listar.html", {"request": request, "partidas": partidas})

@app.get("/partidas_mongo/novo", response_class=HTMLResponse)
def form_nova_partida(request: Request):
    estadios = listar_estadios_mongo()
    times = listar_times_mongo()
    return templates.TemplateResponse("partidas_mongo/form.html", {"request": request, "estadios": estadios, "times": times})

@app.post("/partidas_mongo/novo")
def criar_partida(
    codigo: str = Form(...), data: str = Form(...), horario: str = Form(...),
    estadio_nome: str = Form(...), time_casa_nome: str = Form(...), time_visitante_nome: str = Form(...)
):
    inserir_partida_mongo(codigo, data, horario, estadio_nome, time_casa_nome, time_visitante_nome)
    return RedirectResponse("/partidas_mongo", status_code=303)

@app.get("/partidas_mongo/deletar/{partida_id}")
def deletar_partida(partida_id: str):
    deletar_partida_mongo(partida_id)
    return RedirectResponse("/partidas_mongo", status_code=303)

@app.get("/partidas_mongo/editar/{partida_id}", response_class=HTMLResponse)
def editar_partida_form(request: Request, partida_id: str):
    partida = buscar_partida_mongo(partida_id)
    estadios = listar_estadios_mongo()
    times = listar_times_mongo()
    return templates.TemplateResponse("partidas_mongo/form.html", {"request": request, "partida": partida, "estadios": estadios, "times": times})

@app.post("/partidas_mongo/editar/{partida_id}")
def atualizar_partida(
    partida_id: str,
    codigo: str = Form(...), data: str = Form(...), horario: str = Form(...),
    estadio_nome: str = Form(...), time_casa_nome: str = Form(...), time_visitante_nome: str = Form(...)
):
    atualizar_partida_mongo(partida_id, codigo, data, horario, estadio_nome, time_casa_nome, time_visitante_nome)
    return RedirectResponse("/partidas_mongo", status_code=303)
