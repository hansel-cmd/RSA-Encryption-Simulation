


    



p = 2
q = 7
n = 14
# phi
z = 6


# choose e, where 1 < e < z
# where e should be coprime with z = 10 and 
# coprime with n = 22
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

print(possible_numbers)





