from selenium import webdriver
#acessoa a pagina na web
driver= webdriver.Firefox()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#chromedriver = "C:/Users/arthu/Documents/GitHub/EstudosPython/Automacao/chromedriver"#localizacao do chromedriver
#driver = webdriver.Chrome(chromedriver)
#driver.get("http://econpy.pythonanywhere.com/ex/001.html")



#busca pelo xpath = /html/body/div[2]/div
buyers = driver.find_element_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_element_by_xpath('//span[@class="item-price"]')

#imprimir os compradores e o preco
num_page_items = len(buyers)

for i in range(num_page_items):
    print (buyers[i].text + " : "+ prices[i].text)

driver.close()