# coding: utf-8
""" Подтягивает данные о курсах валют для интернет-банка альфа-банка """
import requests
from bs4 import BeautifulSoup as Soup


def fetch_currency():
    """ Возвращает dict с ценами на доллары и евро """
    parser = "html.parser"
    response = requests.get('https://alfabank.ru/_/rss/_currency.html')
    currencies = Soup(Soup(response.text, parser).description.text, parser).find_all("tr")
    dollar, euro = list(currencies[1]), list(currencies[2])
    return {
        "euro": {
            "buy": euro[1].text,
            "sell": euro[2].text,
        },
        "dollar": {
            "buy": dollar[1].text,
            "sell": dollar[2].text,
        },
    }

if __name__ == '__main__':
    import json
    print json.dumps(fetch_currency(), indent=4)
