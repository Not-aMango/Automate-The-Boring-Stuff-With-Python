from bs4 import BeautifulSoup
import requests
from pathlib import Path
from os import listdir

location = Path.home()/'Comics'
location.mkdir(parents= True,exist_ok= True)

saved_images = len(listdir(location))
if saved_images != 0:
    page = saved_images + 1
    print(f"Resuming Download\n"
          f"Last Downloaded Image: {listdir(location)[-1]}\n"
          f"Last Downloaded ImageNo.: {saved_images}\n")
else: page = 1

downloaded = saved_images
print('Starting Download...')
while True:
    try:
        source = requests.get(f'https://xkcd.com/{page}/', timeout=10)
        source.raise_for_status()

        comic = BeautifulSoup(source.text,'lxml')

        img_url = 'https:'+comic.find('div',id='comic').img['src']
        title = comic.find('div',id='comic').img['title'].replace(' ','-')
        suffix = img_url.split('.')[-1]

        img = requests.get(img_url, timeout=10)
        img.raise_for_status()

        with open(f'/home/notamango/Comics/{title}.{suffix}', 'wb') as image:
            image.write(img.content)

        page += 1
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
        print(f'Downloaded Page: {downloaded}')
