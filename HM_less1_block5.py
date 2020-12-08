# Block 5
earning = int(input("Введите выручку фирмы за период: "))
debit = int(input("Введите расходы фирмы за период: "))
fin_result = earning - debit
profit = round((fin_result / earning), 1)
if earning > debit:
    print(f"Фирма работает с прибылью, рентабельность {profit} процентов")
    personal = int(input("Сколько сотрудников работает на фирме? "))
    fin_result_per_person = fin_result / personal
    print(f"Рентабельность работы фирмы в перерасчете на одного сотрудника составляет {fin_result_per_person} рублей")
else:
    print(f"Фирма работает в убыток. Дефицит: {fin_result} рублей")