from bs4 import BeautifulSoup
import requests
from pathlib import Path

Path(Path.home()/'Comics').mkdir(parents= True,exist_ok= True)

i = 1
downloaded = 0

while True:
    try:
        source = requests.get(f'https://xkcd.com/{i}/', timeout=10)
        source.raise_for_status()

        comic = BeautifulSoup(source.text,'lxml')

        img_url = 'https:'+comic.find('div',id='comic').img['src']
        title = comic.find('div',id='comic').img['title'].replace(' ','-')
        suffix = img_url.split('.')[-1]

        img = requests.get(img_url)
        img.raise_for_status()

        with open(f'/home/notamango/Comics/{title}.{suffix}', 'wb') as image:
            image.write(img.content)

        i += 1
        downloaded += 1
    except requests.exceptions.HTTPError:
        print('\nComics download completed')
        break
    except requests.exceptions.RequestException:
        print('\nNo Internet Connection')
        break
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
        break
    finally:
        print(f'Total comics downloaded: {downloaded}')
