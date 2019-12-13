import os
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

AV_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY', 'Z92Y0437GIRE1RCO')

doc = resp.json()

#Requisição de BTC/USD em Json
resp = requests.get('https://www.alphavantage.co/query', params={
    'function': 'DIGITAL_CURRENCY_DAILY',
    'symbol': 'BTC',
    'market': 'USD',
    'apikey': AV_API_KEY
})

df = pd.DataFrame.from_dict(doc['Time Series (Digital Currency Daily)'], orient='index', dtype=np.float)
df.head()

#para limpar as colunas repetidas
df.drop(columns=[c for c in df.columns.values if 'b.' in c], inplace=True)
df.head()