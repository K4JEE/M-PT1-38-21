import csv
from os import close, read
with open('file.csv', 'w') as f:
    tsv_writer= csv.DictWriter(f, delimiter=';', fieldnames=['model','year','horsepower','engine size'])
    tsv_writer.writeheader()
    tsv_writer.writerow({'model':'80 1.6 Specs','year':'1989','horsepower': '69','engine size': '1595'})
    tsv_writer.writerow({'model':'80 1.6Specs','year':'1993','horsepower': '102','engine size':'1595'})
    tsv_writer.writerow({'model':'80 1.8Specs','year':'1986','horsepower':'75','engine size':'1781'})
f.close()

with open('file.csv', 'r') as f:
    reader= csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
    


