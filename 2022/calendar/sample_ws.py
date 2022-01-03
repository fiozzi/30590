from bs4 import BeautifulSoup
html_file = 'sample_ws.html'
with open(html_file,'r') as f:
    page = f.read()
page
parsed_page = BeautifulSoup(page,'html.parser')
type(parsed_page)
tag_container = parsed_page.find('table')
type(tag_container)
rows = tag_container.find_all('tr')
type(rows)
rows
type(rows[0])
rows[0]
rows[0].find_all('th')
for row in rows[1:]:
    print(row.find_all('td'))
for row in rows[1:]:
    print(row.find_all('td')[1].string)