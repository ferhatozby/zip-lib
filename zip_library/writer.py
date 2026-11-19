from .crc32 import crc32
from .bayt_araclari import sayi_to_byte
def dosya_etiketi_olustur(dosya_adi, icerik):
    crc_degeri = crc32(icerik)

    etiket = b"PK\x03\x04"
    etiket += sayi_to_byte(20, 2)  # sürüm
    etiket += sayi_to_byte(0, 2)  # ayarlar
    etiket += sayi_to_byte(0, 2)  # yöntem (0=sıkıştırmasız)
    etiket += sayi_to_byte(0, 4)  # tarih/saat
    etiket += sayi_to_byte(crc_degeri, 4)  # CRC
    etiket += sayi_to_byte(len(icerik), 4)  # sıkıştırılmış boyut
    etiket += sayi_to_byte(len(icerik), 4)  # orijinal boyut
    etiket += sayi_to_byte(len(dosya_adi), 2)  # ad uzunluğu
    etiket += sayi_to_byte(0, 2)  # ek bilgi uzunluğu (0)

    return etiket + dosya_adi.encode() + icerik

def liste_kaydi_olustur(dosya_adi, icerik, etiket_konumu):
    crc_degeri = crc32(icerik)

    kayit = b"PK\x01\x02"
    kayit += sayi_to_byte(20, 2)  # yapan sürüm
    kayit += sayi_to_byte(20, 2)  # gereken sürüm
    kayit += sayi_to_byte(0, 2)  # ayarlar
    kayit += sayi_to_byte(0, 2)  # yöntem
    kayit += sayi_to_byte(0, 4)  # tarih/saat
    kayit += sayi_to_byte(crc_degeri, 4)  # CRC
    kayit += sayi_to_byte(len(icerik), 4)  # sıkıştırılmış boyut
    kayit += sayi_to_byte(len(icerik), 4)  # orijinal boyut
    kayit += sayi_to_byte(len(dosya_adi), 2)  # ad uzunluğu
    kayit += sayi_to_byte(0, 2)  # ek bilgi uzunluğu
    kayit += sayi_to_byte(0, 2)  # yorum uzunluğu
    kayit += sayi_to_byte(0, 2)  # disk numarası
    kayit += sayi_to_byte(0, 2)  # iç özellikler
    kayit += sayi_to_byte(0, 4)  # dış özellikler
    kayit += sayi_to_byte(etiket_konumu, 4)  # etiketin dosyada kaçıncı baytta başladığı

    return kayit + dosya_adi.encode()

def bitis_kaydi_olustur(dosya_sayisi, liste_toplam_boyut, liste_baslangic):
    kayit = b"PK\x05\x06"
    kayit += sayi_to_byte(0, 2)  # disk no
    kayit += sayi_to_byte(0, 2)  # listenin başladığı disk
    kayit += sayi_to_byte(dosya_sayisi, 2)  # bu diskteki dosya sayısı
    kayit += sayi_to_byte(dosya_sayisi, 2)  # toplam dosya sayısı
    kayit += sayi_to_byte(liste_toplam_boyut, 4)  # listenin toplam boyutu
    kayit += sayi_to_byte(liste_baslangic, 4)  # listenin dosyada nerede başladığı
    kayit += sayi_to_byte(0, 2)  # yorum uzunluğu

    return kayit


def zip_yaz(cikti_dosyasi, dosyalar,):


    tum_etiketler = b""
    tum_liste_kayitlari = b""
    konum = 0

    for (dosya_adi, icerik) in dosyalar:
        etiket_konumu = konum
        etiket = dosya_etiketi_olustur(dosya_adi, icerik)
        tum_etiketler += etiket
        konum += len(etiket)

        liste_kaydi = liste_kaydi_olustur(dosya_adi, icerik, etiket_konumu)
        tum_liste_kayitlari += liste_kaydi

    liste_baslangic = konum
    liste_toplam_boyut = len(tum_liste_kayitlari)

    bitis = bitis_kaydi_olustur(len(dosyalar), liste_toplam_boyut, liste_baslangic)

    with open(cikti_dosyasi, "wb") as dosyalar:
        dosyalar.write(tum_etiketler)
        dosyalar.write(tum_liste_kayitlari)
        dosyalar.write(bitis)


