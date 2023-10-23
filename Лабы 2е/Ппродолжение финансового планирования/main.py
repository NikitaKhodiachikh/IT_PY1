salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total = abs(salary - spend)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(0, months - 1):
    spend = spend + spend * increase
    total = total + spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total, 2))
