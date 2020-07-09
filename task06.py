current_value = int(input("Сколько метров вы можете пробежать сейчас?: "))
future_value = int(input("К какому результату стремитесь?: "))
days = 0
while current_value <= future_value:
    days += 1
    current_value = current_value * 1.1
print(f"Этот результат сможете достичь на {days} день")