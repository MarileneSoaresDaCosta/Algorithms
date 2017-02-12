
""" Solving a Sudoku puzzle 
http://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku  """

c = [[3, 2, 0, 0, 9, 7, 8, 0, 5],
     [9, 0, 0, 0, 0, 6, 0, 7, 1],
     [8, 0, 0, 3, 0, 0, 9, 4, 2],
     [0, 3, 0, 0, 0, 8, 0, 1, 6],
     [0, 0, 0, 0, 1, 0, 0, 0, 0],
     [1, 6, 0, 2, 0, 0, 0, 5, 0],
     [6, 9, 7, 0, 0, 2, 0, 0, 3],
     [4, 1, 0, 9, 0, 0, 0, 0, 7],
     [5, 0, 2, 7, 6, 0, 0, 9, 4]]

solved =    [[3, 2, 1, 4, 9, 7, 8, 6, 5],
             [9, 5, 4, 8, 2, 6, 3, 7, 1],
             [8, 7, 6, 3, 5, 1, 9, 4, 2],
             [2, 3, 9, 5, 7, 8, 4, 1, 6],
             [7, 4, 5, 6, 1, 9, 2, 3, 8],
             [1, 6, 8, 2, 3, 4, 7, 5, 9],
             [6, 9, 7, 1, 4, 2, 5, 8, 3],
             [4, 1, 3, 9, 8, 5, 6, 2, 7],
             [5, 8, 2, 7, 6, 3, 1, 9, 4]]


def findNextCellToFill(grid, i, j):
    for x in range(i,9):  # rows
        for y in range(j,9):
            if grid[x][y] == 0:
                # print 'row x, y', x, y
                return x,y
    for x in range(0,9):  # columns
        for y in range(0,9):
            if grid[x][y] == 0:
                # print 'col x, y', x, y
                return x,y
    return -1,-1



def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i/3), 3 *(j/3)
            # testing if number is in the grid
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False



def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)
    # print 'sud fn i, j', i, j
    if i == -1:
        return True
    for e in range(1,10):
        # print 'e', e
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking > let this loop run further 
            # print 'e, i, j', e, i, j, ' backt'
            grid[i][j] = 0

    return False


print solveSudoku(c)


for i in range(0,9):  # rows
        for j in range(0,9):
            if c[i][j] != solved[i][j]:
                print 'err c[i][j] ', 'i, j', i, j, ' ', c[i][j], ' != solved[i][j]', solved[i][j]

# this was the other possible solution





