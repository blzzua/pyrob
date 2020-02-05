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
def fill_cross():
    move_right() ;fill_cell()
    move_down()  ;fill_cell()
    move_down()  ;fill_cell() ;move_up()
    move_right() ;fill_cell() ;move_left()
    move_left()  ;fill_cell() ;move_up()

@task
def task_2_2():
    move_down();
    for i in range(5):
        fill_cross();
        if i <= 3:
            move_right(n=4)

if __name__ == '__main__':
    run_tasks()
