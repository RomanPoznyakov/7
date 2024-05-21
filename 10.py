
#FizzBuzz: Напишите программу, которая выводит числа от 1 до 100.
#Но для чисел, кратных трём, вместо числа выведите “Fizz”, а для чисел, кратных пяти, выведите “Buzz”.

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()
