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
        return numlist
    elif numlist[0] >= numlist[1]:
        del numlist[1]
        return listmax(numlist)
    elif numlist[0] <= numlist[1]:
        del numlist[0]
        return listmax(numlist)
    else:
        print("error")


# print(listmax([1,102, 3,23, 7, 5, 8, 9,22]))


''''
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    if item = (low + high) // 2
        print(mid)
    else 
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2,3,4,5,6,7,8,9,10,11]

print("The answer:", binary_search(my_list, 9))
#print (binary_search(my_list, -1))

'''


def binary_search(listn, item):
    mid = (len(listn) - 1) // 2
    guess = listn[mid]
    if item == guess:
        return guess
    elif guess > item:
        new_list = listn[:mid - 1]
        print(new_list)
        binary_search(new_list, item)
    else:
        new_list = listn[mid:]
        print(new_list)
        binary_search(new_list, item)


print(binary_search([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12], 7))
# print (binary_search(my_list, -1))
