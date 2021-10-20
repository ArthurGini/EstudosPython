# possivel programa para pegar os dados:
# https://gitlab.com/strider/delockyfier

# Python usando o windows
# https://docs.python.org/pt-br/3/using/windows.html

# Exemplo do google drive api
# https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd

# Library OS
# https://docs.python.org/3/library/os.html

# Show properts dialogs
# https://stackoverflow.com/questions/7985122/show-explorers-properties-dialog-for-a-file-in-windows

# Open explorer em python (pode ser util no caso de usar o pyautogui 'python mexe no mouse')
# https://www.codegrepper.com/code-examples/python/how+to+open+windows+explorer+in+python

# Script Atual:
# Listando todos os arquivos criptografados de determinado path

from os import listdir
from os.path import isfile, join
# from selenium

# mypath = 'G:\Drives compartilhados\Lab Dll\Beats\Arthur'
mypath = 'G:\.file-revisions-by-id'


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

# for i in onlyfiles:
#     if i.contains('wiot'):
for i in onlyfiles:
    if 'wiot' in i:
        print(i)


# print(onlyfiles)
