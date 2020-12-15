#
#
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# 08,02,22,97,38,15,00,40,00,75,04,05,07,78,52,12,50,77,91,08
# 49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,04,56,62,00
# 81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,03,49,13,36,65
# 52,70,95,23,04,60,11,42,69,24,68,56,01,32,56,71,37,02,36,91
# 22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80
# 24,47,32,60,99,03,45,02,44,75,33,53,78,36,84,20,35,17,12,50
# 32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70
# 67,26,20,68,02,62,12,20,95,63,94,39,63,08,40,91,66,49,94,21
# 24,55,58,05,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72
# 21,36,23,09,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95
# 78,17,53,28,22,75,31,67,15,94,03,80,04,62,16,14,09,53,56,92
# 16,39,05,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57
# 86,56,00,48,35,71,89,07,05,44,44,37,44,60,21,58,51,54,17,58
# 19,80,81,68,05,94,47,69,28,73,92,13,86,52,17,77,04,89,55,40
# 04,52,08,83,97,35,99,16,07,97,57,32,16,26,26,79,33,27,98,66
# 88,36,68,87,57,62,20,72,03,46,33,67,46,55,12,32,63,93,53,69
# 04,42,16,73,38,25,39,11,24,94,72,18,08,46,29,32,40,62,76,36
# 20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,04,36,16
# 20,73,35,29,78,31,90,01,74,31,49,71,48,86,81,16,23,57,05,54
# 01,70,54,71,83,51,54,69,16,92,33,48,61,43,52,01,89,19,67,48
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

big_num = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
[ 20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]


def test():
    list2 = [2, 5, 10, 100, 3, 4, 200, 1000000]
    n = list2[1]
    # print(n)
    a = list2[n + 1]
    # print(a)
    b = n * a
    # print(b)
    c = 0
    count = 0
    fn = []
    for s in list2:
        if count < len(list2) - 4:
            va1 = list2[count + 1]
            c1 = s * va1
            va2 = list2[count + 2]
            c2 = s * va2
            va3 = list2[count + 3]
            c3 = s * va3
            va4 = list2[count + 4]
            c4 = s * va4
            fn.append(c1)
            fn.append(c2)
            fn.append(c3)
            fn.append(c4)
        count += 1
    return fn



def find_biggest_product():
    """ Makes the train go boom """

    biggest_num = 0
    calculated_num = 0
    string_count = -1
    index_count = 0
    for num_string in big_num:
        string_count += 1
        print("It is string number:", str(string_count))
        index_count = 0
        print("Deleting Index count, now it is:", str(index_count))
        if string_count > 2 and string_count < 17: # make actual things
            for num in num_string:
                if index_count < 17 and index_count > 2:
                    # Horizontal axes calculation
                    calculated_num = num * big_num[string_count][index_count + 1] * big_num[string_count][index_count + 2] * big_num[string_count][index_count + 3]
                    print(str(num), '*', str(big_num[string_count][index_count + 1]), '*', str(big_num[string_count][index_count + 2]), '*', str(big_num[string_count][index_count + 3]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))

                    calculated_num = num * big_num[string_count][index_count - 1] * big_num[string_count][index_count - 2] * big_num[string_count][index_count - 3]
                    print(str(num), '*', str(big_num[string_count][index_count - 1]), '*', str(big_num[string_count][index_count - 2]), '*', str(big_num[string_count][index_count - 3]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))

                    # Vertical axes calculation
                    calculated_num = num * big_num[string_count + 1][index_count] * big_num[string_count + 2][index_count] * big_num[string_count + 3][index_count]
                    print(str(num), '*', str(big_num[string_count +1][index_count]), '*', str(big_num[string_count + 2][index_count]), '*', str(big_num[string_count + 3][index_count]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))

                    calculated_num = num * big_num[string_count - 1][index_count] * big_num[string_count - 2][index_count] * big_num[string_count - 3][index_count]
                    print(str(num), '*', str(big_num[string_count - 1][index_count]), '*', str(big_num[string_count - 2][index_count]), '*', str(big_num[string_count - 3][index_count]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))


                    # Diagonal axes calculation
                    calculated_num = num * big_num[string_count + 1][index_count + 1] * big_num[string_count + 2][index_count + 2] * big_num[string_count + 3][index_count + 3]

                    print(str(num), '*', str(big_num[string_count + 1][index_count + 1]), '*', str(big_num[string_count + 2][index_count + 2]), '*', str(big_num[string_count + 3][index_count + 3]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))

                    calculated_num = num * big_num[string_count - 1][index_count - 1] * big_num[string_count - 2][index_count - 2] * big_num[string_count - 3][index_count - 3]

                    print(str(num), '*', str(big_num[string_count - 1][index_count - 1]), '*', str(big_num[string_count - 2][index_count - 2]), '*', str(big_num[string_count - 3][index_count - 3]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))

                    calculated_num = num * big_num[string_count + 1][index_count - 1] * big_num[string_count + 2][index_count - 2] * big_num[string_count + 3][index_count - 3]


                    print(str(num), '*', str(big_num[string_count + 1][index_count - 1]), '*', str(big_num[string_count + 2][index_count - 2]), '*', str(big_num[string_count+ 3][index_count - 3]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))

                    calculated_num = num * big_num[string_count - 1][index_count + 1] * big_num[string_count - 2][index_count + 2] * big_num[string_count - 3][index_count + 3]


                    print(str(num), '*', str(big_num[string_count - 1][index_count + 1]), '*', str(big_num[string_count - 2][index_count + 2]), '*', str(big_num[string_count - 3][index_count + 3]))
                    print("The product is:", str(calculated_num))
                    if calculated_num > biggest_num:
                        biggest_num = calculated_num
                        print("The biggest product is:", str(biggest_num))



                index_count += 1
                print("Increasing index count, now it is:", str(index_count))
    return biggest_num


# print("The answer is:", str(find_biggest_product()))


def find_biggest_product_test():
    """ Makes the train go boom """

    biggest_num = 0
    calculated_num = 0
    string_count = 7
    index_count = 0
    num_string = 7
    index_count = 7
    num = big_num[6][7]
    calculated_num = num * big_num[6][8] * big_num[6][9] * big_num[6][10]
    print("10 * Hor_Right:", str(calculated_num))

    calculated_num = num * big_num[6][6] * big_num[6][5] * big_num[6][4]
    print("10 * Hor_Ledt:", str(calculated_num))

    # Vertical axes calculation
    calculated_num = num * big_num[string_count][index_count] * big_num[string_count + 1][index_count] * big_num[string_count + 2][index_count]
    print("10 * Ver_Up:", str(calculated_num))

    calculated_num = num * big_num[string_count - 2][index_count] * big_num[string_count - 3][index_count] * big_num[string_count - 4][index_count]
    print("10 * Ver_Down:", str(calculated_num))


    # Diagonal axes calculation
    calculated_num = num * big_num[string_count][index_count + 1] * big_num[string_count + 1][index_count + 2] * big_num[string_count + 2][index_count + 3]
    print("10 * Dig_Up_Right:", str(calculated_num))


    calculated_num = num * big_num[string_count - 2][index_count - 1] * big_num[string_count - 3][index_count - 2] * big_num[string_count - 4][index_count - 3]
    print("10 * Dig_Down_Left:", str(calculated_num))


    calculated_num = num * big_num[string_count][index_count - 1] * big_num[string_count + 1][index_count - 2] * big_num[string_count + 2][index_count - 3]
    print("10 * Dig_Up_Ledt:", str(calculated_num))

    calculated_num = num * big_num[string_count - 2][index_count + 1] * big_num[string_count - 3][index_count + 2] * big_num[string_count - 4][index_count + 3]
    print("10 * Dig_Down_Right:", str(calculated_num))
                
                
                


    return calculated_num

print(find_biggest_product())