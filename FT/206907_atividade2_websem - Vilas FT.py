"""
Nome: Vinícius Vilas Boas
RA: 206907
Professor: Ivan Luiz Marques Ricarte

Atividade Número 2:
Nesta atividade, vamos extrair informação sobre um curso a partir de diversas páginas HTML do catálogo da DAC.
No mínimo, você deve ser capaz de obter e salvar informações sobre disciplinas obrigatórias
(nome, créditos, ementa, pré-requisitos) para um curso selecionado pelo código para o catálogo 2019.
Possibilidades adicionais incluem o processamento de ênfases, disciplinas eletivas, outros anos de catálogo
e muito mais...
"""

import requests
from lxml import html

def buscaCurso(numCurso):
    numCurso = str(numCurso)
    endereco = "https://www.dac.unicamp.br/sistemas/catalogos/grad/catalogo2019/proposta/sug"+numCurso+".html"
    curUrl = requests.get(endereco)
    tree = html.fromstring(curUrl.content)
    nome = tree.xpath("/html/body/div/div[1]/div/div[3]/div[1]/h2/text()")
    nome = nome[0]
    nome = str(nome)
    print(nome + '\n')
    return endereco

def buscaMaterias(endereco):
    curUrl = requests.get(endereco)
    tree = html.fromstring(curUrl.content)
    materia = tree.xpath("/html/body/div/div[1]/div/div[3]/div[1]/a/text()")
    for mat in materia:
        mat = mat.split('(')
        print(f'Código da Matéria: {mat[0]}')
        print(f'Créditos: ({mat[1]}')
        print('\n')
    return endereco

def buscaContMateria(endereco):
    curUrl = requests.get(endereco)
    tree = html.fromstring(curUrl.content)
    conteudo = tree.xpath("/html/body/div/div[1]/div/div[3]/div[1]/a/@href")
    link_array = []
    for content in conteudo:
        content = str(content)
        content = content[3:len(content)]
        content = "https://www.dac.unicamp.br/sistemas/catalogos/grad/catalogo2019/"+content
        link_array.append(content)
    return link_array

"""
def buscaInfoMateria(link_array):
    aux = ''
    for link in link_array:
        aux = requests.get(link)
        tree = html.fromstring(aux.content)
        treex = tree.xpath("/html/body/div/div/div[1]/div[3]/div/a/text()")
    for elements in treex:
        print(elements)
        
"""
try:
    response = requests.get('https://www.dac.unicamp.br/sistemas/catalogos/grad/catalogo2019/cursos.html')
    tree = html.fromstring(response.content)

    print('Digite o número do curso: ')
    num = int(input())
    check = 0

    cursos = tree.xpath('/html/body/div/div/div[1]/div[3]/div/span/text()')
    for curso in cursos:
        curso = int(curso)
        if curso == num:
            check = check + 1
            break

    if check:
        resultado = buscaCurso(num)
        resultado = buscaMaterias(resultado)
        resultado = buscaContMateria(resultado)
        # buscaInfoMateria(resultado)
    else:
        print('Não existe curso com o número informado')

        # Se a URL passada estiver incompleta, errado, etc, mostra pro usuário que a URL não é válida e apresenta o erro
except requests.exceptions.MissingSchema as e:
    print('ERRO')
    print(f'Houve algum erro com a URL que está sendo utilizada.\n'
              f' Erro: {e}.')

    # Caso o valor passado não seja válido, avisa o usuário, passa instruções e apresenta o erro.
except ValueError as e:
    print('ERRO')
    print(f'O valor passado como código de curso não é válido.\n'
          f'Instrução: O valor passado para servir como código de curso deve ser do tipo inteiro.\n'
          f'Erro: {e}.')