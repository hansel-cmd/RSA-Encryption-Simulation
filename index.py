from helper import *



# TODO
# Encryption c = m^e mod n
# c is the cipher text
# m is the plain plain text
def encrypt(plain_text):

    public_key_n, public_key_e = get_public_key_values()

    print("Encrypting...")

    # encrypt each plain text characters to ascii code
    # We can put % 127 at the end to avoid going outside the
    # ascii boundary, but this will cause some plain letter to have
    # similar encryption letter which we need to avoid
    cipher_text = [chr(ord(i) ** public_key_e % public_key_n) for i in plain_text]

    print(f"{Highlight.YELLOW}Original message letters:", [i for i in plain_text])
    print(f"{Highlight.YELLOW}Encrypted message letters:", cipher_text)

    cipher_text = ascii(''.join(cipher_text))[1:-1]

    print(f"{Highlight.GREEN}Original message: {plain_text}")
    print(f"{Highlight.GREEN}Encrypted message: {cipher_text}")

    return cipher_text


# TODO
# Decryption m = c^d mod n
# c is the cipher text
# m is the plain plain text
def decrypt(cipher_text):
    
    private_key_n, private_key_d = get_private_key_values()

    print("Decrypting...")
    
    cipher_text = cipher_text.encode().decode('unicode_escape')

    # decrypt each character from the cipher text
    # We can put % 127 at the end to avoid going outside the
    # ascii boundary, but this will cause some plain letter to have
    # similar encryption letter which we need to avoid
    plain_text = [chr(ord(i) ** private_key_d % private_key_n) for i in cipher_text]

    print(f"{Highlight.YELLOW}Encrypted message letters:", cipher_text)
    print(f"{Highlight.YELLOW}Decrpyted message letters:", plain_text)

    plain_text = ''.join(plain_text)

    print(f"{Highlight.GREEN}Encrypted message: {ascii(''.join(cipher_text))[1:-1]}")
    print(f"{Highlight.GREEN}Decrypted message: {plain_text}")

    return plain_text


def generate_public_private_key():

    print(f"{Highlight.YELLOW}Generate public and private key...")
    # Choose the first prime number [preferrably a large prime number]
    while True:
        p = input(f"{Highlight.WHITE}Enter the value of first prime p: ")
        try:
            p = int(p)
        except ValueError:
            print(f"{Highlight.RED}Invalid input.")    
        if is_prime(p): break
        print(f"{Highlight.RED}Sorry, input is not prime.")

    # Choose the second prime number [preferrably a large prime number]
    while True:
        q = input(f"{Highlight.WHITE}Enter the value of second prime q: ")
        try:
            q = int(q)
        except ValueError:
            print(f"{Highlight.RED}Invalid input.")    
        if is_prime(q): break
        print(f"{Highlight.RED}Sorry, input is not prime.")

    p = int(p)
    q = int(q)

    # compute n = pq
    n = p * q
    # compute z = (p-1)(q-1)
    z = (p - 1) * (q - 1)

    print(f"{Highlight.GREEN}n is {n} \nz is {z}")

    # choose e, where 1 < e < z
    # where e should be coprime with z and 
    # coprime with n
    possible_numbers = get_co_primes(n, z)
    print(f"{Highlight.YELLOW}{possible_numbers}")

    # This part should not be a user input
    # This should be generated by the algorithm itself, i.e., 
    # using random.choice([list])
    # but for the sake of this discussion, we ask for 
    # user input for the value of e.
    print(f"""{Highlight.BLUE}Pls note that this step should be done by the algorithm itself
    (see comment inside the source code), and should not ask for any user input.""")
    while True:
        e = input(f"{Highlight.WHITE}Please choose your {Highlight.BLUE}e value {Highlight.WHITE}in the list highlighted in yellow: ")
        try:
            e = int(e)
            if e in possible_numbers: break
            print(f"{Highlight.RED}Number is not in the list.")
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")
    
    print(f"{Highlight.GREEN}e is {e}")

    # # find number d, such that ed - 1 is exactly divisible by z
    # # 1 solution, but I dont like this
    # all_d_values = [i for i in range (1, 1000) if ((e * i) - 1) % z == 0]
    # print(f"{Highlight.YELLOW}{all_d_values}")

    all_d_values = [d for d in range(1, 1000) if (d * e) % z == 1]
    print(f"{Highlight.YELLOW}{all_d_values}")

    # This part should not be a user input
    # This should be generated by the algorithm itself, i.e., 
    # using random.choice([list])
    # but for the sake of this discussion, we ask for 
    # user input for the value of d.
    print(f"""{Highlight.BLUE}Pls note that this step should be done by the algorithm itself
    (see comment inside the source code), and should not ask for any user input.""")
    while True:
        d = input(f"{Highlight.WHITE}Please choose your {Highlight.BLUE}d value {Highlight.WHITE}in the list highlighted in yellow: ")
        try:
            d = int(d)
            if d in all_d_values: break
            print(f"{Highlight.RED}Number is not in the list.")
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")
        
    # keys are generated using n, d, and e
    # Public key is (n, e)
    # Private key is (n, d)
    public_key = {
        'n': n,
        'e': e
    }

    private_key = {
        'n': n,
        'd': d
    }
    print(f"{Highlight.GREEN}public_key: {public_key}\nprivate_key: {private_key}\n")

    return {
        "public_key": public_key,
        "private_key": private_key
    }


def main():

    # We do not need this line of code because e and d are
    # already given. We only use this if we need to generate
    # the values for e and d.
    # keys = generate_public_private_key()

    p = 11
    q = 13
    n = p * q
    e = 7
    d = 223

    # given:
    # public_key = {n: p * q, e: 7}
    # private_key = {n: p * q, d: 223}
    print(f"""{Highlight.BLUE}
        Given:
        p = 11, q = 13
        e = 7, d = 223
        n = p * q

        public_key: (n = 143, e = 7)
        private_key: (n = 143, d = 223)
    """)

    plain_text = input(f"{Highlight.WHITE}Enter the text message you want to encrypt: ")
    encrypt(plain_text)

    cipher_text = input(f"\n{Highlight.WHITE}Enter the text message you want to decrypt: ")
    decrypt(cipher_text)

    print(Highlight.WHITE)


main()
