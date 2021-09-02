from uuid import uuid4
class Fan:
    def __init__(self,nom):
        self.nom = nom

    def __repr__(self):
        return self.nom

    def get_fanlar(self):
        return self.nom

class Talaba:
    def __init__(self,ism,familya,tyil,yil):
        self.ism = ism
        self.familya =familya
        self.tyil = tyil
        self.yosh = yil-tyil
        self.fanlar = []
        self.bosqich = 1

    def get_name(self):
        return self.ism

    def get_surname(self):
        return self.familya

    def get_yosh(self):
        return self.yosh

    def fanga_yozil(self,element):
        self.fanlar.append(element)

    def remove_fan(self,element):
        if element in self.fanlar:
            self.fanlar.remove(element)
            return f'{element} fani sizning fanlar ro\'yxatingizdan o\'chirildi'
        else:
            return 'Siz bu fanga yozilmagansiz!'

    def get_fanlar(self):
        return [s.nom for s in self.fanlar]

    def get_bosqich(self):
        return self.bosqich

    def set_bosqich(self,bosqich):
        self.bosqich+=bosqich

    def update_bosqich(self):
        self.bosqich+=1

    def __eq__(self, element):
        return self.bosqich==element

    def __le__(self, other):
        return self.bosqich>=other

    def __lt__(self, other):
        return self.bosqich>other

    def all_about(self):
        return f"Ism: {self.ism} Familya: {self.familya} Yosh: {self.yosh} Bosqich: {self.get_bosqich()}"

    def __repr__(self):
        return self.all_about()



matem = Fan('Oliy matematika')
dasturlash = Fan('Backend')
til = Fan('C++')

talaba1 = Talaba('Aziz','Lazizov',2000,2021)
talaba2 = Talaba('Aziz','Lazizov',2000,2021)

talaba1.fanga_yozil(matem)
talaba1.fanga_yozil(dasturlash)
talaba2.fanga_yozil(til)

# Inkapsulatsa va classga murojat qilish

class Shaxs:
    def __init__(self,ism,fam,tyil,pasport):
        self.ism =ism
        self.fam = fam
        self.tyil = tyil
        self.pasport = pasport

    def get_name(self):
        return self.ism

    def get_info(self):
        return f"Ism: {self.ism} Familya: {self.fam} Passport: {self.pasport}"

    def get_age(self,yil):
        return yil - self.tyil

    def __repr__(self):
        return self.get_info()

kishi1 = Shaxs('Oybek','hakimov',1999,'AA0905009')


from uuid import uuid4
class Avto:
    __num_avto = 0
    def __init__(self,model,rang,yili,narh):
        self.model = model
        self.rang = rang
        self.__yili = yili
        self.__km = 0
        self.narh = narh
        self.id = uuid4()
        Avto.__num_avto +=1

    def get_info(self):
        return f'Model: {self.model} Rangi: {self.rang} Yili: {self.__yili} Narxi: {self.narh} Km: {self.__km}'

    def add_km(self,kilometr):
        if kilometr>=0:
          self.__km +=kilometr
        else:
            return 'Faqatgina musbat son kirita olasiz!'

    @classmethod
    def get_nums(cls):
        return cls.__num_avto

avto1 = Avto('Hyundai','Silver',2020,2000)

avto1.add_km(300)
avto1.add_km(-300)
talaba2.update_bosqich()
talaba2.update_bosqich()

