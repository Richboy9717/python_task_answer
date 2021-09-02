# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input('Yoshingizni kiriting: '))
# if yosh <= 4 or yosh >= 60:
#   print('Sizga kirish bepul!')
# elif yosh <= 18:
#     print('Sizga kirish 10_000 so\'m!')
# elif yosh >= 18:
#     print('Sizga kirish 20_000 so\'m')
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ' \
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# son1 = float(input('Birinchi sonni kiriting: '))
# son2 = float(input('Ikkinchi sonni kiriting: '))
# if son1 < son2:
#   print(son1 , 'Kichik' , son2 , 'dan')
# elif son1 > son2:
#   print(son1 , 'Katta' , son2 , 'dan')
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# so = int(input('Juft son kiriting!: '))
# if so % 2 == 0:
#   print('Rahmat')
# else:
#   print('Toq son kiritdingiz!')
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['osh','mastava','sup','shavla','shashlik','tabaka','bostirma']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for s in range(5):
#   savat.append(input(f'Savatga {s+1} - mahsulot nomini kiriting!: '))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     elif mahsulot is not mahsulotlar:
#         mavjud_emas.append(mahsulot)
# if mahsulot in mahsulotlar:
#     bor_mahsulotlar.append(mahsulot)
# else:
#     mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f'Do\'konimizda ushbu mahsulotlar yo\'q')
#     for mahsulot in mavjud_emas:
#         print(mavjud_emas)
# else:
#     print(f'siz so\'ragan barcha mahsulotlar do\'konimizda mavjud')
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['ilxom','anvar','azizbek','munisa','zakir']
# log = input('Yangi login kiriting: ')
# log = log.lower()
# if len(log) < 5:
#     print('Login 5 tadan ko\'proq bo\'lishi kerak!')
# elif log in foydalanuvchilar:
#     print('Bu login allaqachon band qilingan!')
# else:
#     print('Xush kelibsiz' , log)

#Foydalanuvchidan biror butun son kiritishni so'rang.
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son = int(input("Istalgan butun son kiriting: "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# # print(','.join(sttudents)) #','.join string metodi hissoblanadi
# print(sttudents['aziz'])

# mobile = {
#     'aziz':5,
#     'xasan':5,
#     'xusan':4
# }
# python = {
#     'azim':5,
#     'xusan':5,
#     'ziyod':4
# }
# web = {
#     'bobur':5,
#     'baxrom':5,
#     'xusan':4
# }
# sttudents = {'aziz' : {'algebra':10,
#                        'fizika' :20,
#                        'tarix' :30
#                        },
#              'azim' : 45,
#              'anvar' : 100,
#              'bobur' : 70
#              }
# print(sttudents['aziz'].values())
# for kalit,qiymat in sttudents['aziz'].items():
#     print(f'Kalit: {kalit.title()}')
#     print(f'Qiymat: {qiymat}\n')
# for kalit,qiymat in sttudents.items():
#     print(f'Kalit: {kalit.title()}')
#     print(f'Qiymat: {qiymat}\n')
# for va in sttudents['aziz'].keys():
#     print(va)
                # Bozorlik dasturi

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in sorted(mahsulotlar):
#     if mahsulot in bozorlik:
#         print(f'{mahsulot.title()} do\'konimizda bor narxi {mahsulotlar[mahsulot]}')
# for buyum in sorted(bozorlik):
#     if buyum not  in mahsulotlar:
#         print(f'Iltimos {buyum.title()}ni ham do\'koningizga olib keling')

# def kvadrat (num):
#     print(num**2)
# def kub (num):
#     print(num**3)
# kub(3)
# kvadrat(3)
# def email (**kwargs):
#     """ushbu dastur emailni qanday jo'natishni aytadi"""
#     print("istalgan matn: " ,kwargs.keys())
# email(to="ilhomjon.97.17@gmail.com",text="This is text")
# def t_yil():
#     """yosh va ismni ko'rsatuvchi dastur"""
#     s=int(input('Tug\'ilgan yilingizni kiriting: '))
#     ism = input('Ismingizni kiriting: ')
#     ism = ism.lower()
#     if ism == 'ilhomjon' or ism == 'ilkhomjon':
#         return (f'Xurmatli Admin siz {2021 - s} yoshda ekansiz!')
#     else:
#         return (f'Xurmatli {ism.title()} siz {2021 - s} yoshda ekansiz!')
#
# print(t_yil())
# def arifmetik(*nums):
#     return sum(nums) / len(nums)
# print(arifmetik(1,2,3))
# def greet(name,from_):
#     print(f'Hello {name} from {from_}')
# greet('PdP','ilhomjon'.title())
# greet(from_='ilhomjon',name='PdP'.title()) #tartibini bilmasa o'zgaruvchidan keyin barobar qilib yozish mumkin
# def send_email(to,text, **kwargs):
#     print("To: " ,to)
#     print("Text: " , text)
#     print("Kimga: " , kwargs)
# send_email(to="ilhomjon.97.17@gmail.com" , text= "Assalomu alaykum FullStack developer")
####Faqat Arbitrary keywordlar bilan####
# def send_email(**kwargs):
#     print("Kimga: " , kwargs)
# send_email(to="ilhomjon.97.17@gmail.com" , text= "Assalomu alaykum FullStack developer",kimga="ilhomjon.1797@gmail.com")
### * bilan ** keywordlarning farqi birinchisiga nom berish
###shart emas ikkinchisiga nom berish kerak
#masalan:
# def keywords_one(*text):
#     print(text)
#     return type(text)
# print(keywords_one('asil','aziz','va ho kazo'))

# def keywords_two(**text):
#     print(text)
#     return(type(text))
# print(keywords_two(a='asil',b='aziz',c='va ho kazo'))

# def send_email(to,text, bcc=''):
#     print("To: " ,to)
#     print("Text: " , text)
#     print("Kimga: " , bcc)
# send_email(to="ilhomjon.97.17@gmail.com" , text= "Assalomu alaykum FullStack developer")
                        ##Default parametrs
# def send_email(to,text, bcc=''):
#     print("To: " ,to)
#     print("Text: " , text)
#     print("Kimga: " , bcc)
# send_email(to="ilhomjon.97.17@gmail.com" , text= "Assalomu alaykum FullStack developer")
#bcc='' bu standart qiymat deyiladi va funksiyani chaqirganda buni kiritish kiritmaslik
# foydalanuvchining ixtiyoriga qaraydi.buni faqat ohirida ishlatish mumkin.
# def send_email(to='',text='Python', bcc=''):      #Default sifatida ichiga qiymat qo'shsa ham bo'ladi
#     print("To: " ,to)
#     print("Text: " , text)
#     print("Kimga: " , bcc) #funksiya ichidagi local o'zgaruvchilarni tashqarida ishlata olmaysiz
#     global a        #agar localniy o'zgaruvchini globalga o'zgartirmoqchi bo'lsa shunday yozish kerak
#     a='I\'m learning ' , text
# send_email()
# print(a)
            # Lambda bu ham huddi def kabi funksiya ozgina qatorli kodlarga yaxshi
# son = lambda a,b: a+b
# print(son(1,2))
            #Recursion
# def factorial(n):
#     if n == 1: #buning nomi factorial
#         return 1
#     return n*factorial(n-1)
# print(factorial(2))

# i = 1
# while i < 20:
#     print(i)
#     if i % 3 == 0:
#         break
# #2 dan 9 gacha bo’lgan sonlarning karra jadvalini ekranga chiqaruvchi dastur tuzing
# numbers = list(range(2,10))
# for karra in numbers:
#     print(f'{karra} karra {karra} = {karra*karra}')
# 1 - 100 oraliqdagi natural sonlardan 7 ga karrali sonlarning kvadratlarini ekranga chiqaring.
# def kvad():
#     num = range(7,101,7)
#     for kvadrat in num:
#         print(f'{kvadrat} ning kvadrati {kvadrat*kvadrat} ga teng!')
#     return 'Dastur tugadi!'
# print(kvad())
# Standart kiruvchi ma’lumotdan sonlarni o’qib olib, ushbu sonlarning raqamlarini teskari tartibda chiqaruvchi dastur tuzing. Masalan:
# Sonlar: 102 346 5897
# Natija: 201 643 7985
# sonlar = int(input(f'Sonlar kiriting: '))
# for son in sonlar:
#     print()
# num = int(input(f'Sonlar kiriting: '))
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# #
# print("Reversed Number: " + str(reversed_num))
# s = tuple(input(f'Sonlar kiriting: '))
# print(str(s)[::-1])
# logins = ['admin','ilhom','adham','komil']
# login = list(input(f'Loginingizni kiriting: '))
# while len(login) < 5:
#     login = list(input(f'Uzunroq oginingizni kiriting: '))
#     if login in logins:
#         print('Bu login allaqachon ro\'yxatdan o\'tkazilgan\n Boshqa kiriting: ')
#     else:
#         logins.append(login)
#
#
#
# print(logins)
# num = 3
# ac = 'I eat %d apples and pineapple %d' %(2,3)
# print(ac)
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va
# qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['kartoshka','tuhum','piyoz','sabzi','tuz','guruch','makaron','kofe','icecrim','vafli']
# savat = []
# print('Savatga 5 ta mahsulot kiriting!')
# for s in range(5):
#     savat.append(input(f'{s+1} - mahsulotni kiriting: '))
# print('\n')
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f'{mahsulot.title()} do\'konimizda mavjud')
#     elif savat not in mahsulotlar:
#         print('Kechirasiz ', mahsulot.title() ,' do\'konimizda yo\'q')

# mahsulotlar = ['kartoshka','tuhum','piyoz','sabzi','tuz','guruch','makaron','kofe','icecrim','vafli']
# savat = []
# print('Savatga 5 ta mahsulot kiriting!')
# for s in range(5):
#     savat.append(input(f'{s+1} - mahsulotni kiriting: '))
# print('\n')
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     elif savat not in mahsulotlar:
#         mavjud_emas.append(mahsulot)
# if len(mavjud_emas) == 0:
#     print('Siz so\'ragan barcha mahsulotlar mavjud')
# else:
#     print('Quyidagi mahsulotlar do\'konimizdda yo\'q: ')
#     for m in mavjud_emas:
#         print(m.title())
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan,
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvhilar = ['admin','anvar','hasana','husan','bobur']
# login = input('Yangi login kiriting: ')
# if login.lower() in foydalanuvhilar:
#     print("Login band, yangi login tanlang!")
# elif login not in foydalanuvhilar:
#     print("Xush kelibsiz, foydalanuvchi!", login.title())



