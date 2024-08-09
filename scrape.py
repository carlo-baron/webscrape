import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://en.m.wikipedia.org/wiki/List_of_Generation_Z_slang")
soup = BeautifulSoup(response.content, 'html.parser')
pattern = r'"([^"]*)"'


for tr in soup.find_all('tr'):
    i = 0
    first = ''
    second = ''
    for td in tr.find_all('td'):
        if i == 0:
            first = td.get_text(strip=True)
            i+=1
        elif i == 1:
            match = re.search(pattern, td.get_text(strip=True))
            if match:
                extracted_text = match.group(1)
                second = extracted_text
                print(f"\"{first}\" : \"{second}\",")
                i = 0
                break
            