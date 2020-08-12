from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

un = input("Digite seu nome de usuário/email: ")
pw = input("Digite sua senha: ")
link = input("Digite o link do sorteio: ")
amount = int(input("Quantas vezes você deseja comentar?"))
preText = input("Começo do comentário: ") + " "
postText = " " + input("Final do comentário: ")
personsToBeTagged = ["salomaozao"]

driver = webdriver.Chrome()
driver.get(link)

# login:
driver.find_elements_by_class_name("sqdOP")[1].click()
sleep(1)
# creds
driver.find_elements_by_class_name("_2hvTZ")[0].send_keys(un)
driver.find_elements_by_class_name("_2hvTZ")[1].send_keys(pw)
# click
sleep(.5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(2)

# getFollowers
driver.get("https://www.instagram.com/" + un)
sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
sleep(1.5)
for c in range(amount):
    personsToBeTagged.append(driver.find_elements_by_class_name("FPmhX")[c].text)
    print("Conta registrada: " + driver.find_elements_by_class_name("FPmhX")[c].text)

# comment
driver.get(link)
driver.fullscreen_window()
sleep(2.5)

driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()

print("Comentando!")
textbox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
submitBtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/button')
for c in range(amount):
    while True:
        try:
            textbox.send_keys(preText + "@" + personsToBeTagged[c])
            print(f"Comentário para {personsToBeTagged[c]} \033[32m enviado com sucesso!", end="")
            submitBtn.click()
            print(" Enviado!")
            sleep(2.5)
            break
        except:
            print(f"Comentário para {personsToBeTagged[c]} \033[31m falhou!", end="")


print(f"Acabou! {amount} comentários!")

# login > getFollowers > comment
