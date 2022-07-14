# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# Иначе – False.

def palindrome(text):
    return ''.join(text.split(' ')).lower() == ''.join(text.split(' ')).lower()[::-1]

print(palindrome(' 3 a1Race cAr1  a3       '))
