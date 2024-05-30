import csv
import sqlite3

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
        sql = "INSERT OR IGNORE INTO noc(codigo, nome) VALUES (:codigo, :nome)"
        for line in reader:
            cx.execute(sql, line)
            

        cx.commit()
        

def atletas(cx: sqlite3.Connection):
    with open("scrapping/eventos2.csv") as f:
        reader = csv.DictReader(f, lineterminator='\n')

if __name__ == "__main__":
    cx = sqlite3.connect("database/banco.db")
    esportes(cx)
    eventos(cx)
    paises(cx)
    cx.close()
