# 6 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах..

# WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW


with open('RLE_in.txt', 'r', encoding='utf-8') as in_RLE:
    list_1 = []

    string = in_RLE.read()
    count = 1
    for i in range(len(string)-1):
        if i <= len(string):
            if string[i] == string[i + 1]:
                count += 1
            else:
                a = string[i]
                list_1.append(string[i]), list_1.append(str(count))
                count = 1
    list_1.append(string[i]), list_1.append(str(count))
    print(''.join(list_1))

with open('RLE.txt', 'w', encoding='utf-8') as out:
    list_2 = []
    for x in range(len(list_1)-1):
        if x % 2 == 0:
            list_2.append(list_1[x] * int(list_1[x+1]))
    out.write(''.join(list_2))
    print(''.join(list_2))
