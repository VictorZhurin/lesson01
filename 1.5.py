plus = int(input('Введите вашу выручу: '))
minus = int(input('Введите сумму ваших издержек: '))
check = plus - minus
if plus > minus:
    print('Ваше дело прибыльно!')

    print('Сумма вашей прибыли: ', check)
    people = int(input('Сколько сотрудников в вашей компании: '))
    b = check / people
    print('Ваша прибыль на одного сотрудника компании равна ', b)

else:
    print('Увы, вы в убытке')

