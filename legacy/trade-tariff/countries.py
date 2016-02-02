#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

soup = BeautifulSoup(sys.stdin.read(), "html.parser")
soup.prettify()

for table in soup.find_all("table"):
    if table.find('th'):
        for tr in table.find_all('tr'):
            td = tr.find('td')
            if td:
                print(td.text.strip())
