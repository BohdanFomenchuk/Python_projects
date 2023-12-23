import random
import string
import os
import struct
from Cryptodome.Cipher import AES
from Cryptodome import Random

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print('Key:', key)


def encrypt_file(password, filename):
    chunk_size = 64 * 1024
    output_filename = filename + '.encrypted'
    # Random initialisation vector
    iv = Random.new().read(AES.block_size)
    # Cypher creation
    encryptor = AES.new(password, AES.MODE_GCM, iv)
    # Get file size
    file_size = os.path.getsize(filename)
    # Open input file
    with open(filename, 'rb') as input_file:
        with open(output_filename, 'wb') as outputfile:
            outputfile.write(struct.pack('<Q', file_size))
            outputfile.write(iv)
            while True:
                chunk = input_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += bytes(' ', 'utf-8') * (16 - len(chunk) % 16)
                outputfile.write(encryptor.encrypt(chunk))


def decrypt_file(password, filename):
    chunk_size = 64 * 1024
    output_filename = os.path.splitext(filename)[0]
    # Open encrypted file and write data
    # IV needs fot cypher creation.
    with open(filename, 'rb') as infile:
        original_size = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        # Cypher creation from key and IV
        decryptor = AES.new(password, AES.MODE_GCM, iv)
        # Write decrypted data to file
        with open(output_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(original_size)


def main():
    choice = input("do you want to (E)ncrypt or (D)ecrypt?: ")
    if choice == 'E':
        filename = 'data.txt'
        password = input('Password: ')
        encrypt_file(password.encode("utf8"), filename)
        print('done.')
    elif choice == 'D':
        filename = 'data.txt.encrypted'
        password = input('Password: ')
        decrypt_file(password.encode("utf8"), filename)
        print('done.')
    else:
        print('no option selected.')


if __name__ == "__main__":
    main()
