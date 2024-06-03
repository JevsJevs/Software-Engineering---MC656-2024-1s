import csv
import sqlite3
from utils import get_event_id

def get_athlete_id(url: str):
    return url.split("athlete-profile-n")[1].split("-")[0]

def esportes(cx: sqlite3.Connection):
    with open("scrapping/esportes.csv") as f:
        reader = csv.DictReader(f, lineterminator='\n')
        for line in reader:
            cx.execute(
                "INSERT OR IGNORE INTO esporte (id, nome) VALUES (:id, :esporte_pt)",
                line)
        cx.commit()

def eventos(cx: sqlite3.Connection):
    with open("scrapping/eventos2.csv") as f:
        reader = csv.DictReader(f, lineterminator='\n')
        cx.executemany(
            "INSERT OR IGNORE INTO evento (id, nome, esporte) VALUES (:evento_id, :evento_pt, :esporte_id)",
            reader
        )
        cx.commit()

def paises(cx: sqlite3.Connection):
    with (open("scrapping/noc_pt.csv") as g):
        reader = csv.DictReader(g, lineterminator='\n')
        cx.execute("DELETE FROM noc")
        sql = "INSERT OR IGNORE INTO noc(codigo, nome) VALUES (:codigo, :nome)"
        for line in reader:
            line["nome"] = line["nome"].split("\n")[0]
            cx.execute(sql, line)
            

        cx.commit()
        

def atletas(cx: sqlite3.Connection):
    with open("scrapping/kaggle/athletes.csv") as f:
        reader = csv.DictReader(f, lineterminator='\n')
        cx.execute("DELETE FROM atleta")
        sql = "INSERT OR IGNORE INTO atleta(id, nome, idade, genero, noc) VALUES (:url, :name, :birth_date, :gender, :country_code)"
        for line in reader:
            line["gender"] = "F" if line["gender"] == "Female" else "M" if line["gender"] == "Male" else "X"
            line["url"] = get_athlete_id(line["url"])
            cx.execute(sql, line)
        cx.commit()


def medals(cx: sqlite3.Connection):
    with open("scrapping/kaggle/medals.csv") as f:
        reader = csv.DictReader(f, lineterminator='\n')
        cx.execute("DELETE FROM medalha")
        sql = "INSERT OR IGNORE INTO medalha(evento, atleta, tipo) values (?, ?, ?)"
        for line in reader:
            evento = get_event_id(line["event"], line["discipline"])
            atleta = get_athlete_id(line["athlete_link"])
            tipo = ["O", "P", "B"][int(line["medal_code"]) - 1]
            cx.execute(sql, [evento, atleta, tipo])
        cx.commit()

if __name__ == "__main__":
    cx = sqlite3.connect("database/banco.db")
    # esportes(cx)
    # eventos(cx)
    paises(cx)
    # atletas(cx)
    # medals(cx)
    cx.close()
