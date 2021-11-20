import numpy as np
import math

def grid_reading(key, table):
    _key = sorted(key)
    order = [key.index(i) for i in _key]
    print(list(key))
    #print(_key)
    print('Порядок использования столбцов:', order)
    m = table.shape[0]
    res = ''
    for j in order:
        for i in range(m):
            res += table[i][j]
    return res

ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
print('ru: ',ru)

print('####################################################################')
# 1. Маршрутное шифрование
print('# 1.')
def task1_rout(text, key):
    print('Текст: ', text)
    text = text.replace(' ','').lower()
     
    print('Ключ:', key)
    key = key.lower()
    
    n = len(key)
    t_len = len(text)
    m = math.ceil(t_len/n)
    A = np.full((m,n),'')
    print('Длина текста:', t_len)
    print('n = ', n, '\nm = ', m)
    
    for k in range(n*m - t_len):
        text += text[-1]
    #print(text)
    
    k = 0
    for i in range(m):
        for j in range(n):
            A[i][j] = text[k]
            k += 1
    print(A)
    
    res = grid_reading(key, A)
    
    print('Криптограмма: ', res)
    

text = 'Нельзя недооценивать противника'
key = 'пароль'
task1_rout(text, key)

print('----------------------------------------------------')
text = 'Live long and prosper'
key = 'Spock'
task1_rout(text, key)

print('####################################################################')
# 2. Шифрование с помощью решеток

def rotate_90r(A):
    x = A.shape[0]
    y = A.shape[1]
    res = np.empty((y,x))
    for i in range(x):
        for j in range(y):
            res[j, x-1-i] = A[i,j]
    return res
    
def generate_key(lenth):
    key = ''
    while (len(key) != lenth):
        _key = np.random.randint(len(ru))
        if (key.count(ru[_key]) == 0):
            key += ru[_key]
    return key
    

print('# 2.')
def task2_grid(text):
    print('Текст: ', text)
    text = text.replace(' ','').lower()
    
    t_len = len(text)
    print('Длина текста:', t_len)
       
    size = math.ceil(np.sqrt(t_len))    # количество чисел в маленькой таблице
    while size % np.sqrt(size) != 0:
        size += 1
    
    for k in range(size*size - t_len):
        text += text[-1]
    
    t_s = int(np.sqrt(size))    # размер малькой таблицы
    t_s2 = t_s * 2      # размер большой таблицы
    t_el = np.arange(1,size+1)     # массив значений size
    
    key = generate_key(t_s2)    
    #key = 'шифр'
    print('Ключ:', key)
    key = key.lower()
    
    
    A0 = np.empty((t_s,t_s)) 
    n = 0
    for i in range(t_s):
        for j in range(t_s):
            A0[i][j] = t_el[n]
            n += 1
        
    A1 = np.concatenate((A0,rotate_90r(A0)),axis=1)
    A2 = np.concatenate((A1,rotate_90r(rotate_90r(A1))),axis=0)  
    #print(A0)
    #print(A1)
    print('Квадрат цифр:\n', A2)
     
    R = np.zeros((t_s2,t_s2))
    tmp = t_el.copy()
    for k in range (size):
        r = np.random.randint(4)
        tmp_count = 0
        for i in range (t_s2):
            for j in range (t_s2):
                if (A2[i][j] == k + 1):
                    if(tmp_count == r):
                        R[i][j] = A2[i][j]
                        tmp_count = -100
                        tmp = tmp[tmp != k+1]
                    else:
                        tmp_count += 1
    print('Сгенерированная схема:\n', R)
    
    n = 0
    answer = np.full((t_s2, t_s2),'')
    
    for k in range(4):
        for i in range(t_s2):
            for j in range(t_s2):
                if(R[i][j] != 0):
                    answer[i][j] = text[n]
                    n += 1
        #print(k)
        #print(R)
        #print(answer)
        R = rotate_90r(R)
        
    print('Схема из букв:\n', answer)
    
    res = grid_reading(key, answer)
    print('Криптограмма: ', res)


text = 'договор подписали'
task2_grid(text)

print('----------------------------------------------------')

text = 'за что мне все эти страдания'
task2_grid(text)

print('####################################################################')
letters = {ru[i]:i for i in range(len(ru))}
print('Словарь букв ru: ', letters)

# 3. Таблица Виженера
print('# 3.')

vigenere_table = np.array(ru)
for i in range(1, len(ru)):
    row = np.roll(ru, -i)
    vigenere_table = np.vstack((vigenere_table, row))
print('Таблица Виженера: \n',vigenere_table)

def task3_vigenere(text, key):
    print('Текст: ', text)
    text = text.replace(' ','').lower()
    
    t_len = len(text)
    print('Длина текста:', t_len)
    
    print('Ключ:', key)
    key = key.lower()
    
    n = len(key)
    _key = key
    
    while len(_key) < t_len:
        _key += _key[len(_key) - n]
    print('-----')
    print(text)
    print(_key)
    print('-----')
    
    res = ''
    for i in range(t_len):
        x = letters[_key[i]]    # номера букв ключа
        y = letters[text[i]]    # номера букв текста
        
        res += vigenere_table[x][y]
    print('Криптограмма: ', res)


text = 'криптография серьезная наука'
key = 'математика'
task3_vigenere(text, key)

print('----------------------------------------------------')
text = 'ты не пройдешь'
key = 'Гендальф'
task3_vigenere(text, key)