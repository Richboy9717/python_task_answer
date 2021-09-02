
print('Ushbu dastur so\'zni anagram yoki no anagram ekanini aniqlaydi')
a = input('Birinchi so\'zni kiriting!: ')
a2 = input('ikkinchi so\'zni kiriting!: ')
a = a.lower()
a2 = a2.lower()
if len(a) == len(a2):
    an = sorted(a)
    an2 = sorted(a2)
    if an == an2:
        print('Anagram')
    else:
        print('No anagram')
else:
    print('No anagram')