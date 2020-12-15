def sumofsq():
    total1 = 0
    for x in range(1, 101):
        total1 = total1 + x**2
    return total1

print(sumofsq())

def sqrofsum():
    total2 = 0
    for x in range(1, 101):
        total2 = total2 + x
    sqrsum1 = total2**2
    return sqrsum1

print(sqrofsum())

def sumoftwo():
    notsum = sqrofsum() - sumofsq()
    return notsum

print(sumoftwo())


