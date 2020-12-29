import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = [input().split() for _ in range(nb_elevators)]      # elevator_floor, elevator_pos
elevators.sort()

change_dir = False
block = 0
while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    floor = clone_floor

    if direction == 'RIGHT':
        change_dir = True if clone_pos-exit_pos > 0 else False
        if elevators != [] and floor < len(elevators):
            change_dir = True if clone_pos-int(elevators[floor][1]) > 0 else False
    elif direction == 'LEFT':
        change_dir = True if clone_pos-exit_pos < 0 else False
        if elevators != [] and floor < len(elevators):
            change_dir = True if clone_pos-int(elevators[floor][1]) < 0 else False

    
    if change_dir == True and block <= floor:
        print('BLOCK')
        change_dir = False
        block += 1
    elif change_dir == True:
        print('WAIT')
        block += 1
    else:
        print('WAIT')

    
