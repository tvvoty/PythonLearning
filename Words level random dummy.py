import random
# weights_list2 = []
# wei_count = 0.1
# for x in range(1, 10001):
#     wei_count = wei_count * 1.0006
#     weights_list.append(wei_count)
#
# print(weights_list)

level_list = list(range(1, 10001))
print(level_list)
weightlist = list(range(1, 10001))
# weightlist.reverse()
print(weightlist)
image_word_list = random.choices(level_list, weights=weightlist, k=1000)
print(image_word_list)

def averege_word_level():
    sum_of_words = 0
    for each_word_level in image_word_list:
        sum_of_words += each_word_level
    print(sum_of_words)
    print(len(image_word_list))
    average_sum = sum_of_words / len(image_word_list)
    return average_sum
print(averege_word_level())