import sys
import math
# Links to read
# https://www.codingame.com/blog/one-hour-learn-bot-programming/
# http://files.magusgeek.com/csb/csb_en.html
# https://www.codementor.io/blog/basic-pathfinding-explained-with-python-5pil8767c1
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

can_boost = True
checkpoints = []

last_target = (0, 0)

def get_distance(xA, yA, xB, yB):
    return math.floor(math.sqrt((xA - xB) ** 2 + (yA - yB) ** 2))

def get_closest_point_in_checkpoint(x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist):
    closest_x = math.floor(next_checkpoint_x + 500 * ((x - next_checkpoint_x)/next_checkpoint_dist))
    closest_y = math.floor(next_checkpoint_y + 500 * ((y - next_checkpoint_y)/next_checkpoint_dist))
    return closest_x, closest_y

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(f"next checkpoint dist {next_checkpoint_dist}", file=sys.stderr, flush=True)

    thrust = 100

    if (next_checkpoint_angle < -90 or next_checkpoint_angle > 90 or next_checkpoint_dist < 1000):
        thrust = 5
    
    distance_opponent_checkpoint = get_distance(opponent_x, opponent_y, next_checkpoint_x, next_checkpoint_y)
    distance_with_opponent = get_distance(x, y, opponent_x, opponent_y)


    if (distance_with_opponent > 4000 and distance_opponent_checkpoint < next_checkpoint_dist and next_checkpoint_angle == 180 and can_boost): # magic value == BAD
        thrust = "BOOST"
        can_boost = False

    closest_point = get_closest_point_in_checkpoint(x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist)

    print(f"thrust {thrust}", file=sys.stderr, flush=True)

    print(f"{closest_point[0]} {closest_point[1]} {thrust}")
