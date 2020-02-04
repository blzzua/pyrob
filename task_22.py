#!/usr/bin/python3

from pyrob.api import *

methods="""
    методы:
move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
wall_is_above()	если сверху стена, возвращает True, иначе — False
wall_is_beneath()	если снизу стена, возвращает True, иначе — False
wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
wall_is_on_the_right()	если справа стена, возвращает True, иначе — False
fill_cell()	Закрасить текущую клетку
cell_is_filled()	Возвращает True, если текущая клетка закрашена
mov(r, v)	Поместить значение v в регистр r
"""

def fill_right():
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        fill_cell()

def fill_left():
    fill_cell()
    while not wall_is_on_the_left():
        move_left()
        fill_cell()
 

@task(delay=0.01)
def task_5_10():
    while not wall_is_beneath():
        fill_right()
        if wall_is_beneath(): 
            fill_left()
        else:
            move_down()
            fill_left()
    if wall_is_above() and wall_is_beneath() and wall_is_on_the_left()  and wall_is_on_the_right() :
        fill_cell()
        pass


if __name__ == '__main__':
    run_tasks()
