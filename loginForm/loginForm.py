from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from elementLocator import *
from time import sleep
import pytest

@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.get('https://app-staging.oexpress.id/login')
    yield driver
    driver.quit()

'''Positive Case'''
def testLogin(driver):
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    sleep(1)
    driver.save_screenshot('loginForm/resultSS/loginDefault.png')


def testLupaPasswordButton(driver):
    driver.find_element(By.LINK_TEXT, buttonForgetPass).click()
    sleep(1)
    driver.save_screenshot('loginForm/resultSS/buttonLupaPassword.png')

    #Negative Case
    driver.find_element(By.XPATH, fillEmail).send_keys("Fe")
    assert 'email terlalu pendek.' in driver.find_element(By.XPATH,errorForgetpassword).text
    sleep(1)
    driver.save_screenshot('loginForm/resultSS/ErrorForgetPasswordEmailPendek.png')

    driver.find_element(By.XPATH, fillEmail).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE)
    assert 'email tidak boleh kosong.' in driver.find_element(By.XPATH,errorForgetpassword).text
    sleep(1)
    driver.save_screenshot('loginForm/resultSS/ErrorForgetPasswordEmailKosong.png')

    #Submit Forget Password
    driver.find_element(By.XPATH, fillEmail).send_keys("fidel.ferdinandus@gmail.com" + Keys.ENTER)
    sleep(3)
    driver.save_screenshot('loginForm/resultSS/SuccessForgetPassword.png')


#Negative Case
def testFalseEmail(driver):
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandussss@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert 'Kombinasi email dan password salah' in driver.find_element(By.XPATH,errorEmail).text
    sleep(1)
    driver.save_screenshot('loginForm/resultSS/errorEmail.png')

def testFalsePassword(driver):
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakeppppppp')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,buttonSubmit).click()
    assert 'Akun Anda tidak aktif' in driver.find_element(By.XPATH,errorPassword).text
    sleep(1)
    driver.save_screenshot('loginForm/resultSS/errorPassword.png')