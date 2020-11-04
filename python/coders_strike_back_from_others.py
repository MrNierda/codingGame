import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
boosted = False
checkpoints = []

accumerr = 0
lasterr = 0
P, I, D = 0.03, 0.00, 0.02
lasttarget = (0,0)

def distance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in raw_input().split()]
    opponent_x, opponent_y = [int(i) for i in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    newpos = (x,y)
    target = (next_checkpoint_x, next_checkpoint_y)
    if target not in checkpoints:
        checkpoints.append(target)
    if target != lasttarget:
        lasttarget = target
        accumerr = 0
        lasterr = 0
    err = distance(newpos, target)
    accumerr += err
    errdiff = err - lasterr
    PID = (P*err + D*errdiff + I*accumerr)
    lasterr = err
    
    print >> sys.stderr, "P: " + str(P*err) + " I: " + str(I*accumerr) + " D: " + str(D*errdiff)
    print >> sys.stderr, "PID: " + str(PID)
    thrust = max(0, min(100, PID))

    if 60 <= abs(next_checkpoint_angle):
        thrust = 10
        print >> sys.stderr, "Angle big: " + str(next_checkpoint_angle)

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    if not boosted and 10 >= abs(next_checkpoint_angle) and next_checkpoint_dist >= 6000:
        strthrust = "BOOST"
        boosted = True
    else:
        strthrust = str(int(thrust))
    
    print >> sys.stderr, "Thrust: " + strthrust
    print >> sys.stderr, "Checkpoints: " + str(checkpoints)
    print str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + strthrust