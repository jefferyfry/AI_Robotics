__author__ = 'jeffro'
# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

#this actually builds value and policy at the same time
def optimum_policy(grid,goal,cost):
    #init value
    value = [[99 for row in range(len(grid))] for col in range(len(grid[0]))]
    policy = [[' ' for row in range(len(grid))] for col in range(len(grid[0]))]

    openList = []
    #add init to open list
    openList.append([goal[0],goal[1],0])
    #mark goal processed
    grid[goal[0]][goal[1]] = -1
    #mark goal in policy
    policy[goal[0]][goal[1]] = '*'

    #open list index = 0
    openListIndex = 0

    while (openListIndex < len(openList)):
        #grab next item on open list
        openCell = openList[openListIndex]
        openCellRow = openCell[0]
        openCellCol = openCell[1]
        openCellValue = openCell[2]
        value[openCellRow][openCellCol] = openCellValue

        #go through delta array to get next cells
        for i in range(len(delta)):
            #use delta to expand to new cell
            newCellRow = openCellRow + delta[i][0]
            newCellCol = openCellCol + delta[i][1]
            newCellValue = openCellValue + 1
            #ensure valid cell
            if newCellRow< 0 or newCellCol < 0 or newCellRow >= len(grid) or newCellCol >= len(grid[0]):
                continue
            #if newCell is wall, mark it a wall in the value grid
            elif grid[newCellRow][newCellCol] == 1:
                value[newCellRow][newCellCol] = 99
            #if newCell has been already processed, skip
            elif grid[newCellRow][newCellCol] < 0:
                continue
            # add new cell to the open list
            else:
                #add new cell (open cell g + 1) to open list
                openList.append([newCellRow,newCellCol,newCellValue])
                #mark new cell in grid as 1 to show visited
                grid[newCellRow][newCellCol] = -1
                policy[newCellRow][newCellCol] = delta_name[(i+2)%4]
        #next in the openList
        openListIndex+=1

        for i in range(len(policy)):
            print value[i]

    return policy

policy = optimum_policy(grid,goal,cost)
for i in range(len(policy)):
    print policy[i]

