#from secrets.txt import accessKey, secretKey


import boto3
import os

client = boto3.client('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey)	

print("Fazendo upload dos arquivos .py nessa pasta para o bucket da AWS")

#para qualquer arquivo .py nesse diretorio
for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'artrepositorio'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
        print ('Arquivo: {}'.format(file))