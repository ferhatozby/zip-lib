def  crc32(veri):
    crc = 0xFFFFFFFF
    for byte in veri:
        crc = crc ^ byte
        for i in range(8):
            if (crc & 1) == 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc = crc >> 1
    return crc ^ 0xFFFFFFFF

