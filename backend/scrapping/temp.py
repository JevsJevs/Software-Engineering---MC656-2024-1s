import csv
import re

with (open("temp.txt") as f,
      open("esportes2.csv", 'w') as out):
    writer = csv.writer(out, lineterminator='\n')
    writer.writerow(["evento_pt", "evento_id", "esporte_id"])
    regex = re.compile(r"\('(.+)', '(.+)', '(.+)'\)")
    for line in f.readlines():
        groups = regex.match(line).groups()
        writer.writerow(groups)