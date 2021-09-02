# Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini alifbo tartibida chiqaradigan dastur tuzing
# Masalan:  Ismlar: john, alice, bob
#   Natija: alice, bob, john
words = input("Vergul bilan ajratib so'zlar kiriting: ").split(sep=",")
words.sort()
# words.sort(reverse=False) bu ikkinchi usul
print(words)