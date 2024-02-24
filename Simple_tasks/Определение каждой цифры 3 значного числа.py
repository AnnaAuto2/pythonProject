x = int(input())

a = x % 1000 // 100
b = x % 100 // 10
c = x % 10

max_number = max(a, b, c)
min_number = min(a, b, c)

srednee = (a + b + c) - max_number - min_number

if max_number - min_number == srednee:
    print("Число интересное")
else:
    print("Число неинтересное")