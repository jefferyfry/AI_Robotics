__author__ = 'jeffro'
# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    #init value
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    openList = []
    #add init to open list
    openList.append([goal[0],goal[1],0])
    #visited
    grid[goal[0]][goal[1]] = -1

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
        #next in the openList
        openListIndex+=1


    return value

valueGrid = compute_value(grid,goal,cost)
for i in range(len(valueGrid)):
    print valueGrid[i]