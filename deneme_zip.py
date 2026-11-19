from zip_library.bayt_araclari import sayi_to_byte
from zip_library.crc32 import crc32

from zip_library.writer import zip_yaz
import zlib
print(sayi_to_byte(20,2))
print(crc32(b"merhaba"))
print(zlib.crc32(b"merhaba"))
zip_yaz("kendi.zip", [("a.txt", b"merhaba")])
with open("kendi.zip", "rb") as f:
    veri = f.read(30)
    uzunluk = int.from_bytes(veri[26:28], "little")
    ek_uzunluk = int.from_bytes(veri[28:30], "little")
    ad = f.read(uzunluk)
    print(ad)
    f.read(ek_uzunluk)
    print(f.read(7))