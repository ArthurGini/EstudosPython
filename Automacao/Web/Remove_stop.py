import nltk
import string 

#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download ('stopwords')
nltk.download ('punkt')

stopwords = nltk.corpus.stopwords.words('portuguese')

#Conhecendo as palavras
#print (len(stopwords))
#print (stopwords)

#Listando os acentos
#for c in string.punctuation:
    #print ("["+ c +"]")

#limpando uma string
text = "Eu de américo brasiliense gosto de bolacha porque quando eu choro me entrsitece"

text_token = word_tokenize(text)

token_without_stop = [word for word in text_token if not word in stopwords.words()]

print (token_without_stop)

