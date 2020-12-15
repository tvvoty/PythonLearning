a = 1
b = 2
c = 0
s = 0
list1 = [1, 2]

while c < 4000000:
    c = a+b
    a = b
    b = c
    list1.append(c)
print(list1)

for x in list1:
    if x % 2 == 0:
        s = s + x

print(s)




#second try


