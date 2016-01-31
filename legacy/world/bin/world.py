#!/usr/bin/env python3

import requests
from time import sleep

url = 'https://www.gov.uk/api/world-locations'

while True:
    json = requests.get(url).json()
    for r in json['results']:
        print("%s\t%s\t%s" % (r['details']['iso2'], r['details']['slug'], r['title']))
    if (not 'next_page_url' in json):
        break
    url = json['next_page_url']
    sleep(0.5)
