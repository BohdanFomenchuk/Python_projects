import hashlib
import itertools as it


def md5_crack(hashed_str, pin_len):
    # Create a list of possible pins
    pins = [''.join(p) for p in it.product("0123456789", repeat=pin_len)]
    # Iterate over each pin and digest hash for it
    for pin in pins:
        hashed = hashlib.md5(pin.encode())
        if hashed.hexdigest() == hashed_str:
            return str(pin)
