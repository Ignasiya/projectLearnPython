loan_amount = float(input("Введите размер кредита (желаемая сумма денежных средств):"))

loan_rate = float(input("Введите процентную ставку по кредиту (процент годовых): "))
# Вычисляем месячный процент начислений, соответствующий указанному годовому:
monthly_deduction_rate = (1 + loan_rate/100) ** (1/12) - 1

monthly_loan_payment = float(input("Введите желаемый ежемесячный платёж: "))
if monthly_loan_payment < loan_amount * monthly_deduction_rate:
    print("Кредит не может быть выдан. Размер платежа должен погашать начисляемые % по кредиту.")
else:
    print("Кредит может быть выдан на следующих условиях:")
    remaining_debt = loan_amount
    loan_months = 0
    interest_charges = payment = debt_decrease = 0
    overall_loan_price = 0
    print()
    labels = ("month".rjust(8), "remaining debt".rjust(15), "charges".rjust(15),
              "debt decrease".rjust(15), "payment".rjust(15))
    print(*labels)  # Над таблицей выведем заголовки столбцов.
    print('-'*(8 + 15*4 + 4))  # И черту соответствующей длины.
    print(f"{loan_months:8} {remaining_debt:15.2f} {interest_charges:15.2f}",
          f"{debt_decrease:15.2f} {payment:15.2f}")  # Момент взятия кредита.
    while remaining_debt > 0.01:  # Пока долг больше одной копейки...
        loan_months += 1  # +1 месяц расчёта
        # Вычисляем размер начисленных процентов по кредиту:
        interest_charges = remaining_debt * monthly_deduction_rate
        # Вычисляем чему должен быть равен платёж в этом месяце:
        if monthly_loan_payment > remaining_debt + interest_charges:
            payment = remaining_debt + interest_charges
        else:
            payment = monthly_loan_payment
        # Вычисляем размер погашения основной суммы долга:
        debt_decrease = payment - interest_charges
        remaining_debt -= debt_decrease
        # Параллельно суммируем общий объём выплат по кредиту:
        overall_loan_price += payment
        # Выводим все рассчитанные значения в очередную строку таблицы:
        print(f"{loan_months:8} {remaining_debt:15.2f} {interest_charges:15.2f}",
              f"{debt_decrease:15.2f} {payment:15.2f}")
                
    print("Месяцев на погашение кредита:", loan_months)
    print("Полная стоимость кредита:", f"{overall_loan_price:0.2f}")


labels = "первый второй третий четвёртый".split()
data = [(1, 2, 3, 4),
        (10, 20, 30, 40),
        (100, 200, 300, 400)
       ]
with open('test.csv', 'w') as csv_file:
    print(','.join(labels), file=csv_file)
    for row in data:
        print(','.join(map(str, row)), file=csv_file)