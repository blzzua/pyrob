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

def count_field_size():
    i=1
    if not wall_is_on_the_left():
        #im in left corner
        move_left()
    while not wall_is_beneath():
        move_down()
        i+=1
    return i

def fill_up_n_cell(n=0):
    i=1
    if n > 0:
        need_to_fill_cnt=n
        while i < need_to_fill_cnt:
            i=i+1
            move_up()
            fill_cell()
        move_down(n=need_to_fill_cnt-1)
    else:
        pass

@task(delay=0.01)
def task_4_11():
    field_size=count_field_size()
    need_to_fill_cnt=field_size-1
    while need_to_fill_cnt > 1 :
        move_right()
        fill_up_n_cell(need_to_fill_cnt)
        need_to_fill_cnt=need_to_fill_cnt-1
    move_left(field_size-3)

if __name__ == '__main__':
    run_tasks()
