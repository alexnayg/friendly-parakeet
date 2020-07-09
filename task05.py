revenue = int(input("Необходимо ввести выручку фирмы: "))
costs = int(input("Необходимо ввести издержки фирмы: "))
if costs > revenue:
    lesion = revenue - costs
    print(f"Убыток вашей фирмы составил: {lesion}")
else:
    print("Ваша фирма работает в прибыль!")
    profitability = revenue // costs
    print(f"Примерная рентабельность вашей фирмы:{profitability}")
    quantity_workers = int(input("Сколько сотрудников в вашей фирме ?: "))
    revenue_by_workers = revenue // quantity_workers
    print(f"Каждый сотрудник зарабатывает примерно по {revenue_by_workers} в месяц.")
