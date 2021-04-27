'''
Author: kok-s0s
Date: 2021-04-27 20:22:03
LastEditTime: 2021-04-27 20:35:29
Description: file content
'''
# import base64

# # 编码过程
# s = "我是一个字符串"
# # a bytes-like object is required
# encoder = base64.b64encode(s.encode("utf-8"))
# print(encoder) # byte类型 b'5oiR5piv5LiA5Liq5a2X56ym5Liy'

# str_encoder = encoder.decode('utf-8')
# print(str_encoder) # str类型 5oiR5piv5LiA5Liq5a2X56ym5Liy

# # 解码过程
# decoder = base64.b64decode(str_encoder)
# print(decoder.decode('utf-8')) # 我是一个字符串


import base64

cipherText = input("CipherText:")

plainText = base64.b64decode(cipherText)

print(plainText.decode('utf-8'))
