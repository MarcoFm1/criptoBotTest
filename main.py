import discord
import requests
import pandas as pd
import matplotlib.pyplot as plt
import time
from discord.ext import commands

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c32172ed-101a-4372-8ea9-d923f19f84e8'
}

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

cripto = str(input("Introduce la abreviacion de la cripto: "))

params = {
  'symbol': cripto
}


max_price = 0
id = 0


price_df = pd.DataFrame(columns=['Simbolo', 'Precio', 'Fecha'])

@bot.command(name='saludar')
async def saludar(ctx):
    await ctx.send('Hola!')

@bot.event
async def on_ready():
    print(f'Conectado a Discord como {bot.user}')

    max_price = 0  # Definimos max_price aquí
    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        price = data['data'][f'{cripto}']['quote']['USD']['price']
        timestamp = pd.Timestamp.now()

        diferencia = price - max_price 

        price_df.loc[timestamp] = [f'{cripto}', price, timestamp]

        # Verificaciones
        if price < max_price - 0.01:
            print("=========================================")

            print(f'El precio del {cripto} ha bajado. {diferencia}')

            max_price = price

            print(price_df)

            await bot.get_channel(1093774983471308811).send(f'El precio de {cripto} ha bajado. {diferencia}') # Envia mensaje a Discord

        elif (price == max_price):
            print("=========================================")

            await bot.get_channel(1093774983471308811).send(f"el precio esta igual bro") # Envia mensaje a Discord

        else:
            print("=========================================")

            print(f"EL PRECIO SUBIO +{diferencia}!")
            print(price_df)

            await bot.get_channel(1093774983471308811).send(f"EL PRECIO SUBIO +{diferencia}!") # Envia mensaje a Discord

        max_price = max(price, max_price)
        @bot.command(name='grafico')
        async def grafico(ctx):         
          plt.plot(pd.to_datetime(price_df['Fecha']), price_df['Precio'])
          plt.title(f'Comportamiento del precio de {cripto} en los últimos 7 días')
          plt.xlabel('Fecha')
          plt.ylabel('Precio (USD)')
          plt.xticks(rotation=45)
          plt.tight_layout()
          plt.savefig('grafico.png')
          await ctx.send(file=discord.File('grafico.png'))        
        time.sleep(30)




        
bot.run('MTA5Mzk4OTc3MjQzMjc4OTUzNg.GSyFUn.4QLCzcLOJOfUqspuECOOAT0qqIMv3ZTQ19y608')
