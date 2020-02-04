#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_5_4():
    for (stop_condition, move) in [
        ( wall_is_on_the_right, move_right ), 
        ( wall_is_beneath, move_down ), 
        ( wall_is_on_the_left, move_left ), 
        ( wall_is_above, move_up ) ]:
        while not stop_condition():
            move()


if __name__ == '__main__':
    run_tasks()
