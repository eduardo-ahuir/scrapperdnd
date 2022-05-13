# -*- coding: utf-8 -*-
import sqlite3
import time
from translate import Translator

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


con = sqlite3.connect('bdmonstruos.db')
cur = con.cursor()
print("conexion realizada")
# Instantiate options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
# Load the HTML page
driver.get("https://www.aidedd.org/dnd-filters/monsters.php")
time.sleep(10)
# Parse processed webpage with BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="lxml")

data = []
table = soup.find('table', attrs={'class':'liste'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    print(str(cols[1])+str(cols[2]))
    valor1=str(cols[1]).replace("'","")
    valor2 = str(cols[2])
    valor3 = str(cols[3]).replace("'", "")
    valor4 = str(cols[4]).replace("'", "")

    cur.execute("INSERT INTO mounstruos(nombre,cr,tipo,tamanyo) VALUES(?,?,?,?)",[valor1,valor2,valor3,valor4])
    con.commit()
con.close()
