arr1 = [2, 4, 6]


def rec_sum(arr):
    total = 0
    print(arr)
    if len(arr) == 0:
        print(total)
        return 0
    else:
        total = arr1.pop(0) + rec_sum(arr1)


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def sum(numlist):
    lists_sum = numlist[0] + numlist[1:]


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


def listamount(numlist):
    if numlist == []:
        return 0
    else:
        return 1 + listamount(numlist[1:])





def listmax(numlist):
    if len(numlist) == 1:
        return numlist[0]
        print(numlist[0])
    elif numlist[0] >= numlist[1]:
        x = numlist[0]
        print(numlist[0])
        return x > listmax(numlist[1:])
    elif numlist[0] <= numlist[1]:
        x = numlist[1]
        print(numlist[1])
        return x > listmax(numlist[1:])
    else:
        print("error")

print(listmax([1, 33, 4, 5, 8, 22]))
