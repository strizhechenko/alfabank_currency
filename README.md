# Курсы валют альфабанка

## Использование

Из bash, возвращает json (ну и глазами читаемо более менеее)

	python alfa_currency.py 
	{
	    "dollar": {
	        "sell": "70,25", 
	        "buy": "68,25"
	    }, 
	    "euro": {
	        "sell": "77,0201", 
	        "buy": "73,3083"
	    }
	}

В Python

	from alfa_currency import fetch_currency
	
	currency = fetch_currency()
	
	print currency['euro']['buy']
	print currency['dollar']['sell']
