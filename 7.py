
#Подсчет гласных и согласных: Попросите пользователя ввести строку. Посчитайте количество гласных и согласных букв в этой строке.

quest = int(input('Сколько будет строк? '))
gls = 0
sgl = 0
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
while quest > count:
    poem = input()
    for i in poem:
        if i.isalpha():
            if i in vse_gls:
                gls += 1
            else:
                sgl += 1
    count += 1

print('Кол-во гласных:', gls)
print('Кол-во согласных:', sgl)
