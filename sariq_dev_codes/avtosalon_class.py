from avto_class import Avto
class Avtosalon:
    def __init__(self,nomi,manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.sotuvda = []
        self.avtolar = []

    def add_avto(self,*cars):
        for car in cars:
            if isinstance(car,Avto):
                self.avtolar.append(car)
        else:
            return f'Bu yerga faqat Avto klasiga oid obyekt qo\'sha olasiz holos'

    def __getitem__(self,index):
        return self.avtolar[index]

    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat

    def __repr__(self):
        return self.nomi

    def get_cars(self):
        return [x.model for x in self.avtolar]

    def salon_info(self):
        return f"Nomi: {self.nomi} Manzil: {self.manzil} Avtomobillar: {self.get_cars()}"

    def see_method(self,nom):
        return [p for p in dir(nom) if p.startswith('__') is False]

avto1 = Avto('Hyundai','Silver',2020,2000)
avto2 = Avto('Sonata','Silver',2019,2000)
avto3 = Avto('Hyundai','Silver',2020,2000)
avto4 = Avto('Sonata','Silver',2019,2000)

salon1 = Avtosalon('Hyundai Filial','Namangan viloyati Chortoq tuman')
salon1.add_avto(avto1,avto2,avto3,avto4)
salon1[0] = Avto('BMW','Qora',2020,10000)
print(salon1[:])