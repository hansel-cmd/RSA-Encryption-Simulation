def encrypt(plain_text, p, q):
    # compute n = pq
    n = p * q
    # compute z = (p-1)(q-1)
    z = (p - 1) * (q - 1)

    print(f"n is {n} \nz is {z}")

    z_factors = get_factors_of_z(z)
    
    # choose number e, less than n, 
    # which has no common factor with z
    possible_numbers = [i for i in range(1, n) if i not in z_factors]
    print(possible_numbers)
    

    # we need to remove numbers in the list that do not have any number that
    # satisfies the next step: 
    # where we find d, such that ed - 1 is exactly divisible by z
    # example: n = 35, z = 24
    # numbers in the list include 9 and 10 (as these numbers have no common 
    # factor with z = 24), but 9 and 10 do not have the 'd' that will satisfy 
    # the "ed - 1 is exactly divisible by z" condition
    # even if we loop until 10,000.
    new_possible_numbers = [i for i in possible_numbers if [j for j in range (1, 1000) if ((i * j) - 1) % z == 0]]
    print(new_possible_numbers)


    while True:
        e = input("Choose a number in the list: ")
        try:
            e = int(e)
            if e in new_possible_numbers: break
            print("Number is not in the list.")
        except ValueError:
            print("Number is invalid.")
    
    print(f"e is {e}")

    # find number d, such that ed - 1 is exactly divisible by z
    all_d_values = [i for i in range (1, 1000) if ((e * i) - 1) % z == 0]
    print(all_d_values)
    
    while True:
        d = input("Please choose your d value in the list: ")
        try:
            d = int(d)
            if d in all_d_values: break
            print("Number is not in the list.")
        except ValueError:
            print("Number is invalid.")


    
    
    

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


def main():
    plain_text = input("Enter the text message you want to encrypt: ")

    # Choose the first prime number [preferrably a large prime number]
    while True:
        p = input("Enter the value of first prime p: ")
        if is_prime(p): break
        print("Sorry, input is not prime.")

    # Choose the second prime number [preferrably a large prime number]
    while True:
        q = input("Enter the value of second prime q: ")
        if is_prime(q): break
        print("Sorry, input is not prime.")

    p = int(p)
    q = int(q)
    encrypt(plain_text, p, q)



main()