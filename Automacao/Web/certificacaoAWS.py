"""
Programa para acessar a APN da AWS e baixar os certificados automaticamente
"""
from selenium import webdriver
from time import sleep
from getpass import getpass

senha_input = getpass("Password: ")


#Acessa o site
driver= webdriver.Firefox()
driver.get("https://partnercentral.awspartner.com/SiteLogin?startURL=%2FLmsSsoRedirect%3FRelayState%3D%252FAccount%252FTranscript%252FArchived")



#driver.find_element_by_xpath('')

#Realizando o login na APN
#driver.find_element_by_id('email')
email_input = driver.find_elements_by_xpath('//*[@id="loginPage:j_id16:loginComponent:loginForm:email"]')
email_input.send_keys('arthur.gini@brlink.com')

#driver.find_element_by_id('pass')
senha_input = driver.find_elements_by_xpath('//*[@id="loginPage:j_id16:loginComponent:loginForm:password"]')

sleep(100)