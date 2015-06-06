__author__ = 'jeffro'
# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right

goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    #init value
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
             ]

    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
             [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
             [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
             [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
             ]

    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False
        for dir in range(len(forward_name)):
            #print 'dir=',dir
            for row in range(len(grid)):
                #print '     row=',row
                for col in range(len(grid[0])):
                    #print '          col=',col
                    if row == goal[0] and col == goal[1]:
                        if value[dir][row][col]>0:
                            change = True
                            value[dir][row][col] = 0
                            policy[dir][row][col] = '*'
                    elif grid[row][col] == 0:
                        for i in range(len(action)):
                            newDir = (dir + action[i])%4
                            newRow = row + forward[newDir][0]
                            newCol = col + forward[newDir][1]

                            if newRow >= 0 and newCol >= 0 and newRow < len(grid) and newCol < len(grid[0]) and grid[newRow][newCol] == 0:
                                #print "curr=",dir,",",row,",",col
                                #print "new=",newDir,",",newRow,",",newCol
                                newVal = value[newDir][newRow][newCol] + cost[i]
                                #print 'new value calc'
                                if newVal < value[dir][row][col]:
                                    #print 'value change'
                                    value[dir][row][col] = newVal
                                    policy[dir][row][col] = action_name[i]
                                    change = True

    row = init[0]
    col = init[1]
    dir = init[2]

    policy2D[row][col] = policy[dir][row][col]
    while policy[dir][row][col] != '*':
        if policy[dir][row][col] == '#':
            newDir = dir
        elif policy[dir][row][col] == 'R':
            newDir = (dir-1)%4
        elif policy[dir][row][col] == 'L':
            newDir = (dir+1)%4
        row = row + forward[newDir][0]
        col = col + forward[newDir][1]
        dir = newDir
        policy2D[row][col]=policy[dir][row][col]

    return policy2D

optimum_policy = optimum_policy2D(grid,init,goal,cost)
for i in range(len(optimum_policy)):
    print optimum_policy[i]