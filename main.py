import requests
import bs4
from datetime import date
import itertools
from orm import Pars
today = date.today()

for page in itertools.count(start=1):

    url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'

    r = requests.get(url)

    if not r.url == url:
        break
    # print(url)

    soup = bs4.BeautifulSoup(r.text, 'lxml')

    items = soup.find_all('div', class_='search-item') 
    for item in items:
        imge = item.find('img').get('data-src')
        date_posted = item.find('span', class_='date-posted').text

        if 'ago' in date_posted:
            date_posted = today.strftime("%d/%m/%Y")

        price = item.find('div', class_='price').text.replace('\n', '').strip()

        if 'Contact' in price:
            price = '0'
        # print(price)

        Pars.create(date=date_posted, images=imge, price=price)
