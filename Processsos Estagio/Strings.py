import re

#Determinar a maior palavra em uma string 
print ("\nprograma 1: Exibir a maior palavra ")
string = "Aquela boa e velha frase"
string = string.split()
print(max(string, key=len))

#Transformar a string em Camel Case
print ("\nprograma 2: Editar frases para Camel Case")
camel = "camel case bom e velho"
camel = camel.title()
print(camel)

print ("\nprograma 3: tirar os char especial")
string = "hey th~~^^^~$#@$ere"
#char = re.sub('[^a-zA-Z0-9\.]', '', string)
string = re.sub('[^a-zA-Z0-9 \\\]', '', string)
print(string)