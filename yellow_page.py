import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=Pizza&location=London&scrambleSeed=1283856548'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

articles = soup.find_all('div', class_='row businessCapsule--mainRow')

for item in articles:
    name = item.find('span', class_='businessCapsule--name').text
    print(name)
