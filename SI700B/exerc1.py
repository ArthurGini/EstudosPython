"""
Autor: Arthur Briganti Gini
RA: 213253
e-mail: a213253@dac.unicamp.br

Desafio:
Uma palindrome é um número ou um texto cuja leitura é a mesma tanto de frente para traz como de traz para frente.
 Por exemplo, cada um dos seguintes números de 5 dígitos são palindromes: 12321, 55555, 45554 e 11611. 
 Escreva um script que leia um número de 5 dígitos e determine se este é ou não uma palindrome. 
 Se o número não for de 5 dígitos, mostre um alerta ao usuário indicando o problema e permita 
 que o usuário entre com um número correto após a emissão do alerta. 
Não deve ser usado vetores (array).
"""

num = 0

num = input("Insira um numero com 5 digitos: ")
string = str(num)

while (len(string) != 5):
    print("Esse numero nao possui 5 digitos")        
    num = input("Insira um numero com 5 digitos: ")
    string = str(num)

if (string == string[::-1]):    
    print ("O numero: " + string + " e palindromo")
else:
    print ("O numero: " + string + " NAO e palindromo")
    