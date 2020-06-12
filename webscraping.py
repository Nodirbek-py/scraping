import requests
from bs4 import BeautifulSoup as BS
import json
# https://agro-olam.uz/category/yangiliklar/page/1/
for i in range(1, 33):
    html = "https://agro-olam.uz/category/yangiliklar/page/"
    response = requests.get(html + str(i))
    soup = BS(response.text, 'html.parser')
    posts = soup.find_all(class_="td-block-span6")
    data = {}
    for post in posts:
        title = post.find(class_ ='entry-title').text
        date = post.find(class_ = 'entry-date').text
        url = post.find('a')['href']
        image = post.find(class_='entry-thumb')['data-img-url']
        body = requests.get(url)
        inner_soup = BS(body.text, 'html.parser')
        article = inner_soup.find(class_='td-post-content tagdiv-type').text
        data = {
            'title': title,
            'date': date,
            'url': url,
            'image': image,
            'article': article
        }
        with open('data.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.write(',')








