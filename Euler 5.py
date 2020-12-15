'''
def loo():
    x = 0
    t = 10000
    for d in range(1, t):
        if d % 1 == 0 and d % 2 == 0 and d % 3 == 0 and d % 4 == 0 and d % 5 == 0 and d % 6 == 0 and d % 7 == 0 and d % 8 == 0 and d % 9 == 0 and d % 10 == 0 and d % 11 == 0 and d % 12 == 0 and d % 13 == 0 and d % 14 == 0 and d % 15 == 0 and d % 16 == 0 and d % 17 == 18 and d % 19 == 0 and d % 20 == 0:
         print(d)
        else: t += t
        loo()


loo()


x = 0
t = 10000
for d in range(1000000000, 2000000000):
    if d % 1 == 0 and d % 2 == 0 and d % 3 == 0 and d % 4 == 0 and d % 5 == 0 and d % 6 == 0 and d % 7 == 0 and d % 8 == 0 and d % 9 == 0 and d % 10 == 0 and d % 11 == 0 and d % 12 == 0 and d % 13 == 0 and d % 14 == 0 and d % 15 == 0 and d % 16 == 0 and d % 17 == 18 and d % 19 == 0 and d % 20 == 0:
        print(d)


%x = 0
t = 10000
for d in range(3000):
        if d % 1 == 0 and d % 2 == 0 and d % 3 == 0 and d % 4 == 0 and d % 5 == 0 and d % 6 == 0 and d % 7 == 0 and d % 8 == 0 and d % 9 == 0 and d % 10 == 0:
            print(d)
'''


def is_divisible(n):
    for i in range(11, 21):
        if n % i == 0:
            continue
        else:
            return False
    return True

x = 2520

while not is_divisible(x):
    x += 2520

print(x)



