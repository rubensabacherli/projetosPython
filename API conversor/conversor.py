import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacoes = cotacoes.json()

cotacao_dolar = float(cotacoes['USDBRL']['bid'])

print(f'${cotacao_dolar:,.2f}')