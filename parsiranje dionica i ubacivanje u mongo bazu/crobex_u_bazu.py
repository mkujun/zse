"""
ova skripta parsira podatke za crobex i crobex10
"""
__author__ = 'marko'

import urllib2
from bs4 import BeautifulSoup
import csv
from pymongo import Connection
from pymongo.errors import ConnectionFailure
import time
import os

def get_data(ls_symbols):

    godina = time.strftime("%Y")
    mjesec = time.strftime("%-m")
    dan = time.strftime("%-d")
    datum = dan + '.' + mjesec + '.' + godina

    print datum

    for simbol in ls_symbols:

        print 'citam simbole iz liste crobex indexa'
        print 'ovo sam procitao', simbol

        soup = BeautifulSoup(urllib2.urlopen('http://zse.hr/default.aspx?id=44102&index=%s' % simbol))
        tablica = soup.find_all('table', attrs={"id": "dnevna_trgovanja"})

        #web ima dvije tablica sa potpuno istim identifikatorima
        table = tablica[1]

        a = table.find_all('tr')[1].find_all('td')[0].string
        b = table.find_all('tr')[1].find_all('td')[1].string
        c = table.find_all('tr')[1].find_all('td')[2].string
        d = table.find_all('tr')[1].find_all('td')[3].string
        e = table.find_all('tr')[1].find_all('td')[4].string
        f = table.find_all('tr')[1].find_all('td')[5].string
        g = table.find_all('tr')[1].find_all('td')[6].string

        header = "Date,Open,High,Low,Last,Change %,Index turnover\n"

        ukupno = a + ',' + '"' + b + '"' + ',' + '"' + c + '"' + ',' + '"' + d + '"' + ',' + '"' + e + '"' + ',' + '"' + f + '"' + ',' + '"' + g + '"'

        if datum == a:
            with open(simbol + 'azuriranje.csv', 'wb') as f:
                f.write(header)
                f.write(ukupno)
                f.close()

    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Nemogu se spojiti na MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["projekt"]
    assert dbh.connection == c

    ctrl = os.stat("CROBEXazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('CROBEXazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.CROBEX.insert(records)
            print 'UBACIO SAM CROBEX U MONGA'

    ctrl = os.stat("CROBEX10azuriranje.csv").st_size == 0
    if ctrl is False:
        with open('CROBEX10azuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.CROBEX10.insert(records)
            print 'UBACIO SAM CROBEX10 U MONGA'

    #nakon sto se unese u bazu, csv fileovi se brisu
    for simbol in ls_symbols:
        os.remove(simbol + "azuriranje.csv")
        os.remove(simbol + "update.csv")

def citaj_simbole(simboli_datoteka):
    lista_simbola = []
    file = open(simboli_datoteka, 'r')

    for line in file.readlines():
        str_line = str(line)
        if str_line.strip():
            lista_simbola.append(str_line.strip())
        file.close()
    return lista_simbola

def main():
    ls_symbols = citaj_simbole('crobex_indexi.txt')
    get_data(ls_symbols)

if __name__ == '__main__':
    main()
