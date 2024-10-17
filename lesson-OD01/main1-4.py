# Исходную строку переводим в нижний регистр, убираем пробелы и знаки препинания
# Разбиваем строку на символы, из них создаем список
# Сортируем символы в списке в обратном порядке
# Объединяем отсортированные символы в новую строку
# Проверяем равенство исходной и полученной строки. Если они равны, то возвращаем true.
# Если они не равны, то возвращаем false.


import re


def is_palindrome(string):
    clean_string = re.sub(r'[\W_]', '', string.lower())
    chars = list(clean_string)
    chars.reverse()
    new_string = "".join(chars)
    return clean_string == new_string


print(is_palindrome("abba"))
print(is_palindrome("abc"))
print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome("A man, a plan, a canal. Panama"))
print(is_palindrome("1, 2, 3, 4, 5, 5, 4, 3, 2, 1"))
print(is_palindrome(""))
