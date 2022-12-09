import datetime
import time
from src.logger import logger
import requests
import re
from scrapy.selector import Selector
from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv('token')
chat_id = os.getenv('chat_id')
user_agent = os.getenv('user_agent')
from src.scraper.init_db import Anime, Session



class EmptyPageException(Exception):
    """Raises when page is empty"""
    pass

def _get_series_cnt_(content: Selector) -> tuple:
    text = "".join(content.xpath("./text()").getall())
    series_match = re.search(r"(\d+)\sсери", text)
    films_match = re.search(r"(\d+)\sфильм", text)

    series_cnt = int(series_match.group(1)) if series_match else 0
    films_cnt = int(films_match.group(1)) if films_match else 0
    return series_cnt, films_cnt


def _scrap_page_(session:Session, url:str, page_num:int, session_dt:datetime.datetime)->dict:
    page_url = url + f"page-{page_num}/"
    response = requests.get(page_url, headers={
        "User-Agent": user_agent  # global var
    })

    content = response.content.decode("cp1251").encode('utf-8')

    selections = Selector(text=content).xpath('//div[contains(@class, "all_anime_global")]')
    links = selections.xpath('./a/@href').getall()

    titles_name = selections.xpath('.//div[contains(@class, "aaname")]/text()').getall()
    if len(titles_name) == 0:
        raise EmptyPageException

    titles_info = selections.xpath('.//div[contains(@class, "aailines")]')
    series_cnts = [_get_series_cnt_(item) for item in titles_info]

    for link, title, (series_cnt, films_cnt) in zip(links, titles_name, series_cnts):
        anime = Anime(url=link, title=title, series_cnt=series_cnt,
              films_cnt=films_cnt, changed_at=session_dt)

        if session.query(Anime).filter(Anime.url == link).first() is None:
            session.add(anime)
        else:
            session.query(Anime).filter(Anime.url == link).update(dict(series_cnt=series_cnt,
              films_cnt=films_cnt, changed_at=session_dt))



def scrap_over_pages(url: str) -> tuple:
    """The function gets url to scrape site content specifically title name,title page source,
     count of series,count of films'
    from all content pages of site and return dict object
    INPUT:
    URL:url adress must be like https://jut.su/anime/page-(\d)/
    Note: It's also use global constants from .env file

    OUTPUT:
    dict: the dict object which kind is {title_internal_link:
    {'title_internal_link':title internal link,
     'title': title name in Russian,
     'series_cnt': series count,
     'film_cnt': film count
      }}"""
    logger.info("Started session")
    session_dt = datetime.datetime.now()
    page_num = 1
    status = 1
    session = Session()
    # session.commit()
    # session.close()
    while status == 1:
        try:
            _scrap_page_(session, url, page_num, session_dt)
            logger.info(f"Parsed page {page_num}.")
            time.sleep(1)
            page_num += 1

        except EmptyPageException:
            status = 0
        except Exception as e:
            status = -1
            logger.error(e)
    if status == 0:
        session.commit()
        logger.info(f"Succesfully commited changes to database")

    session.close()

    logger.info(f"Ended session with status={status}")
    return status

if __name__== "__main__":
    status = scrap_over_pages("https://jut.su/anime/")
