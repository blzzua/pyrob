#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    def check_up():
        if not wall_is_above():
            move_up()
            fill_cell()
            move_down()
    
    def check_down():
        if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()

    def check_inside():
        if ( wall_is_above() and wall_is_beneath()) :
            fill_cell()



    """
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
    while not wall_is_on_the_right():
        check_up()
        check_down()
        check_inside()
        move_right()
    check_up()
    check_down()
    check_inside()

if __name__ == '__main__':
    run_tasks()
