#1.2 Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. 
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите число: "))
d = {i : 3*i + 1 for i in range(1,number+1)}
print(f"Итоговая последовательность: {d}")