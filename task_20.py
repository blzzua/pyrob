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

def run_left():
    while not wall_is_on_the_left():
        move_left()

def is_second_wall_is_beneath():
    move_down()
    if  wall_is_beneath():
        move_up()
        return True
    else:
        move_up()
        return False

@task(delay=0.01)
def task_4_3():
    while not is_second_wall_is_beneath():
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_on_the_right(): 
                fill_cell()
        move_down()
        run_left()
    move_right()

if __name__ == '__main__':
    run_tasks()
