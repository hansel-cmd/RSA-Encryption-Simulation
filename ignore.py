##### Ignore this File #####

from helper import Replace
from helper import Highlight
    
p = 2
q = 7
n = 14
z = 6


private_key_d = 11
private_key_n = 14
private_key_e = 5

# 73 ** 7 % 143 % 127 = 83
# 83 ** 223 % 143 % 127 = 73


# 108 ** 7 % 143 = 4
# 4 ** 223 % 143 = 108

# p = 11, q = 13
# public_key: {'n': 143, 'e': 7}
# private_key: {'n': 143, 'd': 223}
# ['E', 'A', '\x08', 'H', 'A', 'M', 'A', 'N']


# p = 11, q = 19
# n = 209, e = 7, d = 283
# 108 ** 7 % 209 = 48
# 48 ** 283 % 209 = 108
# \x11\n0\x02\x12"\n\x03\x14\x15&\x02"0\x14

cipher_text = input("Enter something XD")
cipher_text = ascii(cipher_text.encode().decode('unicode_escape'))

# Since a string will typically use escape character,
# i.e., 'SAMPLE\\x08...', we have to replace this type
# of pattern with its true value (hex ascii code)
cipher_text = Replace.replace_to_ascii(cipher_text)
cipher_text = [i for i in cipher_text]
print(cipher_text)

# decrypt each character from the cipher text
plain_text = [chr(ord(i) ** private_key_d % private_key_n % 127) for i in cipher_text]

# for i in cipher_text:
#     print(f"{i} | {ord(i)} | {chr(ord(i) ** private_key_d % private_key_n % 127)}")
                                    # n = 14
                                    # e = 5
                                    # d = 11
                                    # 73 ** 5 % 14 % 127 = 5
                                    # 5 ** 11 % 14 % 127 = 3 should be 73
# 73
test_i = 'I'
# 5
test_i_2 = '\x05'
# 83
test_i_3 = 'S'

print(f"{test_i} | {ord(test_i)}")
print(f"{test_i_2} | {chr(ord(test_i_2))}")
print(f"{test_i_3} | {ord(test_i_3)}")


# print(chr(ord(17)))
for i in range (0, 128):
    print(ascii(chr(i)))

