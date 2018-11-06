import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def browser_close():
    driver.close()

def algumacoisa(driver):
    sleep = time.sleep
    sleep(3)
    driver.find_element_by_id('lst-ib').send_keys(conteudo_pesquisa)
    sleep(1)
    driver.find_element_by_id('lga').click()
    driver.find_element_by_name('btnK').click()
    sleep(3)
    driver.find_element_by_id('hdtb-tls').click()
    sleep(2)
    driver.find_element_by_class_name('mn-dwn-arw')
    sleep(2)
    driver.find_element_by_id('qdr_d')

def db():
    print('SQLITE')

def send_msg():
    print('Send_msg')


def listar_noticias(driver):
    for x in (1, 10):
        xpath = '//*[@class="g"][' + str(x) + ']'
        resultado_pesquisa = driver.find_element_by_xpath(xpath).text

        print(resultado_pesquisa)

url_itausa_24h = 'https://www.google.com/search?q=Itausa&source=lnt&tbs=qdr:d&sa=X&ved=0ahUKEwjg69u0ub7eAhXGIJAKHeIQAPMQpwUIJA&biw=994&bih=634'
conteudo_pesquisa = 'Itausa'
driver = browser(url_itausa_24h)
listar_noticias(driver)

