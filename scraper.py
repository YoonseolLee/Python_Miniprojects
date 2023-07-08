import requests
from bs4 import BeautifulSoup
import pandas as pd

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

rows = soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')
# print(len(rows)) -> 잘 스크래핑이 됐는지 확인차 쓰는 것임

countries_list = [] #아직은 빈 리스트이다.

for row in rows:
    dic = {}

    dic['country'] = row.find_all('td')[1].text
    dic['population 2020'] = row.find_all('td')[2].text.replace(',','')
    countries_list.append(dic)

print(countries_list[0])

# df = pd.DataFrame(countries_list)
# df.to_excel('countries_data.xlsx', index=False)
# df.to_csv('countries_data.csv', index=False)
