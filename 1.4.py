number = int(input('Введите число : '))
b = number % 10
number = number // 10
while number > 0:
    if b > number:
        print(b)
        break
    else:
        print(number)
        break
