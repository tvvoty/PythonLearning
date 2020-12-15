import os

os.chdir('')

print(os.getcwd())

namenumber = 0
for f in os.listdir():
    namenumber += 1
    print(f)
    new_name = str(namenumber) + '.jpg'
    os.rename(f, new_name)
