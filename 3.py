
#Факториал числа: Запросите у пользователя целое неотрицательное число 
#и вычислите его факториал. Факториал числа n, вычисляется как n! = 1 × 2 × 3 × … × n.

n = int(input("Введите неотрицательное число и будет вычислен его факториал: "))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1
    
print(factorial)
