from flask import Flask
import csv

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

@app.route("/medals/top/<int:n>", methods=["GET"])
def top_n(n):
    # Retorna os n países com mais medalhas de ouro
    with open("../lib/Olympics_Medal_Table.csv") as f:
        table = csv.DictReader(f)
        ranking = sorted(table, key=lambda x: int(x["Gold"]), reverse=True)
        return ranking[:n]
        
@app.route("/medals/ratio", methods=["GET"])
def medals_ratio():
    # Retorna os países ordenados pelo razão de ouro/total
    with open("../lib/Olympics_Medal_Table.csv") as f:
        table = csv.DictReader(f)
        ranking = sorted(table, key=lambda x: int(x["Gold"]) / int(x["Total"]), reverse=True)
        return ranking
    
@app.route("/medals/compare", methods=["GET"])
def medals_compare():
    # Retorna o top 10 (provisoriamente) de medalhas de ouro dos jogos atuais e da última edição
    with open("../lib/Olympics_Medal_Table.csv") as f:
        table = csv.DictReader(f)
        ranking = sorted(table, key=lambda x: int(x["Gold"]), reverse=True)[:10]
        f.close()
    with open("../lib/Olympics_Medal_Table_Past.csv") as f:
        table = csv.DictReader(f)
        ranking_past = sorted(table, key=lambda x: int(x["Gold"]), reverse=True)[:10]
        f.close()
    return {"current": ranking, "past": ranking_past}

# Daqui pra baixo não funcional apenas com o csv que temos    
@app.route("/medals/category/<category>", methods=["GET"])
def medals_by_category(category):
    with open("../lib/Olympics_Medal_Table.csv") as f: # substituir isso por uma busca no db de medalhas
        table = csv.DictReader(f)
        return [entry for entry in table if entry["Category"] == category]
    
@app.route("/medals/continent/<continent>", methods=["GET"])
def medals_by_continent(continent):
    with open("../lib/Olympics_Medal_Table.csv") as f: # substituir isso por um join para pegar os continentes
        table = csv.DictReader(f)
        ranking = [entry for entry in table if entry["Continent"] == continent]
        ranking.append({"Total": sum(int(entry["Total"]) for entry in ranking), 
                        "Gold": sum(int(entry["Gold"]) for entry in ranking), 
                        "Silver": sum(int(entry["Silver"]) for entry in ranking), 
                        "Bronze": sum(int(entry["Bronze"]) for entry in ranking)})
        return ranking