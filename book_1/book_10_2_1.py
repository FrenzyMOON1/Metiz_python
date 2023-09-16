file_name = "guest.txt"

with open(file_name, "w", encoding='utf-8') as f:
    while True:
        f.write(input('Доброго времени суток, введите ваше имя: ') + '\n')
        print('Чтобы покинуть, введите exit / чтобы продолжить введите любой символ. ')
        print('Если вам не нравится программа, то укажите причину. ')
        answer = input('Ввод: ')
        if answer == 'exit':
            break
        else:
            f.write('Комментарий: ' + answer + '\n' + '\n')
