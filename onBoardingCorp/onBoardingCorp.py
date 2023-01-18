from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from elementLocator import *
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    sleep(10)
    #Positive Case
    driver.find_element(By.XPATH,fillNamaPerusahaan).send_keys('Angin Sejuk Banget Deh')
    sleep(3)
    driver.find_element(By.XPATH,fillNamaOwner).send_keys('Lucky Lucky')
    sleep(3)
    driver.find_element(By.XPATH,fillBidangUsaha).send_keys('Peternakan')  
    sleep(3)
    driver.find_element(By.XPATH,fillNPWP).send_keys('2190873627182')
    sleep(3)
    driver.find_element(By.XPATH,fillTeleponPerusahaan).send_keys('081934148333')
    sleep(3)
    driver.find_element(By.XPATH,fillAlamatPerusahaan).send_keys('Jalan kembang desa No.12 RT.001 RW. 005')
    sleep(3)
    driver.find_element(By.XPATH,fillEmail).send_keys('berkemah@gmail.com')
    sleep(3)
    driver.find_element(By.XPATH,clickLokasi).click()
    sleep(3)
    driver.find_element(By.XPATH,fillLokasi).send_keys('Koja')
    sleep(3)
    driver.find_element(By.XPATH,chooseLokasi).click()
    sleep(3)
    driver.save_screenshot('onboardingCorp/resultSS/Form1 - Hasil Pengisian Form1.png')
    sleep(3)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, buttonSelanjutnya)))
    driver.find_element(By.XPATH,buttonSelanjutnya).click()

                                        #FORM 2
    
    #Positive Case
    sleep(5)
    driver.find_element(By.XPATH,fillBagianPengiriman).send_keys('Budi Corpo')
    driver.find_element(By.XPATH,fillNamaToko).send_keys('Serba Adashop')
    sleep(2)
    driver.find_element(By.XPATH,fillTeleponWarehouse).send_keys('081934148333')
    driver.find_element(By.XPATH,fillNamaFinance).send_keys('Khatijah Elaine')

        #OfficeHour
    sleep(2)
    driver.find_element(By.XPATH,fillStartJamKerja).click()
    sleep(1)
    driver.find_element(By.XPATH,fillStartJamKerja).send_keys('0730')
    sleep(2)
    driver.find_element(By.XPATH,fillFinishJamKerja).click()
    sleep(1)
    driver.find_element(By.XPATH,fillFinishJamKerja).send_keys('1630')
    sleep(3)
    

        #OfficeDays
    driver.find_element(By.XPATH,pickHariKerjaSelasa).click()
    driver.find_element(By.XPATH,pickHariKerjaSenin).click()
    driver.find_element(By.XPATH,pickHariKerjaSabtu).click()
    sleep(2)

        #PeriodeTagihan
    driver.find_element(By.XPATH,clickPeriodeTagihan).click()
    sleep(2)
    driver.find_element(By.XPATH,choosePeriodeTagihanBulanan).click()
    sleep(2)

        #PickupHour
    driver.find_element(By.XPATH,fillStartPickup).click()
    sleep(1)
    driver.find_element(By.XPATH,fillStartPickup).send_keys('0930')
    sleep(2)
    driver.find_element(By.XPATH,fillFinishPickup).click()
    sleep(1)
    driver.find_element(By.XPATH,fillFinishPickup).send_keys('1500')
    sleep(2)

        #CaraPembayaran
    driver.find_element(By.XPATH,choosePembayaranInvoice).click()
    sleep(2)

        #PajakPembayaran
    driver.find_element(By.XPATH,choosePajakPPN).click()
    sleep(2)

        #Servis
        #OfficeHour
    driver.find_element(By.XPATH,chooseServisKiss).click()
    sleep(2)
    driver.find_element(By.XPATH,chooseServisSatset).click()
    sleep(2)

    #Positive Case If User Tick Alamat Perusahaan = Alamat Pengiriman
    driver.find_element(By.XPATH,radioSamakanPickup).click()
    sleep(2)
    driver.save_screenshot('onboardingCorp/resultSS/Form2 - AlamatPerusahaanSamaDenganPickup.png')


    #Negative Case
    driver.find_element(By.XPATH,radioSamakanPickup).click()
    sleep(2)
    assert 'Lokasi Kota / Kecamatan tidak boleh kosong.' in driver.find_element(By.XPATH,errorLokasi).text
    sleep(1)
    driver.save_screenshot('onboardingCorp/resultSS/Form2 - ErrorLokasi.png')

    driver.find_element(By.XPATH,fillAlamatToko).send_keys('Jalan Kebayoran buat Corp deh')
    sleep(2)
    driver.find_element(By.XPATH,clickLokasiToko).click()
    sleep(2)
    driver.find_element(By.XPATH,fillLokasi).send_keys('Koja')
    sleep(3)
    driver.find_element(By.XPATH,chooseLokasi).click()
    sleep(10)
    driver.save_screenshot('onboardingCorp/resultSS/Form2 - HasilPengisian Form2.png')
    sleep(20)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, buttonSelanjutnya)))
    driver.find_element(By.XPATH,buttonSelanjutnya).click()

                                                #FORM 3
    sleep(4)
    driver.find_element(By.XPATH,uploadKTP).send_keys('/Users/fidel/Documents/orderOnlineTest/onBoardingCorp/spongebob.jpeg')
    sleep(2)
    driver.find_element(By.XPATH,uploadNPWP).send_keys('/Users/fidel/Documents/orderOnlineTest/onBoardingCorp/patrick.jpeg')
    sleep(2)
    driver.find_element(By.XPATH,uploadSIUP).send_keys('/Users/fidel/Documents/orderOnlineTest/onBoardingCorp/squidward.jpeg')
    driver.save_screenshot('onboardingCorp/resultSS/Form3 - UploadFile.png')
    sleep(2)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, buttonSelanjutnya)))
    driver.find_element(By.XPATH,buttonSelanjutnya).click()



                                                #FORM 4

    #Negative Case
    sleep(5)
    driver.find_element(By.XPATH,clickBank).click()
    sleep(1)
    driver.find_element(By.XPATH,clickBank).click()
    sleep(1)
    assert 'Bank tidak boleh kosong.' in driver.find_element(By.XPATH,errorBank).text
    sleep(2)
    driver.save_screenshot('onboardingCorp/resultSS/Form4 - errorBank.png')

   #Positive Case
    driver.find_element(By.XPATH,clickBank).click()
    driver.find_element(By.XPATH,fillBank).click()
    driver.find_element(By.XPATH,fillRekening).send_keys('14045500505')
    driver.find_element(By.XPATH,fillPemilikRekening).send_keys('Nartoo Kyubee')
    driver.save_screenshot('onboardingCorp/resultSS/Form4 - HasilPengisianForm4.png')
    sleep(7)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, buttonSelanjutnya)))
    driver.find_element(By.XPATH,buttonSelanjutnya).click()

    sleep(3)
    driver.save_screenshot('onboardingCorp/resultSS/FormFinal - Success Register Corp.png')
    sleep(1)
    driver.find_element(By.XPATH,clickButtonMengerti).click()
    sleep(3)