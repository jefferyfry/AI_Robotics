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
            for col in range(len(grid[0])):
                if row == goal[0] and col == goal[1]:
                    if value[row][col]>0:
                        change = True
                        value[row][col] = 0
                        policy[row][col] = '*'
                elif grid[row][col] == 0:
                    #cycle through the neighbor cells
                    for indexNbr in range(len(delta)):
                        nbrVal = cost_step
                        #cycle through the possible moves (left,forward, right)
                        for move in range(-1,2):
                            nbrRow = row+delta[(indexNbr+move)%4][0]
                            nbrCol = col+delta[(indexNbr+move)%4][1]

                            if move == 0: #success
                                outcome = success_prob
                            else: #fail
                                outcome = failure_prob

                            #calculate costs for in grid
                            if nbrRow >=0 and nbrCol >= 0 and nbrRow < len(grid) and nbrCol < len(grid[0]) and grid[nbrRow][nbrCol]==0:
                                nbrVal = nbrVal + value[nbrRow][nbrCol]*outcome
                            #collision costs for out of grid
                            else:
                                nbrVal = nbrVal + collision_cost*outcome

                        if nbrVal < value[row][col]:
                            change = True
                            value[row][col] = nbrVal
                            policy[row][col] = delta_name[indexNbr]
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

