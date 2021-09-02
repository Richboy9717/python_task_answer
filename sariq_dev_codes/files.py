# #faylni ochish
# fayl = open('pi.txt') #lekin bu usul tavswiya qilinmaydi
# fayl.close()
# pi = fayl.read()
#
# print(pi)
# f = 'pi.txt'
# with open(f) as fayl:
#     pi = fayl.read()
#
# print(pi)
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi,type(pi))
# with open('pi.txt') as fayl:
#     pi = fayl.readlines()
#     pi = [talaba.rstrip() for talaba in pi]
#     print(pi)
    # for qotor in fayl:
        # print(qotor,end='')


#
# fayl = 'ustozlar.txt'
# with open(fayl,'w') as f:
#     f.write('Anvar Narzulloh\n')
#     f.write(str(talaba1))
#     f.write(str(talaba2))
#
# with open(fayl,'a') as f:
#     f.write('\nSamig bekjanov')
#
# with open(fayl) as f:
#     f = f.read()
# print(f)



# import pickle
#
# talaba1 = 'Aziz', 'Lazizov', 2000, 2021
# talaba2 = 'Aziz', 'Lazizov', 2000, 2021
#
# with open('f.dat','wb') as fayl:
#     pickle.dump(talaba1,fayl)
#     pickle.dump(talaba2, fayl)
# with open('f.dat','rb') as file:
#     talaba3= pickle.load(file)
#     talaba4 = pickle.load(file)
# print(talaba3,' ',talaba4)

# file = 'dars_33.txt'
# with open(file,'r') as fayl:
#     f = fayl.read()
#     print(f)

# def tyil_file(tyil):
#     file = 'pi_million_digits.txt'
#     with open(file) as fayl:
#         fayl = fayl.read()
#     if tyil in fayl:
#         return tyil
#     else:
#         return 'Bu raqam mavjud emas!'

# >>> isinstance("salom",str)
# True # "salom" bu str
# >>> isinstance(9.5,int)
# False # 9.5 int (butun son) emas
# >>> isinstance(avto1,Avto)
# True # avto1 Avto klassiga tegishli


import pickle
file = 'pi_million_digits.txt'
with open(file) as fayl:
    fayl = fayl.read()
    fayl = fayl.rstrip()
    fayl = fayl.replace(' ','')
    fayl = fayl.replace('\n','')
    fayl = float(fayl)
fayl = fayl
with open('pi.dat','wb') as f:
    pickle.dump(fayl,f)

with open('pi.dat','rb') as files:
    files = pickle.load(files)
