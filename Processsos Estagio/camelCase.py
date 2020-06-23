import re

def CamelCase(str):  

  str = re.sub('[^a-zA-Z0-9\.]', '', str)

  print(str)

  list_words = str.split(" ")
  aux = ""


  for index, word in enumerate(list_words):
    print(index)
    print(word)
    if index == 0:
      aux = aux + word.lower()
    else:
      aux = aux = word.title()
      #aux = aux + word.upper() + word[1:].lower()

  print(aux)

  # code goes here
  return str

# keep this function call here 
print(CamelCase(input()))
