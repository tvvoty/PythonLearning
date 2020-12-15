




f = open('C:\\Users\\Windows 8.1\\Desktop\\QWERTY to Colemak fused uni 1.ahk', 'r+', encoding='utf-8')


for line in f:
    # print(line)
    word_list = []
    finline = ''

    for char in line:
        # print(char)
        word_list.append(char)
    # print(word_list)
    if word_list[0] == '\ufeff':
        del word_list[0]
    del word_list[-1]
    # print(word_list)
    word_list[3] = word_list[3].upper()
    # print(word_list)
    for it in word_list:
        finline += it
    print(finline)


for num in [1,2,3,4]
    pring(n)
