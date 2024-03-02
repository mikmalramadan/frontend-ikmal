from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import vobject  # Install library vobject untuk membaca file vcf

# Fungsi untuk membaca kontak dari file VCF
def baca_vcf(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    vcard = vobject.readOne(data)
    return vcard.contents['fn']

# Fungsi untuk membuat grup baru
def buat_grup(nama_grup, kontak):
    # Path ke WebDriver (GeckoDriver)
    driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

    # Buka WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    input("Tekan Enter setelah Anda login di WhatsApp Web")

    # Klik tombol buat grup
    new_chat_button = driver.find_element_by_xpath('//div[@title="Obrolan Baru"]')
    new_chat_button.click()
    time.sleep(2)

    # Pilih "Grup"
    grup_button = driver.find_element_by_xpath('//span[@title="Grup"]')
    grup_button.click()
    time.sleep(2)

    # Masukkan nama grup
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(nama_grup)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Tambahkan kontak ke grup
    for k in kontak:
        search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(k)
        time.sleep(1)
        # Pilih kontak
        contact = driver.find_element_by_xpath(f'//span[@title="{k}"]')
        contact.click()
        time.sleep(1)

    # Klik tombol buat
    create_button = driver.find_element_by_xpath('//span[@data-testid="arrow"]')
    create_button.click()
    time.sleep(2)

    driver.quit()

# Contoh penggunaan
nama_grup = "Nama Grup Anda"
file_vcf = "path/to/your/contacts.vcf"  # Ganti dengan path ke file VCF Anda
kontak = baca_vcf(file_vcf)
buat_grup(nama_grup, kontak)
