import random

# 1. Тест Ферма
def test_Ferma(n):
    print('')
    if n % 2 == 0:
        return print('Ошибка: число ', n,' чётное')
    if n < 5:
        return print('Ошибка: число ', n,' < 5')
    
    a = random.randint(2, n - 2)
    r = ( a ** (n - 1) ) % n
    
    if r == 1:
        return print('Число ', n,' , вероятно, простое')
    else:
        return print('Число ', n,' составное')
    
    
# 2. Символ Якоби
def Yakobi(n, a):
    print('# символ Якоби (', a,'/',n,')')
    if n % 2 == 0:
        return print('Ошибка: число ', n,' чётное')
    if n < 3:
        return print('Ошибка: число n (', n,') < 3')
    if a < 0 or a >= n:
        return print('Ошибка: число a (', a,') некорректно')
    
    g = 1
    
    while True:
        if a == 0:
            return 0
        if a == 1:
            return g
        
        k = 0
        while a % (2**k) == 0:
            k += 1
        k -= 1
            
        a1 = a / (2**k)
        #print(a, ' = 2 ^', k, ' * ', a1)
        
        s = 0
        if k % 2 == 0:
            s = 1
        else:
            if (n - 1) % 8 == 0 or (n + 1) % 8 == 0:
                s = 1
            if (n - 3) % 8 == 0 or (n + 3) % 8 == 0:
                s = -1
            
        if a1 == 1:
            return g*s
        
        if (n - 3) % 4 == 0 and (a1 - 3) % 4 == 0:
            s = -s
            
        a = n % a1
        n = a1
        g = g*s


# 3. Тест Соловэя-Штрассена
def test_Sol_Shtr(n):
    print('')
    if n % 2 == 0:
        return print('Ошибка: число ', n,' чётное')
    if n < 5:
        return print('Ошибка: число ', n,' < 5')
    
    a = random.randint(2, n - 3)
    r = ( a ** ((n - 1)/2) ) % n
    
    if r != 1 and r != n-1:
        return print('Число ', n,' составное')
    
    s = Yakobi(n, a)
    
    if (r - s) % n != 0:
        return print('Число ', n,' составное')
    else:
        return print('Число ', n,' , вероятно, простое')
    
    
# 4. Тест Миллера-Рабина
def test_Mil_Rab(n):
    print('')
    if n % 2 == 0:
        return print('Ошибка: число ', n,' чётное')
    if n < 5:
        return print('Ошибка: число ', n,' < 5')
    
    s = 0
    while n - 1 % (2**s) == 0:
        s += 1
    s -= 1
    r = (n - 1) / (2**s)
    #print(n - 1, ' = 2 ^', s, ' * ', r)
    
    a = random.randint(2, n - 3)
    y = ( a ** r ) % n
    
    if y != 1 and y != n-1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = (y*y) % n
            if y == 1:
               return print('Число ', n,' составное')
            j += 1
        if y != n - 1:
            return print('Число ', n,' составное')
    
    return print('Число ', n,' , вероятно, простое')


# Функция проверки функций тестов
def check(f):
    f(1)
    f(1122)
    f(11)
    f(27)
    f(31)


print('Тест Ферма')
check(test_Ferma)

print('\n-----------------------------------')
print('Символ Якоби')
print('Результат:', Yakobi(27, 5))
print('Результат:', Yakobi(27, 12))
print('Результат:', Yakobi(51, 13))

print('\n-----------------------------------')
print('Тест Соловэя-Штрассена')
check(test_Sol_Shtr)

print('\n-----------------------------------')
print('Тест Миллера-Рабина')
check(test_Mil_Rab)