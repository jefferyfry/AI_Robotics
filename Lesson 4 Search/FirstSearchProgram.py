__author__ = 'jeffro'
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    openList = []
    #add init to open list
    openList.append([0,init[0],init[1]])

    #mark as visited
    grid[init[0]][init[1]] = 1

    #open list index = 0
    openListIndex = 0

    while (openListIndex < len(openList)):
        #grab next item on open list
        openCell = openList[openListIndex]

        #if open cell is goal
        if [openCell[1],openCell[2]]==goal:
            return openCell
        #expand
        else:
            #go through delta array to get movement vectors
            for i in range(len(delta)):
                #use delta to expand to new cell
                newCell = [openCell[0]+1,openCell[1] + delta[i][0],openCell[2] + delta[i][1]]
                #ensure valid cell
                if newCell[1]< 0 or newCell[2] < 0 or newCell[1] >= len(grid) or newCell[2] >= len(grid[0]):
                    continue
                #if newCell was already visited or wall skip, reuse grid since you don't visit walls or revisit cells
                elif grid[newCell[1]][newCell[2]]:
                    continue
                # add new cell to the open list
                else:
                    #add new cell (open cell g + 1) to open list
                    openList.append(newCell)
                    #mark new cell in grid as 1 to show visited
                    grid[newCell[1]][newCell[2]] = 1
        #next in the openList
        openListIndex+=1

    return 'fail'

print search(grid,init,goal,cost)


