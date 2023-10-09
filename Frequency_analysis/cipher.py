class Cipher:
    def __init__(self):
        self.shift = 0
        self.alphabet = 26
        self.e_ascii = 69
        self.plaintext = ""
        self.dict_shift = 1
    def cipher_text_char_num(self, cipher_text):
        cipher_char_num = {}
        for i in cipher_text.upper():
            if i in cipher_char_num:
                cipher_char_num[i] += 1
            else:
                cipher_char_num[i] = 1
        cipher_char_num_sorted = sorted(cipher_char_num.items(), key=lambda x: x[1], reverse=True)
        return cipher_char_num_sorted

    def cipher_text_relative_freq(self, cipher_char_num):
        for i in cipher_char_num:
            cipher_char_num[i] = round((cipher_char_num[i] / len(cipher_char_num)), 3)
        cipher_relative_freq_sorted = sorted(cipher_char_num.items(), key=lambda x: x[1], reverse=True)
        return cipher_relative_freq_sorted

    def shift_find(self, cipher_text):
        self.plaintext = ''
        most_common_cipher_char = self.cipher_text_char_num(cipher_text)
        self.shift = self.e_ascii - ord(most_common_cipher_char[self.dict_shift][0].upper())
        plaintext = self.from_cipher_to_plain(cipher_text)
        most_common_plain_char = self.cipher_text_char_num(plaintext)
        index_sum = [y[0] for y in most_common_plain_char].index('E') + [y[0] for y in most_common_plain_char].index('T')
        if index_sum < 8:
            return print(self.plaintext.capitalize())
        else:
            self.dict_shift += 1
            self.shift_find(cipher_text)

    def from_cipher_to_plain(self, cipher_text):
        for i in cipher_text.upper():
            if i.isalpha():
                if ord(i) + self.shift > 90:
                    self.plaintext += chr(ord(i) + self.shift - 26)
                elif ord(i) + self.shift < 65:
                    self.plaintext += chr(ord(i) + self.shift + 26)
                else:
                    self.plaintext += chr(ord(i) + self.shift)
            else:
                self.plaintext += chr(ord(i))
        return self.plaintext



