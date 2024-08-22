# Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        # Пробуем сложить два переданных в функцию значения
        Sum = a + b
    except TypeError:
        # Обрабатываем наступившее исключение TypeError,возвращая из функции строковое представление этих значений
        return f"{a}{b}"
    return Sum

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
