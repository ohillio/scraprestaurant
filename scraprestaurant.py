from types import NoneType
from bs4 import BeautifulSoup
import requests
import random
#comment

pagenumber = int(input('How many pages do you want to check?'))
pgnumbers = random.sample(range(1,100),pagenumber)
random1 = input('Do you want to pick one restaurant or all the restaurants? (all/one)')
single = list()
if random1 == 'all':
    for i in pgnumbers:
        url = f'https://www.yellowpages.com/new-york-ny/restaurants?page={i}'
        html_texts = requests.get(url).text
        soup = BeautifulSoup(html_texts, 'lxml')
        restaurants = soup.find_all('div', class_= 'result')
        for restaurant in restaurants:
            isopen = restaurant.find('div',class_ = 'open-status')
            if isopen is not None:
                if isopen.text == "OPEN NOW":
                    info = restaurant.find('div', class_ = 'info-section info-primary')
                    info2 = restaurant.find('div', class_ = 'info-section info-secondary')
                    business = info.find('a', class_='business-name')
                    restaurant_name = business.find('span').text
                    telephone = info2.find('div', class_ = 'phones phone primary').text
                    address = info2.find('div', class_ = 'street-address').text
                    locality = info2.find('div', class_= 'locality').text
                    print(f'{restaurant_name} \ntelephone:{telephone} \naddress:{address}, {locality}')
elif random1 =='one':
    url = f'https://www.yellowpages.com/new-york-ny/restaurants?page={random.randint}'
    html_texts = requests.get(url).text
    soup = BeautifulSoup(html_texts, 'lxml')
    restaurants = soup.find_all('div', class_= 'result')
    for restaurant in restaurants:
        isopen = restaurant.find('div',class_ = 'open-status')
        if isopen is not None:
            if isopen.text == "OPEN NOW":
                single.append(restaurant)
    info = single[random.randint(0,(len(single)-1))].find('div', class_ = 'info-section info-primary')
    info2 = single[random.randint(0,(len(single)-1))].find('div', class_ = 'info-section info-secondary')
    business = info.find('a', class_='business-name')
    restaurant_name = business.find('span').text
    telephone = info2.find('div', class_ = 'phones phone primary').text
    address = info2.find('div', class_ = 'street-address').text
    locality = info2.find('div', class_= 'locality').text
    print(f'{restaurant_name} \ntelephone:{telephone} \naddress:{address}, {locality}')
else:
    print('Not a valid input')