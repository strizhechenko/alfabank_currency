# coding: utf-8
""" Подтягивает данные о курсах валют для интернет-банка альфа-банка """
from urllib2 import urlopen
import xml.etree.ElementTree as etree


def fetch_currency():
    """ Возвращает dict с ценами на доллары и евро """
    endpoint = 'https://alfabank.ru/_/rss/_currency.html'
    tree = etree.parse(urlopen(endpoint))
    root = tree.getroot()
    currency = root.find('channel/item/description')
    open('tmp.xml', 'w').write(currency.text.encode('cp1251'))
    root = etree.parse('tmp.xml').getroot()
    euro = root.find('div/table')[3]
    dollar = root.find('div/table')[4]
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
