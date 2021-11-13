# 1. Реализовать шрифт Цезаря с произвольным ключом k

# с изменением всех символов
print('Шрифт Цезаря с изменением всех символов')

def Cesar0(text, k):
    res = ''
    for i in text:
        e = ord(i) + k
        res += chr(e)
    return res

def de_Cesar0(text, k):
    res = ''
    for i in text:
        e = ord(i) - k
        res += chr(e)
    return res

k = 3
r = Cesar0('Veni, vidi, vici',k)
print(r)
print(de_Cesar0(r,k))


# алфавиты
print('\nАлфавиты:')
ru = [chr(i) for i in range ( ord('А'), ord('я') + 1)]
en = [chr(i) for i in range ( ord('A'), ord('Z') + 1)] + [chr(i) for i in range ( ord('a'), ord('z') + 1)]
print('ru = ',ru)
print('\nen = ',en)


# по заданному алфавиту
print('\nШрифт Цезаря по заданному алфавиту')

def Cesar(text, k, abc):
    res = ''
    for i in text:
        if i in abc:
            n = abc.index(i)
            e = (n+k) % len(abc)
            res += abc[e]
        else:
            res += i
    return res

def de_Cesar(text, k, abc):
    res = ''
    for i in text:
        if i in abc:
            n = abc.index(i)
            e = (n-k) % len(abc)
            res += abc[e]
        else:
            res += i
    return res

k = 3
r = Cesar('Veni, vidi, vici', k, en)
print(r)
print(de_Cesar(r, k, en))
k = 1000
r = Cesar('Торопись медленно', k, ru)
print(r)
print(de_Cesar(r, k, ru))


# 2. Реализовать шрифт Атбаш
print('\nШрифт Атбаш')

def Atbash(text, abc):
    res = ''
    for i in text:
        if i in abc:
            e = abc.index(i)
            res += abc[-e-1]
        else:
            res += i
    return res

r = Atbash('абвгд', ru)
print(r)
print(Atbash(r,ru))
r = Atbash('Hello, world!', en)
print(r)
print(Atbash(r,en))