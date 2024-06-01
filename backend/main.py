from flask import Flask
from flask import jsonify
import csv
import sqlite3

# cx = sqlite3.connect("database/banco.db")

app = Flask(__name__)

@app.route("/")
def basePath():
    return "<h1>Hello World - Welcome to our project</h1>"

@app.route("/medals/<country>", methods=["GET"])
def medals_by_country(country):
    with open("../lib/Olympics_Medal_Table.csv") as f:
        table = csv.DictReader(f)
        for entry in table:
            if entry["NOC"] == country:
                return entry
        return {"error": f"country '{country}' does not exist"}, 404
            
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