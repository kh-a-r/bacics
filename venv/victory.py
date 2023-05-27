answer = 'да'

while answer == 'да':

    count = 0
    total = 5

    year = int(input('Когда родился Пушкин: '))
    if year == 1799:
        count += 1

    year = int(input('Когда родился Лермонтов: '))
    if year == 1814:
        count += 1

    year = int(input('Когда родился Моцарт: '))
    if year == 1756:
        count += 1

    year = int(input('Когда родился Бах: '))
    if year == 1684:
        count += 1

    year = int(input('Когда родился Дж.Депп: '))
    if year == 1963:
        count += 1


    print('Количество правильных ответов: ', count)
    print('Количество неправильных ответов: ', total - count)
    print('Процент правильных ответов: ', count/total*100)
    print('Процент неправильных ответов: ', (total - count)/total*100)

    answer = input('Вы хотите начать игру сначала? ')
    if answer == 'нет':
        break
