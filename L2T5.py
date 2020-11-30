# Урок 2. Практическое задание 5.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
# включительно. # Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

i = 32
while i < 128:
    print(f'{i:3} = "{chr(i)}" ', end='')
    i += 1
    if i % 10 == 2:
        print()