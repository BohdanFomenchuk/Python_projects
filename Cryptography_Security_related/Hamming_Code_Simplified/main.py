def hamming_encode(word):
    binary = ("".join('{0:08b}'.format(ord(i)) for i in word))
    encoded = ""
    for i in binary:
        encoded += i + i + i
    return encoded


def hamming_decode(binary):
    i = 1
    decoded = ""
    for b in binary[0::3]:
        if int(b) + int(binary[i]) + int(binary[i + 1]) >= 2:
            decoded += "1"
        else:
            decoded += "0"
        i += 3

    return from_binary_to_ascii(decoded)


def from_binary_to_ascii(binary):
    bit_index = 7
    ascii_char_list = []
    ascii_num = 0
    for bit in binary:
        if bit == "1":
            ascii_num += 2 ** bit_index
        bit_index -= 1
        if bit_index < 0:
            bit_index = 7
            ascii_char_list.append(chr(ascii_num))
            ascii_num = 0
    return "".join(ascii_char_list)



