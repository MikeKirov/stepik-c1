from random import choice
import sys
from time import *

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено',
           'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
           'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
           'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да',
           'Сконцентрируйся и спроси опять', 'Весьма сомнительно']


# игра
def start_game():
    while True:
        sleep(1)
        print(f'ХОРОШО {user_name} ДАВАЙ СВОЙ ВОПРОС!')
        print()
        input('>>> ')
        thinking()
        sleep(1.2)
        print('>>>', choice(answers), '<<<')
        print()
        sleep(1)
        if repeat_game():
            continue
        else:
            sleep(1.2)
            print('НУ ВСЕ БЫВАЙ! ДО СКОРОГО!')
            sleep(1)
            sys.exit()


# обдумывание ответа
def thinking():
    thoughts_counter = 3
    thoughts = ['ТАААК, А ВОТ ЭТО ДЕЙСТВИТЕЛЬНО ИНТЕРЕСНО...', 'ТАК-ТАК ТАК, ЧТО-ТО ПРИПОМИНАЮ', 'GOOOOOD MOOORNING VIIIETNAM!!!',
                'ЗИМА - ХОЛОДА, ОДИНОКИЕ МОРЯ, АХ ДА, О ЧЕМ ЭТО Я... У ТЕБЯ ЖЕ ВОПРОС!!!',
                'ЕРОР!!! ЕРОР!!! ОБНАРУЖЕНА СИСТЕМНАЯ ОШИБКА... ШЧ-ШЧ) ША ВСЕ СДЕЛАЕМ',
                'ТЮЮЮ, ЭТО Я ЗНАЮ И ТАК, А ВОТ НАДО ЛИ ТЕБЕ ЭТО ЗНАТЬ НАДО ЕЩЁ ПОДУМАТЬ... ЛАДНО, ВОТ ОТВЕТ НА ТВОЙ ВОПРОС',
                'МОЙ ОТВЕТ Ж - ЧЕРВИ! А НЕТ, ЭТО ДРУГОЙ ВОПРОС', 'ФРИ СЭКОНДС ПЛИЗ']
    for _ in range(thoughts_counter):
        sleep(1.2)
        print(choice(thoughts))
        sleep(1.2)
        print('...')
        sleep(1.2)


# повторная игра
def repeat_game():
    repeat = input('ХОЧЕШЬ УЗНАТЬ ЧТО-НИБУДЬ ЕЩЁ? ДА / НЕТ: ').lower()
    if repeat in ["да", "+", "lf"]:
        sleep(1.0)
        start_game()
        return True
    elif repeat in ["нет", "-", "ytn"]:
        sleep(1.0)
        return False
    else:
        sleep(1.0)
        print("ВЫЙДИ И ЗАЙДИ НОРМАЛЬНО! ШЧ-ШЧ) НУ ТАК КАК?")
        print()
        sleep(1.0)
        repeat_game()


# проверка ответа
def response_check():
    answer = input('ХОЧЕШЬ ЕГО ЗАДАТЬ? ДА / НЕТ: ').lower()
    if answer in ["да", "+", "lf"]:
        return True
    elif answer in ["нет", "-", "ytn"]:
        sleep(0.5)
        print("НА НЕТ И СУДА НЕТ.")
        print()
        sleep(0.5)
        print("ВСЕ")
        sleep(0.5)
        print("ГО")
        sleep(0.5)
        print()
        sleep(0.5)
        print("ХО")
        sleep(0.5)
        print("РО")
        sleep(0.5)
        print("ШЕ")
        sleep(0.5)
        print("ГО")
        sleep(0.5)
        print("!")
        sleep(0.5)
        sys.exit()
    else:
        print("ЭЭЭМ, ЧТО?")
        response_check()

sleep(0.7)
print('ПРИВЕТ! Я - МАГИЧЕСКИЙ ШАР!')
sleep(1.2)
print('ВОТ УЖЕ 2000 ЛЕТ Я ОТВЕЧАЮ ЛЮДЯМ НА ИХ САМЫЕ ДУШЕРАЗДИРАЮЩИЕ ВОПРОСЫ')
sleep(1)
print('УВЕРЕН У ТЕБЯ ТОЖЕ ЕСТЬ ХОТЯ БЫ 1 ТАКОЙ')
sleep(0.9)
response_check()
sleep(0.9)
print()
user_name = input(f'ОТЛИЧНО! ПРЕЖДЕ ВСЕГО ХОТЕЛОСЬ БЫ УЗНАТЬ ТВОЕ ИМЯ? ').upper()
sleep(0.5)
start_game()
