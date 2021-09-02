# def is_leap(year):
#
#     # year = int(input('Yilni kiriting: '))
#
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
# or
def is_leap(year):
    leap = False
    if (year%4==0 and year%100==0) or year%400==0:
        leap=True
        return leap
    else:
        return leap
print(is_leap(1985))