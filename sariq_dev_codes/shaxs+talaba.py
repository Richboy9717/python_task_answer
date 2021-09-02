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

kishi1 = Shaxs('Oybek','hakimov',1999,'AA0905009')

class Manzil:
    def __init__(self,uy,kocha,tuman,vil):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.vil = vil
    def get_manzil(self):
        return f"Uy: {self.uy} Ko\'cha: {self.kocha} Tuman: {self.tuman} Viloyat: {self.vil}"

class Talaba(Shaxs):
    def __init__(self,ism,fam,tyil,pasport,yil,idraqam,manzil):
        super().__init__(ism,fam,tyil,pasport)
        self.yosh = yil-tyil
        self.bosqich = 1
        self.idraqam = idraqam
        self.manzil = manzil

    def get_name(self):
        return self.ism

    def get_surname(self):
        return self.fam

    def get_yosh(self):
        return self.yosh

    def all_about(self):
        info = f"Ism: {self.ism} Familya: {self.fam} Yosh: {self.yosh}"
        info += f"Pasport: {self.pasport} Bosqich{self.bosqich} ID: {self.idraqam}"
        return info

    def get_id(self):
        return self.idraqam

    def see_methods(self,nom):
        return [e for e in dir(nom) if e.startswith('__') is False]

talaba1_manzil = Manzil(77,'Nurli ko\'cha','Chortoq','Namangan')
talaba1_fan = "Python darslari","Matematika"
talaba1 = Talaba('Aziz','Lazizov',1999,'AA0900300',2021,'ID23034045',talaba1_manzil)

talaba1.fanga