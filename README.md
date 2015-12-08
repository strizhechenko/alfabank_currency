# Курсы валют альфабанка

buy - за сколько банк покупает, sell - за сколько банк продаёт.

## Использование

### Как утилиту:

Возвращает json (ну и глазами читаемо более менеее)

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

### Как библиотеку python

Возвращает dict с евро и долларами.

	from alfa_currency import fetch_currency
	
	currency = fetch_currency()
	
	print currency['euro']['buy']
	print currency['dollar']['sell']
