# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:10:46 2021

@author: Администратор
"""

# mehmonlar = ['Ali' , 'Vali' , 'Aziz' , 'Laziz']
# print(mehmonlar)

# for mehmon in mehmonlar:
#   print('salom' , mehmon)
#   print(f'Assalomu alaykum hurmatli  {mehmon} sizni biz taklif qilib qolamiz')
#   print(f'Hurmat bilan')
# sonlar = list(range(0,11))
# print(sonlar)
# for son in sonlar:
#     print(son , ' ning kvadrati' , son**2 , ' ga temg')
#     print(son , 'ning kubi ' , son**3 , ' ga teng')
# raqamlar = list(range(11))
# r_kv = []
# for so in raqamlar:
#     r_kv .append (so**2)
#     # print(raqamlar)
# print(r_kv)
# print(raqamlar)
# dostlar = []
# print('5-ta eng yaqin do\'stingizni kiriting!')
# for n in range(5):
#       dostlar.append((input(f'{n+1}-Do\'stingizni ismini kiriting!')))
# print(dostlar)
# dostlar = ['Anasxon', 'Azizbek', 'Axadjon', 'Akmal', 'Rasuljon']
# for xd in dostlar :
#     print(f'Assalomu Alaykum  {xd} xush kelibsiz')
# print(f'Yuqoridagi kod {len (dostlar)} martta takrorlandi')
# toq_sonlar = list(range(11 , 101 , 2))
# kub = []
# for n in toq_sonlar:
#     print(f'{n} ning kubi {n**3}  ga teng')
# kinolar = []
# print(f'Bugun qaysi kinoga Bordingiz?')
# for kd in range(5):
#     kinolar .append(input(f'{kd+1}- kinoyingiz nomi nima?'))
# print(kinolar)
# suhbat = []
# print('So\'rovimmizda qatnashing')
# print(f'\tBugun necha kishi bilan suhbatlashdingiz?')
# for sor in range(3):
#     suhbat.append(input(f'{sor+1}- suhbatdoshingiz ismini kiriting!\n >>>>'))
# print(suhbat)    

# login = input(f'Loginingizni kiriting!')
# if login == 'Admin':
#     print('Xush kelibsiz Admin!')
# else:
#     print('Xush kelibsiz,' + login )
# print(f'Ikkita sonni kiriting')
# son = float(input('Istalgan sonni kiriting!\n>>>'))
# print("Son manfiy") if son<0 else print("Son musbat")


# ismlar = ['Anasxon' , 'Rasuljon' , 'Azizbek' , 'Lazizbek']
# for n in ismlar:
#     print(f'Assalomu alaykum {n}')
# print('Kod ', len(ismlar) , 'martta takrorlandi')
# sonlar = list(range(11, 101 , 2))
# for son in sonlar:
#     print(f'{son} ning kubi {son**3}  ga teng')
# kino = []
# ki = (input(f'Beshta eng yoqtirgan filimingizni kiriting'))
# kino.append(ki)
# kun=input('Bugun qaysi kun?\n>>')
# if kun .lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dengizga boramiz!')
# elif kun .title()=='Juma':
#     print('Bugun jumaga boramiz!')
# else:
#     print('Bugun ishga chiqamiz!')
# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')
# chipta = int(input('Yoshingizni kiriting!'))
# if chipta <= 4 or chipta >= 60:
#     print('Sizga kirish bepul!')
# elif chipta <= 18:
#     print('Sizga kirish 10_000 so\'m')
# elif chipta >= 18:
#     print('Sizga kirish 20_000 so\'m')
# print('Ikkita son kiriting!')
# son = float(input('Birinchi sonni kiriting\n>'))
# so = float(input('Ikkinchi sonni kiriting!\n>'))
# if son == so:
#     print('Sonlar teng')
# elif son<so:
#     print(f'{son} kichik {so} dan')
# elif son>so:
#     print(f'{son} katta {so} dan')
# son = float(input('Juft son kiriting!'))
# if son%2:
#     print('Bu juft son emas!')
# else:
#     print('Rahmat!')
# mahsulotlar = ['Qozonkabob' , 'osh' , 'mastava' , 'sho\'rva' , 'kichra' ,\
#                 'dimlama' , 'shashlik']
# savat = []
# for n in range(5):
#     savat.append(input(f'{n+1} - kinoyingizni kiriting!'))
# if savat in mahsulotlar:
#     print('Buyurtmangiz qabul qilindi')
# else:
#     print('Kechirasiz bizda bunday taom yo\'q')
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for avto in cars:
#     if avto !='gm':
#         print(avto.upper())
#     else:
#         print(avto.title())
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for cars in cars:
#     if cars == 'gm':
#         print(cars.upper())
#     else:
#         print(cars.title())
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for cars in cars:
#     if cars == 'gm':
#         print(cars.upper())
#     else:
#         print(cars.title())

# ismlar = []
# print('Eng yaqin 5 ta do\'stingizni kiriting!')

# sonlar = [23,20,-20,0,7.15]
# for son in sonlar:
#     print(f'{son} ning kvadrati {son**2} ga teng ')
#     print(f'{son} ning kubi {son**3} ga teng ')
#     print(f'{son}ning 2 ga ko\'paytmasi {son**2} ga teng ')
#     print(f'{son} ning kvadrati {son**2} ga teng ')
# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# print(sonlar)
# sonlar[0] = sonlar[0]+sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 37
# del sonlar[5]
# print(sonlar)
# for n in range(5):
#     ismlar.append(input(f'{n+1} - do\'stingizni ismini kiriting!\n>>'))
# ismlar = ('Anasxon', 'Rasuljon', 'Azizbek', 'Islomjon', 'Ismoil')
# ismlar = list(ismlar)
# for ism in ismlar:
# friends = []
# friends.append('Anasxon')
# friends.append('Rasuljon') 
# friends. insert(1,'Azizbek')
# friends.insert(2,'Mansurbek')
# ism = friends.pop(1)

# login = input(f'Loginingizni kiriting')
# if login.lower() == 

# print('Beshta davlat nomini kiriting!')
# for n in range(5):
#     davlat.append(input(f'{n+1} - Davlat nomini kiriting!\n>>'))
# dav = davlat[:]
# davlat = ['AQSh', 'Angliya', 'Kanada', 'Turkiya', 'Misr']
# print(len(davlat))

# print(sorted(davlat,reverse=False))
# sonlar = list(range(121,1201,2))
# print(max(sonlar))
# print(min(sonlar))
# print(sum(sonlar))
# taomlar = ['osh','mastava' , 'shorva' , 'kichra','tabaka']
# nonushta = taomlar[:]
# del nonushta [0]
# del nonushta [1:]
# nonushta = tuple(nonushta)
# nonushta.append('osh')
# ism = 'ilhomjon'
# mehmonlar = ['Ali' , 'vali' , 'samad' , 'ahad' , 'hamdam']
# for mexx in mehmonlar:
#     print(f'Hurmatli {mexx} sizni 17-noyabr kuni tug\'ilgan kunimga taklif qilaman')
#     print('Hurmat bilan '+ ism)
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
# print(mehmonlar)
# ismlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for ism in ismlar:
#     print(f'Assalomu alaykum {ism}')
# sonlar = list(range(11,100,2))
# for s in sonlar:
#     print(f'{s} ning kvadrati {s**3} ga teng')
# print('Besjta eng yoqtirgan kinoyingizni kiriting!')
# kinolar = []
# for kino in range(5):
#     kinolar.append(input(f'{kino+1}-kinoyingizni kiriting!\n>>'))
# print(kinolar)
# suhbat = []
# for s in range(5):
#     suhbat.append(input(f'{s+1}-suhbatdoshingizni ismini kiriting!\n>>'))
# print(suhbat)
# for ss in suhbat:
#     print(f'Assalomu alaykum {ss}')
# ism = input(f'Ismingizni kiriting!:')
# if ism.lower() == 'ali':
#     print(f'Assalomu alaykum Ali')
# else:
#     print(f'Kechirasiz biz Alini kutyapmiz')
# yosh = int(input(f'Assalomu alaykum yoshingizni kiriting!\n>>'))
# if yosh >= 18:
#     print('Xush kelibsiz')
# else:
#     print('Kechirasiz sizga kirish mumkin emas!')
# # kv = float(input(f'Istalgan sonni kiriting!:'))
# # print(f'{kv} ning kvadrati {kv**2} ga teng')
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#    if car!='gm':    print(car.upper())
#    else:    print(car.title())
# login = input('Loginingizni kiriting!:')
# if login.lower()=='admin':  print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
# else:   print('Xush kelibsiz')
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")
elif x<y:   print(f'{x} kichik {y} dan')
elif x>y:   print(f'{x} katta {y} dan')






