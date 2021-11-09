d = 223
n = 143
e = 7
p = 11
q = 13

plain_text = input(f"Enter the text message you want to encrypt: ")

cipher_text = [chr(ord(i) ** e % n % 127) for i in plain_text]

for i in cipher_text:
    print(f"{i} | {ord(i)} | {ascii(i)} | {ord(i) ** d % n}")
