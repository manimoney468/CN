def crc16_encode(data, key):
    appended_data = data + '0' * 16
    data_int = int(appended_data, 2)
    key_int = int(key, 2)
    remainder = data_int
    for i in range(len(data) + 16):
        if (remainder >> 31) & 1:
            remainder ^= (key_int << 16)
        remainder <<= 1
    crc_binary = bin(remainder)[2:].zfill(16)
    return crc_binary
data = input("Enter binary data: ")
key = "11000000000000101" 
if len(data) != 16:
    print("Input data must be 16 bits long.")
else:
    print("Encoded Data CRC-16:", crc16_encode(data, key))
