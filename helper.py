from math import gcd
import os
os.system("")

class Highlight():
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    WHITE = '\033[37m'


# function gcd is from math module, we need this to get
# the greatest factor of both numbers
def common_factors(first_number, second_number):
    fact = gcd(first_number, second_number)
    return [i for i in range(1, fact + 1) if fact % i == 0]


def is_prime(number):

    if number > 1:
        for n in range(2, number):
                if (number % n) == 0:
                    return False
        return True
    else:
        return False

# This function will get all the coprimes of n and z
def get_co_primes(n, z):
    common_factors_of_n_and_z = []
    for i in range(2, z):
        all_cf = common_factors(i, n)
        for j in all_cf:
            common_factors_of_n_and_z.append(j)
        all_cf = common_factors(i, z)
        for j in all_cf:
            common_factors_of_n_and_z.append(j)

    possible_numbers = []
    for i in range(2, z):
        if i not in common_factors_of_n_and_z and is_prime(i):
            possible_numbers.append(i)
            
    return possible_numbers


def get_public_key_values():
    # ask user his public_key
    print(f"{Highlight.YELLOW}Please enter your PUBLIC KEY values.")
    while True:
        public_key_n = input(f"{Highlight.WHITE}n: ")
        try:
            public_key_n = int(public_key_n)
            break
        except ValueError:
            print(f"{Highlight.RED}Input is invalid.")

    while True:
        public_key_e = input(f"{Highlight.WHITE}e: ")
        try:
            public_key_e = int(public_key_e)
            break
        except ValueError:
            print(f"{Highlight.RED}Input is invalid.")
    
    return (public_key_n, public_key_e)

def get_private_key_values():
    # ask user his private_key
    print(f"{Highlight.YELLOW}Please enter your PRIVATE KEY values.")
    while True:
        private_key_n = input(f"{Highlight.WHITE}n: ")
        try:
            private_key_n = int(private_key_n)
            break
        except ValueError:
            print(f"{Highlight.RED}Input is invalid.")

    while True:
        private_key_d = input(f"{Highlight.WHITE}d: ")
        try:
            private_key_d = int(private_key_d)
            break
        except ValueError:
            print(f"{Highlight.RED}Input is invalid.")
    
    return (private_key_n, private_key_d)

