
#Поиск максимума: Попросите пользователя ввести три числа. Найдите и выведите максимальное из них, используя условный оператор.

number_first = float(input("Введите первое число: "))
number_second = float(input("Введите второе число: "))
number_third = float(input("Введите третье число: "))

max_number = number_first
if number_second > max_number:
    max_number = number_second
if number_third > max_number:
    max_number = number_third
print("Самым большим является число", max_number)
