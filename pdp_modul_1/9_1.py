# 1 - 100 oraliqdagi natural sonlardan 7 ga karrali sonlarning kvadratlarini ekranga chiqaring.
def kvad():
    num = range(7,101,7)
    for kvadrat in num:
        print(f'{kvadrat} ning kvadrati {kvadrat*kvadrat} ga teng!\n')
    return 'Dastur tugadi!'
print(kvad())