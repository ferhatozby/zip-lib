from zip_library.bayt_araclari import sayi_to_byte
from zip_library.crc32 import crc32
import zlib
print(sayi_to_byte(20,2))
print(crc32(b"merhaba"))
print(zlib.crc32(b"merhaba"))