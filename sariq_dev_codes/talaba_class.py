class Talaba:
    def __init__(self,ism,familya,tyil,yil):
        self.ism = ism
        self.familya =familya
        self.tyil = tyil
        self.yosh = yil-tyil

    def get_name(self):
        return self.ism

    def get_surname(self):
        return self.familya

    def get_yosh(self):
        return self.yosh

    def all_about(self):
        return f"\nIsm: {self.ism}\nFamilya: {self.familya}\nYosh: {self.yosh}"

