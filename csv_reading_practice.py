import csv

with open("files/nfl_standings.txt") as standingscsv:
    for row in csv.reader(standingscsv):
        print(f"Team: {row[0]} W: {row[1]} L: {row[2]}")