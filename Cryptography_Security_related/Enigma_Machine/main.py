from enigma import Enigma

enigma = Enigma()
enigma.starting_shift = int(input("Enter starting shift (from 0 to 25): "))
choice = input("Choose machine mode (decrypt or encrypt")

if choice == 'decrypt':
    enigma.plaintext = input("Write a text to be decrypted: ")
    enigma.decrypt()
elif choice == 'encrypt':
    enigma.plaintext = input("Write a text to be encrypted: ")
    enigma.encrypt()
else:
    print("Incorrect operation mode")

# ALWAURKQEQQWLRAWZHUYKVN
# WEATHERREPORTWINDYTODAY