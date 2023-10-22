def xor_hex_strings(hex_str1, hex_str2):
    # Convert hexadecimal strings to integers
    int1 = int(hex_str1, 16)
    int2 = int(hex_str2, 16)
    print(int1)
    # XOR the integers
    result_int = int1 ^ int2
    print(result_int)
    # Convert the result back to a hexadecimal string
    result_hex = format(result_int, '02X')

    return result_hex


# Input: Intercepted messages
message1 = "391813c092a2d5ac9acb705dfe41be3df08de67d1145cbcc3f"
message2 = "03adeae2c8c2f2336c8a8d312733c2456e76e0b2d9068adc3f"
message3 = "72d0954e354045f09461dc4c911d0b58ff8963efb12c34303f"

# Break the XOR cipher
clear_text_hex = xor_hex_strings(xor_hex_strings(message1, message2), message3)
print(clear_text_hex)
# Convert the clear text from hexadecimal to ASCII
clear_text = bytes.fromhex(clear_text_hex).decode('ascii')

# Output the clear text
print(clear_text)