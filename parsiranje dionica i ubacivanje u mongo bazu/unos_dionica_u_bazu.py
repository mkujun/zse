"""
ova skripta radi unos svih dionica sa liste crobexa u mongo bazu podataka.
namijenjeno je za server koji bi se svaki dan azurirao i spremao podatke u 
mongo bazu za taj dan
"""
__author__ = 'marko'

import urllib2
from bs4 import BeautifulSoup
import csv
from pymongo import Connection
from pymongo.errors import ConnectionFailure
import time
import os

import crobex_u_bazu

def get_data(ls_symbols):

    godina = time.strftime("%Y")
    mjesec = time.strftime("%m")
    dan = time.strftime("%d")
    datum = dan + '.' + mjesec + '.' + godina

    print datum

    for simbol in ls_symbols:

        pero = 0

        print 'citam simbole iz liste crobex'
        print 'ovo sam procitao', simbol

        soup = BeautifulSoup(urllib2.urlopen('http://zse.hr/default.aspx?id=17560&dionica=%s' % simbol))

        table = soup.find('table', attrs = { "id" : "dnevna_trgovanja"})

        rows = []

        for row in table.find_all('tr'):
            rows.append([val.text.encode('utf8') for val in row.find_all('td')])

        with open(simbol + 'update.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(row for row in rows if row)
        #DO OVDJE IDE PARSIRANJE I SPREMANJE SVIH PODATAKA

        #OVDJE DALJE KRECE PROVJERA I SPREMANJE U BAZU
        with open(simbol + 'update.csv', mode='r') as f:
            reader = csv.reader(f)
            for num, row in enumerate(reader):
                if datum in row[0]:
                    print 'postoji zapis za trazeni dan', simbol
                    print num,row
                    pero = 1
                    if pero == 1:
                        with open(simbol + 'azuriranje.csv', 'wb') as f:
                            writer = csv.writer(f)
                            writer.writerow(rows[0])
                            writer.writerow(row)
                if pero == 0:
                    with open(simbol + 'azuriranje.csv', 'wb') as f:
                        writer = csv.writer(f)

    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Nemogu se spojiti na MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["projekt"]
    assert dbh.connection == c

    print 'OVO JE UPDATE DIONICE'

    ctrl = os.stat("ARNT-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ARNT-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ARNT.insert(records)
            print 'UBACIO SAM ARNT U MONGA'

    ctrl = os.stat("ATPL-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ATPL-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ATPL.insert(records)
            print 'UBACIO SAM ATPL U MONGA'

    ctrl = os.stat("JDPL-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('JDPL-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.JDPL.insert(records)
            print 'UBACIO SAM JDPL U MONGA'


    ctrl = os.stat("KOEI-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('KOEI-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.KOEI.insert(records)
            print 'UBACIO SAM KOEI U MONGA'

    ctrl = os.stat("KRAS-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('KRAS-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.KRAS.insert(records)
            print 'UBACIO SAM KRAS U MONGA'

    ctrl = os.stat("PODR-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('PODR-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.PODR.insert(records)
            print 'UBACIO SAM PODR U MONGA'

    ctrl = os.stat("RIVP-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('RIVP-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.RIVP.insert(records)
            print 'UBACIO SAM RIVP U MONGA'

    ctrl = os.stat("VART-R-1azuriranje.csv").st_size == 0
    if ctrl is False:
        with open('VART-R-1azuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.VART.insert(records)
            print 'UBACIO SAM VART U MONGA'

    ctrl = os.stat("ZABA-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ZABA-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ZABA.insert(records)
            print 'UBACIO SAM ZABA U MONGA'

    ctrl = os.stat("DLKV-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('DLKV-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.DLKV.insert(records)
            print 'UBACIO SAM DLKV U MONGA'

    ctrl = os.stat("ERNT-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ERNT-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ERNT.insert(records)
            print 'UBACIO SAM ERNT U MONGA'

    ctrl = os.stat("THNK-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('THNK-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.THNK.insert(records)
            print 'UBACIO SAM THNK U MONGA'

    ctrl = os.stat("ATGR-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ATGR-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ATGR.insert(records)
            print 'UBACIO SAM ATGR U MONGA'

    ctrl = os.stat("PTKM-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('PTKM-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.PTKM.insert(records)
            print 'UBACIO SAM PTKM U MONGA'

    ctrl = os.stat("ADPL-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ADPL-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ADPL.insert(records)
            print 'UBACIO SAM ADPL U MONGA'


    ctrl = os.stat("VDKT-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('VDKT-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.VDKT.insert(records)
            print 'UBACIO SAM VDKT U MONGA'


    ctrl = os.stat("LKRI-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('LKRI-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.LKRI.insert(records)
            print 'UBACIO SAM LKRI U MONGA'

    ctrl = os.stat("LEDO-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('LEDO-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.LEDO.insert(records)
            print 'UBACIO SAM LEDO U MONGA'

    ctrl = os.stat("ADRS-P-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ADRS-P-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ADRS.insert(records)
            print 'UBACIO SAM ADRS U MONGA'

    ctrl = os.stat("RIZO-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('RIZO-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.RIZO.insert(records)
            print 'UBACIO SAM RIZO U MONGA'

    ctrl = os.stat("ULPL-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('ULPL-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.ULPL.insert(records)
            print 'UBACIO SAM ULPL U MONGA'

    ctrl = os.stat("VPIK-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('VPIK-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.VPIK.insert(records)
            print 'UBACIO SAM VPIK U MONGA'

    ctrl = os.stat("INA-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('INA-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.INA.insert(records)
            print 'UBACIO SAM INA U MONGA'

    ctrl = os.stat("BLJE-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('BLJE-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.BLJE.insert(records)
            print 'UBACIO SAM BLJE U MONGA'

    ctrl = os.stat("DDJH-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('DDJH-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.DDJH.insert(records)
            print 'UBACIO SAM DDJH U MONGA'

    ctrl = os.stat("HT-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('HT-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.HT.insert(records)
            print 'UBACIO SAM HT U MONGA'

    ctrl = os.stat("HT-R-Aazuriranje.csv").st_size == 0
    if ctrl is False:
        with open('HT-R-Aazuriranje.csv')as f:
            records = csv.DictReader(f)
            dbh.HT.insert(records)
            print 'UBACIO SAM HT U MONGA'

    print 'GOTOVO SAM SA UBACIVANJEM DIONICA'

    #ova petlja brise csv fileove koji su ubaceni u bazu
    for simbol in ls_symbols:
        os.remove(simbol + "azuriranje.csv")
        os.remove(simbol + "update.csv")

    print 'SADA KRECE UBACIVANJE CROBEXA'

    crobex_u_bazu.main()

    print 'GOTOV I SA TIME'

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
    ls_symbols = citaj_simbole('crobex.txt')
    get_data(ls_symbols)

if __name__ == '__main__':
    main()