# import sys
# d = []
#
# try:
#
#     print(d)
#     print(ozgaruvchi)
# except (IndexError,NameError) as i:
#     print(i)
#     sys.exit()
# for d in range(7):
#     print(d*2,end=' ')
# IndexError va KeyError hosil qiladigan kod yozing
# ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}

# try:
# ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
# print(ages ['pel'])
# # except KeyError or IndexError:
# #     print('Xato kiritdingiz')
# d = {}
# try:
#     print(42/0)
#     print(d[0])
# except ZeroDivisionError as a:
#     print(a.__class__.__name__)
# except KeyError as e:
#     print(e.__class__.__name__,e)