from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from elementLocator import *
from time import sleep
import pytest

@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.get('https://app-staging.oexpress.id/corp/register')
    yield driver
    driver.quit()

'''Positive Case'''
def testCorpRegister(driver):
    driver.find_element(By.XPATH,fillCorpName).send_keys('MauMundur MalahMaju')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    sleep(4)
    driver.save_screenshot('registerCorpForm/resultSS/RegisterCorpBerhasil.png')

'''Negative Case'''
def testEmailTerdaftar(driver):
    driver.find_element(By.XPATH,fillCorpName).send_keys('MauMundur MalahMaju')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert 'Email sudah terdaftar di dalam sistem' in driver.find_element(By.XPATH,errorRegisteredEmail).text
    sleep(1)
    driver.save_screenshot('registerCorpForm/resultSS/errorEmailTerdaftar.png')


def testKolomEmail(driver):
    driver.find_element(By.XPATH,fillCorpName).send_keys('MauMundur MalahMaju')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandusgmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert 'email harus email valid.' in driver.find_element(By.XPATH,errorFillEmail).text
    sleep(1)
    driver.save_screenshot('registerCorpForm/resultSS/errorEmail.png')

def testKolomPassword(driver):
    driver.find_element(By.XPATH,fillCorpName).send_keys('MauMundur MalahMaju')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('ab')
    driver.find_element(By.XPATH,fillPhone).send_keys('081934148333')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert '' in driver.find_element(By.XPATH,errorFillPassword).text
    sleep(1)
    driver.save_screenshot('registerCorpForm/resultSS/errorPasswordPendek.png')

def testKolomPhone(driver):
    driver.find_element(By.XPATH,fillCorpName).send_keys('MauMundur MalahMaju')
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.find_element(By.XPATH,fillPhone).send_keys('99')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert '' in driver.find_element(By.XPATH,errorFillPhone).text
    sleep(1)
    driver.save_screenshot('registerCorpForm/resultSS/errorNomorPendek.png')