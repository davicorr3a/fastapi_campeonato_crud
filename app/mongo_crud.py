# app/mongo_crud.py
from pymongo import MongoClient

# Conexão básica com MongoDB local

def conectar_mongo():
    client = MongoClient("connectionString")
    db = client["Client"]
    return db

# ------------------- CRUD LIGA -------------------
def inserir_liga_mongo(nome, divisao):
    db = conectar_mongo()
    return db.ligas.insert_one({"nome": nome, "divisao": divisao})

def listar_ligas_mongo():
    db = conectar_mongo()
    return list(db.ligas.find())

def buscar_liga_mongo(id_str):
    db = conectar_mongo()
    return db.ligas.find_one({"_id": ObjectId(id_str)})

def atualizar_liga_mongo(id_str, nome, divisao):
    db = conectar_mongo()
    return db.ligas.update_one(
        {"_id": ObjectId(id_str)},
        {"$set": {"nome": nome, "divisao": divisao}}
    )

def deletar_liga_mongo(id_str):
    db = conectar_mongo()
    return db.ligas.delete_one({"_id": ObjectId(id_str)})

# ------------------- CRUD TIME -------------------
def inserir_time_mongo(nome, nome_time, temporada, categoria, total_jogadores, liga_nome):
    db = conectar_mongo()
    return db.times.insert_one({
        "nome": nome,
        "nome_time": nome_time,
        "temporada": temporada,
        "categoria": categoria,
        "total_jogadores": total_jogadores,
        "liga_nome": liga_nome
    })

def listar_times_mongo():
    db = conectar_mongo()
    return list(db.times.find())

def buscar_time_mongo(id_str):
    db = conectar_mongo()
    return db.times.find_one({"_id": ObjectId(id_str)})

def atualizar_time_mongo(id_str, nome, nome_time, temporada, categoria, total_jogadores, liga_nome):
    db = conectar_mongo()
    return db.times.update_one(
        {"_id": ObjectId(id_str)},
        {"$set": {
            "nome": nome,
            "nome_time": nome_time,
            "temporada": temporada,
            "categoria": categoria,
            "total_jogadores": total_jogadores,
            "liga_nome": liga_nome
        }}
    )

def deletar_time_mongo(id_str):
    db = conectar_mongo()
    return db.times.delete_one({"_id": ObjectId(id_str)})

# ------------------- CRUD ESTADIO -------------------
def inserir_estadio_mongo(nome, localizacao, capacidade, tipo_de_gramado, patrocinadores):
    db = conectar_mongo()
    return db.estadios.insert_one({
        "nome": nome,
        "localizacao": localizacao,
        "capacidade": capacidade,
        "tipo_de_gramado": tipo_de_gramado,
        "patrocinadores": patrocinadores
    })

def listar_estadios_mongo():
    db = conectar_mongo()
    return list(db.estadios.find())

def buscar_estadio_mongo(id_str):
    db = conectar_mongo()
    return db.estadios.find_one({"_id": ObjectId(id_str)})

def atualizar_estadio_mongo(id_str, nome, localizacao, capacidade, tipo_de_gramado, patrocinadores):
    db = conectar_mongo()
    return db.estadios.update_one(
        {"_id": ObjectId(id_str)},
        {"$set": {
            "nome": nome,
            "localizacao": localizacao,
            "capacidade": capacidade,
            "tipo_de_gramado": tipo_de_gramado,
            "patrocinadores": patrocinadores
        }}
    )

def deletar_estadio_mongo(id_str):
    db = conectar_mongo()
    return db.estadios.delete_one({"_id": ObjectId(id_str)})

# ------------------- CRUD PARTIDA -------------------
def inserir_partida_mongo(codigo, data, horario, estadio_nome, time_casa_nome, time_visitante_nome):
    db = conectar_mongo()
    return db.partidas.insert_one({
        "codigo": codigo,
        "data": data,
        "horario": horario,
        "estadio_nome": estadio_nome,
        "time_casa_nome": time_casa_nome,
        "time_visitante_nome": time_visitante_nome
    })

def listar_partidas_mongo():
    db = conectar_mongo()
    return list(db.partidas.find())

def buscar_partida_mongo(id_str):
    db = conectar_mongo()
    return db.partidas.find_one({"_id": ObjectId(id_str)})

def atualizar_partida_mongo(id_str, codigo, data, horario, estadio_nome, time_casa_nome, time_visitante_nome):
    db = conectar_mongo()
    return db.partidas.update_one(
        {"_id": ObjectId(id_str)},
        {"$set": {
            "codigo": codigo,
            "data": data,
            "horario": horario,
            "estadio_nome": estadio_nome,
            "time_casa_nome": time_casa_nome,
            "time_visitante_nome": time_visitante_nome
        }}
    )

def deletar_partida_mongo(id_str):
    db = conectar_mongo()
    return db.partidas.delete_one({"_id": ObjectId(id_str)})
