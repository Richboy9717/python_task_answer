# Standart kirituvchi ma’lumot sifatida ismlarni o’qib olib, ularning ichidan eng kaltasini chiqaruvchi dastur tuzing


'''
Standart kirituvchi ma’lumot sifatida ismlarni
o’qib olib, ularning ichidan eng kaltasini chiqaruvchi dastur
'''
def ask_names(*args):
    return min(args,key=len)
print(ask_names('aziz','asad','azizbek','baxrom'))