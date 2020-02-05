#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.01)
def task_9_3():
    field_size=1
    while not wall_is_on_the_right():
        move_right()
        field_size+=1

    for y in range(field_size):
        for x in range(field_size):
            if (x != y  and field_size - x != y + 1):
                fill_cell()
            if x != field_size-1:
                move_left()
        if y != field_size-1:
            move_right(field_size-1)
            move_down()
    pass

if __name__ == '__main__':
    run_tasks()
