from cipher import Cipher

# Iye mkx pyyv kvv yp dro zoyzvo cywo yp dro dswo, kxn cywo yp dro zoyzvo kvv yp dro dswo, led iye mkx'd pyyv kvv yp dro zoyzvo kvv yp dro dswo.
# Khoor Zruog ! Frqjudwxodwlrqv, brx kdyh vxffhvvixoob ghfubswhg ph ! Kdyh ixq zlwk wklv sxccoh

cipher_text = "Iye mkx pyyv kvv yp dro zoyzvo cywo yp dro dswo, kxn cywo yp dro zoyzvo kvv yp dro dswo, led iye mkx'd pyyv kvv yp dro zoyzvo kvv yp dro dswo."

letter_relative_freq = {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
                        'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
                        'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
                        'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
                        'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10,
                        'Z': 0.07}

cipher = Cipher()
plaintext = cipher.shift_find(cipher_text)

