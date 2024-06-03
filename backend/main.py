from flask import Flask
from flask import jsonify
import sqlite3
import os
from models import *

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(PROJECT_ROOT, 'database', 'banco.db')

@app.route("/")
def basePath():
    return "<h1>Hello World - Welcome to our project</h1>"

@app.route("/medals", methods=["GET"])
def medals():
    cx = sqlite3.connect(DB_PATH)
    cur = cx.cursor()
    cur.execute("""
        SELECT noc.nome as pais,
               noc.codigo as codigo,
               SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
               SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
               SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
        FROM noc
        JOIN atleta ON noc.codigo = atleta.noc
        JOIN medalha ON atleta.id = medalha.atleta
        GROUP BY noc.codigo
        ORDER BY Ouro DESC, Prata DESC, Bronze DESC
    """)
    results = cur.fetchall()
    cur.close()
    cx.close()
    result = {"table": []}
    for row in results:
        result["table"].append({
            "codigo": row[1],
            "nome": row[0],
            "ouro": row[2],
            "prata": row[3],
            "bronze": row[4],
        })
    return result

@app.route("/medals/<country>", methods=["GET"])
def medals_by_country(country):
    cx = sqlite3.connect(DB_PATH)
    cur = cx.cursor()
    cur.execute("""SELECT noc.nome as NOC, 
                          SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
                          SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
                          SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
                   FROM noc
                   JOIN atleta ON noc.codigo = atleta.noc
                   JOIN medalha ON atleta.id = medalha.atleta
                   WHERE noc.codigo = ?
                   GROUP BY noc.nome
                   ORDER BY Ouro DESC, Prata DESC, Bronze DESC
    """, (country,))
    row = cur.fetchone()
    result = {
        "country": {
            "nome": row[0],
            "ouro": row[1],
            "prata": row[2],
            "bronze": row[3],
        }
    }
    cur.close()
    cx.close()

    return result

@app.route("/medals/top/<int:n>", methods=["GET"])
def medals_top(n):
    cx = sqlite3.connect(DB_PATH)
    cur = cx.cursor()
    cur.execute("""
        SELECT noc.nome as pais,
               noc.codigo as codigo,
               SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
               SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
               SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
        FROM noc
        JOIN atleta ON noc.codigo = atleta.noc
        JOIN medalha ON atleta.id = medalha.atleta
        GROUP BY noc.codigo
        ORDER BY Ouro DESC, Prata DESC, Bronze DESC
        LIMIT ?
    """, (n,))
    results = cur.fetchall()
    result = {"table": []}
    for row in results:
        result["table"].append({
            "codigo": row[1],
            "nome": row[0],
            "ouro": row[2],
            "prata": row[3],
            "bronze": row[4],
        })
    cur.close()
    cx.close()
    return result

@app.route("/medals/ratio", methods=["GET"])
def medals_ratio():
    # Retorna os países ordenados pelo razão de ouro/total
    cx = sqlite3.connect(DB_PATH)
    cur = cx.cursor()
    cur.execute("""
        SELECT noc.nome as pais,
               noc.codigo as codigo,
               SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
               SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
               SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
        FROM noc
        JOIN atleta ON noc.codigo = atleta.noc
        JOIN medalha ON atleta.id = medalha.atleta
        GROUP BY noc.codigo
        HAVING Ouro + Prata + Bronze > 10
        ORDER BY Ouro/(Ouro + Prata + Bronze) DESC
    """)
    results = cur.fetchall()
    cur.close()
    cx.close()
    result = {"table": []}
    for row in results:
        result["table"].append({
            "codigo": row[1],
            "nome": row[0],
            "ouro": row[2],
            "prata": row[3],
            "bronze": row[4],
            "ratio": row[2] / (row[2] + row[3] + row[4])
        })
    return result

@app.route("/medals/category/<category>", methods=["GET"])
def medals_by_category(category):
    # Retorna os países ordenados pelo número de medalhas em uma dada categoria(ex: basquete, basquete 3x3, atletismo)
    cx = sqlite3.connect(DB_PATH)
    cur = cx.cursor()
    cur.execute("""
        SELECT noc.nome as nome,
            noc.codigo as codigo, 
            SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
            SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
            SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
        FROM noc
        JOIN atleta ON noc.codigo = atleta.noc
        JOIN medalha ON atleta.id = medalha.atleta
        JOIN esporte ON medalha.esporte = esporte.id
        JOIN evento ON medalha.evento = evento.id AND Medalha.esporte = evento.esporte
        WHERE esporte.id = ?
        GROUP BY noc.nome
        ORDER BY Ouro DESC, Prata DESC, Bronze DESC
""", (category,))
    results = cur.fetchall()
    result = {"table": []}
    for row in results:
        result["table"].append({
           "codigo": row[1],
            "nome": row[0],
            "ouro": row[2],
            "prata": row[3],
            "bronze": row[4],
        })
    cur.close()
    cx.close()
    return result
