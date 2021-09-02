#
#
# # class Talaba:
# #     def __init__(self,ism,familya,tyil):
# #         self.ism = ism
# #         self.familya = familya
# #         self.tyil = tyil
# #     def get_name(self):
# #         return self.ism
# #     def get_age(self,yil):
# #         return yil - self.tyil
# #     def get_info(self):
# #         return f"Ism: {self.ism.title()} Familya: {self.familya.title()}"
# # talaba1 = Talaba('ilhom','rahimov',1997)
# # print(talaba1.familya)
#
# # Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida
# # odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
# # Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida
# # yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin
# # (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
# # Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
# # class User:
# #     def __init__(self,username,ism,familya,tyil,email=None):
# #         self.username = username
# #         self.ism = ism
# #         self.familya = familya
# #         self.tyil = tyil
# #         self.email = email
# #     def username(self):
# #         return self.username
# #     def name(self):
# #         return self.ism
# #     def sn(self):
# #         return self.familya
# #     def get_email(self):
# #         return self.email
# #     def get_info(self):
# #         return f"Foydalanuvchi: {self.username} \nIsm: {self.ism.title()} \nFamilya: {self.familya.title()} \nEmail: {self.email}"
# # user1 = User('richboy9717','ilhomjon','rahimov',1997,'ilhomjon.97.17@gmail.com')
# # user2 = User('richboy','azimjon','rahimov',1995)
# # user3 = User('aliyev','ali','vali',1993)
# # user4 = User('jassy','jek','ma',1988)
# # # print(user4.get_info())
# # users = [user1.get_info(),user2.get_info(),user3.get_info(),user4.get_info()]
# # for us in users:
# #     print(us,'\n')
# # class Fan():
# #     def __init__(self,nomi):
# #         self.nomi = nomi
# #         self.talabalar_soni = 0
# #         self.talabalar = []
# #     def add_student(self,talaba):
# #         self.talabalar.append(talaba)
# #         self.talabalar_soni+=1
# #     def get_students(self):
# #         return [x.get_info() for x in self.talabalar]
# # def see_methods(klass):
# #     return [method for method in dir(klass) if method.startswith('__') is False]
#
# # print(see_methods(Talaba))
# # matem = Fan('Oliy matematika')
# # talaba2 = Talaba('ali','valiyev',1990)
# # matem.add_student(talaba1)
# # matem.add_student(talaba2)
# # print(talaba1.get_info())
# # Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
# # (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
# # Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# # get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
# # class Avto:
# #     def __init__(self,model,rang,narx,yili):
# #         self.model = model
# #         self.rang = rang
# #         self.karobka = 'avto'
# #         self.narx = narx
# #         self.km = 0
# #         self.yili = yili
# #         self.avtolar_soni = 0
# #         self.avtolar = []
# #     def add_avto(self,avto):
# #         self.avtolar_soni += 1
# #         return self.avtolar.append(avto)
# #     def update_km(self,plus):
# #         self.km += plus
# #     def get_info(self):
# #         return f"model: {self.model} rang: {self.rang} karobka: {self.karobka} narx: {self.narx} km: {self.km}  yili: {self.yili}"
# #
# # avto1 = Avto('malibu','qora',"35000 $",2021)
# # avto1.add_avto(avto1)
# # avto1.update_km(200)
#
# # Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
# # Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# # Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
# # Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# # dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va
# # obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)
# # class Avtosalon:
# #     def __init__(self,nom,manzil,avtolar):
# #         self.nom = nom
# #         self.manzil = manzil
# #         self.avtolar = avtolar
# #         self.top_avto = []
# #     def add_car(self,new_car):
# #         self.avtolar.append(new_car)
# #     def all_info(self):
# #         return [n for n in self.avtolar]
# #     def get_info(self):
# #         return f"model: {self.model} rang: {self.rang} karobka: {self.karobka} narx: {self.narx} km: {self.km}  yili: {self.yili}"
# # salon = Avtosalon('hyundai','namangan viloyati chortoq tumani',avto1.avtolar)
# from uuid import uuid4
# class Shaxs:
#     def __init__(self,ism,fam,tyil,pr):
#         self.ism = ism
#         self.fam = fam
#         self.tyil = tyil
#         self.__pr = pr
#         self.__id = uuid4()
#
#     def get_id(self):
#         return self.__id
#     def get_pr(self):
#         return self.__pr
#     def get_info(self):
#         info = f'{self.ism} {self.fam} {self.tyil} ,'
#         info+= f'Passport: {self.pr},tug\'ilgan yil: {self.tyil}'
#         return info
#     def get_age(self,yil):
#         return yil - self.tyil
#
# class Talaba(Shaxs):
#     """Classga xos xususiyat"""
#     # talabalar_soni = 0
#     """Incapsulatsa yordamida Classni xos xususiyatiga murojat"""
#     __talabalar_soni = 0
#     def __init__(self,ism,fam,tyil,bosqich,guruh,pr,manzil):
#         super().__init__(ism,fam,tyil,pr)
#         self.bosqich = bosqich
#         self.guruh = guruh
#         self.manzil = manzil
#         self.fanlar = []
#         Talaba.__talabalar_soni += 1
#         # Talaba.talabalar_soni+=1 #class xususiyatiga murojat
#     def get_bosqich(self):
#         return self.bosqich
#     def get_guruh(self):
#         return self.guruh
#     def set_bosqich(self,b):
#         self.bosqich = self.b
#         return self.bosqich
#     def set_guruh(self,g):
#         self.guruh = self.g
#         return self.guruh
#
#     def __repr__(self):
#         info = f'Ism-familya: {self.ism.title()} {self.fam.title()}\n'
#         info += f'Tug\'ilgan yil: {self.tyil}'
#         return info
#     # def __str__(self): #bu ham xuddi repr kabi bir hil vazifa bajaradi lekin odatda repr ishlatish yaxshi
#     #     info = f'Ism-familya: {self.ism.title()} {self.fam.title()}\n'
#     #     info += f'Tug\'ilgan yil: {self.tyil}'
#     #     return info
#     @classmethod
#     def get_nums(cls):
#         return cls.__talabalar_soni
# class Manzil:
#     def __init__(self,uy,kocha,tuman,shahar):
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.shahar = shahar
#     def get_manzil(self):
#         return f'{self.shahar},{self.tuman},{self.kocha},{self.uy}'
# talaba1_manzil = Manzil(77,'nurli hayot','chortoq','namangan')
# talaba1 = Talaba('ali','valiyev',2000,2,45,'AA9020020',talaba1_manzil)
# talaba1 = Talaba('ali','valiyev',2000,2,45,'AA9020020',talaba1_manzil)
# talaba1 = Talaba('ali','valiyev',2000,2,45,'AA9020020',talaba1_manzil)
# talaba1 = Talaba('ali','valiyev',2000,2,45,'AA9020020',talaba1_manzil)
# print(talaba1)
class Avto:
    def __init__(self,model,rang,narx,yili):
        self.model = model
        self.rang = rang
        self.karobka = 'avto'
        self.narx = narx
        self.km = 0
        self.yili = yili
        self.avtolar_soni = 0
        self.avtolar = []
    def add_avto(self,avto):
        self.avtolar_soni += 1
        return self.avtolar.append(avto)
    def update_km(self,plus):
        self.km += plus
    def get_info(self):
        return f"model: {self.model} rang: {self.rang} karobka: {self.karobka} narx: {self.narx} km: {self.km}  yili: {self.yili}"
    def __repr__(self):
        return f"model: {self.model} rang: {self.rang} karobka: {self.karobka} narx: {self.narx} km: {self.km}  yili: {self.yili}"
    def __lt__(self, boshqa):#boshqa bu solishtiriladigon o'zgaruvchi
        return self.narx>boshqa.narx

# avto1 = Avto('malibu',"qora",35000,2021)
# avto2 = Avto('lacetti',"qora",25000,2020)
# avto1.update_km(5000)
# avto2.update_km(5000)
# print(avto1)
# print(avto2)
# print(avto1<avto2)
