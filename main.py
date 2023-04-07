#Descargamos e importamos la libreria discord.py creada por la comunidad
import os
import discord
from discord.ext import commands
import pandas as pd
import time
from binance.client import Client

api_key = os.environ["ACA VA LA API_KEY"]
api_secret = os.environ["ACA VA LA API_SECRET"]
client = Client(api_key, api_secret, testnet=True)

print("Hello World!")

