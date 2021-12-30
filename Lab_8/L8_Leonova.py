# 1. Сложение неотрицательных целых чисел 
# b - система счисления
def algoritm1(u, v, b):
    n = len(u)
    print('* ', u, v, n, b)
    if len(u) != len(v):
        return print('Ошибка, числа разной разрядности')
    
    u, v, w = list(u), list(v), []
    k = 0

    for j in range(n-1,-1,-1):
        a = int(u[j]) + int(v[j]) + k
        w.append(a % b)
        k = a // b
        #print(j, a, w, k)
                 
    w.append(k)
    res = ''
    for i in w[::-1]:
        res += str(i)
    return res


# 2. Вычитание неотрицательных целых чисел 
def algoritm2(u, v, b):
    n = len(u)
    print('* ', u, v, n, b)
    if int(u) < int(v):
        return print('Ошибка, u < v')
    if len(u) != len(v):
        return print('Ошибка, числа разной разрядности')
    
    u, v, w = list(u), list(v), []
    k = 0

    for j in range(n-1,-1,-1):
        a = int(u[j]) - int(v[j]) + k
        w.append(a % b)
        k = a // b
        #print(j, a, w, k)
                 
    w.append(k)
    res = ''
    for i in w[::-1]:
        res += str(i)
    return res


# 3. Умножение неотрицательных целых чисел столбиом
def algoritm3(u, v, b):
    if u < v:
        u, v = v, u
    print('* ', u, v, b)
    
    n = len(u)
    m = len(v)
    u, v = list(u), list(v)
    w = [0] * (m + n)
    
    for j in range(m-1,-1,-1):
        if v[j] != 0:
            k = 0
            for i in range(n-1,-1,-1):
                t = int(u[i]) * int(v[j]) + w[i+j+1] + k
                w[i+j+1] = t % b 
                k = t // b
                #print(j,i, t, w, k)
            
            w[j] = k

    res = ''
    for i in w:
        res += str(i)
    return res


# 4. Быстрый столбик
def algoritm4(u, v, b):
    if u < v:
        u, v = v, u
    print('* ', u, v, b)
    
    t = 0
    n = len(u)
    m = len(v)
    u, v = list(u), list(v)
    w = [0] * (m + n)
    
    for s in range(0, m + n):
        for i in range(0, s + 1):
            if 0 <= n-i-1 < n and 0 <= m-s+i-1 < m:
                t += int(u[n-i-1]) * int(v[m-s+i-1])
        
        #print(s, i, t)
        w[m+n-s-1] = t % b
        t = t // b

    res = ''
    for i in w:
        res += str(i)
    return res


# словарь {символ: число}
str2num = {chr(i) : (i - ord('A') + 10) for i in range(ord('A'),ord('Z'))}
for i in '0123456789':
    str2num[i] = int(i)
# словарь {число: символ}
num2str = {value : key for (key, value) in str2num.items()}


# перевод b-ичного числа в десятичное
def to_10(u_str, b, array = False):
    # array = True, если число u передано в виде массива чисел
    u_array = u_str if array else [str2num[letter] for letter in u_str]
    u = 0
    for i in range(len(u_array)):
        u += (b ** i) * u_array[len(u_array) - i - 1]
    return u


# перевод десяичного числоа в b-ичное
def to_b(u, b):
    q, r = u // b, u % b    # частное q и остаток r
    w = num2str[r]

    while q >= b:
        q, r = q // b, q % b
        w += num2str[r]

    if q != 0: w += num2str[q]
    
    return w[::-1]


# 5. Деление многоразрядных целых чисел
# Возвращает: частное q, остаток r
def algoritm5(u_str, v_str, b):
    u = u_str; v = v_str;
    n = len(u) - 1; t = len(v) - 1 # разрядности чисел
    print('* ', u, v, n, t, b) 
    u_10 = to_10(u, b); v_10 = to_10(v, b)
    if v[0] == 0 or not (n >= t >= 1):
        return "Некорректные входные данные"

    q = [0] * (n - t + 1)
    # шаг 2
    while u_10 >= v_10 * (b ** (n - t)):
        q[n - t] += 1
        u_10 -= v_10 * b ** (n - t)

    u = to_b(u_10, b)
    
    u = [str2num[letter] for letter in u]
    v = [str2num[letter] for letter in v_str]

    # шаг 3
    for i in range(n, t, -1):
        if u[n - i] >= v[0]:
            q[i-t-1] = b - 1
        else:
            q[i-t- 1] = (u[n-i] * b + u[n-i+1]) // v[0]
        
        while q[i-t-1] * (v[0]*b + v[1]) > u[n-i] * (b**2) + u[n-i+1]*b + u[n-i+2]:
            q[i-t-1] -= 1
        
        u_10 = to_10(u, b, True)
        u_10 -= v_10 * q[i-t-1] * (b ** (i-t-1))

        if u_10 < 0:
            u_10 += v_10 * (b ** (i-t-1))
            q[i-t-1] -= 1

        u = to_b(u_10, b); u = [str2num[letter] for letter in u]

    res = ''
    for i in q[::-1]:
        res += str(i)
    res += ', '
    for i in u:     # r
        res += str(i)
    return res


def check(f):
    print('Результат: ',f('34','12', 10))
    print('Результат: ',f('1234','567', 10))
    print('Результат: ',f('67890','12345', 10))
    print('Результат: ',f('11','10', 2))
    print('Результат: ',f('1100101','1010101', 2))
    
    
print('1. Сложение неотрицательных целых чисел') 
check(algoritm1)

print('\n2. Вычитание неотрицательных целых чисел')
check(algoritm2)

print('\n3. Умножение неотрицательных целых чисел столбиом')
check(algoritm3)

print('\n4. Быстрый столбик')
check(algoritm4)

print('\n5. Деление многоразрядных целых чисел') 
check(algoritm5)
print('Результат: ',algoritm5('DEF','ABC', 16))