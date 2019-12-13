# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

import hashlib


def get_subs(string: str) -> int:
    result = 0
    length = len(string)
    subs = []
    hash_str = hashlib.sha1(string.encode('utf-8')).hexdigest()
    for i in range(length):
        for j in range(1, length - i + 1):
            sub = string[i:i+j]
            if sub == string or sub == '':
                continue
            sub_test = string[:i] + sub + string[i+j:length]
            hash_sub = hashlib.sha1(sub_test.encode('utf-8')).hexdigest()
            if hash_str == hash_sub and sub not in subs:
                subs.append(sub)
                result += 1
    return result


print(get_subs('hellohello'))