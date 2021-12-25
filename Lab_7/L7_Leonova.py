# Расширенный алгоритм Евклида
# d = НОД(a,b) = ax + by
def nod3(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == 1 or b == 1:
        return 1
    if abs(a) < abs(b):
        a, b = abs(b), abs(a)

    x, y = [1,0], [0,1]
    a_, b_ = a, b
    
    while b_ != 0:
        a_, b_, p = b_, a_ % b_, a_ // b_
        
        x[0], x[1] = x[1], x[0] - p*x[1]
        y[0], y[1] = y[1], y[0] - p*y[1]
    
    d = a_
    #print(a,'*',x[1],' + ',b,'*',y[1],' = ',d)
    return d, abs(y[0]), abs(x[0])


# Функция
def f(c, u, v):
    if c < r:
        return a*c % p, u+1, v
    else:
        return b*c % p, u, v+1
    

# Печать промежуточных шагов
def pr(c,uc,vc,d,ud,vd):
    print(' ',c,'   ',uc,' + ',vc,'x    ', d,'   ',ud,'+',vd,'x')


# p-метод Полларда для задач дискретного логарифмирования
def Pollard_log(a, p, r, b, u, v):
    c = a**u * b**v % p
    d = c
    uc, vc = u, v
    ud, vd = u, v

    print('  c       log_c       d      log_d')
    print('--------------------------------------')
    pr(c,uc,vd,d,ud,vd)    

    c, uc, vc = f(c, uc, vc)
    c %= p
    d, ud, vd = f(*f(d, ud, vd))
    d %= p
    pr(c,uc,vd,d,ud,vd)
    
    while c%p != d%p:
        c, uc, vc = f(c, uc, vc)
        c %= p
        d, ud, vd = f(*f(d, ud, vd))
        d %= p
        pr(c,uc,vd,d,ud,vd)
              
    v = vc - vd
    u = ud - uc
    
    d, x, y = nod3(v, r)
    
    while d != 1:
        v /= d
        u /= d
        r /= d
        d, x, y = nod3(v, r)
        pr(c,uc,vd,d,ud,vd)
    
    return x*u % r


print('p-метод Полларда ля задач дискретного логарифмирования')
a = 10
p = 107
r = 53
b = 64
u = 2
v = 2
print(Pollard_log(a, p, r, b, u, v))
