import random

r = random.randint(1,10)
matn = 'Men 1 va 10 oralig\'ida bir son o\'yladim.\n'\
       '3 ta urinishda u sonni topishga urinib ko\'ring!\n'
t = range(1,4)
print(matn)
for s in t:

    ri = int(input('Taxminingizni yozing: '))
    if ri < r:
        print('Siz kiritgan son men o\'ylagan sondan kichik!\n')
    if ri > r:
        print('Siz kiritgan son men o\'ylagan sondan katta!\n')

    if ri == r:
        print('Siz sonni topdingiz Tabriklayman!')

        break