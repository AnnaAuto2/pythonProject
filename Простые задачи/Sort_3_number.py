# Сортировка трёх
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

a = int(input())
b = int(input())
c = int(input())

max_number = max(a, b, c)
min_number = min(a, b, c)

srednee = (a + b + c) - max_number - min_number

print(max_number)
print(srednee)
print(min_number)