import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = {}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    if clone_floor == exit_floor:
        target = exit_pos
    elif clone_floor in elevators:
        target = elevators[clone_floor]
    
    if direction == 'RIGHT' and clone_pos > target:
        print('BLOCK')
    elif direction == 'LEFT' and clone_pos < target:
        print('BLOCK')
    else:
        print('WAIT')