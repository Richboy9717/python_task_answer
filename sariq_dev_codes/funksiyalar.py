from uuid import uuid4
class Shaxs:
    shaxslar = 0
    def __init__(self,ism,fam,tyil):
        self.ism = ism
        self.fam = fam
        self.tyil = tyil
        self.__id = uuid4()

    def get_info(self):
        return f"Ism : {self.ism.title()},\nFamilya : {self.fam.title()},\nTug'ilgan yil : {self.tyil},\nId : {self.__id}"
    def __repr__(self):
        return self.ism.title()
shaxs1 = Shaxs('asad','valiyev',2000)

class Talaba(Shaxs):
    """Classga xos xususiyat"""
    # talabalar_soni = 0
    """Incapsulatsa yordamida Classni xos xususiyatiga murojat"""
    __talabalar_soni = 0

    def __init__(self,ism,fam,tyil,bosqich,guruh,pr,manzil):
        super().__init__(ism,fam,tyil)
        self.bosqich = bosqich
        self.guruh = guruh
        self.manzil = manzil
        self.fanlar = []
        Talaba.__talabalar_soni += 1
        # Talaba.talabalar_soni+=1 #class xususiyatiga murojat

    def get_bosqich(self):
        return self.bosqich

    def get_name(self):
        return self.ism

    def get_guruh(self):
        return self.guruh

    def set_bosqich(self,b):
        self.bosqich = self.b

        return self.bosqich
    def set_guruh(self,g):
        self.guruh = self.g
        return self.guruh


    def __repr__(self):
        info = f'Ism-familya: {self.ism.title()} {self.fam.title()}\n'
        info += f'Tug\'ilgan yil: {self.tyil}'
        return info
    # def __str__(self): #bu ham xuddi repr kabi bir hil vazifa bajaradi lekin odatda repr ishlatish yaxshi
    #     info = f'Ism-familya: {self.ism.title()} {self.fam.title()}\n'
    #     info += f'Tug\'ilgan yil: {self.tyil}'
    #     return info
    @classmethod
    def get_nums(cls):
        return cls.__talabalar_soni
