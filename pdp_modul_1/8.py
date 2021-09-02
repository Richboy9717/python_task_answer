
#2 dan 9 gacha bo’lgan sonlarning karra jadvalini ekranga chiqaruvchi dastur tuzing
# numbers = list(range(2,11))
# for karra in numbers:
#     print(f'{karra} karra {karra} = {karra*karra}')
numbers = range(2,11)
for karra in numbers:
    for r in numbers:
        print(f'{karra} karra {r} = {r*karra}')