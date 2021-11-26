# Шифрование гаммирование

# Алфавиты
ru = [chr(i) for i in range(ord('а'), ord('я')+1)]
en = [chr(i) for i in range(ord('a'), ord('z')+1)]
#print('ru: ',ru)
#print('en: ',en)

# Словари букв и номеров
dict_ru = {ru[i]:i for i in range(len(ru))}
dict_en = {en[i]:i for i in range(len(en))}
print('\nru: ',dict_ru)
print('en: ',dict_en)


def gamma(text, key, abc):
    if abc == ru:
        dict_abc = dict_ru
    else:
        dict_abc = dict_en
    abc_len = len(abc)
    
    print('\nТекст: ', text)
    text = text.replace(' ','').lower()
    t_len = len(text)
    
    print('Ключ:', key)
    key = key.lower()
    k_len = len(key)
    gamma = key
    
    while len(gamma) < t_len:
        gamma += gamma[len(gamma) - k_len]
        
    print('-----')
    print(text)
    print(gamma)
    print('-----')
    
    res = ''
    for i in range(t_len):
        x = dict_abc[gamma[i]]   # номера букв ключа
        y = dict_abc[text[i]]    # номера букв текста
        
        res += abc[(x + y) % abc_len]
    print('Криптограмма: ', res)


text = 'приказ'
key = 'гамма'
gamma(text, key, ru)

print('----------------------------------------------------')

text = 'Live long and prosper'
key = 'Spock'
gamma(text, key, en)
