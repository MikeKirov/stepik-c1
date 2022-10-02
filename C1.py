# s = "01234567891011121314151617"
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[7])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-10])

# n = input()
# n = "abcdefghijklmnop"
# for i in range(0, len(n), 2):
#     print(n[i])

# n = "abcde"
# for i in range(len(n)):
#     print(n[-i-1])

# im = "Яша"
# f = "Кук"
# ot = "Поршевич"
# print(f[0], im[0], ot[0], sep='')

# s, summ = input(), 0
# for i in s:
#     summ += int(i)
# print(summ)
#
# n, x, y = input(), 0, 0
# for i in n:
#     if "+" == i:
#         x += 1
#     if "*" == i:
#         y += 1
# print("Символ + встречается", x, "раз")
# print("Символ * встречается", y, "раз")
#
# line, counter = input(), 0
# for i in range(len(line) - 1):  #len(line)-1, чтобы на строку[i+1] отладчик не ругался
#     if line[i] == line[i + 1]:  #а то получается, что в последней итерации цикла for мы выходим за рамки
#         counter += 1
# print(counter)
#
# line, x, y = input(), 0, 0
# gl = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
# sogl = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
# for i in range(len(line)):
#     if  line[i] in gl:
#         x += 1
#     if  line[i] in sogl:
#         y += 1
# print("С Количество гласных букв равно", x)
# print("С Количество согласных букв равно", y)

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-10:])

# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())

# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))

# n = input()
# f = n.find('h')
# l = n.rfind('h')
# print(n[l:f:-1])  #первая h включена, вторая нет
# print(n[:f])  #без h
# print(n[l:])  #c h

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers),  numbers[-1],  numbers[::-1], sep="\n")
# if "5, 17" in numbers:
#     print('YES')
# else:
#     print("NO")
# print(numbers[1:-1])

# counter = 0
# z = []
# for i in range(97, 123):
#     counter += 1
#     z.append(chr(i)*counter)
# print(z)
#
# print([chr(97 + i) * (i + 1) for i in range(26)])

# n, z, y = int(input()), [], []
# for i in range(n):
#     l = int(input())
#     z.append(l)
# for i in range(len(z) - 1):
#     y.append(z[i] + z[i+1])
# print(y)

# n = int(input())
# z = [n]
# for i in range(n):
#     l = int(input())
#     if z[i] % 2 == 0:
#         z.append(l)
# print(z)
#
# print([int(input()) for i in range(2, int(input())+1) if ])
#
#
# print([int(input()) ** 3 for _ in range(int(input()))])
# print([chr(97 + i) * (i + 1) for i in range(26)])

# n, z = int(input()), []
# for i in range(n):
#     l = int(input())
#     z.append(l)
# z.remove(min(z))  # или del z[z.index(min(z))]
# z.remove(max(z))  # или del z[z.index(max(z))]
# print(z)

# z = [input() for i in range(int(input()))]
# k = [input() for j in range(int(input()))]
# y = []
# for i in z:
#     counter = 0
#     for j in k:
#         if j.lower() in i.lower():
#             counter += 1
#         if counter == len(k):
#             y.append(i)
# print(*y, sep = '\n')
#
# s = [input() for _ in range(int(input()))]
# k = [input() for _ in range(int(input()))]
# for i in s:
#     count = 0
#     for j in k:
#         if j.lower() in i.lower():
#             count += 1
#             if count == len(k):
#                 print(i)

# num, n, z, p = int(input()), [], [], []
# for i in range(num):
#     l = int(input())
#     if l < 0:
#         n.append(l)
#     if l == 0:
#         z.append(l)
#     if l > 0:
#         p.append(l)
# print(*(n + z + p), sep = '\n')

# print(*input().split(), sep = '\n')
# n = input().split('\')
# print('\n'.join(*n))
#
# ip = '192.168.1.24'
# numbers = ip.split('.')    # указываем явно разделитель
# print(numbers)

# ip = input().split('.')
# flag = True
# answer = 'НЕТ'
# for i in ip:
#     if int(i) < 256:
#         answer = 'ДА'
#         print(i)
# print(answer)
# Вставил число 25 по индексу 3;

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers_copy = numbers.copy()
# numbers.extend(numbers_copy)
# numbers.insert(3, 25)
# print(numbers)

# n = [int(i) for i in input().split()]
# y = n.index(max(n))
# z = n.index(min(n))
# n[z], n[y] = n[y], n[z]
# print(*n)

# n = input().lower().split()
# print('Общее количество артиклей:', n.count('a') + n.count('an') + n.count('the'))

# n = int(input().replace('#', ''))
# for i in range(n):
#     m = input()
#     if "#" in m:
#         b = m.replace(m[m.index("#")::], "").rstrip()
#         print(b)
#     if "#" not in m:
#         print(m)

# l = [int(i) for i in input().split()]
# l.sort()
# print(*l)
# l.sort(reverse=True)
# print(*l)
# or
# a = sorted(map(int, input().split()))
# print(*a)
# print(*reversed(a))

# chars = [c for c in 'abcdefg']
# print(chars)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [m[1::] for m in keywords]
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(m) for m in keywords]
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [m for m in keywords if len(m) >= 5]
# print(new_keywords)

# palindromes = [i for i in range(100, 1001) if  i % 10 == i // 100]
# print(palindromes)

# # palindromes = [x for x in range(101, 1000) if x // 100 == x % 10]
# # palindromes = [x for x in range(101, 1000) if x == int(str(x)[::-1])]
# palindromes = [i for i in range(100, 1001) if  str(i)[0] == str(i)[2]]
# print(palindromes)

# print(*[i for i in input() if i in'0123456789'], sep = '')
# print(*(i for i in input() if i.isdigit()), sep="")

# print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])
# print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])

# a = [4, 5, 9, -1, 90, -34]
# n = len(a)
# b = []
# while len(a) > 0:
#     b.append(min(a))
#     a.remove(min(a))
# a = b
# # n = len(a)
# # counter = 0
# # for i in range(n):
# #     a.append(min(a[:(n - counter)]))
# #     a.remove(min(a[:(n - counter)]))
# #     counter += 1
# # # n = len(a)
# # # for j in range(n-1):
# # #     for i in range(n-j-1):
# # #         if a[i] > a[-1-j]:
# # #             a[i], a[-1-j] = a[-1-j],a[i]
# # # # n = len(a)
# # # # for i in range(n - 1):
# # # #     for j in range(n - i - 1):
# # # #         if a[j] > a[j + 1]:
# # # #             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)

# print([i for i in range(2, int(input()) + 1, 2)])

# print(max([len(i) for i in input().split()]))

# print(*[i[1:] + i[0] + "ки" for i in input().split()])

# n = input().split('-')
# if ''.join(n).isdigit():
#     if len(n)==4 and n[0]=='7' and len(n[1])==3 and len(n[2])==3 and len(n[3])==4:
#         print('YES')
#     elif len(n)==3 and len(n[0])==3 and len(n[1])==3 and len(n[2])==4:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')
#
# n = input().split("-")
# c = [len(i) for i in n]
# if c == [3, 3, 4] and ''.join(n).isdigit():
#     print("YES")
# elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
#     print("YES")
# else:
#     print("NO")

# # объявление функции
# def draw_triangle():
#     for i in range(10):
#         print("*" * i)
# # основная программа
# draw_triangle()  # вызов функции
# print()

# def draw_triangle(fill, base):
#     for i in range(base // 2 + 1):
#         for j in range(i + 1):
#             print(fill, end='')
#         print()
#     for i in range(base // 2 - 1, -1, -1):
#         for j in range(i + 1):
#             print(fill, end='')
#         print()
# fill = input()
# base = int(input())
# draw_triangle(fill, base)
# print()
#
# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#     for i in range(base // 2, 0, -1):
#         print(fill * i)
# fill = input()
# base = int(input())
# draw_triangle(fill, base)
#
# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))
# fill = input()
# base = int(input())
# draw_triangle(fill, base)

# def print_fio(name, surname, patronymic):
# #    print((surname[0]+name[0]+patronymic[0]).upper())
#      print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())

# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)

# def print_digit_sum(n):
#     print_digit_sum = 0
#     while n != 0:
#         last_digit = n % 10
#         print_digit_sum += last_digit
#         n = n // 10
#     print(print_digit_sum)
# n = int(input())
# print_digit_sum(n)
#
# def print_digit_sum(num):
#     print(sum([int(i) for i in num]))
# print_digit_sum(input())

# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     return result
# print(do_something([2, 2, 2, 2]))


13.3 / 1
# def convert_to_miles(km):
#     return km * 0.6214
# num = int(input())
# print(convert_to_miles(num))

13.3 / 2
# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     if month in [4, 6, 9, 11]:
#         return 30
#     if month in [2]:
#         return 28
# num = int(input())
# print(get_days(num))
#
# def get_days(month):
#     return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
# num = int(input())
# print(get_days(num))

13.3 / 3
# def get_factors(n):
#     return [i for i in range(1, n + 1) if n % i == 0]
# n = int(input())
# print(get_factors(n))
#
# def get_factors(n):
#     z = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             z.append(i)
#     return z
# n = int(input())
# print(get_factors(n))

13.4 / 4
# def get_factors(n):
#     return len([i for i in range(1, n + 1) if n % i == 0])
# n = int(input())
# print(get_factors(n))

13.4 / 5
# def find_all(target, symbol):
#     return [i for i in range(len(target)) if target[i] == symbol]
# s = input()
# char = input()
# print(find_all(s, char))

13.4 / 6
# def merge(list1, list2):
#     return sorted(list1 + list2)
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# print(merge(numbers1, numbers2))

13.4 / 7
# n = int(input())
# def quick_merge(n):
#     return sorted([int(i) for i in range(n) for i in input().split()])
# print(*quick_merge(n))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# print(*sorted(sum([list(map(int, input().split())) for _ in range(int(input()))], [])))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# def quick_merge(n):
#     s = []
#     for i in range(n):
#         n = [int(i) for i in input().split()]
#         s += n
#     s.sort()
#     return s
# n = int(input())
# print(*quick_merge(n))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# def quick_merge(list1, list2):
#     result = []
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):   # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#     return result
# n = int(input())
# numbers1 = [int(c) for c in input().split()]
# for _ in range(1, n):
#     numbers1 = quick_merge(numbers1, [int(c) for c in input().split()])
# print(*numbers1)

13.5 / 1
# def is_valid_triangle(side1, side2, side3):
#     if a < (b+c) and b < (a+c) and c < (a+b):
#         return True
#     else:
#         return False
# a, b, c = int(input()), int(input()), int(input())
# print(is_valid_triangle(a, b, c))

13.5 / 2
# def is_prime(n):
#     return (len([i for i in range(1, n + 1) if n % i == 0])) == 2
# n = int(input())
# print(is_prime(n))

13.5 / 3
# def is_prime(num):
#     return (len([i for i in range(1, num + 1) if num % i == 0])) == 2
# def get_next_prime(num):
#     z = num + 1
#     while is_prime(z) == False:
#         z += 1
#     return z
# n = int(input())
# print(get_next_prime(n))

13.5 / 4
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
#
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
# txt = input()
# print(is_password_good(txt))

13.5 / 5
# def is_one_away(word1, word2):
#     counter = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 counter += 1
#     if len(word1) - counter == 1:
#         return True
#     return False
# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))

13.5 / 6
# def is_palindrome(text):
#     text = "".join(c for c in text if c.isalpha()).lower()
###   text = [i.lower() for i in text if i.isalpha()]
#     return text == text[::-1]
# txt = input()
# print(is_palindrome(txt))

13.5 / 7
# def is_valid_password(p):
#     z = p.split(":")
#     a, b, c = z[0], int(z[1]), int(z[2])
#     return len(z) == 3 and a == a[::-1] and (len([i for i in range(1, b + 1) if b % i == 0])) == 2 and c % 2 == 0
# psw = input()
# print(is_valid_password(psw))

13.5 / 8
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()','')
#     return not text
# txt = input()
# print(is_correct_bracket(txt))

13.5 / 9
# def convert_to_python_case(text):
#     z = text[0].lower()
#     for i in text[1:]:
#         if i.isupper():
#             z = z + '_' + i.lower()
#         else:
#             z += i
# ###     s += ('_' + c.lower() if c.isupper() else c)
# ###     return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()
#     return z
# txt = input()
# print(convert_to_python_case(txt))

13.6 / 1
# def get_middle_point(x1, y1, x2, y2):
#     x = (x_1 + x_2) / 2
#     y = (y_1 + y_2) / 2
#     return x, y
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

13.6 / 2
# from math import pi
# def get_circle(radius):
#     length = 2 * pi * r
#     square = pi * r**2
#     return length, square
# r = float(input())
# length, square = get_circle(r)
# print(length, square)

13.6 / 3
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     return (min(x1, x2)), (max(x1, x2))
###   return sorted([(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)])
# a, b, c = int(input()), int(input()), int(input())
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# ЭКЗАМЕН
# 14 / 1
# def draw_triangle():
#     for i in range(8):
#         print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))
# draw_triangle()
# print()

14 / 2
# def get_shipping_cost(quantity):
#     return 1000 + (quantity - 1) * 120
# n = int(input())
# print(get_shipping_cost(n))

14 / 3
# from math import factorial
# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k)*factorial(n - k)))
# n = int(input())
# k = int(input())
# print(compute_binom(n, k))

14 / 4
# def number_to_words(num):
#     x = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     y = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     z = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     for i in range(1, 100):
#         if num // 10 == 0:
#             return x[num-1]
#         elif num // 10 == 1:
#             return y[num % 10]
#         elif num % 10 == 0:
#             return z[num // 10 - 2]
#         else:
#             return z[num // 10 - 2] + " " + x[num % 10 - 1]
# n = int(input())
# print(number_to_words(n))
#
# def number_to_words(num):
#     s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто','']
#     if num <= 20:
#         return s[num - 1]
#     else:
#         return s[num // 10 - 1 + 18] + ' ' + s[num % 10 - 1]
# n = int(input())
# print(number_to_words(n))

14 / 5
# def get_month(language, number):
#     en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     return en[number - 1] if 'en' in language else ru[number - 1]
# lan = input()
# num = int(input())
# print(get_month(lan, num))

14 / 6
# def is_magic(date):
#     z = date.split('.')
#     return int(z[0])*int(z[1]) == int(z[2]) % 100
# date = input()
# print(is_magic(date))

14 / 7
# def is_pangram(text):
#     return len(set("".join(c for c in text if c.isalpha()).lower())) == 26
###   return len(set(text.lower().replace(" ", ""))) == 26
# text = input()
# print(is_pangram(text))


15.2 / 1  # УГАДАЙКА ЧИСЕЛ
# УГАДАЙКА ЧИСЕЛ
# import random
# import sys
# from time import *
#
# #an invitation to play
# print("HELLO, THIS IS ONE OF THE MOST SIMPLE BUT FUN OLD GAMES.")
# sleep(1.5)
# print("AND I OFFER YOU TO PLAY!")
# sleep(1)
# print("HOW ARE YOU INTERESTED?")
# sleep(1)
# print()
#
# #game rules
# def game_rules():
#     print('GREAT, YOU NEED TO GUESS THE NUMBER FROM "1" TO "100".')
#     sleep(1.5)
#     print('YOU HAVE "7" ATTEMPT.')
#     sleep(1.3)
#     print('WELL, THIS IS EVERYTHING!)')
#     sleep(1)
#     print('WE START!')
#     sleep(1)
#     print()
#
# # play_again
# def play_again(answer):
#     if answer.lower() == 'YES':
#         return play_game(), True
#     else:
#         return False
#
# # response check
# if input('PRINT "YES" OR "NO": ').lower() in ["yes", "+", "YES"]:
#     print()
#     sleep(0.6)
#     game_rules()
# else:
#     print("WELL, SEE YOU LATER!")
#     sys.exit()
#
# #checking for number
# def it_is_number(num):
#     if num.isdigit():
#         return int(num)
#     else:
#         print("INCORRECT, PLEASE ENTER A NUMBER.", "TRY AGAIN.", sep = "\n")
#         sleep(0.6)
#         return it_is_number(input(f'{name} ENTER YOUR NUMBER: '))
#
# # start the game
# print("GAME - GUESS THE NUMBER!")
# sleep(0.7)
# name = input("HI, WHAT'S YOUR NAME? ")
# sleep(0.9)
# num = random.randint(1, 100)
# counter = 0
# number_of_attempts = 7
# while True:
#     user_num = it_is_number(str(input(f'{name} ENTER YOUR NUMBER: ')))
#     sleep(0.5)
#     if 1 <= user_num <= 100:
#         counter += 1
#         if number_of_attempts == 1:
#             print(f'THE ATTEMPTS ENDED. THE HIDDEN NUMBER IS "{num}"')
#             sleep(0.7)
#             print('WILL YOU PLAY AGAIN?')
#             sleep(0.6)
#             break
#         if user_num > num:
#             number_of_attempts -= 1
#             print("TOO MUCH, TRY AGAIN.")
#             sleep(0.3)
#         elif user_num < num:
#             number_of_attempts -= 1
#             print("TOO LITTLE, TRY AGAIN.")
#             sleep(0.3)
#         else:
#             print(f'GREAT, YOU GUESSED IT!!! THIS NUMBER IS "{num}".')
#             sleep(0.7)
#             print(f'NUMBER OF ATTEMPTS IS "{counter}".')
#             sleep(0.7)
#             print("HOLD THE MEDAL!")
#             sleep(0.7)
#             print("       *")
#             print("(о°∨°)╯╯")
#             print()
#             sleep(1.5)
#             print("SHOULD WE PLAY AGAIN?")
#             sleep(0.65)
#             if input('"YES" OR "NO": ').lower() in ["yes", "+", "YES"]:
#                 num = random.randint(1, 100)
#                 sleep(1)
#                 continue
#             else:
#                 sleep(1.0)
#                 print(f"{name},THANKS FOR PLAYING!")
#                 sleep(1.0)
#                 print("WELL, SEE YOU LATER")
#                 break
#     else:
#         print("YOU DIDN'T ENTER A NUMBER FROM THE SPECIFIED RANGE")
#         sleep(1.0)
#         continue
#
# from random import randint
# def play_again(answer):
#     if answer.lower() == 'д':
#         return play_game(), True
#     else:
#         return False
# def is_digit(num):
#     if num.isdigit():
#         return int(num)
#     else:
#         print('Введите число')
#         return is_digit(input())
# def play_game():
#     guess_counter = 7
#     n = randint(1, 100)
#     print('''Попробуйте угадать число от 1 до 100. У Вас есть 7 попыток.\n'''
#           '''Введите число:''')
#     while True:
#         player_guess = is_digit(str(input()))
#         if guess_counter == 1:
#             print(f'Попытки закончились, было загадано число {n}')
#             break
#         if 1 > player_guess > 100:
#             print(f'Введенное число вне диапазона 1-100')
#         elif player_guess > n:
#             guess_counter -= 1
#             print(f'Загаданное число меньше {player_guess}, осталось {guess_counter} попыток')
#         elif player_guess < n:
#             guess_counter -= 1
#             print(f'Загаданное число больше {player_guess}, осталось {guess_counter} попыток')
#         elif player_guess == n:
#             print(f'Поздравляю! Вы угадали число {n}! c {8 - guess_counter}-й попытки')
#             break
# n = True
# play_game()
# while n:
#     print('Хотите сыграть ещё раз? (д/н)')
#     n = play_again(input())


# Перевод из какой-то случайной сс в десятичную
# def calculator(b, n):
#     if b != 16:
#         return sum([int(n[-1 - i]) * b**i for i in range(len(n))])
#     else:
#         s = list()
#         for i in range(len(n)):
#             if n[-1 - i] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
#                 s.append(int(n[-1 - i]) * b**i)
#             else:
#                 s.append((ord(n[-1 - i]) - 55) * b**i)
#         return sum(s)
# print('Вас приветствует калькулятор переводчик из какой-то случайной сс в десятичную сс.')
# while True:
#     print('Введите основание сс, а затем само число.')
#     base, number = int(input()), input()
#     print('Результат в десятичной сс =', calculator(base, number))
#     output = input('Если желаете покинуть программу, просто напишите EXIT и нажмите ENTER\nВ противном случае нажмите ENTER\n')
#     if output == 'EXIT':
#         break

# # Перевод из десятичной сс в случайную
# n = int(input('В какую систему конвертируем: '))
# num = int(input('Введите число: '))
# res_list = []
#
# while num != 0:
#     x = num % n
#     if x >= 10:
#         sym = chr(87 + x)
#         res_list.insert(0, str(sym.upper()))
#     else:
#         res_list.insert(0, str(x))
#     num = num // n
#
# print(''.join(res_list))

# a, b, c = int(input()), int(input()), int(input())
# p = (a + b + c)/2
# print((p*(p-a)*(p-b)*(p-c))**0.5)



# n, s = int(input()), {}
# for _ in range(n):
#     x = int(input())
#     s.setdefault(x)
# # for key in s:
# #     print(key)
# print(s)


