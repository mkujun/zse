'''
skripta koja radi parsiranje svih dionica za sve podatke od pocetka mjerenja
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import csv

import dohvat_svih_dionica

def get_data(ls_symbols):

    for simbol in ls_symbols:
        driver = webdriver.PhantomJS()
        print 'citam simbole iz liste'
        print "ovo sam procitao", simbol
        driver.get("http://zse.hr/default.aspx?id=17560&dionica=%s" % simbol)

        povijest_link = driver.find_element_by_xpath('//li[@titler="t17565"]')
        povijest_link.click()

        datum_od = driver.find_element_by_xpath('//*[@id="DateFrom"]')
        print datum_od.get_attribute('value')

        value = driver.execute_script('return arguments[0].value;', datum_od)
        print value
	
	#najraniji moguci datum
        driver.execute_script('''
            var datum_od = arguments[0];
            var value = arguments[1];
            datum_od.value = value;
            ''', datum_od, '02.01.1995')
        value = driver.execute_script('return arguments[0].value;', datum_od)
        print ("after update, value = {}".format(value))

       
        botun = driver.find_element_by_xpath('//*[@id="t17565"]/div/form/fieldset/table/tbody/tr/td[5]/input')
        botun.click()

        html = driver.page_source
        soup = BeautifulSoup(html)

        table = soup.find('table', attrs = { "id" : "dnevna_trgovanja"})

        rows = []

        for row in table.find_all('tr'):
            rows.append([val.text.encode('utf8') for val in row.find_all('td')])

        with open(simbol + 'output.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(row for row in rows if row)

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
    #ovdje pozivam skriptu koja dohvati sve dionice i spremi ih u .txt file
    dohvat_svih_dionica.main()
    ls_symbols = citaj_simbole('lista_simbola.txt')
    get_data(ls_symbols)

if __name__ == '__main__':
    main()
