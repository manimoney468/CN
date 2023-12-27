def crc12_encode(data, key):
    appended_data = data + '0' * 12
    data_int = int(appended_data, 2)
    key_int = int(key, 2)
    remainder = data_int
    for i in range(len(data) + 12):
        if (remainder >> 23) & 1:
            remainder ^= (key_int << 12)
        remainder <<= 1
    crc_binary = bin(remainder)[2:].zfill(12)
    return crc_binary
data = input("Enter binary data: ")
key = "1100000011"
if len(data) != 12:
    print("Input data must be 12 bits long.")
else:
    print("Encoded Data (Data + CRC-12):", crc12_encode(data, key))
