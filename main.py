## Scraping local website ##
# with open(file='website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# all_anchor_tags = soup.findAll(name='a')
# for tag in all_anchor_tags:
#     print(tag.text)
#     print(tag.get('href'))
# heading = soup.find(name='h1', id='name')
# sub_heading = soup.find(name='h3', class_='heading')
# print(sub_heading.string)
# company_url = soup.select_one(selector='p em a')
# print(company_url.string)

## Scraping Live Website ##
from bs4 import BeautifulSoup
import requests

res = requests.get(url='https://news.ycombinator.com/news')
yc_web_page = res.text
soup = BeautifulSoup(markup=yc_web_page, features='html.parser')
contents = soup.find_all(name='span', class_='subline')
tags = soup.find_all(name='tr', class_='athing')
max_score = 0
points=[]
a_tag = ''
no_list = []
is_on = True
while is_on:
    for content in contents:
        point = content.find_next(name='span', class_='score')
        point_id = point.attrs.get('id').split('score_')[1]
        points.append(int(content.getText().split(' ')[0]))
        for point1 in points:
            if point1 > max_score:
                max_score = point1
                no_list.append(point.string.split(' '))
                for no in no_list:
                    if int(no[0]) == max_score:
                        a_tag = soup.find(name='a', id=f'up_{point_id}')
                        title = a_tag.find_next(name='a')

                is_on = False
print(title.get('href'))
print(title.string)
print(f'{max_score} points')

