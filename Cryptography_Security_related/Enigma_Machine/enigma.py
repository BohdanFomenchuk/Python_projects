class Enigma:
    def __init__(self):
        self.alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor_1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        self.rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        self.rotor_3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        self.starting_shift = 0
        self.plaintext = ""

    def caesar(self, plaintext):
        encrypted = []
        for i in plaintext.upper():
            if self.starting_shift > 26:
                self.starting_shift -= 26
            if ord(i) + self.starting_shift > 90:
                encrypted.append(chr(ord(i) + self.starting_shift - 26))
            elif ord(i) + self.starting_shift < 65:
                encrypted.append(chr(ord(i) + self.starting_shift + 26))
            else:
                encrypted.append(chr(ord(i) + self.starting_shift))
            self.starting_shift += 1
        return ''.join(encrypted)

    def reverse_caesar(self, ciphertext):
        decrypted = []
        for i in ciphertext.upper():
            if self.starting_shift > 26:
                self.starting_shift -= 26
            if ord(i) - self.starting_shift > 90:
                decrypted.append(chr(ord(i) - self.starting_shift - 26))
            elif ord(i) - self.starting_shift < 65:
                decrypted.append(chr(ord(i) - self.starting_shift + 26))
            else:
                decrypted.append(chr(ord(i) - self.starting_shift))
            self.starting_shift += 1
        return ''.join(decrypted)

    def map(self, plaintext, alphabet, rotor):
        ciphertext = []
        for i in plaintext:
            index = alphabet.find(i)
            ciphertext.append(rotor[index])
        return ''.join(ciphertext)

    def reverse_map(self, ciphertext, alphabet, rotor):
        plaintext = []
        for i in ciphertext:
            index = rotor.find(i)
            plaintext.append(alphabet[index])
        return ''.join(plaintext)

    def encrypt(self):
        zero = self.caesar(self.plaintext)
        print(zero)
        first = self.map(zero, self.alphabet, self.rotor_1)
        print(first)
        second = self.map(first, self.alphabet, self.rotor_2)
        print(second)
        third = self.map(second, self.alphabet, self.rotor_3)
        return print(third)

    def decrypt(self):
        first = self.reverse_map(self.plaintext, self.alphabet, self.rotor_3)
        print(first)
        second = self.reverse_map(first, self.alphabet, self.rotor_2)
        print(second)
        third = self.reverse_map(second, self.alphabet, self.rotor_1)
        print(third)
        zero = self.reverse_caesar(third)
        return print(zero)
