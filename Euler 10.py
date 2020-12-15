from math import sqrt
import functools

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2 # can be i + 1 but it's slower and i guess it works anyway idk

    return True


#def is_prime_new(n):
#    for i in range(1, 2):
#        break
#
#while not is_prime()

# vvv from Euler 7 vvv
def find_the_prime():
    prime_list = []
    x = 0
    while(len(prime_list) < 10003):
        if is_prime(x):
            prime_list.append(x)
        x += 1
    return prime_list[10000]

def summation_of_primes():
    prime_sum_list = []
    x = 0
    while x <= 2000000:
        if is_prime(x):
            prime_sum_list.append(x)
        x += 1
    return prime_sum_list


def list_sum():
    print("The summation of primes is:", functools.reduce(lambda a, b: a + b, summation_of_primes()))

print(summation_of_primes())
list_sum()

