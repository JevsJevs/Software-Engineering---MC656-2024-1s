from flask import Flask
import csv
import sqlite3

app = Flask(__name__)


class MedalTable:
    file_path = ""

    def get_data(self, unsorted=False):
        if unsorted:
            with open(self.file_path) as f:
                table = csv.DictReader(f)
            return list(table)
        else:
            with open(self.file_path) as f:
                table = csv.DictReader(f)
                ranking = sorted(table, key=lambda x: int(x["Gold"]), reverse=True)
            return ranking
            
    def get_ratio(self):
        with open(self.file_path) as f:
            table = csv.DictReader(f)
            ranking = sorted(table, key=lambda x: int(x["Gold"]) / int(x["Total"]), reverse=True)
        return ranking
        
    def get_country(self, country):
        with open(self.file_path) as f:
            table = csv.DictReader(f)
            for entry in table:
                if entry["NOC"] == country:
                    return entry
            return None
    
    def medals_by_continent(self, continent):
        with open(self.file_path) as f:
            table = csv.DictReader(f)
            ranking = [entry for entry in table if entry["Continent"] == continent]
            ranking.append({"Total": sum(int(entry["Total"]) for entry in ranking), 
                            "Gold": sum(int(entry["Gold"]) for entry in ranking), 
                            "Silver": sum(int(entry["Silver"]) for entry in ranking), 
                            "Bronze": sum(int(entry["Bronze"]) for entry in ranking)})
            return ranking
        
class MedalTableCurrent(MedalTable):
    file_path = "../lib/Olympics_Medal_Table.csv"

class MedalTablePast(MedalTable):
    file_path = "../lib/Olympics_Medal_Table_Past.csv"

class MedalTableByCategory(MedalTable):
    file_path = "../lib/Olympics_Medal_Table.csv"

    def get_data(self, category):
        with open(self.file_path) as f:
            table = csv.DictReader(f)
            return [entry for entry in table if entry["Category"] == category]

@app.route("/", methods=["GET"])
def home():
    return "<h1>Hello World - Welcome to our project</h1>"

@app.route("/medals/<country>", methods=["GET"])
def medals_by_country(country):
    querry = MedalTableCurrent().get_country(country)
    if querry:
        return querry
    else:
        return {"error": f"country '{country}' does not exist"}, 404

@app.route("/medals", methods=["GET"])
def medals():
    return MedalTableCurrent().get_data(unsorted = True)

@app.route("/medals/top/<int:n>", methods=["GET"])
def top_n(n):
    return MedalTableCurrent().get_data()[:n]

@app.route("/medals/ratio", methods=["GET"])
def medals_ratio():
    return MedalTableCurrent().get_ratio()

@app.route("/medals/compare", methods=["GET"])
def medals_compare():
    return {"current": MedalTableCurrent().get_data()[:10], "past": MedalTablePast().get_data()[:10]}

@app.route("/medals/category/<category>", methods=["GET"])
def medals_by_category(category):
    return MedalTableByCategory().get_data(category)

@app.route("/medals/continent/<continent>", methods=["GET"])
def medals_by_continent(continent):
    return MedalTableCurrent().medals_by_continent(continent)
