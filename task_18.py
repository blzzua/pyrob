#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    if not wall_is_on_the_left():
        while wall_is_above():
            move_left()
            if wall_is_on_the_left():
                    while wall_is_above():
                        move_right()
    if not wall_is_above():
        while not wall_is_above():
            move_up()
    if not wall_is_on_the_left():
        while not wall_is_on_the_left():
            move_left()

if __name__ == '__main__':
    run_tasks()
