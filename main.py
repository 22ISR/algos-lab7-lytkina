"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.

    -- def isPalindrome(word):
    -- cleaned = ''.join(c.lower() for c in word if c.isalnum())
    -- return cleaned == cleaned[::-1]

Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

    -- def isPalindromeList(words):
    -- return [word for word in words if isPalindrome(word)]

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

    -- def isPalindromeString(text):
    -- words = text.split()
    -- found = set()
    -- for word in words:
    --     cleaned = ''.join(c.lower() for c in word if c.isalnum())
    --     if len(cleaned) > 1 and cleaned == cleaned[::-1]:
    --         found.add(cleaned)
    -- return list(found)

Пример использования:
    isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""