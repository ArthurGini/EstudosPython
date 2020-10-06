"""
Codigo escrito com base nos tutoriais de json em python disponivel em:
https://www.youtube.com/watch?v=acbHR0muN-0
"""
import boto3
import json

dados = """{
    "SinaisVitais": {
        "pressaoArterial": "12/8",
        "frequenciaRespiratoria": 80,
        "data": "17/09/2020",
        "dor": 2,
        "frequenciaCardiaca": 0,
        "satO2": 0,
        "temperatura": 0
    },
    "Pessoal": {
        "idade": 53,
        "transportePublico": null,
        "hobbies": "hipismo",
        "idadeMoradorMaisVelho": 32,
        "tempoAteEmpresa": "30 min",
        "quantidadeMoradores": 2,
        "profissao": "militante",
        "nome": "mariguella",
        "estadoCivil": "casado",
        "sexo": "masculino",
        "Endereco": {
            "cidade": "sertao",
            "estado": "ceara",
            "numero": 55,
            "logradouro": "bem longe vei",
            "apto": 0,
            "cep": "14820"
        }
    },
    "Saude": {
        "Hospitalizado": {
            "nome": "",
            "possui": 0
        },
        "AtividadeFisica": {
            "nome": "hipismo",
            "realiza": 1
        },
        "bebidaAlcoolica": "muito",
        "testeCOVID19": 0,
        "diarreia": 0,
        "problemaRespiratorio": "sinusite",
        "moradoresDoencaCronicaPreexistente": 0,
        "DoencaCronica": {
            "nome": "",
            "possui": 0
        },
        "moradoresComSintomas": 1,
        "alergia": "nao",
        "fumante": 1,
        "vacinaGripe": 0,
        "prevenirCOVID19": 0,
        "Medicamento": {
            "qual": "cachaça",
            "fazUso": 1
        },
        "perdaSentidos": 0,
        "distanciamentoSocial": 0,
        "pesoIdeal": 1,
        "alimentacaoSaudavel": 0,
        "febre": 0,
        "sabeCOVID19": 0,
        "tosse": 0,
        "Cirurgia": {
            "realizou": 1,
            "tipo": "tira bala",
            "ano": 1954
        }
    },
    "id": 1,
    "email": "mariguella@gmail.com",
    "status": false
}"""

#abrindo arquivo externo .json
#with open('dados.json') as f:
#    dados = json.load(f)

#Para ler arquivos json como string
dados = json.loads(dados)

pessoal = dados.get("Pessoal")

vitais = dados.get("SinaisVitais")

print("Nome: " + pessoal.get("nome"))
print("Idade: " + str(pessoal.get("idade")))
print("Data: " + str(vitais.get("data")))
print("Status:" + str(dados["status"]))

#nome #idade
#sinais vitais  - data
#Status


#def formatString(string):
    #if string

#for saude in dados.items:
#    print(saude)


"""
def linha():
    print("\n ----------------------------------------------- \n")

#chaves
for chave in dados:
    print("Chave do JSON: " + chave)

linha()
#itens
for itens in dados.items():
    print("Item do JSON: ")
    print(itens)
linha()

#valores
for valores in dados.values():
    print("Valor do JSON:")
    print(valores)
linha()

#valor especifico
print("Valores da Pessoa: ")
print(dados["Pessoal"])
linha()

#pegando items de determinado campo
for dadosPessoais in dados["Pessoal"].items():
    print("Dados pessoais:")
    print(dadosPessoais)
linha()


for dadosSaude in dados["Saude"]:
    #for atividade in dadosSaude["AtividadeFisica"]:
    print(dadosSaude["AtividadeFisica"]) #+ str(dadosSaude["realiza"]))
linha()
"""

