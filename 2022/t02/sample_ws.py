#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import ics
import configparser
import datetime
import uuid

html_file = 'sample_ws.html'
with open(html_file, "r") as ht:
    page = ht.read()
parsed_page = BeautifulSoup(page, 'html.parser')
tag_container = parsed_page.find('table')
rows = tag_container.find_all('tr')

print('\n\n'.join(map(str,rows)))

# search_url = 'samplews.html'
# schedule_page = requests.get(search_url)
# schedule_soup = BeautifulSoup(schedule_page.text, 'html.parser')
# soup_container = schedule_soup.find('table')
# rows = soup_container.find_all('tr')

# # next(rows)
# for row in rows[2:]:
#     all_data = row.find_all('td')
#     if len(all_data)==6:
#         e = ics.Event()
#         # read params from config file
#         tz = {}
#         if config['EVENT'].get('EVENT_TZ'):
#             tz = {'TZID': config['EVENT'].get('EVENT_TZ')}
#         date = all_data[0].string.strip()
#         date = date[6:10]+date[3:5]+date[:2]
#         tstart = all_data[1].string.strip()[:2] + all_data[1].string.strip()[3:5] + '00'
#         tend = all_data[1].string.strip()[8:10] + all_data[1].string.strip()[11:13] + '00'
#         e.add_line(name='uid', value= str(uuid.uuid1())+'@fabrizioiozzi.com')
#         e.add_line(name='dtstart', param=tz, value= date + 'T' + tstart)
#         e.add_line(name='dtend', param=tz, value= date + 'T' + tend)
#         e.add_line(name='location', value= all_data[2].contents[0].string.strip())
#         t = datetime.datetime.today()
#         e.add_line(name='dtstamp', value=f'{t.strftime("%Y%m%d")}T{t.strftime("%H%M%S")}')
#         myCal.add_container(e)

# with open('my.ics', 'w') as my_file:
#     my_file.write(myCal.build())
