class Shaxs:
    def __init__(self,ism,fam,tyil,pr):
        self.ism = ism
        self.fam = fam
        self.tyil = tyil
        self.pr = pr
    def get_info(self):
        info = f'{self.ism} {self.fam} {self.tyil} ,'
        info+= f'Passport: {self.pr},tug\'ilgan yil: {self.tyil}'
        return info
    def get_age(self,yil):
        return yil - self.tyil
class Talaba(Shaxs):
    def __init__(self,ism,fam,tyil,bosqich,guruh,pr,manzil):
        super().__init__(ism,fam,tyil,pr)
        self.bosqich = bosqich
        self.guruh = guruh
        self.manzil = manzil
        self.fanlar = []
    def get_bosqich(self):
        return self.bosqich
    def get_guruh(self):
        return self.guruh
    def set_bosqich(self,new_bosqich):
        self.bosqich =  new_bosqich
        return self.bosqich
    def set_guruh(self,new_guruh):
        self.guruh = new_guruh
        return self.guruh
class Manzil:
    def __init__(self,uy,kocha,tuman,shahar):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.shahar = shahar
    def get_manzil(self):
        return f'{self.shahar},{self.tuman},{self.kocha},{self.uy}'

talaba1_manzil = Manzil(77,'nurli hayot','chortoq','namangan')
talaba1 = Talaba('ali','valiyev',2000,2,45,'AA9020020',talaba1_manzil)

# print(talaba1.manzil.get_manzil())

class Fan:
    def __init__(self,fans=[]):
        self.fans = fans = []
    def fanga_yozil(self,nom):
        self.fans.append(nom)
        return f'{self.fans} Fanlar ro\'yxatiga qo\'shildi'
# matem = Fan('matematika')
# python = Fan('Dasturlash asoslaari')
# print(python.fanga_yozil(talaba1.ism.title()))
# print(matem.fanga_yozil(talaba1.ism))
# print(python.fans)
