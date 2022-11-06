# https://inf-ege.sdamgia.ru/test?id=11679346


"""
print("z w y x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((y <= z) or (not (x) and w)) == (w == z)) == 1:
                    if 0 < x + y + z + w < 4:
                        print(z, w, y, x)
"""
"""
for n in range(10**4, 10**5):
    r = str(n)
    a = int(r[0]) + int(r[2]) + int(r[4])
    b = int(r[1]) + int(r[3])
    r = f"{min(a,b)}{max(a,b)}"
    if r == "723":
        print(n)
        break
"""
"""
from turtle import *

speed(10**10)
k = 20
w = Screen()
left(90)
for i in range(14):
    right(60)
    forward(2 * k)
    right(60)
    forward(2 * k)
    right(270)
    
up()
goto(0, 0)
for x in range(-7, 20):
    for y in range(-15, 7):
        goto(x * k, y * k)
        dot(3)

w.mainloop()
"""
"""
from itertools import permutations

lst = permutations("ольга", r=5)
k = 0
for i in lst:
    s = "".join(i)
    if s[0] != "ь" and "оь" not in s and "аь" not in s:
        k += 1
print(k)
"""
"""
n = 101 * "1"
while "1111" in n:
    n = n.replace("1111", "22", 1)
    n = n.replace("222", "1", 1)
print(n)
"""
"""
n = 2 * 216**6 + 3 * 36**9 - 432
k = 0
while n != 0:
    if n % 6 == 5:
        k += 1
    n //= 6
print(k)
"""
"""
def fx(x, a):
    return ((x in a) <= (x**2 <= 81))

def fy(y, a):
    return ((y**2 <= 36) <= (y in a))

a = [i for i in range(-100, 100)]

for x in range(-100, 100):
    if not fx(x, a):
        a.remove(x)
for y in range(-100, 100):
    if not fy(y, a):
        a.remove(y)
print(a)
print(len(a) - 1)
"""
"""
def f(n):
    if n == 1:
        return 1
    return f(n - 1) * n
print(f(5))
"""
"""
with open("егэ_информатика\\17.txt") as f:
    lst = list(map(int, f.readlines()))
    m = 0
    k = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if (lst[i] % 160 != lst[j] % 160) and \
                (lst[i] % 7 == 0 or lst[j] % 7 == 0):
                k += 1
                m = max(m, lst[i] + lst[j])
print(k, m)
"""
"""
# p     1П 2В 3П 4В
# any any p>2 p==2
# any all p>3 p==3
# all any p==4 or p ==2  #p>4 # p>2

def f(x, y, p):
    if x + y >= 77 or p > 4:
        return p == 4 or p == 2

    h = [
        f(x + 1, y, p + 1),
        f(x * 2, y, p + 1),
        f(x, y + 1, p + 1),
        f(x, y * 2, p + 1)
    ]

    return all(h) if p % 2 == 0 else any(h)


for i in range(1, 70):
    if f(7, i, 0):
        print(i)
"""
"""
def f(x, y):
    if x > y or x == 33:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(3, 15) * f(15, 50))
"""
"""
with open("C:\\Users\\Андрей\\Desktop\\программирование\\егэ_информатика\\inf_22_10_20_24.txt") as f:
    k = 0
    for i in f:
        if i.count("E") > i.count("A"):
            k += 1
    print(k)
"""
"""
def f(n):
    m = 0
    if n**0.5 == int(n**0.5):
        k = 1
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                m = max(n // i, m)
                k += 2
                if k > 3:
                    return 0
        if k == 3:
            return (n, m)
    return 0


for n in range(123456789, 223456789 + 1):
    q = f(n)
    if q:
        print(q)
"""
