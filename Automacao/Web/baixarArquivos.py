import requests
import os

def baixarArquivo(url, endereco):
    #faz a requisição ao servidor

    resposta = requests.get(url)
    #Verificação se o processamento esta ok
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novoArquivo:
            novoArquivo.write(resposta.content)
        print("Download completo. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    #Definindo a url de base e a pasta de saída
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    OUTPUT_DIR = 'autoDownloads'

    #Varrendo os arquivos e mudando um numero para cada download dos pdfs
    for i in range(1,26):
    #No python o inicio do intervalo ele inclui e o final ele exclui, oq resta uma varredura de 1 a 25
        nomeArquivo = os.path.join(OUTPUT_DIR, 'notaDeAula {}.pdf'.format(i))
        baixarArquivo(BASE_URL.format(i),nomeArquivo)
