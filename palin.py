a = int(input())
b = str(a)
rev = 0
for i in range(2,a):
    if i % 2 != 0:
        if str(i) == str(i)[::-1]:
            print(i)