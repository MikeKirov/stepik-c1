# Генератор безопасных паролей
from random import choice


# генерация пароля(ей)
def gen_pass(pass_len, chars):
    password = ''
    for j in range(pass_len):
        password += choice(chars)
    return password


num_of_pass = int(input("Сколько паролей нужно сгенерировать?: "))
pass_len = int(input("Укажите длину пароля: "))
if pass_len < 8:
    print("Недопустимая длина пароля. Задана минимальная длина равная 8.")
    pass_len = 8
chars = ''
if input('Введите "+" если хотите чтобы в пароле использовались прописные буквы: ') == '+':
    chars += 'abcdefghijklmnopqrstuvwxyz'
if input('Введите "+" если хотите чтобы в пароле использовались заглавные буквы: ') == '+':
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if input('Введите "+" если хотите чтобы в пароле использовались цифры: ') == '+':
    chars += '0123456789'
if input('Введите "+" если хотите чтобы в пароле использовались символы: ') == '+':
    chars += '!#$%&*+-=?@^_.'
if input('Введите "+" если хотите чтобы в пароле использовались неоднозначные символы "il1Lo0O" ') != '+':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')
for i in range(num_of_pass):
    print(gen_pass(pass_len, chars))
