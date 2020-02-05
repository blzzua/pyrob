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

@task
def task_8_21():
    directions={'rd': (move_right,move_down) ,'ru': (move_right,move_up) ,'ld': (move_left,move_down),'lu': (move_left,move_up)}

    def opposite_corner():
        if wall_is_on_the_left() and wall_is_above():
            direction='rd'
        elif wall_is_on_the_left() and wall_is_beneath():
            direction='ru'
        elif wall_is_on_the_right() and wall_is_above():
            direction='ld'
        elif wall_is_on_the_right() and wall_is_beneath():
            direction='lu'
        else:
            direction='no' ## not in corner
        return direction

    direction=opposite_corner()
    while True:
        for move in directions[direction]:
            move()
        if opposite_corner() != 'no':
            break

if __name__ == '__main__':
    run_tasks()
