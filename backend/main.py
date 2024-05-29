from flask import Flask
import csv
import sqlite3

cx = sqlite3.connect("database/teste.db")

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
    with open("../lib/Olympics_Medal_Table.csv") as f:
        table = csv.DictReader(f)
        return list(table)
