'''
n = 99 * 99
print(n)
num = []
for x in range(1, 9801):
    num.append(str(x))
print(num)

for each_num in num:
    if len(each_num) > 3:
        if each_num[0] + each_num[1] == each_num[3] + each_num[2]:
            print(each_num)
'''
#for each_num in num:
#    if len(num) > 3:
#        if num[0] + num[1] == num[3] + num[2]:
#            print(num)
#print(num)
#print(num[12][1])

nums = []
qnums = []
for x in range(100, 1000):
    for y in range(100, 1000):
        nums.append(str(y * x))

for each_num in nums:
    if len(each_num) > 5:
        if each_num[0] + each_num[1] + each_num[2] == each_num[5] + each_num[4] + each_num[3]:
            print(each_num)
            qnums.append(each_num)
qnums.sort()
print(qnums)

