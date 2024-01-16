from functools import reduce

data_stream = [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0]


def hamming_encode(data):
    # Calculate the number of redundant bits needed (r)
    r = 1
    while 2 ** r < len(data) + r + 1:
        r += 1

    # Create the encoded data array
    encoded_data = [0] * (len(data) + r)
    j = 0

    # Fill in the data bits
    for i in range(1, len(encoded_data) + 1):
        if i & (i - 1) != 0:  # Skip powers of 2
            encoded_data[i - 1] = int(data[j])
            j += 1

    # Fill in the redundant bits
    for i in range(r):
        mask = 2 ** i
        parity = 0
        for j in range(1, len(encoded_data) + 1):
            if j & mask == mask:
                parity ^= encoded_data[j - 1]
        encoded_data[mask - 1] = parity

    return encoded_data


encoded = hamming_encode(data_stream)
test = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0]


def hamming_error_detection(bits_stream):
    return reduce(lambda x, y: x ^ y, [i for (i, b) in enumerate(bits_stream) if b])


def decode(data):
    if hamming_error_detection(data) != 0:
        if data[hamming_error_detection(data)] == 1:
            data[hamming_error_detection(data)] = 0
        elif data[hamming_error_detection(data)] == 0:
            data[hamming_error_detection(data)] = 1

    return data


print(hamming_error_detection(test))
print(decode(test))
