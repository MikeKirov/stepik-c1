# Шифр Цезаря
import sys


# выбор языка
def language_selection():
    global language
    lang = input('Выберите язык шифрования "РУССКИЙ" - "РУ" || АНГЛИЙСКИЙ" - "EN". >>> ').lower()
    if lang in ['ru', 'he', 'ру']:
        language = 1
        encryption_step()
    elif lang in ['ен', 'ут', 'en']:
        language = 2
        encryption_step()
    else:
        print("Ввод некоретных данных...")
        print()
        language_selection()


# шаг шифрования
def encryption_step():
    global user_step
    if language == 1:
        step = input('Выбран русский язык. Максимальный шаг шифрования 31. Введите число от "1" до "31". >>> ')
        if step.isdigit():
            if 0 < int(step) < 32:
                user_step = int(step)
                answer()
            else:
                print("Ввод некоретных данных...")
                print()
                encryption_step()
        else:
            print('Ввод некоретных данных...')
            print()
            encryption_step()
    if language == 2:
        step = input('Выбран английский язык. Максимальный шаг шифрования 25. Введите число от "1" до "25". >>> ')
        if step.isdigit():
            if 0 < int(step) < 26:
                user_step = int(step)
                answer()
            else:
                print("Ввод некоретных данных...")
                print()
                encryption_step()
        else:
            print('Ввод некоретных данных...')
            print()
            encryption_step()


# выбор шифрования
def answer():
    global code_0
    global enc_type
    what_doing = input('Введи "+" чтобы "ЗАШИФРОВАТЬ" текст или "-" чтобы "ДЕШИФРОВАТЬ. >>> ')
    if what_doing == "+":
        code_0 = 1
        enc_type = ("Шифрование текста завершено\n>>>")
        checking_the_text()
    elif what_doing == "-":
        code_0 = 2
        enc_type = ("Дешифровка текста завершена\n>>>")
        checking_the_text()
    else:
        print("Ввод некоретных данных...")
        print()
        answer()


# проверка текста
def checking_the_text():
    global text
    global enc_type
    text = input("Введите текст:\n>>>")
    for i in text:
        if language == 1 and i.isalpha() and i not in rus_l and i not in rus_U:
            print("Ввод некоретных данных... Переключите языковую раскладку")
            checking_the_text()
        elif language == 2 and i.isalpha() and i not in en_l and i not in en_U:
            print("Ввод некоретных данных... Переключите языковую раскладку")
            checking_the_text()
    else:
        coding()


# шифровка
def coding():
    if language == 1:
        alphabet = rus_l
        alphaBET = rus_U
        num_abc = 32
    elif language == 2:
        alphabet = en_l
        alphaBET = en_U
        num_abc = 26
    result = ''
    if code_0 == 1:
        for i in range(len(text)):
            if text[i].isalpha() and text[i].islower():
                result += alphabet[(alphabet.index(text[i]) + user_step) % num_abc]
            elif text[i].isalpha() and text[i].isupper():
                result += alphaBET[(alphaBET.index(text[i]) + user_step) % num_abc]
            else:
                result += text[i]
    if code_0 == 2:
        for i in range(len(text)):
            if text[i].isalpha() and text[i].islower():
                result += alphabet[(alphabet.index(text[i]) - user_step) % num_abc]
            elif text[i].isalpha() and text[i].isupper():
                result += alphaBET[(alphaBET.index(text[i]) - user_step) % num_abc]
            else:
                result += text[i]
    return result


# все варианты шифрования
def all_variants():
    print()
    variats = input('Желаете увидеть все варианты кодирования?\n"+" || "-"\n>>> ')
    if variats == "+":
        coding_2()
    elif variats == "-":
        sys.exit()
    else:
        print("Ввод некоретных данных...")
        print()
        all_variants()


# вывод всех возможных результатов
def coding_2():
    if language == 1:
        alphabet = rus_l
        alphaBET = rus_U
        num_abc = 32
    elif language == 2:
        alphabet = en_l
        alphaBET = en_U
        num_abc = 26
    result = ''
    for j in range(1, num_abc + 1):
        for i in range(len(text)):
            if text[i].isalpha() and text[i].islower():
                z = alphabet.rfind(text[i])
                result += alphabet[z - j]
            elif text[i].isalpha() and text[i].isupper():
                z = alphaBET.rfind(text[i])
                result += alphaBET[z - j]
            else:
                result += text[i]
        print(result)
        result = ''
    print()
    play_again()


# повторить игру
def play_again():
    again = input('На этом все?\n"+" || "-"\n>>> ')
    if again == "-":
        print()
        language_selection()
    elif again == "+":
        print("Всего доброго!")
        sys.exit()
    else:
        print("Ввод некоретных данных...")
        print()
        play_again()


en_l = 'abcdefghijklmnopqrstuvwxyz'
en_U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_l = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_U = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
language = ''
enc_type = ''
user_step = ''
text = ''
code_0 = ''
print('Приветствую, сейчас мы изучим такую интересную штуку как "ШИФР ЦЕЗАРЯ"')
print('Суть его в том чтобы менять каждую букву в письме на другую, которая следует за данной с заданным шагом')
print('Возьмем к примеру слово "ПРИВЕТ" и поменяем ве буквы с шагов в 4. В итоге получится "УФМЁИЦ"')
print("А теперь давай попробуем что-нибудь зашифровать. Также, можешь воспользоваться дешифровкой.")
print()
language_selection()
print(enc_type, coding())
all_variants()
