"""
skripta koja dohvaca sve dionice sa zagrebacke burze i sprema ih u txt file
"""

from selenium import webdriver
from bs4 import BeautifulSoup

def main():
  
  driver = webdriver.PhantomJS()
  driver.get("http://zse.hr/default.aspx?id=9978")

  html = driver.page_source
  soup = BeautifulSoup(html)

  dionice = soup.find('table', attrs = { "id" : "dnevna_trgovanja"})

  lista = []
  f = open('lista_simbola.txt', 'w')

  for ime_dionice in dionice.find_all('tr')[1:]:
	  lista.append([val.text.encode('utf8') for val in ime_dionice.find_all('a')])	

  for clan in lista:
	  
	  f.write(" ".join(clan) + "\n")
  f.close()
