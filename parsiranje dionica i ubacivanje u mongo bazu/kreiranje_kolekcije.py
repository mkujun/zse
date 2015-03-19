"""
ovo je skripta za rucni unos podataka u mongo, za svaku dionicu pojedinacno se kreirala kolekcija te je bilo potrebno rucno
namjestiti opisne podatke o dionici/kolekciji, nakon toga su se ubacivali povijesni podaci
"""
__author__ = 'marko'

import csv
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["projekt"]
    assert dbh.connection == c
    symbol = {
        "name" : "Crobex",
        "sector" : "General",
        "isIndex" : 1
    }

    dbh.CROBEX.insert(symbol, safe=True)
    print "Successfully inserted document: %s" % symbol


    with open('dionice/crobexpovijest.csv')as f:
        records = csv.DictReader(f)
        dbh.CROBEX.insert(records)

    print 'TEST'

if __name__ == "__main__":
    main()