


def div35 (top, firstnum, secondnum):
    result35 = 0
    for each_number in range(1, top):
        if each_number % firstnum == 0 or each_number % secondnum == 0:
            result35 += each_number
    print(result35)


# print(div35(1000, 3, 5))
#top1 = input("Top: ")
#first = input("First: ")
#second = input("Secnond: ")
div35(int(input("Top")), int(input("fitst")), int(input("second")))
