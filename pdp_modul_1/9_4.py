# Standart kiruvchi ma’lumotdan sonlarni o’qib olib, ushbu sonlarning raqamlarini teskari tartibda chiqaruvchi dastur tuzing. Masalan:
# Sonlar: 102 346 5897
# Natija: 201 643 7985
print(f'Ushbu dastur kiritilgan raqamni teskari ko\'rinishga keltiradi!\n')
son = input(f'Istalgan butun Sonlar kiriting: ')
sonla = 0
while son != 0:
    sonl = son % 10
    sonla = sonla * 10 + sonl
    son //= 10
print('Natija: ',sonla)
# son = list(son)
# print(str(son.reverse()))