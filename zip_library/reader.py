def zip_oku(dosya_yolu):
    with open(dosya_yolu, "rb") as f:
        veri = f.read()
    konum = veri.rfind(b"PK\x05\x06")
    liste_boyutu = int.from_bytes(veri[konum+12:konum+16], "little")
    liste_baslangic = int.from_bytes(veri[konum+16:konum+20], "little")
    ad_uzunlugu = int.from_bytes(veri[liste_baslangic + 28:liste_baslangic + 30], "little")
    etiket_konumu = int.from_bytes(veri[liste_baslangic + 42:liste_baslangic + 46], "little")
    dosya_adi = veri[liste_baslangic + 46:liste_baslangic + 46 + ad_uzunlugu]
    etiket_veri = veri[etiket_konumu:etiket_konumu + 30]
    icerik_uzunluk = int.from_bytes(etiket_veri[18:22], "little")
    etiket_ad_uzunluk = int.from_bytes(etiket_veri[26:28], "little")
    etiket_ek_uzunluk = int.from_bytes(etiket_veri[28:30], "little")
    icerik_baslangic = etiket_konumu + 30 + etiket_ad_uzunluk + etiket_ek_uzunluk
    icerik = veri[icerik_baslangic: icerik_baslangic + icerik_uzunluk]
    return [(dosya_adi, icerik)]