# -*- coding: utf-8 -*-
import sqlite3

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class scrapper():
    # Instantiate options
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Load the HTML page
    driver.get("https://www.aidedd.org/dnd-filters/monsters.php")

    # Parse processed webpage with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, features="lxml")

    for td in soup.find_all('td', class_="item"):
        f = open('output3.txt', 'a')
        valor = td.get_text()
        f.write(td.get_text())
        f.close()


class db():
    con = sqlite3.connect('bdmonstruos.db')
    cur = con.cursor()
    sc = scrapper()
    # Insert a row of data
    cur.execute("INSERT INTO mounstruos VALUES (" + sc.valor + ")")
    # Save (commit) the changes
    con.commit()
    con.close()
