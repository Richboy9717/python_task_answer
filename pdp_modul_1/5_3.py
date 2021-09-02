# ax^2 + bx + c = 0 kvadrat tenglama nechta yechimga ega ekanligini hisoblaydigan dastur yozing.
# a, b va c o'zgaruvchilarini standart input orqali qabul qiling.
#
# Misollar
# Input: a = 1, b = 4, c = 4
# Natija: "Tenglama 1ta yechimga ega"
#
# Input: a = 2, b = 2, c = 4
# Natija: "Tenglama 0ta yechimga ega"
#
# Input: a = 1, b = 6, c = 8
# Natija: "Tenglama 2ta yechimga ega"
print('Ushbu dastur kvadrat tenglamaning nechta yechimga ega ekanini aniqlaydi.\n')

a  = int(input('a = '))
b  = int(input('b = '))
c  = int(input('c = '))
if b ** 2 - 4 * a * c == 0:
    print('Tenglama bitta yechimga ega!\n')
elif b ** 2 - 4 * a * c > 0:
    print('Tenglama iikitta yechimga ega!\n')
else:
    print('Tenglama nolta yechimga ega!')