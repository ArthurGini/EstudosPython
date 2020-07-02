#Programa baseado no 
# https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c

import tweepy
import csv
import pandas as pd

#Entrada de credenciais 


#Acesso a plataforma
auth = tweepy.OAuthHandler(consumer_key, consumer_pass)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Abrindo e criando o arquivo
csvfile = open('hash.csv', 'a')
csvWriter = csv.writer(csvfile)

#Criando a pesquisa
for tweet in tweepy.Cursor(api.search, q="#RAP", count=5, lang="en", since ="2020-04-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])