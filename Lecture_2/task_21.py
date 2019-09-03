#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    move_right()
    move_down()
    y = 0
    for i in range(6):
        for j in range (i+2+y):
            fill_cell()
            move_left()
        move_down()

        for k in range (i+3+y):
            move_right()
            fill_cell()
        y += 1
        move_right()
        move_down()
    move_left(13)




if __name__ == '__main__':
    run_tasks()
