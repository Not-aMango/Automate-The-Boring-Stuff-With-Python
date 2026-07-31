from bs4 import BeautifulSoup
import requests

source = requests.get('https://timesofindia.indiatimes.com/us').text
soup = BeautifulSoup(source,'html.parser')

i = 1
for headline_class in soup.find_all('a', class_="border_color VXZ9M yNCw_"):
    print()
    print(f'{i}. Headline:')
    print(headline_class.find('div',class_='Kt6Pm style_change').text)
    try:
        print(headline_class.p.text)
    except Exception: pass
    print()
    i += 1
