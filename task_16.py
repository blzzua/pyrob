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
def task_8_22():
    global direction 
    global check_wall 
    def select_open_direction(excepted_direction = None):
        global direction
        global check_wall
            
        if not wall_is_above() and ( not excepted_direction is None or excepted_direction != move_up ):
            direction=move_up
            check_wall=wall_is_above
        elif not wall_is_on_the_left() and ( not excepted_direction is None or excepted_direction != move_left):
            direction=move_left
            check_wall=wall_is_on_the_left
        elif not wall_is_on_the_right() and ( not excepted_direction is None or excepted_direction != move_right):
            direction=move_right
            check_wall=wall_is_on_the_right
        elif not wall_is_beneath() and ( not excepted_direction is None or excepted_direction != move_down):
            direction=move_down
            check_wall=wall_is_beneath
        else:
            print(" как я сюда попал:", direction.__name__, " from  ", excepted_direction.__name__, ) 

    
    select_open_direction()
    while not check_wall():
        direction()
    # поворот
    select_open_direction(direction)
    while not check_wall():
        direction()
        
if __name__ == '__main__':
    run_tasks()
