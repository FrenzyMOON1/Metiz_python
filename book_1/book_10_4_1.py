import json


def get_digital():
    file_name = 'top_digital.json'
    digital = input(int('Ваше любимое число: '))
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(digital, f)


def take_digital():
    file_name = 'top_digital.json'
    try:
        with open(file_name, encoding='utf-8') as f:
            digital = json.load(f)
    except FileNotFoundError:
        get_digital()
    else:
        print(digital)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(int(input('Введите другое число: ')), f)


take_digital()
