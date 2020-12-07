# # Block 1 part 1
variable1 = 2
variable2 = "three"
variable3 = 5
variable4 = 6.2

print(variable4 + variable3)
print(f'{variable3} + {variable2}')

# # Block 1 part 2
user_number1 = input("Введите число, пожалуйста\n>>>")
user_number2 = input("Введите число, пожалуйста\n>>>")
user_number1 = int(user_number1)
user_number2 = int(user_number2)
user_numbers_summ = user_number1 + user_number2
user_message1 = input("Введите сообщение, пожалуйста\n>>>")
user_message2 = input("Введите сообщение, пожалуйста\n>>>")

print(f"Вы вводили числа: '{user_number1}' '{user_number2}'\nСумма введенных чисел равна {user_numbers_summ}")
print(f"Вы вводили следующие сообщения: \n '{user_message1}' '{user_message2}'")

# Block 2
user_time_sec = input("Введите время в секундах\n>>>")
user_time_sec = int(user_time_sec)

hours = user_time_sec // (60 * 60)
minutes = (user_time_sec % (60 * 60)) // 60
sec = (user_time_sec % (60 * 60)) % 60

print(f"Точное время: {hours} : {minutes} : {sec}")

# Block 3
n = input("Введите число: \n>>>")
summ_1 = n + n
summ_2 = summ_1 + n
n = int(n)
summ_1 = int(summ_1)
summ_2 = int(summ_2)
result = (n + summ_1 + summ_2)
print(n)
print(summ_1)
print(summ_2)
print(f"Сумма чисел составляет: {result}")

# Block 4

user_number = int(input("Введите число: "))
last_number = user_number % 10  # Извлекаем последнюю цифру от введенного числа делением числа с остатком на 10
user_number = user_number // 10  # Приобразовываем введенное пользователем число за минусом последней цифры
# с помощью деления введенного нацело (//) на 10
while user_number > 0:  # Задействуем цикл while
    if user_number % 10 > last_number:  # Условие цикла если остаток от деления модицицированного число
        # на 10 будет больше за последнее число
        last_number = user_number % 10  # то последнее число (last_number) преобразовываем путем деления
        # user_bumber с остатком на 10. Для перебора всех цифр c конца и сравнения с last_number.
    user_number = user_number // 10  # делим полученное user_number нацело на 10 для завершения цикла,
    # пока user_number не будет равно 0
max_number = last_number  # Для читабельности кода
print(f"Максимальное число: {max_number}")


# Block 5
income = int(input("Введите выручку фирмы за период: "))
debit = int(input("Введите расходы фирмы за период: "))
fin_result = income - debit
if income > debit:
    print(f"Фирма работает с прибылью, рентабельность {fin_result} рублей")
    personal = int(input("Сколько сотрудников работает на фирме? "))
    fin_result_per_person = fin_result / personal
    print(f"Рентабельность работы фирмы в перерасчете на одного сотрудника составляет {fin_result_per_person} рублей")
else:
    print(f"Фирма работает в убыток. Дефицит: {fin_result} рублей")

# Block 6

distance_a = 3 # расстояние в первый день
distance_b = 15 # расстояние в крайний день
day = 1
while distance_a <= distance_b:
    print(f"День {day}, расстояние: {round(distance_a, 2)} км")
    distance_a = distance_a * 0.1 + distance_a
    day += 1
if distance_a > distance_b:
    day += 1
    print(f"Спортсмен достиг результата на {day} день - пробежал на менее {day} км")