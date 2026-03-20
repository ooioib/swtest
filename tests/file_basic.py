# test/file_basic.py 

import csv
with open("data/add.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)