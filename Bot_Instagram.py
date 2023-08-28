from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from Basecode import iniciar_driver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condicoes_esperadas
import pyautogui

driver, wait = iniciar_driver()


class Bot():

    def abrir_site(self, site):
        driver.get(site)
        sleep(3)

    def loguin(self, username, password):
        # inserir username
        campo_username = wait.until(condicoes_esperadas.element_to_be_clickable((By.XPATH,
                                                                                 "//input[@name='username']")))
        campo_username.send_keys(username)
        sleep(1)
        # inserir password
        campo_password = wait.until(condicoes_esperadas.element_to_be_clickable((By.XPATH,
                                                                                 "//input[@name='password']")))
        campo_password.send_keys(password)
        entrar = driver.find_element(By.XPATH,
                                     '//div[text()="Entrar"]')
        entrar.click()
        sleep(1)
        # ativar notificacoes? (desativado por padrao, para ativar, mude o XPATH para ---> //button[@class='_a9-- _a9_0']
        try:
            driver.implicitly_wait(5)
            notificacoes = driver.find_element((By.XPATH,
                                                "//button[@class='_a9-- _a9_1']"))
            notificacoes.click()
            sleep(5)
        except:
            sleep(5)
            pass

    def perfil_curtir(self, perfil):
        while True:
            # ir para o link do perfil (preferi assim por ser mais direto e acertivo)
            driver.get(perfil)
            # ultima postagem
            sleep(4)
            driver.execute_script('window.scrollTo(0,500);')
            sleep(4)
            postagens = wait.until(condicoes_esperadas.visibility_of_any_elements_located((By.XPATH,
                                                                                           "//div[@class='_aagu']")))
            postagens[1].click()
            # verificar like
            like_publicacao = driver.find_elements(By.XPATH,
                                                   "//*[@aria-label='Curtir']")
            if like_publicacao:
                sleep(1)
                like_publicacao[0].click()
                pyautogui.alert(
                    text='foto curtida, encerrando em 5 segundos',
                    title='Parabens!')
                sleep(5)
                driver.close()

            else:
                pyautogui.alert(
                    text='encerrando em 5 segundos',
                    title='Etapa desconsiderada')
                sleep(5)
                driver.close()


insta_bot = Bot()
insta_bot.abrir_site()  # link do instagram
insta_bot.loguin()  # (username='',password='')
insta_bot.perfil_curtir()  # link do perfil
