# import math
#
# a = float(input('Haqiqiy son kiriting!\n: '))
# b = int(math.log10(abs(a)))
# c = a / pow(10 , b)
# print(f'{a} ning standart shakli {c} ga darajasi esa {b} ga teng')
# print(f'{a}--> {c}*10^{b}')
son = float(input('Istalgan Sonni kiriting!: '))
# if son <= 0:
#     print('Manfiy son')
# elif son >= 0:
#     print('Musbat son')
if abs(son) >= 10:
    print('juft son')
elif abs(son) <= 9:
    print('toq son')








