# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from __future__ import barry_as_FLUFL
from msilib.schema import tables
import random

sweets = 2021

def move_player():
    while True:
        move = int(input('Ваш ход, но не более 28 конфет: '))
        if move > 28:
            print('error')
        else:
            return move


player = True
first_move = random.randint(1, 2)
if first_move == 1:
    player = True
    print('Ход первого игрока: ')
else:
    player = False
    print('Ход бота: ')
while sweets != 0:
    if player is True:
        sweets -= move_player()
        print(f'На столе осталось {sweets} конфет')
        player = False
    elif player is False:
        if 56 > sweets >= 29:
            move_bot = random.randint (1, sweets - 28)
            print(f'бот взял {move_bot} конфет')
            sweets -= move_bot
            print(f'На столе осталось {sweets} конфет')
            player = True
        else:
            move_bot = random.randint(1, 29)
            print(f'На столе осталось {sweets} конфет')
            sweets -= move_bot
            print(f'На столе осталось {sweets} конфет')
            player = True
    if sweets <= 28:
        if player is True:
            print('Победил игрок')
            break
        else:
            print('Победа бота')


