import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    vertical_move = ('N', -1) if initial_ty > light_y else ('S', 1) if initial_ty < light_y else ('', 0)

    horizontal_move = ('W', -1) if initial_tx > light_x else ('E', 1) if initial_tx < light_x else ('', 0)

    direction = vertical_move[0] + horizontal_move[0]
    initial_tx += horizontal_move[1]
    initial_ty += vertical_move[1]

    print(direction)
