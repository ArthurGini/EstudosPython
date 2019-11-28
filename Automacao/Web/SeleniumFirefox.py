from selenium import webdriver

#jeito antigo de acessar o firefoz pela biblioteca
#driver= webdriver.Firefox()
#driver.get("http:google.com")

chromedriver = "C:/Users/arthu/Documents/GitHub/EstudosPython/Automacao/chromedriver"#localizacao do chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http:google.com")
