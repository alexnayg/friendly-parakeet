user_number = int(input("Введите целое положительное число:"))
max_number = 0
while user_number > 0:
    check = user_number % 10
    user_number = user_number // 10
    if check > max_number:
        max_number = check
    else:
        continue
print(f"Максимальна цифра в числе: {max_number}")
