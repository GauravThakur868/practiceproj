a = int(input())
b = str(a)
c = a -1
d = 0
print(2)
for i in range(2,a**10):
    if i % 2 != 0:
        if str(i) == str(i)[::-1] and c > 0:
            if i%2!=0 and i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%6!=0 and i%7!=0 and i%8!=0 and i%9!=0:
                print(i)
                c = c-1
