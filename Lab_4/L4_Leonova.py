# Функция для проверки разных реализаций вычисления НОД(a,b)
def check(nod_func):
    print(nod_func(0, 105))
    print(nod_func(1, 105))
    print(nod_func(91, 105))
    print(nod_func(100000, 100))
    print(nod_func(12345, 678))
    print(nod_func(12345, 24690))


# 1. Алгоритм Евклида
def nod1(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == 1 or b == 1:
        return 1
    if a < b:
        a, b = b, a

    d = nod1(a % b, b)
    return d


# 2. Бинарный алгоритм Евклида
def nod2(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == 1 or b == 1:
        return 1
    if a < b:
        a, b = b, a

    g = 1
    if a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        g *= 2
    
    d = int( g * nod2(a - b, b) )
    return d


# 2. Расширенный алгоритм Евклида
# d = НОД(a,b) = ax + by
def nod3(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == 1 or b == 1:
        return 1
    if a < b:
        a, b = b, a

    x, y = [1,0], [0,1]
    a_, b_ = a, b
    
    while b_ != 0:
        a_, b_, p = b_, a_ % b_, a_ // b_
        
        if b_ != 0:
            x[0], x[1] = x[1], x[0] - p*x[1]
            y[0], y[1] = y[1], y[0] - p*y[1]
        
    d = a_
    print(a,'*',x[1],' + ',b,'*',y[1],' = ',d)
    return d


# 2. Расширенный бинарный алгоритм Евклида
def nod4(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == 1 or b == 1:
        return 1
    if a < b:
        a, b = b, a

    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        g *= 2
        
    a, b, g = int(a), int(b), int(g)
    u, v, A, B, C, D = a, b, 1 , 0, 0, 1
      
    while u != 0:
        while u % 2 == 0:
            u /= 2
            if A % 2 == 0 and B % 2 == 0:
                A /= 2
                B /= 2
            else:
                A = (A + b) / 2
                B = (B - a) / 2
                
        while v % 2 == 0:
            v /= 2
            if C % 2 == 0 and D % 2 == 0:
                C /= 2
                D /= 2
            else:
                C = (C + b) / 2
                D = (D - a) / 2
        
        if u >= v:
            u, A, B = u-v, A-C, B-D
        else:
            v, C, D = v-u, C-A, D-B
            
    A, B, C, D = int(A), int(B), int(C), int(D)        
    d = int( g * v )
    print(a,'*',C,' + ',b,'*',D,' = ',d)
    return d


print('Алгоритм Евклида')
print(check(nod1))

print('\nБинарный алгоритм Евклида')
print(check(nod2))

print('\nРасширенный алгоритм Евклида')
print(check(nod3))

print('\nРасширенный бинарный алгоритм Евклида')
print(check(nod4))
