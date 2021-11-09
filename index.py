from helper import Highlight
from helper import Replace


# TODO
# Encryption c = m^e mod n
# c is the cipher text
# m is the plain plain text
def encrypt(plain_text):

    # ask user his public_key
    print(f"{Highlight.YELLOW}Please enter your public key values.")
    while True:
        public_key_n = input(f"{Highlight.WHITE}n: ")
        try:
            public_key_n = int(public_key_n)
            break
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")

    while True:
        public_key_e = input(f"{Highlight.WHITE}e: ")
        try:
            public_key_e = int(public_key_e)
            break
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")

    print("Encrypting...")
    # encrypt each plain text characters to ascii code
    # we need % 127 so as to prevent from going outside
    # the ascii boundary
    cipher_text = [chr(ord(i) ** public_key_e % public_key_n % 127) for i in plain_text]
    
    plain_text = [i for i in plain_text]
    print(f"{Highlight.YELLOW}Original message letters:", plain_text)
    print(f"{Highlight.YELLOW}Encrypted message letters:", cipher_text)

    print(f"{Highlight.GREEN}Original message: '{''.join(plain_text)}'")
    print(f"{Highlight.GREEN}Encrypted message:", ascii(''.join(cipher_text)))

    return cipher_text

# TODO
# Decryption m = c^d mod n
# c is the cipher text
# m is the plain plain text
def decrypt(cipher_text):
    
    # ask user his private_key
    print(f"{Highlight.YELLOW}Please enter your private key values.")
    while True:
        private_key_n = input(f"{Highlight.WHITE}n: ")
        try:
            private_key_n = int(private_key_n)
            break
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")

    while True:
        private_key_d = input(f"{Highlight.WHITE}d: ")
        try:
            private_key_d = int(private_key_d)
            break
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")

    print("Decrypting...")
    
    # Since we have hex value for ascii codes that
    # are not printable, i.e., backspace, shift out/in
    # we need to encode the string as ascii
    # this results to -> 'SAMPLE\x08WORLD'
    cipher_text = ascii(cipher_text.encode().decode('unicode_escape'))

    # Since a string will typically use escape character,
    # i.e., 'SAMPLE\\x08...', we have to replace this type
    # of pattern with its true value (hex ascii code)
    cipher_text = Replace.replace_to_ascii(cipher_text)
    cipher_text = [i for i in cipher_text]

    # decrypt each character from the cipher text
    plain_text = [chr(ord(i) ** private_key_d % private_key_n % 127) for i in cipher_text]

    print(f"{Highlight.YELLOW}Encrypted message letters:", cipher_text)
    print(f"{Highlight.YELLOW}Decrpyted message letters:", plain_text)

    print(f"{Highlight.GREEN}Encrypted message:", ascii(''.join(cipher_text)))
    print(f"{Highlight.GREEN}Decrypted message: '{''.join(plain_text)}'")

    return plain_text

    
def get_factors_of_z(number):
    return [factor for factor in range (1, number + 1) if number % factor == 0]


def is_prime(number):

    try:
        number = int(number)
    except ValueError:
        return False

    if number > 1:
        for n in range(2, number):
                if (number % n) == 0:
                    return False
        return True
    else:
        return False


def generate_public_private_key():

    print(f"{Highlight.YELLOW}Generate public and private key...")
    # Choose the first prime number [preferrably a large prime number]
    while True:
        p = input(f"{Highlight.WHITE}Enter the value of first prime p: ")
        if is_prime(p): break
        print(f"{Highlight.RED}Sorry, input is not prime.")

    # Choose the second prime number [preferrably a large prime number]
    while True:
        q = input(f"{Highlight.WHITE}Enter the value of second prime q: ")
        if is_prime(q): break
        print(f"{Highlight.RED}Sorry, input is not prime.")

    p = int(p)
    q = int(q)

    # compute n = pq
    n = p * q
    # compute z = (p-1)(q-1)
    z = (p - 1) * (q - 1)

    print(f"{Highlight.GREEN}n is {n} \nz is {z}")

    z_factors = get_factors_of_z(z)
    
    # choose number e, less than n, 
    # which has no common factor with z
    possible_numbers = [i for i in range(1, n) if i not in z_factors]

    # we need to remove numbers in the list that do not have any number that
    # satisfies the next step: 
    # where we find d, such that ed - 1 is exactly divisible by z
    # example: n = 35, z = 24
    # numbers in the list include 9 and 10 (as these numbers have no common 
    # factor with z = 24), but 9 and 10 do not have the 'd' that will satisfy 
    # the "ed - 1 is exactly divisible by z" condition
    # even if we loop until 10,000.
    new_possible_numbers = [i for i in possible_numbers if [j for j in range (1, 1000) if ((i * j) - 1) % z == 0]]
    print(f"{Highlight.YELLOW}{new_possible_numbers}")

    # This part should not be a user input
    # This should be generated by the algorithm itself, i.e., 
    # using random.choice([list])
    # but for the sake of this discussion, we ask for 
    # a user input for the value of e.
    print(f"""{Highlight.BLUE}Pls note that this step should be done by the algorithm itself
    (see comment inside the source code), and should not ask for any user input.""")
    while True:
        e = input(f"{Highlight.WHITE}Please choose your {Highlight.BLUE}e value {Highlight.WHITE}in the list highlighted in yellow: ")
        try:
            e = int(e)
            if e in new_possible_numbers: break
            print(f"{Highlight.RED}Number is not in the list.")
        except ValueError:
            print(f"{Highlight.RED}Number is invalid.")
    
    print(f"{Highlight.GREEN}e is {e}")

    # find number d, such that ed - 1 is exactly divisible by z
    all_d_values = [i for i in range (1, 1000) if ((e * i) - 1) % z == 0]
    print(f"{Highlight.YELLOW}{all_d_values}")
    
    # This part should not be a user input
    # This should be generated by the algorithm itself, i.e., 
    # using random.choice([list])
    # but for the sake of this discussion, we ask for 
    # a user input for the value of d.
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

    keys = generate_public_private_key()
    
    plain_text = input(f"{Highlight.WHITE}Enter the text message you want to encrypt: ")

    encrypt(plain_text, keys["public_key"]["e"], keys["public_key"]["n"])

    cipher_text = input(f"{Highlight.WHITE}Enter the text message you want to decrypt: ")
    decrypt(cipher_text)

    


main()