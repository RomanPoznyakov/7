
#Сумма элементов списка: Создайте список чисел. Вычислите и выведите сумму всех элементов списка.
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

numbers = list(map(int, input('Введите числа через пробел: ').split()))

print(listsum(numbers))
