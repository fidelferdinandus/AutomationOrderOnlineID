from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from elementLocator import *
from time import sleep 
import pytest

@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.get('https://app-staging.oexpress.id/register')
    yield driver
    driver.quit()


#Positive Case
def testRegister(driver):
    driver.find_element(By.XPATH,fillName).send_keys('Fidel Ferdinandus')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    sleep(5)
    driver.save_screenshot('registerForm/resultSS/RegisterBerhasil.png')

    

#Negative Case
def testEmailTerdaftar(driver):
    driver.find_element(By.XPATH,fillName).send_keys('Fidel Ferdinandus')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    sleep(1)
    driver.find_element(By.XPATH,buttonSubmit).click()
    sleep(3)
    assert 'Email sudah terdaftar di dalam sistem' in driver.find_element(By.XPATH,errorRegisteredEmail).text
    sleep(3)
    driver.save_screenshot('registerForm/resultSS/errorEmailTerdaftar.png')
    

def testKolomNama(driver):
    driver.find_element(By.XPATH,fillName).send_keys('Fidel M4nt@p b4n93tz')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    sleep(1)
    driver.save_screenshot('registerForm/resultSS/errorKolomNama.png')

def testKolomEmail(driver):
    driver.find_element(By.XPATH,fillName).send_keys('Fidel Ferdinandus')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandusgmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert 'email harus email valid.' in driver.find_element(By.XPATH,errorFillEmail).text
    sleep(1)
    driver.save_screenshot('registerForm/resultSS/errorEmailTidakValid.png')

def testKolomPassword(driver):
    driver.find_element(By.XPATH,fillName).send_keys('Fidel Ferdinandus')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('a')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert '' in driver.find_element(By.XPATH,errorFillPassword).text
    sleep(1)
    driver.save_screenshot('registerForm/resultSS/errorPasswordPendek.png')

def testKolomPhone(driver):
    driver.find_element(By.XPATH,fillName).send_keys('Fidel Ferdinandus')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('0')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert '' in driver.find_element(By.XPATH,errorFillPhone).text
    sleep(1)
    driver.save_screenshot('registerForm/resultSS/errorNomorPendek.png')