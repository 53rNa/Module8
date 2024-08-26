# Задача "План перехват"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    # Подсчитываем сумму чисел в numbers путём перебора и увеличиваем переменную result.

    for item in numbers:
        try:
            result += (item)

        # Если при переборе встречается данные, отличные от числового, то обработать исключение TypeError,
        # увеличив счётчик incorrect_data на 1
        except (TypeError):  # Обработка исключений, если элемент не число
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    # Возвращаем кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.
    return result, incorrect_data


def calculate_average(numbers):
    try:
        # В numbers может быть записана не коллекция, а другие типы данных, например числа, Проверяем это
        if not isinstance(numbers, (list, tuple, set, str)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)

        # Коллекция numbers может быть пустой, обрабатываем исключение ZeroDivisionError при делении на 0 и возвращаем 0
        average = total_sum / (len(numbers) - incorrect_data)

        return average

    except ZeroDivisionError:
        return 0
    # Обрабатываем исключение TypeError. В таком случае функция вернёт None
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
