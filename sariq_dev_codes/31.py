from funksiyalar import Shaxs,Talaba
from tasks import Manzil
talaba1_manzil = Manzil(77,'Nurli hayot','Chortoq','Namangan')
talaba1 = Talaba('ali','valiyev',2001,1,45,'AA9022030',talaba1_manzil)
talaba2 = Talaba('aziz','lazizov',2000,2,40,'AA3899112',talaba1_manzil)

talabalar = [talaba1,talaba2]
print(talabalar[0].get_info())




