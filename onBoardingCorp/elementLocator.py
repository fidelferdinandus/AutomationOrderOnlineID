fillEmail = '//input[@type="email"]'
fillPassword = '//input[@type="password"]'
buttonSubmit ='//button[@class="btn btn-primary"]'


#Slide 1
fillNamaPerusahaan = '//input[@name="company_name"]'
fillNamaOwner = '//input[@name="owner_name"]'
fillBidangUsaha = '//input[@name="company_business"]'
fillNPWP = '//input[@name="company_npwp"]'
fillTeleponPerusahaan = '//input[@name="company_phone"]'
fillEmail = '//input[@type="email"]'
fillAlamatPerusahaan = '//input[@name="company_address"]'
clickLokasi = '//div[@class="multiselect__select"]'
fillLokasi = '//input[@class="multiselect__input"]'
chooseLokasi = '//span[@class="multiselect__option--highlight multiselect__option"]'
buttonSelanjutnya = '//button[@class="btn btn-sm btn-primary"]'


#Slide 2
fillBagianPengiriman = '//input[@name="warehouse.sender_name"]'
fillTeleponWarehouse = '//input[@name="warehouse.phone"]'
fillNamaToko = '//input[@name="warehouse.name"]'
fillNamaFinance = '//input[@name="finance_name"]'
fillStartJamKerja = '//input[@name="working_hour.start"]'
fillFinishJamKerja = '//input[@name="working_hour.end"]'
fillStartPickup = '//input[@name="pickup_time.start"]'
fillFinishPickup = '//input[@name="pickup_time.end"]'
radioSamakanPickup = '//input[@id="store-address"]'
fillAlamatToko = '//input[@name="warehouse.address"]'
clickLokasiToko = '//div[@class="multiselect"]/div[@class="multiselect__select"]'
clickPeriodeTagihan = '//div[@class="multiselect select-status me-2"]/div'
errorLokasi = '//span[@class="text-danger"]'


    #HariKerja
pickHariKerjaSenin = '//div[text()[contains(.,"Senin")]]'
pickHariKerjaSelasa = '//div[text()[contains(.,"Selasa")]]'
pickHariKerjaRabu = '//div[text()[contains(.,"Rabu")]]'
pickHariKerjaKamis= '//div[text()[contains(.,"Kamis")]]'
pickHariKerjaJumat = '//div[text()[contains(.,"Jumat")]]'
pickHariKerjaSabtu = '//div[text()[contains(.,"Sabtu")]]'
pickHariKerjaMinggu = '//div[text()[contains(.,"Minggu")]]'
    #Periode Tagihan
choosePeriodeTagihanBulanan = '//li[@id="null-0"]/span'
choosePeriodeTagihanMingguan = '//li[@id="null-1"]/span'
choosePeriodeTagihanHarian = '//li[@id="null-2"]/span'
    #CaraPembayaran
choosePembayaranInvoice = '//input[@id="payment-type-invoicing"]'
choosePembayaranNettOff = '//input[@id="payment-type-netoff"]'
    #PajakPembayaran
choosePajakPPN = '//input[@id="tax-ppn"]'
choosePajakNonPPN = '//input[@id="tax-non-ppn"]'
    #Servis
chooseServisSatset = '//input[@id="permission-service-0"]'
chooseServisKiss = '//input[@id="permission-service-1"]'
chooseServisSerbu = '//input[@id="permission-service-2"]'
chooseServisGocap = '//input[@id="permission-service-3"]'

#Slide 3
uploadKTP = '//div[@class="onboard-ktp p-4"]/div[1]/div[2]//input[@class="d-none"]'
uploadNPWP = '//div[@class="onboard-ktp p-4"]/div[2]/div[2]//input[@class="d-none"]'
uploadSIUP = '//div[@class="onboard-ktp p-4"]/div[3]/div[2]//input[@class="d-none"]'


#Slide 4
clickBank = '//div[@class="multiselect__select"]'
fillBank ='//span[text()[contains(.,"BRI")]]'
fillRekening = '//input[@name="bank.account_number"]'
fillPemilikRekening = '//input[@name="bank.account_name"]'
clickButtonMengerti = '//button[@class="btn btn-primary d-block w-100 mt-4"]'
errorBank = '//span[@class="text-danger"]'

