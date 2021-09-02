#Standart input orqali vergul bilan ajratilgan sonlarni o'qing va
# u yerda nechta son qatnashganini ekranga chiqaring (takrorlanishlar inobatga olinmasin).

# Misollar:
# Input: 2,3,3,4
# Natija: 3

son = set(input('Vergul bilan ajratib sonlar kiriting: ').split(sep=','))
print('Natija: ', len(son))