# import requests
#
# with open('page.html', 'w', encoding='utf-8') as file:
#     page = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
#
#     file.write(page.text)


from bot.parser.currency_parser import CurrencyParser


cp = CurrencyParser()

cp.get_currency_list()
