import requests
from xml.etree import ElementTree
import xmltodict
from xml.dom.minidom import parse, parseString
import json
import os
import logging

logging.basicConfig(filename='google_news.log', level=logging.DEBUG)


def connect_to_url_download_data(url, headers=None, ):
    if not headers:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    content = r.content.decode('utf-8')
    return content

def google_news_xml_parse_to_json(url: str):
    logging.debug(f'Connecting to {url}')
    content = connect_to_url_download_data(url)
    with open(f"xml_content2.json", 'w') as f:
            json.dump(content, f)
    logging.debug(content)
    xml_json_content = xmltodict.parse(content)
    logging.debug(json.dumps(xml_json_content, indent=4))
    news_list = xml_json_content['rss']['channel']['item']
    return news_list

def get_news_by_topic(topic_name: str):
    print(f"Getting news for {topic_name}")
    url = ""
    if topic_name == 'Top News':
        url = "https://news.google.com/rss/?output=rss"
        topic_name = "Top News"
    # elif topic_name.upper() in ["WORLD", "NATION", "BUSINESS", "TECHNOLOGY", "ENTERTAINMENT", "SPORTS", "SCIENCE", "HEALTH"]:
    #     # News by predefined topics
    #     url = "https://news.google.com/news/rss/headlines/section/topic/{}/?output=rss".format(topic_name)
    else:
        # News by query term
        url = "https://news.google.com/rss/search?q={}&output=rss".format(topic_name)

    topic_key = topic_name.replace(' ', '_')
    news_json = google_news_xml_parse_to_json(url)
    return news_json

if __name__ == "__main__":
    print(get_news_by_topic("WORLD"))