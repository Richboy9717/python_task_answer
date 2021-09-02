from __future__ import print_function
car0 = {
    'model': 'lacetti',
    'rang': 'oq',
    'narx':'7000',
    'yil': '2020',
    'karobka':'avtomat',
    'km': '2500'
    }
car1 = {
    'model': 'malibu',
    'rang': 'qora',
    'narx':'12000',
    'yil': '2020',
    'karobka':'avtomat',
    'km': '2000'
    }
car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'narx':'9000',
    'yil': '2020',
    'karobka':'avtomat',
    'km': '3500'
    }
# cars = car0,car1,car2
# for car in cars:
#     print(f'{car["model"].title()} '
#           f'{car["rang"].lower()} '
#           f'{car["yil"]}-yil '
#           f'{car["narx"]}-$')
# print(cars[0])
# malibus = []
# for n in range(10):
#     new_car= {
#         'model': 'malibu',
#         'rang': None,
#         'narx':None,
#         'yil': '2021',
#         'karobka':'avtomat',
#         'km': 0
#         }
#     malibus.append(new_car)
#
# for malibu in malibus[:3]:
#     malibu['rang']='qora'
#     malibu['karobka'] = 'avto'
# for malibu in malibus[3:6]:
#     malibu['rang']='qizil'
#     malibu['karobka'] = 'mex'
# for malibu in malibus:
#     if malibu['karobka']=='avto':
#         malibu['narx'] = '5000 $'
#     else:
#         malibu['narx'] = '4500 $'
# for m in malibus:
#     print(m)
# dasturchilar = {'ali': ['java','javascript'],
#                 'vali': ['php','c#'],
#                 'hasan': ['c++','sql'],
#                 'husan':['note js','django'],
#                 'ilhom':['python','data scaince']}
# for ism,tillar in dasturchilar.items():
#     print(f'{ism.title()}-quyidagi dasturlash tillarini bilaadi: ')
#     for til in tillar:
#         print(til.upper())
# for ism,tillar in dasturchilar.items():
#     print(f'\n{ism.title()}-quyidagi dasturlash tillarini bilaadi: ')
#     for til in tillar:
#         print(til.upper(),end=',')
# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }
# for ism,info in hamkasblar.items():
#     print(f'\n{ism.title()} {info["familiya"].title()} {info["tyil"]}- yilda tug\'ilgan '
#           f'\nMa\'lumoti: {info["malumot"]}'
#           f'\nQuyidagi dasturlash tillarini biladi: ')
#     for til in info['tillar']:
#         print(f'{til.upper()}')

# savol = "Ismingizni kiriting: "
# ism = input(savol)
# m = f'Salom {ism.title()},Yoshingizni kiriting: '
# yosh = int(input(m))
# b = f'B\'yingizni kiriting: '
# height = float(input(b))
# son = 1
# while son <= 5:
#     print(son,end=' ')
#     son+=1
# print('(Kiritilgan sonning kvadratini qaytaruvchi dastur)')
# son = 'Sonni kiriting'
# son += (' (dasturni to\'xtatish uchun "exit" deb yozing): ')
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(son)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# ishora

# print('(Kiritilgan sonning kvadratini qaytaruvchi dastur)')
# son = 'Sonni kiriting'
# son += (' (dasturni to\'xtatish uchun "exit" deb yozing): ')
# ishora = True
# while ishora:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# break

# print('(Kiritilgan sonning kvadratini qaytaruvchi dastur)')
# son = 'Sonni kiriting'
# son += (' (dasturni to\'xtatish uchun "exit" deb yozing): ')
# while True:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# # continue
#
# son = 0
# while son <= 10:
#     son += 1
#     if son % 2 == 0:
#         continue
#     else:
#         print(son)
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# savol = f'Yoqtirgan kitobingizni kiriting'
# savol += f'(dasturni to\'xtatish uchun "exit" deb yozing): '
# kitoblar = []
# while True:
#     nom = input(savol)
#     kitoblar.append(nom)
#     if nom == 'stop':
#         break
# for kitob in kitoblar:
#     print(kitob.capitalize(),end=',')
#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
# 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
# 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin
# va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb
# yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# savol = 'Yoshingizni kiriting: '
# ishora = True
# while ishora:
#     kirish = input(savol)
#     if type(kirish) == str:
#         if kirish == 'exit' or kirish == 'quit':
#             pay = 'Dastur to\'xtatildi'
#             ishora = False
#         else:
#             continue
#     else:
#         if int(kirish) < 7:
#             pay = 'Sizga kirish 2000 so\'m'
#             ishora = False
#         elif int(kirish) >= 7 and int(kirish) < 18:
#             pay = 'Sizga kirish 3000 so\'m'
#             ishora = False
#         elif int(kirish) >= 18 and int(kirish) < 65:
#             pay = 'Sizga kirish 10000 so\'m'
#             ishora = False
#         elif int(kirish) >= 65:
#             pay = 'Sizga kirish bepul!'
#             ishora = False
#         else:
#             continue
# print(pay)
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if str(qiymat).lower()=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# que = 'Buyurtmani kiriting (dasturni to\'xtatish uchun "stop" deb yozing): '
# buyurtma = []
# n = 0
# while True:
#     qiymat = input(que)
#     if qiymat == 'stop':
#         break
#     else:
#         print(n+1,'- Buyurtmangiz qabul qilindi')
#         buyurtma.append(qiymat)
#         n+=1
# print(f'Siz kiritgan buyurtmalar ro\'yxati: ')
# for b in buyurtma:
#     print(f'{b.title()}')
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# e_bozor = {}
# sorov = 'E-Bozor uchun mahsulot nomini kiriting: '
# sorov_2 = 'E-Bozor uchun mahsulot narxini kiriting: '
# while True:
#     mahsulot = input(sorov)
#     narx = input(sorov_2)
#     e_bozor[mahsulot]=int(narx)
#     j = input('Yana mahsulot kiritasizmi? ha/yo\'q: ')
#     if j == 'yo\'q':
#         break
# for v,q in e_bozor.items():
#     print(v.title(),q)
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f'{buyurtma.title()}ni narxi {narh} so\'m')
#     else:
#         print(f'{buyurtma.title()} bizda mavjud emas!')
# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def jufttoq():
#     print(f'Ushbu dastur kiritilgan sonni juft yoki toq ekanini aniqlaydi.\n')
#     q = int(input(f'Istalgan butun sonni kiriting: '))
#     if q % 2:
#         return f'Siz kiritgan {q} soni toq son'
#     else:
#         return f'Siz kiritgan {q} soni juft son'
# print(jufttoq())
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def kk():
#     print(f'Ushbu dastur kiritilgan sonni katta yoki kichikligini aniqlaydi.\n')
#     q1 = int(input(f'1-sonni kiriting: '))
#     q2 = int(input(f'2-sonni kiriting: '))
#     if q1 < q2:
#         print(f'{q1} kichik {q2} dan')
#     elif q2 < q1:
#         print(f'{q2} kichik {q1} dan')
#     elif q1 == q2:
#         print(f'Sonlar teng')
#     return 'Dastur tugadi!'
# print(kk())
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
# sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.
# def bolinish():
#     s = list(range(2,11))
#     sa = int(input('Sonni kiriting: '))
#     for n in s:
#         if sa % n == 0:
#             print(f'{sa} {n} ga qoldiqsiz bo\'linadi')
#     return 'Dastur tugaadi!'
# print(bolinish())

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili
# va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing.
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

# def info():
#     ism = input('Ismingizni kiriting: ')
#     fam = input('Familyangizni kiriting: ')
#     tyil = input('Tug\'ilgan yilingizni kiriting: ')
#     tjoy = input('Tug\'ilgan joyingizni kiriting: ')
#     email = input('Emailingizni kiriting: ')
#     # if email == None:
#
#     tel = input('Telefoningizni kiriting: ')
#     mijozlar = {
#         "ism":ism,
#         "familya":fam,
#         "yil":tyil,
#         "joy":tjoy,
#         "email":email,
#         "tel":tel
#     }
#     for k,v in mijozlar.items():
#         print(k.title(),v)
# print(info())
# m = []
# def info():
#     while True:
#         ism = input('Ismingizni kiriting: ')
#         fam = input('Familyangizni kiriting: ')
#         tyil = input('Tug\'ilgan yilingizni kiriting: ')
#         tjoy = input('Tug\'ilgan joyingizni kiriting: ')
#         email = input('Emailingizni kiriting: ')
#         tel = input('Telefoningizni kiriting: ')
#         mijozlar = {
#             "ism: ":ism,
#             "familya: ":fam,
#             "yil: ":tyil,
#             "joy: ":tjoy,
#             "email: ":email,
#             "tel: ":tel
#         }
#         m.append(mijozlar)
#         p = input('Yana kiritasizmi? ha/yo\'q: ')
#         if p == 'yo\'q':
#             break
#     for mijoz in m[::]:
#         for mk,mv in mijoz.items():
#             print(mk.title(),mv)
#     return '\n'
# print(info())

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri
# va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

#matem
# def aylana():
#     print('Ushbu dastur radiusni qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug\'at ko\'rinishida qaytaradi')
#     son = float(input('Sonning radiusini kiriting: '))
#     pi = 3.14159
#     umumiy = {
#         'radius':son, #radius aylananing markazidan chetigacha tortilgan chiziq
#         'diametr':son*2, #diametr radiusning 2 ga ko'paytmasi
#         'perimetr':son*2*pi, # perimetr radiusni 2 ga ko'paytirib pi ga ko'paytiramiz
#         'yuzi':pi*son**2 # yuzini aniqlashda pini radiusini 2 kvadratga oshiramiz
#     }
#     for ak,av in umumiy.items():
#         print(ak,av)
#     # return 'Dastur muvaffaqiyatli bajarildi'
# aylana()
#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
#
# print(fibonacci(10))
# def oraliq(min,max,qadam = None):
#     sonlar = []
#     while min <= max:
#         sonlar.append(min)
#         if qadam:
#             min += qadam - 1
#
#         min +=1
#     return sonlar
# print(oraliq(0,21,2))
# def avto_info(kompaniya, model, rangi, karobka, yili, narx=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':karobka,
#             'yil':yili,
#             'narh':narx}
#     return avto
# print('Kompaniyamizdagi mashinalar ro\'yxatini shakllantirish')
# avtolar = []
# while True:
#     print(f'Quyidagi ma\'lumotlarni kiiriting!')
#     kompaniya = input('Kompaniyani kiriting: ')
#     model = input('Modelni kiriting: ')
#     rangi = input('Rangni kiriting: ')
#     karobka = input('Karobkani kiriting: ')
#     yili = input('Yilini kiriting: ')
#     narx = input('Narxni kiriting: ')
#     avtolar.append(avto_info(kompaniya,model,rangi,karobka,yili,narx))
#     s = input('Yana kiritasizmi? yes/no: ')
#     if s == 'no':
#         break
# print('Salonimizdagi avtolar ')
# for avto in avtolar:
#     for ak,av in avto.items():
#         print(ak.title(),av)
#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi
# har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)
# def kharf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#     return matnlar
# ism = ['ali','vali','hasan','husan']
# print(ism,kharf(ism[:]))
# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(2,3,4,5,6))
# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# def kop(*sonlar):
#     for son in sonlar:
#         yigindi= 0
#         yigindi = son*son
#     return yigindi
# print(kop(2,3,4,23))

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument,
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
# def talabalar(ism,familya,**malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familya'] = familya
#     return malumotlar
# print(talabalar('ilhom','rahimov',tyil = 1997, kurs = 1))

# for i in range(1,int(input())):
#     print(((10**i)//9)*i)
# arr = list(set(map(int,input('Baholar: ').split())))
# arr.sort()
# print(arr[-2])


# score_list = {}
# for _ in range (int(input())):
#     name = input()
#     score = float(input())
#     if score in score_list:
#         score_list[score].append(name)
#     else:
#         score_list[score] = [name]
# new_list = []
# for i in score_list:
#     new_list.append([i, score_list[i]])
# new_list.sort()
# result = new_list[1][1]
# result.sort()
# print(*result, sep = "\n")

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
# print('{0:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name])))