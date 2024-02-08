# Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение,
# которое будет выведено в случае ошибки проверки результата:

assert abs(-42) == 42, "Should be absolute value of a number"

# Форматирование строк с помощью str.format

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# Форматирование строк с помощью f-strings
# Для использования возможностей f-strings нужно указывать символ f перед строкой в таком формате: f"ваша строка {my_var}".
# В фигурных скобках указывается имя переменной, значение которой надо подставить в строку, или выражение, результат
# исполнения которого также требуется подставить в вашу строку.
# Предлагаем вам применять именно этот подход в данном курсе.

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")


# Пример
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

# Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения подстроки в строку
# и -1, если подстрока не найдена.
# Пример
# Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и,
# в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"