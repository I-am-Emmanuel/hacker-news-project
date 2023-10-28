from time import sleep
from celery import shared_task
from django.utils import timezone
# from hacker_news import celery
from news.models import NewsItem

import pprint
import requests

from bs4 import BeautifulSoup





# def sorted_hack_news_list(hknlist:list) -> list:
#     return sorted(hknlist, key=lambda k: k['votes'], reverse=True)

@shared_task
# @celery.task
def create_custome_hackn():
    print('Getting news from Hacker News.....')
    try:
        page1 = requests.get('https://news.ycombinator.com/news')
        page2 = requests.get('https://news.ycombinator.com/news?p=2')
        page3 = requests.get('https://news.ycombinator.com/news?p=3')
        page4 = requests.get('https://news.ycombinator.com/news?p=4')

        soupobj1 = BeautifulSoup(page1.text, 'html.parser')
        soupobj2 = BeautifulSoup(page2.text, 'html.parser')
        soupobj3 = BeautifulSoup(page3.text, 'html.parser')
        soupobj4 = BeautifulSoup(page4.text, 'html.parser')

        link1 = soupobj1.select('.titleline')
        # vote = soupobj.select('.score')
        subtext1 = soupobj1.select('.subtext')
        link2 = soupobj2.select('.titleline')
        # vote = soupobj.select('.score')
        subtext2 = soupobj2.select('.subtext')
        link3 = soupobj3.select('.titleline')
        subtext3 = soupobj3.select('.subtext')
        link4 = soupobj4.select('.titleline')
        subtext4 = soupobj4.select('.subtext')

        links = link1 + link2 + link3 + link4
        subtext = subtext1 + subtext2 + subtext3 + subtext4
        # hack_news = []
        count = 0
        for index, item in enumerate(links):
            
            title = item.getText()
            # title = 
            link = item.find('a')
            href = link['href'] if link else None
            vote = subtext[index].select('.score')
            author_tag = subtext[index].find('a', href=True, class_='hnuser')
            if author_tag:
                author = author_tag.text
            else:
                author = None
            comments_link = subtext[index].find('a', string=lambda obj: 'comments' in obj, href=True)

            if comments_link:
                comments = comments_link.getText()
            else:
                comments = None
            
            if len(vote):
                point = int(vote[0].getText().replace(' points', ''))
                if not NewsItem.objects.filter(title=title).exists():
                    NewsItem.objects.create(title=title, url=href, points=point, author=author, comments=comments, created_at=timezone.now())
                    # hack_news.append({'title': title, 'href': href, 'votes': point, 'author':author, 'comments': comments})
                    count += 1
                    if count == 100:
                        break
        sleep(10)
        print('News successfully updated to database')
        # return sorted_hack_news_list(hknlist=hack_news)
    except Exception as error_message:
        print(str(error_message))
    


create_custome_hackn()
    


# pprint.pprint(create_custome_hackn.delay(links=mega_link, subtext = mega_subtext))


