a = int(input())
b = str(a)
c = a -1
d = 0
print(2)
for i in range(2,a**10):
    if i % 2 != 0:
        if str(i) == str(i)[::-1] and c > 0:
            print(i)
            c = c-1
