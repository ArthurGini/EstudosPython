import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

frase = 'Python é uma linguagem fenomenal'

text_tokens  = nltk.word_tokenize(frase)
#print (palavras)


tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

print (tokens_without_sw)

csvfile = open('word-list.csv', 'a')
csvWriter = csv.writer(csvfile)