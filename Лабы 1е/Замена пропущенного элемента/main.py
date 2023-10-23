numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
first_list = numbers[:4]
second_list = numbers[5:]
numbers[4] = (sum(first_list) + sum(second_list)) / len(numbers)
print("Измененный список:", numbers)

