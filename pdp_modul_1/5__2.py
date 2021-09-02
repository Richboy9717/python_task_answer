#                    Shart
# Standar input orqali son qabul qiling, agar bu son 3ga qoldiqsiz bo'linsa ekranga "Fiz", 5ga qoldiqsiz bo'linsa "Biz", ham 5ga ham 3ga qoldiqsiz bo'linsa "FizBiz" ni ekranga chiqaring.
# Agar son hech qaysi shartni bajarmasa sonni o'zini ekranga chiqaring.

print(f'Assalomu alaykum!\n ')
son = int(input('Biror sonni kiriting!: '))
if son % 3 == 0 and son % 5 == 0:
    print('FizBiz')
elif son % 5 == 0:
    print('Biz')
elif son % 3 == 0:
    print('Fiz')
else:
    print(f'Natija:{son}')