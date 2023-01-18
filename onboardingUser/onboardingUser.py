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


def testIsiForm(driver):
    #Login
    driver.find_element(By.XPATH,fillEmail).send_keys('fidel.ferdinandus@gmail.com')
    driver.find_element(By.XPATH,fillPassword).send_keys('mamapapakucakep')
    sleep(4)
    driver.find_element(By.XPATH,buttonSubmit).click()
   
    
                                                         #FORM 1
    #Negative Case
    sleep(5)
    driver.find_element(By.XPATH,fillAlamat).send_keys('Ja')
    sleep(1)
    assert 'Alamat terlalu pendek.' in driver.find_element(By.XPATH,errorAlamat).text
    driver.save_screenshot('onboardingUser/resultSS/Form1 - Error Alamat.png')
    sleep(2)

    driver.find_element(By.XPATH,fillTelepon).send_keys('09')
    sleep(1)
    assert 'No. Handphone tidak valid, Eg. 08123456789' in driver.find_element(By.XPATH,errorFillPhone).text
    driver.save_screenshot('onboardingUser/resultSS/Form1 - Error Telpon.png')
    sleep(2)

    driver.find_element(By.XPATH,clickLokasi).click()
    driver.find_element(By.XPATH,fillLokasi).send_keys('B' + Keys.ENTER)
    sleep(2)
    driver.find_element(By.XPATH,clickOutwit).click()
    sleep(2)
    driver.find_element(By.XPATH,clickLokasi).click()
    sleep(2)
    driver.find_element(By.XPATH,fillLokasi).send_keys(Keys.BACK_SPACE + Keys.DELETE + Keys.BACK_SPACE + Keys.DELETE)
    assert 'Lokasi Kota / Kecamatan tidak boleh kosong.' in driver.find_element(By.XPATH,errorLokasi).text
    driver.save_screenshot('onboardingUser/resultSS/Form1 - Error Lokasi.png')

    #Positive Case
    driver.find_element(By.XPATH,fillNamaToko).send_keys('Angin Damai Banget')
    driver.find_element(By.XPATH,fillNamaOwner).send_keys('Bedjoe')
    driver.find_element(By.XPATH,fillTelepon).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + '081934148333')
    driver.find_element(By.XPATH,fillAlamat).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + 'Jalan - jalan ke pasar baru RT.05 RW 015 Kec. Mantap Kel. Siap')
    driver.find_element(By.XPATH,clickLokasi).click()
    driver.find_element(By.XPATH,fillLokasi).send_keys(Keys.BACK_SPACE + Keys.DELETE + 'Koja')
    sleep(3)
    driver.find_element(By.XPATH,chooseLokasi).click()
    sleep(3)
    driver.save_screenshot('onboardingUser/resultSS/Form1 - Hasil Pengisian Form1.png')
    sleep(1)
    driver.find_element(By.XPATH,buttonSelanjutnya).click()
    sleep(5)



                                                       #FORM 2
    

    #Positive Case If User Tick Alamat Perusahaan = Alamat Pengiriman
    driver.find_element(By.XPATH,radioPickup).click()
    sleep(2)
    driver.save_screenshot('onboardingUser/resultSS/Form2 - AlamatPerusahaanSamaDenganPickup.png')
    sleep(1)
    driver.find_element(By.XPATH,radioPickup).click()
    sleep(1)
    
 
    #Negative Case
    driver.find_element(By.XPATH,fillNamaPengirim).send_keys('Ja')
    sleep(1)
    assert 'Nama Penanggung Jawab terlalu pendek.' in driver.find_element(By.XPATH,errorNamaPengirim).text
    driver.save_screenshot('onboardingUser/resultSS/Form2 - ErrorNamaPengirim.png')
    sleep(2)

    driver.find_element(By.XPATH,fillPenanggungJawab).send_keys('Na')
    sleep(1)
    assert 'Nama Penanggung Jawab terlalu pendek.' in driver.find_element(By.XPATH,errorPenanggungJawab).text
    driver.save_screenshot('onboardingUser/resultSS/Form2 - ErrorPenanggungJawab.png')
    sleep(2)

    driver.find_element(By.XPATH,fillTeleponPic).send_keys('09')
    sleep(1)
    assert 'No. Handphone tidak valid, Eg. 08123456789' in driver.find_element(By.XPATH,errorTeleponPic).text
    driver.save_screenshot('onboardingUser/resultSS/Form2 - ErrorTelponPIC.png')
    sleep(2)

    driver.find_element(By.XPATH,fillAlamatPic).send_keys('Hi')
    sleep(1)
    assert 'Alamat terlalu pendek.' in driver.find_element(By.XPATH,errorAlamatPic).text
    driver.save_screenshot('onboardingUser/resultSS/Form2 - ErrorAlamatPIC.png')
    sleep(2)


    #Positive Case
    driver.find_element(By.XPATH,fillNamaPengirim).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE +'Budi Pekerti')
    driver.find_element(By.XPATH,fillPenanggungJawab).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE +'Nartoh')
    driver.find_element(By.XPATH,fillTeleponPic).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + '081934148333')
    driver.find_element(By.XPATH,fillAlamatPic).send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + 'Jalan - jalan ke pasar baru RT.05 RW 015 Kec. Mantap Kel. Siap')
    driver.find_element(By.XPATH,clickLokasi).click()
    driver.find_element(By.XPATH,fillLokasi).send_keys(Keys.BACK_SPACE + Keys.DELETE + 'Koja')
    sleep(3)
    driver.find_element(By.XPATH,chooseLokasi).click()
    sleep(3)
    driver.save_screenshot('onboardingUser/resultSS/Form2 - HasilPengisian Form2.png')
    sleep(1)
    driver.find_element(By.XPATH,buttonSelanjutnya).click()
    sleep(5)
    

                                            #Form 3
    #Positive Case

    driver.find_element(By.XPATH,optionBank).click()
    driver.find_element(By.XPATH,fillBank).click()
    driver.find_element(By.XPATH,fillRekening).send_keys('14045')
    driver.find_element(By.XPATH,fillPemilikRekening).send_keys('Narto Kyubee')
    sleep(1)
    driver.save_screenshot('onboardingUser/resultSS/Form3 - HasilPengisianForm3.png')
    sleep(3)
    driver.find_element(By.XPATH,buttonSelanjutnya).click()
    sleep(5)

    
                                                #Form 4
    #Positive Case
    sleep(4)
    driver.find_element(By.XPATH,uploadKTP).send_keys('/Users/fidel/Documents/orderOnlineTest/onboardingUser/spongebob.jpeg')
    sleep(3)
    driver.save_screenshot('onboardingUser/resultSS/Form4 - uploadKTP.png')
    driver.find_element(By.XPATH,buttonSelanjutnya).click()
    sleep(5)