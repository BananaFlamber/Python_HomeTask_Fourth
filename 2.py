print("\033c")

lst = map(int, input("Введите числа через пробел: ").split())

new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]

print(f"Список из неповторяющихся элементов заданной Вами последовательности: {new_lst}")
