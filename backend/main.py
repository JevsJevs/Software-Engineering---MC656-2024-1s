from flask import Flask
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def basePath():
    return "<h1>Hello World - Welcome to our project</h1>"

@app.route("/medals", methods=["GET"])
def medals():
    cx = sqlite3.connect("database/banco.db")
    cur = cx.cursor()
    cur.execute("""
        SELECT noc.nome as NOC, 
               SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
               SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
               SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
        FROM noc
        JOIN atleta ON noc.codigo = atleta.noc
        JOIN medalha ON atleta.id = medalha.atleta
        GROUP BY noc.nome
        ORDER BY Ouro DESC, Prata DESC, Bronze DESC
    """)
    results = cur.fetchall()
    cur.close()
    cx.close()
    return results

@app.route("/medals/<country>", methods=["GET"])
def medals_by_country(country):
    cx = sqlite3.connect("database/banco.db")
    cur = cx.cursor()
    cur.execute("""SELECT noc.nome as NOC, 
                          SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
                          SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
                          SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
                   FROM noc
                   JOIN atleta ON noc.codigo = atleta.noc
                   JOIN medalha ON atleta.id = medalha.atleta
                   WHERE noc.nome = ?
                   GROUP BY noc.nome
                   ORDER BY Ouro DESC, Prata DESC, Bronze DESC
    """, (country,))
    results = cur.fetchall()
    cur.close()
    cx.close()
    return results

@app.route("/medals/top/<int:n>", methods=["GET"])
def medals_top(n):
    cx = sqlite3.connect("database/banco.db")
    cur = cx.cursor()
    cur.execute("""SELECT noc.nome as NOC, 
                          SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
                          SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
                          SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
                   FROM noc
                   JOIN atleta ON noc.codigo = atleta.noc
                   JOIN medalha ON atleta.id = medalha.atleta
                   GROUP BY noc.nome
                   ORDER BY Ouro DESC, Prata DESC, Bronze DESC
                   LIMIT ?
    """, (n,))
    results = cur.fetchall()
    cur.close()
    cx.close()
    return results

@app.route("/medals/ratio", methods=["GET"])
def medals_ratio():
    # Retorna os países ordenados pelo razão de ouro/total
    cx = sqlite3.connect("database/banco.db")
    cur = cx.cursor()
    cur.execute("""SELECT noc.nome as NOC, 
                          SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
                          SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
                          SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze,
                          COUNT(medalha.tipo) as Total
                   FROM noc
                   JOIN atleta ON noc.codigo = atleta.noc
                   JOIN medalha ON atleta.id = medalha.atleta
                   GROUP BY noc.nome
                   ORDER BY Ouro/Total DESC
    """)
    results = cur.fetchall()
    cur.close()
    cx.close()
    return results

@app.route("/medals/category/<category>", methods=["GET"])
def medals_by_category(category):
    # Retorna os países ordenados pelo número de medalhas em uma dada categoria(ex: basquete, basquete 3x3, atletismo)
    cx = sqlite3.connect("database/banco.db")
    cur = cx.cursor()
    cur.execute("""SELECT noc.nome as NOC, 
                          SUM(CASE WHEN medalha.tipo = 'O' THEN 1 ELSE 0 END) as Ouro,
                          SUM(CASE WHEN medalha.tipo = 'P' THEN 1 ELSE 0 END) as Prata,
                          SUM(CASE WHEN medalha.tipo = 'B' THEN 1 ELSE 0 END) as Bronze
                   FROM noc
                   JOIN atleta ON noc.codigo = atleta.noc
                   JOIN medalha ON atleta.id = medalha.atleta
                   JOIN evento ON medalha.evento = evento.id
                   JOIN esporte ON evento.esporte = esporte.id
                   WHERE esporte.nome = ?
                   GROUP BY noc.nome
                   ORDER BY Ouro DESC, Prata DESC, Bronze DESC
    """, (category,))
    results = cur.fetchall()
    cur.close()
    cx.close()
    return results