#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from bs4 import BeautifulSoup
import requests
import ics
from ics import Calendar, Event

c = Calendar()

"""
c1 = Container(
    ContentLine(name="TZOFFSETFROM", value="+0200"),
    ContentLine(name="TZOFFSETTO", value="+0100"),
    ContentLine(name="TZNAME", value="CET"),
    ContentLine(name="DTSTART", value="19701025T030000")
        ) ]

c.extra = [
    Container(
        name="VTIMEZONE", [
        ContentLine(name="TZID", value="Europe/Rome"),
        ContentLine(name="X-LIC-LOCATION", value="Europe/Rome"),
        Container(
            name="STANDARD", [
            ContentLine(name="TZOFFSETFROM", value="+0200"),
            ContentLine(name="TZOFFSETTO", value="+0100"),
            ContentLine(name="TZNAME", value="CET"),
            ContentLine(name="DTSTART", value="19701025T030000") ]
        ) ]
    )
]
"""

c.extra = [
    Container(
        name="VTIMEZONE", 
        ContentLine(name="TZID", value="Europe/Rome"),
        ContentLine(name="X-LIC-LOCATION", value="Europe/Rome"),
        Container(
            name="STANDARD", [
            ContentLine(name="TZOFFSETFROM", value="+0200"),
            ContentLine(name="TZOFFSETTO", value="+0100"),
            ContentLine(name="TZNAME", value="CET"),
            ContentLine(name="DTSTART", value="19701025T030000") ]
        ) ]
    )
]

search_url = "https://didattica.unibocconi.it/lezioni/pop_orariogiorn.php?codice_ins=30540&classe=27&gruppo=27&fe_lingua_short=I"
schedule_page = requests.get(search_url)
schedule_soup = BeautifulSoup(schedule_page.text, 'html.parser')
soup_container = schedule_soup.find('table')
# print(soup_container.prettify())
rows = soup_container.find_all('tr')

# next(rows)
for row in rows[2:]:
    all_data = row.find_all('td')
    if len(all_data)==6:
        e = Event()
        e.name = "Lezione 30540"
        date = all_data[0].string.strip()
        date = date[6:10]+'-'+date[3:5]+'-'+date[:2]
        tstart = all_data[1].string.strip()[:2] + ':' + all_data[1].string.strip()[3:5] + ':00'
        tend = all_data[1].string.strip()[8:10] + ':' + all_data[1].string.strip()[11:13] + ':00'
        e.begin = date + 'T' + tstart
        e.end = date + 'T' + tend
        e.description = all_data[2].contents[0].string.strip()
        # print(all_data[0].string.strip(), all_data[1].string.strip(), all_data[2].contents[0].string)
        c.events.add(e)

with open('my.ics', 'w') as my_file:
    my_file.writelines(c)
