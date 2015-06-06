__author__ = 'jeffro'
# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    openList = []
    #add init to open list
    openList.append([0,heuristic[init[0]][init[1]],init[0],init[1]])

    #mark as visited
    grid[init[0]][init[1]] = 1

    #open list index = 0
    openListIndex = 0

    while (openListIndex < len(openList)):
        #grab next item on open list
        openCell = openList[openListIndex]
        expand[openCell[2]][openCell[3]] = openListIndex
        #if open cell is goal
        if [openCell[2],openCell[3]]==goal:
            return expand
        #expand
        else:
            #closest newCell (closest to goal)
            closestNewCell = None
            #go through delta array to get movement vectors
            for i in range(len(delta)):
                #use delta to expand to new cell
                row = openCell[2] + delta[i][0]
                col = openCell[3] + delta[i][1]
                #ensure valid cell
                if row< 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                    continue
                #if newCell was already visited or wall skip, reuse grid since you don't visit walls or revisit cells
                elif grid[row][col]:
                    continue
                # add closest new cell to the open list
                else:
                    gVal = openCell[0]+1
                    hVal = gVal + heuristic[row][col]
                    #check if this new cell is the closest
                    if closestNewCell==None or hVal<closestNewCell[1]:
                        closestNewCell=[gVal,hVal,row,col]
                    #mark new cell in grid as 1 to show visited
                    grid[row][col] = 1
            #no way to get to the goal
            if closestNewCell == None:
                return 'fail';

            openList.append(closestNewCell)

        #next in the openList
        openListIndex+=1

    return expand

expand = search(grid,init,goal,cost,heuristic)
for i in range(len(expand)):
    print expand[i]


