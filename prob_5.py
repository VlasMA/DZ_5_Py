# 5 Создайте программу для игры в "Крестики-нолики".


from distutils.file_util import move_file


field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def field_print():
    for i in field:
        print(i)

field_print()

move = True

def move_field(x):
    move_pl = int(input('Укажиет номер ячейки: '))
    if move_pl == 1:
        field[0][0] = x
    if move_pl == 2:
        field[0][1] = x
    if move_pl == 3:
        field[0][2] = x
    if move_pl == 4:
        field[1][0] = x
    if move_pl == 5:
        field[1][1] = x
    if move_pl == 6:
        field[1][2] = x
    if move_pl == 7:
        field[2][0] = x
    if move_pl == 8:
        field[2][1] = x
    if move_pl == 9:
        field[2][2] = x

    

def win(f, z):
    if z == f[0][0] == f[0][1] == f[0][2] or z == f[1][0] == f[1][1] == f[1][2] or \
            z == f[2][0] == f[2][1] == f[2][2] or z == f[0][0] == f[1][0] == f[2][0]\
            or z == f[0][1] == f[1][1] == f[2][1] or z == f[0][2] == f[1][2] == f[2][2]\
            or z == f[0][0] == f[1][1] == f[2][2] or z == f[0][2] == f[1][1] == f[2][0]:
        print ('ПОБЕДИТЕЛЬ - ', z)
        return False
    else:
        return True

    

win_flag = True

while win_flag is True:
    for _ in range(1, 10):
        if move is True:
            move_field('X')
            field_print()
            win_flag = win(field, 'X')
            move = False
        elif move is False:
            move_field('0')
            field_print()
            win_flag = win(field, '0')
            move = True
        if not win_flag:
            break
        win_flag = False
    else:   print('ничья')
