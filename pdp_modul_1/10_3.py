# 1- va 2- topshiriqda yozgan kodingizni try/except ichida yozib, ekranga errorni chiqaradigan kod yozing

#IndexError

try:
    a = [3,5,6,8,9]
    print(a[8])
except IndexError as a:
    print(a.__class__.__name__, a)
#KeyError

try:
    b = {'a':3,'b':5,'c':9,'d':21}
    print(b['f'])
except KeyError as b:
    print(b.__class__.__name__, b)
# TypeError
try:
    a = 12
    b = 'Hello World!'
    print(a + b)
except (TypeError) as e:
    print(e.__class__.__name__,e)


