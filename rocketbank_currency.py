import requests
import bs4

url = 'https://rocketbank.ru/rates'


def text2float(text):
    return float(text.text.strip(' руб.').replace(',', '.'))


def cyr2eng(value):
    return 'EUR' if value == "Евро" else 'USD' if value == "Доллар США" else value


def fetch_currency():
    data = requests.get(url).content
    soup = bs4.BeautifulSoup(data, "html.parser")
    sends = soup.find('h3', text='Переводы между счетами в приложении')
    table = sends.next.next.next
    output = dict()
    for currency in table.find_all('td', attrs={'class': 'first'}):
        cur, buy, sell = currency.parent.find_all('p')
        output[cyr2eng(cur.text)] = {
            'buy': text2float(buy),
            'sell': text2float(sell)
        }
    return output


if __name__ == '__main__':
    import json
    print(json.dumps(fetch_currency(), indent=4))
