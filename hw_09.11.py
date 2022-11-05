"""============================================================================="""
# вариант 9117
"""
print("c b a")
for a in range(2):
    for b in range(2):
        for c in range(2):
            if ((a and not (c)) or (not (b) and not (c))) == 1:
                print(c, b, a)
"""
"""
q = set()
for n in range(1, 10**5):
    r = bin(n)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    r = int(r, 2)
    if r < 100:
        q.add(r)
print(len(q))
"""
"""
from itertools import permutations

lst = permutations("панель", r=6)
k = 0
for i in lst:
    s = "".join(i)
    if s[0] != 'ь' and "еь" not in s:
        k += 1
print(k)
"""
"""
lst = []
for i in range(1, 100):
    n = 81 * '1' + i * '1'
    while "111" in n:
        n = n.replace("111", "2", 1)
        n = n.replace("2222", "1", 1)
    lst.append((n.count("1"), 81 + i))
print(sorted(lst, key=min))
"""
"""
n = 5**55 + 5**555 * 555 - 5
k = 0
while n != 0:
    if n % 5 == 0:
        k += 1
    n //= 5
print(k)
"""
"""
def f(n):
    if n < 1:
        return n
    if n % 2 == 0:
        return n + 3 * f(n - 3)
    return 5 * n + 2 * f(n - 5)

print(f(30))
"""
"""
def f(x, y):
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)

print(f(1, 10) * f(10, 15))
"""
"""
# any any p == 2
# any all p == 3
# all any # p==4 or p==2 # p>4 # p>4
def f(x, y, p):
    if x + y >= 75 or p > 4:
        return p==4 or p == 2
    
    h = [f(x + 1, y, p + 1), f(x *2, y, p + 1), f(x, y+1, p + 1), f(x, y*2, p + 1)]

    return all(h) if p % 2 == 0 else any(h)


for i in range(1,67):
    if f(8,i,0) == 1:
        print(i)
"""
"""============================================================================="""
"""============================================================================="""
# вариант 32531
"""
print("y x z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not(x) or z) and (not(x) or not(y) or not(z))) == 0:
                print(y, x, z)
"""
"""
for n in range(1, 1000):
    if int(bin(n)[2:][::-1], 2)== 23:
        print(n)
"""
"""
from itertools import permutations

lst = permutations("магистр", r=5)
k = 0
for i in lst:
    s = "".join(i)
    if (s.count("и") <= 1 and s.count("а") == 0) or (s.count("и") == 0 and s.count("а") <= 1):
        k += 1
print(k)
"""
"""
n = 93 * "8"
while '222' in n or '888' in n:
    if '222' in n:
        n = n.replace('222', '8', 1)
    else:
        n = n.replace('888', '2', 1)
print(n)
"""
"""
n = 2 * 9**10 - 3**5 + 5
k = 0
while n != 0:
    if n % 3 == 2:
        k += 1
    n //= 3
print(k)
"""
"""
def f(n):
    if n == 0: return 2
    if n <= 15: return f(n - 1)
    if n < 95: return 1.6 * f(n - 3)
    return 3.3 * f(n - 2)

print(f(33))
"""
"""
# all any p == 2
# any all p == 3
# all any # p==4 or p==2 # p>4 # p>2
def f(x, y, p):
    if x + y <= 20 or p > 2:
        return p == 4 or p == 2
    
    h = [f(x - 1, y, p + 1), f(x, y - 1, p + 1)]
    
    if x % 2 == 0:
        h.append(f(x // 2, y, p + 1))
    else:
        h.append(f(x // 2 + 1, y, p + 1))
        
    if y % 2 == 0:
        h.append(f(x, y // 2, p + 1))
    else:
        h.append(f(x, y // 2 + 1, p + 1))
        
    return all(h) if p % 2 == 0 else any(h)


for i in range(11,150):
    if f(10, i, 0) == 1:
        print(i)
"""
"""
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y)


print(f(1, 7) * f(7, 12))
"""
"""============================================================================="""
"""============================================================================="""
# вариант 69857
"""
print('b c a')
for a in range(2):
    for b in range(2):
        for c in range(2):
            if ((a and b) or (c and (not (a) or b))) == 1:
                print(b, c, a)
"""
"""
for n in range(1, 10**3):
    r = bin(n)[2:]
    if r.count("1") > r.count("1"):
        r += "0"
    else:
        r += "0"
    r = int(r, 2)
    if r < 100:
        print(r)
"""
"""
from itertools import product

k = 0
for r in range(3, 8):
    lst = product("ксения", repeat=r)
    for i in lst:
        s = "".join(i)
        if (s[1:].count('к') == s[1:].count('с') == s[1:].count('н') == 0) \
            and (s.count('е') <= 2) and (s.count('и') <= 2) \
                and (s.count('я') <= 2):
            k += 1
print(k)
"""
"""
n = 123 * "4"
while "4444" in n or "7777" in n:
    if "4444" in n:
        n = n.replace("4444", "77", 1)
    else:
        n = n.replace("7777", "44", 1)
print(n)
"""
"""
def f(x, y):
    s = ''
    while x != 0:
        s = str(x % y) + s
        x //= y
    return sum(int(i) for i in s)

lst = []
for i in range(2, 11):
    lst.append((f(2345, i), i))
print(sorted(lst))
"""
"""
def f(n):
    if n <= 1: return 3
    return f(n - 1) + 2 * f(n - 2) - 5

print(f(122))
"""
"""
# p>2 p==2 any any
# p>3 p==3 any all
# all any p==2 or p==4 # p>2 # p>4
def f(x, y, p):
    if x + y >= 78 or p > 4:
        return p == 2 or p == 4
    h = [
        f(x + 3, y, p + 1),
        f(x * 2, y, p + 1),
        f(x, y + 3, p + 1),
        f(x, y * 2, p + 1)
    ]
    return all(h) if p % 2 == 0 else any(h)

for i in range(1, 71):
    if f(7, i, 0):
        print(i)
"""
"""
def f(x, y):
    if x > y or x == 18:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y)

print(f(3, 12) * f(12, 21))
"""
