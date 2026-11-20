from zip_library.bayt_araclari import sayi_to_byte
from zip_library.crc32 import crc32
from zip_library.reader import zip_oku
from zip_library.writer import zip_yaz
import zlib
print(sayi_to_byte(20,2))
print(crc32(b"merhaba"))
print(zlib.crc32(b"merhaba"))
zip_yaz("kendi.zip", [("a.txt", b"merhaba")])
print(zip_oku("kendi.zip"))