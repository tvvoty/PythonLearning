#a = 0
##list1 = []
#for each_number in range(505851475144, 600851475144):
#    if 600851475144 % each_number == 0:
#        list1.append(each_number)
#print(list1[-1])

#a = 12414
#list1 = [132, "haha"]

#for evx in range(1, 998002)


def sum_of_mult():
    sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

print(sum_of_mult())

