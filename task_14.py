#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_11():
     if wall_is_above() and wall_is_beneath():
             fill_cell()
     if not wall_is_above() :
            move_up()
            fill_cell()
            move_down()
     if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()

     while not wall_is_on_the_right():
        move_right()
        if wall_is_above() and wall_is_beneath():
             fill_cell()
        if not wall_is_above() :
            move_up()
            fill_cell()
            move_down()
        if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()


if __name__ == '__main__':
    run_tasks()
