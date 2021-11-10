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

    display_encrypted_char(cipher_text, plain_text)

    cipher_text = ascii(''.join(cipher_text))[1:-1]

    display_encrypted_message(cipher_text, plain_text)

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

    display_decrypted_char(cipher_text, plain_text)

    plain_text = ''.join(plain_text)

    display_decrypted_message(cipher_text, plain_text)

    return plain_text


def generate_public_private_key():

    print(f"{Highlight.YELLOW}Generate public and private key...")
    p = int(ask_for_first_prime_number())
    q = int(ask_for_second_prime_number(p))

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


    # NOTE: comment only 1 of the two
    # e = get_user_input_for_e(possible_numbers)
    e = get_random_value_for_e(possible_numbers)
    
    print(f"{Highlight.GREEN}e is {e}")


    all_d_values = [d for d in range(1, 1000) if (d * e) % z == 1]
    print(f"{Highlight.YELLOW}{all_d_values}")

    # NOTE: comment only 1 of the two
    # d = get_user_input_for_d(all_d_values)
    d = get_random_value_for_d(all_d_values)
        
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
    print(f"\n{Highlight.GREEN}The generated key/value pair\npublic_key: {public_key}\nprivate_key: {private_key}\n")

    return {
        "public_key": public_key,
        "private_key": private_key
    }


def main():

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

    # We do not need this line of code because e and d are
    # already given. We only use this if we need to generate
    # the values for e and d.
    generate_public_private_key()


    plain_text = input(f"{Highlight.WHITE}Enter the text message you want to encrypt: ")
    encrypt(plain_text)

    cipher_text = input(f"\n{Highlight.WHITE}Enter the text message you want to decrypt: ")
    decrypt(cipher_text)

    print(Highlight.WHITE)


main()


