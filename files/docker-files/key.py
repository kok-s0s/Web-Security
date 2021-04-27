'''
Author: kok-s0s
Date: 2021-04-28 01:44:03
LastEditTime: 2021-04-28 02:13:06
Description: file content
'''


import crypt
import random

passwd = input("Please input your password: ")
salt = "$6$" + "".join(
    random.sample(
        '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', 16))
print(crypt.crypt(str(passwd), salt))
