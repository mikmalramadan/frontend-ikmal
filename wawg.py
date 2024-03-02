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

# Fungsi untuk memasukkan kontak ke dalam grup yang sudah ada
def tambahkan_ke_grup(nama_grup, kontak):
    # Path ke WebDriver (saya menggunakan Chrome, sesuaikan dengan browser Anda)
    driver = webdriver.Chrome('path/to/chromedriver')

    # Buka WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    input("Tekan Enter setelah Anda login di WhatsApp Web")

    # Cari nama grup
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(nama_grup)
    time.sleep(2)

    # Klik grup
    group = driver.find_element_by_xpath(f'//span[@title="{nama_grup}"]')
    group.click()
    time.sleep(2)

    # Klik tombol tambah anggota
    add_button = driver.find_element_by_xpath('//div[@title="Tambah anggota"]')
    add_button.click()
    time.sleep(2)

    # Masukkan kontak ke dalam kotak pencarian
    for k in kontak:
        search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(k)
        time.sleep(1)
        # Pilih kontak
        contact = driver.find_element_by_xpath(f'//span[@title="{k}"]')
        contact.click()
        time.sleep(1)

    # Klik tombol tambah
    add_button = driver.find_element_by_xpath('//div[@class="_3s1D4"]')
    add_button.click()
    time.sleep(2)

    driver.quit()

# Contoh penggunaan
nama_grup = "Nama Grup Anda"
file_vcf = "path/to/your/contacts.vcf"  # Ganti dengan path ke file VCF Anda
kontak = baca_vcf(file_vcf)
tambahkan_ke_grup(nama_grup, kontak)
