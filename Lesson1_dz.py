answer = input('Какой язык программирования мы изучаем?')

if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

    a1 = int(input())
    a2 = int(input())
    b1 = int(input())
    b2 = int(input())

    # если не пересекаются
    if b1 > a2 or b2 < a1:
        print('пустое множество')
    # точка (граница)
    elif b1 == a2:
        print(b1)
    elif a1 == b2:
        print(a1)
    # полностью совпадают
    elif a1 == a2 and a2 == b2:
        print(a1, b1)
    # пересечения
    elif a1 <= a2 < b1 <= b2:
        print(a2, b1)
    elif a2 <= a1 < b2 <= b1:
        print(a1, b2)
    elif a1 <= a2 <= b1 and a1 <= b2 <= b1:
        print(a2, b2)
    elif a2 <= a1 <= b2 and a2 <= b1 <= b2:
        print(a1, b1)   