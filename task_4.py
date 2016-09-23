#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_above():#Возвращает True, если сверху стена, иначе — False
        move_up(n=1)
    elif not wall_is_beneath(): 	#Возвращает True, если снизу стена, иначе — False
        move_down(n=1)
    elif not wall_is_on_the_left(): #Возвращает True, если слева стена, иначе — False
        move_left(n=1)
    elif not wall_is_on_the_right(): 	#Возвращает True, если справа стена, иначе — False
        move_right(n=1)


if __name__ == '__main__':
    run_tasks()
