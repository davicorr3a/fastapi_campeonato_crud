# app/postgres_crud.py
import psycopg2
from psycopg2.extras import RealDictCursor

def conectar_pg():
    return psycopg2.connect(
        host="seuhost",      
        port=porta,
        database="database",
        user="user",
        password="password"
    )

# ------------------- CRUD LIGA -------------------

def listar_ligas_pg():
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM campeonato.Liga ORDER BY id")
    ligas = cur.fetchall()
    conn.close()
    return ligas

def criar_liga_pg(nome, divisao):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("INSERT INTO campeonato.Liga (nome, divisao) VALUES (%s, %s)", (nome, divisao))
    conn.commit()
    conn.close()

def deletar_liga_pg(liga_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("DELETE FROM campeonato.Liga WHERE id = %s", (liga_id,))
    conn.commit()
    conn.close()

def buscar_liga_pg(liga_id):
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM campeonato.Liga WHERE id = %s", (liga_id,))
    liga = cur.fetchone()
    conn.close()
    return liga

def atualizar_liga_pg(liga_id, nome, divisao):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("UPDATE campeonato.Liga SET nome = %s, divisao = %s WHERE id = %s", (nome, divisao, liga_id))
    conn.commit()
    conn.close()

# ------------ TIME -------------
def listar_times_pg():
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT t.*, l.nome AS liga_nome 
        FROM campeonato.Time t
        LEFT JOIN campeonato.Liga l ON t.liga_id = l.id
        ORDER BY t.id
    """)
    times = cur.fetchall()
    conn.close()
    return times

def criar_time_pg(nome, nome_time, temporada, categoria, total_jogadores, liga_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO campeonato.Time (nome, nome_time, temporada, categoria, total_jogadores, liga_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nome, nome_time, temporada, categoria, total_jogadores, liga_id))
    conn.commit()
    conn.close()

def deletar_time_pg(time_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("DELETE FROM campeonato.Time WHERE id = %s", (time_id,))
    conn.commit()
    conn.close()

def buscar_time_pg(time_id):
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM campeonato.Time WHERE id = %s", (time_id,))
    time = cur.fetchone()
    conn.close()
    return time

def atualizar_time_pg(time_id, nome, nome_time, temporada, categoria, total_jogadores, liga_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("""
        UPDATE campeonato.Time 
        SET nome = %s, nome_time = %s, temporada = %s, categoria = %s, total_jogadores = %s, liga_id = %s
        WHERE id = %s
    """, (nome, nome_time, temporada, categoria, total_jogadores, liga_id, time_id))
    conn.commit()
    conn.close()

# ------------ ESTADIO -------------
def listar_estadios_pg():
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM campeonato.Estadio ORDER BY id")
    dados = cur.fetchall()
    conn.close()
    return dados

def criar_estadio_pg(nome, localizacao, capacidade, tipo_de_gramado, patrocinadores):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO campeonato.Estadio (nome, localizacao, capacidade, tipo_de_gramado, patrocinadores)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, localizacao, capacidade, tipo_de_gramado, patrocinadores))
    conn.commit()
    conn.close()

def deletar_estadio_pg(estadio_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("DELETE FROM campeonato.Estadio WHERE id = %s", (estadio_id,))
    conn.commit()
    conn.close()

def buscar_estadio_pg(estadio_id):
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM campeonato.Estadio WHERE id = %s", (estadio_id,))
    dados = cur.fetchone()
    conn.close()
    return dados

def atualizar_estadio_pg(estadio_id, nome, localizacao, capacidade, tipo_de_gramado, patrocinadores):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("""
        UPDATE campeonato.Estadio
        SET nome = %s, localizacao = %s, capacidade = %s, tipo_de_gramado = %s, patrocinadores = %s
        WHERE id = %s
    """, (nome, localizacao, capacidade, tipo_de_gramado, patrocinadores, estadio_id))
    conn.commit()
    conn.close()

# ------------ PARTIDAS -------------
def listar_partidas_pg():
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT p.*, 
               e.nome AS estadio_nome,
               tc.nome_time AS time_casa_nome,
               tv.nome_time AS time_visitante_nome
        FROM campeonato.Partidas p
        LEFT JOIN campeonato.Estadio e ON p.estadio_id = e.id
        LEFT JOIN campeonato.Time tc ON p.time_casa_id = tc.id
        LEFT JOIN campeonato.Time tv ON p.time_visitante_id = tv.id
        ORDER BY p.id
    """)
    dados = cur.fetchall()
    conn.close()
    return dados

def criar_partida_pg(codigo, data, horario, estadio_id, time_casa_id, time_visitante_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO campeonato.Partidas (codigo, data, horario, estadio_id, time_casa_id, time_visitante_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (codigo, data, horario, estadio_id, time_casa_id, time_visitante_id))
    conn.commit()
    conn.close()

def deletar_partida_pg(partida_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("DELETE FROM campeonato.Partidas WHERE id = %s", (partida_id,))
    conn.commit()
    conn.close()

def buscar_partida_pg(partida_id):
    conn = conectar_pg()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM campeonato.Partidas WHERE id = %s", (partida_id,))
    dados = cur.fetchone()
    conn.close()
    return dados

def atualizar_partida_pg(partida_id, codigo, data, horario, estadio_id, time_casa_id, time_visitante_id):
    conn = conectar_pg()
    cur = conn.cursor()
    cur.execute("""
        UPDATE campeonato.Partidas
        SET codigo = %s, data = %s, horario = %s, estadio_id = %s,
            time_casa_id = %s, time_visitante_id = %s
        WHERE id = %s
    """, (codigo, data, horario, estadio_id, time_casa_id, time_visitante_id, partida_id))
    conn.commit()
    conn.close()

