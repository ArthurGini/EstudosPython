# Programa baseado no codigo disponivel em: 
# https://github.com/gabrielfroes/python-automated-actions


import os
import sys
import json
import urllib.request
from pathvalidate import sanitize_filename
import configparser

#__ para criação de metodos privados

class Actions:

    def __init__(self, path=''):
        path_config_file = 'config.ini'
        config = configparser.ConfigParser()
        config.read(path_config_file)
        config_link = config['DEFAULT']['config_link']


    self.path = path
    self.config = self.__loadConfig(config_link)
    self.actions = self.__loadActions(self.config)

    #Lendo o arquivo com as urls 
    def __loadConfig(self, link):
        with urllib.request.urlopen(link) as url:
            data = json.loads(url.read().decode())
        return data

    ##Lendo todas as types que tem no config
    def __loadActions (self, config):
        return [item['type'] for item in config]

    ##Verifica e busca o config.ini
    def __getIniPath(self, filename):
        return filename if os.path.isfile(filename) else os.path.join(os.path.dirname(sys.executable), filename)

    def __createFoldersFromList(self, folders, baseFolder=''):
        baseFolder = sanitize_filename(baseFolder)

        #Gerando as pastas de acordo com o json
        for folder in folders:
            folderName = os.path.join(self.path, baseFolder, folder)
            os.makedirs(folderName, True)

    '''
    Teste: 
    pastas = ['captacao', 'mixagem', 'master']
    createFoldersFromList(pastas, 'teste1')
    '''

    def __downloadFilesFromList(self, files, baseFolder=''):
        baseFolder = sanitize_filename(baseFolder)

        for file in files:
            link = file["from"]
            destination = file["to"]
            #tratando a url 
            fileName = link.rsplit("/", 1)[-1]
            fullPathFile = os.path.join(self.path ,baseFolder, destination, fileName)

            if not os.path.isfile(fullPathFile):
                print(f'baixando....{link}')
                urllib.request.urlretrieve(link, fullPathFile)

    """
    links = [{"from": "http://127.0.0.1:5500/samples/", "to":""}]

    downloadFilesFromList(links, "teste1")
    """
    def doActions(self, actionType, folderName):
        [actions] = [item['actions']
                     for item in self.config if (item['type'] == actionType)]
        #faz um for dentro do config que verifica se o type bate com oq foi passado 

        self.__createFoldersFromList(actions['folders'], folderName)
        self.__downloadFilesFromList(actions['files'], folderName)

    '''
    path = '.'
    actions = Actions(path)
    actions.doActions('vlog')
    '''

def iniApp(myActions):
    #interface via terminal
    print("=================================")
    print("Ecolha uma opção: ")
    print("=================================")
    optionNumber = 0
    for action in myActions.actions:
        optionNumber+=1
        print(f" {optionNumber} - {action}")
    optionSelected = int(input("> "))

    print("=================================")
    print("Nome da pasta: ")
    print("=================================")
    folderName = input("> ")

    print("=================================")
    print("Confirma ? (s/n) ")
    print(f"{myActions.actions[optionSelected-1]}")
    print(f": {folderName}")
    print("=================================")
    confirm = (input("> "))
    #fIM DA interface via terminal

    if confirm == "s":
        myActions.doActions(myActions.actions[optionSelected-1], folderName)

    print(": Pressione ENTER para terminar...")

path = '.' if sys.argv else sys.argv[1]
action = Actions(path)
iniApp(action)