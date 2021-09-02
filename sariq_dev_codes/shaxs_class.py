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

kishi1 = Shaxs('Aziz','Lazizov',1999,'AA0090910')
print(kishi1.get_info())

