# Acessando o insta
# https://realpython.com/instagram-bot-python-instapy/

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

senha = input('Insira sua senha: ')

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%2522ifd97x19f8xqhjhfz6cnezhj81ih9kfr1782xwcs954p91uujtah%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Dpt_BR%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D881316a7-35b3-4545-8d0b-dce73127c96e&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522ifd97x19f8xqhjhfz6cnezhj81ih9kfr1782xwcs954p91uujtah%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=pt_BR&pl_dbl=0')

#Realizando o login no Facebook
email_input = browser.find_element_by_id('email')
email_input.send_keys('arthurbriganti@hotmail.com')

senha_input = browser.find_element_by_id('pass')
senha_input.send_keys(senha)

logar_click = browser.find_element_by_id('loginbutton').click()
sleep(5)

#Abrindo o instagram
open_insta_click = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div/div[2]/button/div/div').click()
sleep(5)

close_popup_click = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()

#Entrando no messenger do instagram
open_messenger_click = browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T nav.NXc7H.jLuN9 div._8MQSO.Cx7Bp div._lz6s.Hz2lF div.MWDvN.nfCOa div.ctQZg div._47KiJ div.Fifk5 a.xWeGp svg._8-yf5').click()

sleep(3)
open_chat_click = browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.DT7qQ div.t30g8.L1C6I div.Igw0E.IwRSH.eGOV_._4EzTm div.oYYFH div.pV7Qt._6Rvw2.Igw0E.IwRSH.YBx95.ybXk5._4EzTm.i0EQd div.oNO81 div.Igw0E.IwRSH.eGOV_._4EzTm.i0EQd div.Igw0E.IwRSH.eGOV_.vwCYk div._7WGDw div.N9abW div div.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm a.-qQT3.rOtsg').click()
#open_chat_click = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/a').click()


pyautogui.typewrite("Teste xD", interval=0.2)
pyautogui.press('enter')
