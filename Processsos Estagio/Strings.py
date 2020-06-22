#Determinar a maior palavra em uma string 

string = "Aquela boa e velha frase"
string = string.split()

print(max(string, key=len))

#Transformar a string em Camel Case
camel = "camel case bom e velho"
camel = camel.title()

print(camel)
