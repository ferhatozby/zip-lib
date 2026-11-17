def sayi_to_byte(sayi, kac_byte):
    sonuc= b""
    for i in range(kac_byte):
        parca = sayi & 0xFF
        sonuc = sonuc + bytes([parca])
        sayi = sayi << 8
    return sonuc