'''
Author: kok-s0s
Date: 2021-04-27 20:47:23
LastEditTime: 2021-04-27 20:57:46
Description: file content
'''

# def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
#     from itertools import izip, cycle
#     import base64

#     if decode:
#         data = base64.decodestring(data)
#     xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(data, cycle(key)))

#     if encode:
#         return base64.encodestring(xored).strip()
#     return xored

# # secret_data = input("data:")

# # print("The cipher text is")
# # print(xor_crypt_string(secret_data, encode=True))
# # print("The plain text fetched")
# # print(xor_crypt_string(xor_crypt_string(secret_data, encode=True),
# #                        decode=True))

# cipher = "Oz4rPj0+LDovPiwsKDAtOw=="

# print(xor_crypt_string(cipher, decode=True))

from __future__ import print_function, unicode_literals
from os import urandom


def genkey(length: int) -> bytes:
    """Generate key."""
    return urandom(length)


def xor_strings(s, t) -> bytes:
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])


message = 'This is a secret message'
print('Message:', message)

key = genkey(len(message))
print('Key:', key)

cipherText = xor_strings(message.encode('utf8'), key)
print('cipherText:', cipherText)
print('decrypted:', xor_strings(cipherText, key).decode('utf8'))

# Verify
if xor_strings(cipherText, key).decode('utf8') == message:
    print('Unit test passed')
else:
    print('Unit test failed')
