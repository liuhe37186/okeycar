#!/usr/bin/env python
# encoding: utf-8
# from lib import get_cars
import requests
from bs4 import BeautifulSoup
from setting import headers, domain, car_type, file_output,wait_sec
import json
import bs4
from lib import get_cars
import time

# output_file = open(file_output, 'w+',encoding='utf-8')

# 第一步提取 品牌列表
# 第二部通过品牌列表提取 车辆详细列表(下一页)


def main():
    output_file = open(file_output, 'w+',encoding='utf-8')
    for land_type in car_type:
        start_url = domain+land_type

        result = requests.get(start_url, headers=headers)

        html_content = result.content
        html_content_soup = BeautifulSoup(html_content,'html5lib')
        tags =  html_content_soup.find_all('dl')
        # print(tags)
        for tag in tags:
            cars=[]
            if tag.get('class') == None:
                car={}
                for child in tag.children:
                    if isinstance(child,bs4.element.Tag):
                        
                        if child.name == 'dt':
                            brandName=child.get_text(strip=True)
                        if child.name == 'dd':
                            for h4 in child.find_all('h4'):
                                series=h4.get_text(strip=True)
                                href=h4.a.attrs['href']
                                # print(car)
                                time.sleep(wait_sec)

                                car = get_cars(brandName,series,href)
                                # cars.append(car)
                                line = json.dumps(car, indent=2,ensure_ascii=False)

                                print(line+'\n')
                                # # 输出 Unicode 到文件
                          
                                output_file.write(line)
                                output_file.write(',\n')


main()

def test():
    url='http://www.okeycar.com/794/meiguiche/'
    url_1 = 'https://car.autohome.com.cn/price/series-3170-0-3-0-0-0-0-1.html'
    get_cars('美规奥迪','美规Q7',url)

# test()