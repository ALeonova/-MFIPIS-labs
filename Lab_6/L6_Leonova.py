# Алгоритм Евклида
def nod(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == 1 or b == 1:
        return 1
    if a < b:
        a, b = b, a
    d = nod(a % b, b)
    return d


# Функция
def eval_(f, x, n):
    return eval(f)


# p-метод Полларда
def Pollard(n, c, f):
    print('n = ', n, '; c = ', c,'; f = ', f)
    a, b = c, c

    while True:
        a = eval_(f, a, n) % n
        b = eval_(f, eval_(f, b, n), n) % n
        print('a = ',a,' b = ',b)
        
        if a - b < 0:
            d = 1
        else:
            d = nod(a-b, n)
        
        if 1 < d and d < n:
            return d
        if d == n:
            return print('Делитель не найден')
        if d == 1:
            print('1')


print('p-метод Полларда')
print('Результат: ',Pollard(1359331, 1, '(x**2 + 5) % n'))
