print("Программа для перевода секунд в часы/минуты/секунды")
time = int(input("Введите время в секундах >>>  "))
hour = (time // 60) // 60
minute = (time // 60) % 60
second = time % 60
print(f"{hour}:{minute}:{second}")
