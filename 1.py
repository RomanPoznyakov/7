
# Проверка на четность/нечетность:
# Запросите у пользователя целое число и определите, является ли оно четным или нечетным. Выведите соответствующее сообщение.
number = int(input("Введите целое число: "))

if number % 2 == 0:
    print("Число", number, "является четным")
else:
    print("Число", number, "является нечетным")
