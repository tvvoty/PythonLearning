from math import sqrt

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
        i = i + 1

    return True


#def is_prime_new(n):
#    for i in range(1, 2):
#        break
#
#while not is_prime()

def find_the_prime():
    prime_list = []
    x = 0
    while(len(prime_list) < 10003):
        if is_prime(x):
            prime_list.append(x)
        x += 1
    return prime_list[10000]

print(find_the_prime())

