# -*- coding: utf-8 -*-
import sqlite3
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

tabla = ""


def consulta(self, cadena):
    self.cursor.execute(cadena)
    self.con.commit()
    return self.cursor.fetchall()




con = sqlite3.connect('bdmonstruos.db')
cur = con.cursor()
print("conexion realizada")
# Instantiate options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
# Load the HTML page
driver.get("https://www.aidedd.org/dnd-filters/monsters.php")
time.sleep(0)
# Parse processed webpage with BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="lxml")

for td in soup.find_all("td", class_="item"):
    valor = str(td.get_text()).replace("'", "")
    print(valor)
    cur.execute("INSERT INTO pruieba(nombre) VALUES("+"'"+valor+"'"+")")
    soup.find_all("td", class_="center")
    valor = str(soup.get_text()).replace("'", "")
    print(valor)
    cur.execute("INSERT INTO pruieba(cr) VALUES("+"'"+valor+"'"+")")
con.commit()
con.close()
