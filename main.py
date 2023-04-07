import requests
import pandas as pd
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c32172ed-101a-4372-8ea9-d923f19f84e8'
}

cripto = str(input("Introduce la abreviacion de la cripto: "))

params = {
  'symbol': cripto
}

max_price = 0
id = 0

price_df = pd.DataFrame(columns=['Simbolo', 'Precio'])

while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    price = data['data'][f'{cripto}']['quote']['USD']['price']
    timestamp = pd.Timestamp.now()

    price_df.loc[timestamp] = [f'{cripto}', price]
    
  # Verifica si el precio actual es menor que el precio máximo registrado menos una cantidad arbitraria.
    if price < max_price - 0.01:
        print("=========================================")
        print('El precio de la cripto ha bajado.')

        max_price = price
        print(price_df)


    else:
        print("=========================================")
        print("EL PRECIO SUBIO!")
        print(price_df)

    max_price = max(price, max_price)

    time.sleep(30)