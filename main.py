# -*- coding: utf-8 -*-
import sqlite3
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

con = sqlite3.connect('bdmonstruos.db')
cur = con.cursor()
# Instantiate options
driver = webdriver.Chrome(ChromeDriverManager().install())

# Load the HTML page
driver.get("https://www.aidedd.org/dnd-filters/monsters.php")

# Parse processed webpage with BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="lxml")
time.sleep(5)
for td in soup.find_all('tbody', class_="item"):
    f = open('output3.txt', 'a')
    valor = str(td.get_text()).replace("'","")
    f.write(td.get_text())
    f.close()
    # Insert a row of data
    print("insertando"+" "+valor)
    cur.execute("INSERT INTO mounstruos VALUES ("+"'"+valor+"'"+")")
    # Save (commit) the changes
    con.commit()
con.close()
