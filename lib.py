#!/usr/bin/env python
# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from setting import headers, domain, car_type, file_output
import bs4
def get_cars(brand_name,series,url):
    result = requests.get(url,headers=headers)
    html = result.content
    soup = BeautifulSoup(html,'html5lib')
    # print(soup.prettify())

    car= {}
    car['brandName']=brand_name
    car['series']=series
    car['href']=url
    car['级别'] = soup.find('a',class_='carlink').get_text()
    ul = soup.find('ul',class_='carcolor-list fn-clear')
    # print(ul)
    colors=[]
    if ul != None and isinstance(ul,bs4.element.Tag):

        for li in ul.find_all('li'):
            color = li.a.get_text().split('(')[0]
            colors.append(color)
        car['外观颜色']= ','.join(colors)
    car_type=[]
    for div in soup.find_all('div',class_='interval01-list-cars'):
        # print(div)
            
        for p in div.find_all('p'):
            print(p.a.get_text())
            car_type.append(p.a.get_text().replace(u'\xa0',' '))
        car['车型']=car_type
    # print(car)
    return car