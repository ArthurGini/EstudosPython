#Programa baseado no 
# https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c

import tweepy
import csv
import pandas as pd

#Entrada de credenciais 
access_token = '211988975-41TdCzdJDhvp9EhIV1ef0ggAOxWxFMl6GMSzbPmg'

#Acesso a plataforma
auth = tweepy.OAuthHandler(consumer_key, consumer_pass)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Abrindo e criando o arquivo
csvfile = open('hash.csv', 'a')
csvWriter = csv.writer(csvfile)

#Ver que a só 7 dias anteriodes 

#Criando a pesquisa
for tweet in tweepy.Cursor(api.search, q="#amor", count=5, lang="en", since ="2020-08-24").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

#Limpando a base
