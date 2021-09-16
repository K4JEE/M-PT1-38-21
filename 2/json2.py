import json
import csv
with open('file.csv') as f:
    reader=csv.DictReader(f)
    rows=list(reader)

with open('file2.json', 'w') as f:
    json.dump(rows, f)
f.close

with open('file2.json', 'r') as f:
    data = json.load(f)
print(data)