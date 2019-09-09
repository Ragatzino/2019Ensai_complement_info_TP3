import requests
from lxml import etree


if __name__ == "__main__":
    response = requests.get('https://fr.wikipedia.org/wiki/Web_scraping')
    tree = etree.HTML(response.text)
    # On récupère les p qui suivent les h2
    result = tree.xpath('//h2/following-sibling::p')
    for p in result:
        print(p.text)
