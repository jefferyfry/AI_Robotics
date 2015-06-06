__author__ = 'jeffro'
# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False
        for row in range(len(grid)):
            #print '     row=',row
            for col in range(len(grid[0])):
                #print '          col=',col
                if row == goal[0] and col == goal[1]:
                    if value[row][col]>0:
                        change = True
                        value[row][col] = 0
                        policy[row][col] = '*'
                elif grid[row][col] == 0:
                    for i in range(len(delta)):
                        #row,col forward neighbor row
                        nbrRow = row + delta[i][0]
                        nbrCol = col + delta[i][1]
                        nbrVal = cost_step

                        #row,col left neighbor row
                        nbrLeftRow = row + delta[(i+1)%4][0]
                        nbrLeftCol = col + delta[(i+1)%4][1]

                        #row,col right neighbor row
                        nbrRightRow = row + delta[(i-1)%4][0]
                        nbrRightCol = col + delta[(i-1)%4][1]

                        #if forward nbr cell is valid then calculate costs
                        if nbrRow >=0 and nbrCol >= 0 and nbrRow < len(grid) and nbrCol < len(grid[0]) and grid[nbrRow][nbrCol]==0:
                            nbrVal = nbrVal + value[nbrRow][nbrCol]*success_prob

                            #calulate cost for left going off grid
                            if nbrLeftRow < 0 or nbrLeftCol < 0 or nbrLeftRow >= len(grid) or nbrLeftCol >= len(grid[0]):
                                nbrVal = nbrVal + collision_cost * failure_prob
                            #calculate left cost otherwise
                            else:
                                nbrVal = nbrVal + value[nbrLeftRow][nbrLeftCol] * failure_prob

                            #calulate cost for right going off grid
                            if nbrRightRow < 0 or nbrRightCol < 0 or nbrRightRow >= len(grid) or nbrRightCol >= len(grid[0]):
                                nbrVal = nbrVal + collision_cost * failure_prob
                            #calculate right cost otherwise
                            else:
                                nbrVal = nbrVal + value[nbrRightRow][nbrRightCol] * failure_prob

                            if nbrVal < value[row][col]:
                                change = True
                                value[row][col] = nbrVal
                                policy[row][col] = delta_name[i]
                                #print '====='
                                #for debugRow in value:
                                #    print debugRow


    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print row
for row in policy:
    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 1000.00, 1000.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']

