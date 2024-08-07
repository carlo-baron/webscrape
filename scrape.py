import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.m.wikipedia.org/wiki/List_of_Generation_Z_slang")
soup = BeautifulSoup(response.content, 'html.parser')

for tr in soup.find_all('tr'):
    first_child = tr.find('td')
    if first_child:
        print(first_child.get_text(strip=True))
