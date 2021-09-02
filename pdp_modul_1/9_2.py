# 2 dan 9 gacha bo’lgan sonlarning karra jadvalini ekranga chiqaruvchi dastur tuzing
def jadval():
    '''2 dan 9 gacha bo’lgan sonlarning karra jadvalini ekranga chiqaruvchi dastur'''
    for k in list(range(2,10)):
        for ka in list(range(2,10)):
            print(f'{k} karra {ka} = {k*ka}\n')
    return 'Dastur tugadi!'
print(jadval())