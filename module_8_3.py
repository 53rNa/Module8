# Задача "Некорректность"

# Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом
# message - сообщение, которое будет выводиться при выбрасывании исключения
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = None
        self.__numbers = None

        self.__is_valid_vin(vin)
        self.__vin = vin

        self.__is_valid_numbers(numbers)
        self.__numbers = numbers

    # Проверяем корректность VIN номера. Выбрасываем исключение IncorrectVinNumber при некорректных данных
    def __is_valid_vin(self, vin_number):

        # Если передано не целое число
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')

        # Если переданное число находится не в диапазоне от 1000000 до 9999999 включительно
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    # Проверяем корректность автомобильных номеров. Выбрасываем исключение IncorrectCarNumbers при некорректных данных
    def __is_valid_numbers(self, numbers):
        # Если передана не строка
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        # Переданная строка должна состоять ровно из 6 символов
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
