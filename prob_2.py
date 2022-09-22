# Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

l = [1, 5, 2, 3, 4, 6, 1, 7]
lr = [l[i] for i in range(1, len(l)) if l[i] > max(l[:i])]
lr.insert(0, l[0])
print(lr)
