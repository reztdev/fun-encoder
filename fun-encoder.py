# author : Muhammad Rizki

def string_to_binary(string):
    payload = ""
    for byte in string:
        payload += "\\x{:02b}".format(ord(byte))
    return payload

def string_plain_data(input_string):
    return [ord(character) for character in input_string]

def encrypt(data):
    encrypted_data = []
    for byte_data in range(len(data)):
        enc_value = data[byte_data]
        enc_value ^= byte_data
        enc_value = (((enc_value & 0xFFFF) >> 14) | (enc_value << 2)) & 0xFFFF
        enc_value ^= byte_data
        enc_value = (((enc_value & 0xFFFF) >> 14) | (enc_value << 2)) & 0xFFFF
        encrypted_data.append(enc_value)
    return encrypted_data

def result_plain_data(input_text):
    plain_data = string_plain_data(input_text)
    output = "[" + ",".join(f"0x{value:04X}" for value in plain_data) + "]"
    return output

def encrypt_plain_data(data):
    encrypt_data = encrypt(data)
    encrypt_string = ''.join(chr(value & 0xFFFF) for value in encrypt_data)
    return encrypt_string

def decrypt(encrypted_data):
    decrypted_data = []
    for enc_value in range(len(encrypted_data)):
        dec_value = encrypted_data[enc_value]
        dec_value = (((dec_value & 0xFFFF) << 14) | (dec_value >> 2)) & 0xFFFF
        dec_value ^= enc_value
        dec_value = (((dec_value & 0xFFFF) << 14) | (dec_value >> 2)) & 0xFFFF
        dec_value ^= enc_value
        decrypted_data.append(dec_value)
    return decrypted_data

def decrypt_plain_data(encrypted_data):
    decrypted_data = decrypt(encrypted_data)
    decrypted_string = ''.join(chr(value) for value in decrypted_data)
    return decrypted_string
