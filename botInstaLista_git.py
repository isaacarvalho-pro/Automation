
from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import random

class InstagramBot:
    #função de inicio, pedindo as informções de usuario e senha 
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path='C:\Python39\geckodriver.exe')
    #função de login, entra no insta e loga no site com informações dadas de usuario e senha 
    def login(self):
        driver = self.driver
        #nomedavariaveldonavegador.get('url') vai para o site
        driver.get("https://www.instagram.com/")
        time.sleep(4)
        #//input[@name="username"]
        #//input[@name="password"]
        
        #acha o objeto html e aplica um click na parte de colocar o usuario 
        usuario = driver.find_element_by_xpath("//input[@name='username']")
        usuario.click()
        usuario.clear()
        #digita o usuario 
        usuario.send_keys(self.username)
        time.sleep(2)
        #mesma coisa mas para o campo senha
        senha = driver.find_element_by_xpath('//input[@name="password"]')
        senha.click()
        senha.clear()
        #digita a senha
        senha.send_keys(self.password)
        #pressiona o enter, assim efetuando login
        senha.send_keys(Keys.RETURN)
        time.sleep(5)
        #chama a função de comentario
        self.comentalista()

    #função que faz escrever que nem um humano
    @staticmethod
    def digite_como_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comentalista(self):
        driver = self.driver
        #coloque aqui a lista de contas a serem visitadas com '' e , ex: ['isaacdofort','isaacbiroliro']
        listacontas = []
        cont = 0
        #loop que faz comentar nas fotos 
        for nome in listacontas:
            #aqui uso essa variavel para colocar o nome da lista na url 
            nomeconta = listacontas[cont]
            driver.get('https://www.instagram.com/'+ nomeconta +'/')
            time.sleep(4)
            #aqui seleciono a foto mais recente 
            driver.find_elements_by_class_name('_9AhH0')[0].click()
            #entro no link dela
            url = driver.current_url
            #e aqui é onde os comentarios são feitos
            try:
                driver.get(url)
                time.sleep(3)
                #coloque a lista de comentarios aqui da mesma forma das contas que mostrei lá em cima
                comentarios = []
                time.sleep(3)
                campo_curtida = driver.find_elements_by_class_name("wpO6b  ")[1].click()
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.digite_como_pessoa(random.choice(comentarios),campo_comentario)
                time.sleep(random.randint(60,200))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)
            cont = cont + 1
            #essa variavel passa o nome da lista
            
            

          

#coloque aqui o usuario e senha dentro dos parenteses com '' e , ex: ('usuario', 'senha')
instabot = InstagramBot('usuario', 'senha')
instabot.login()
        
            