
""" Solving a Sudoku puzzle """

# example of Sudoku puzzle

c = [[1, 0, 2, 6, 0, 4, 8, 0, 0],
     [0, 0, 0, 0, 8, 1, 4, 2, 5],
     [0, 0, 4, 0, 0, 0, 0, 0, 0],
     [0, 0, 9, 1, 6, 8, 2, 5, 0],
     [5, 3, 1, 4, 2, 9, 0, 8, 6],
     [0, 6, 8, 5, 3, 7, 9, 0, 0],
     [0, 0, 0, 0, 0, 0, 3, 0, 0],
     [8, 9, 3, 7, 5, 0, 0, 0, 0],
     [0, 0, 7, 9, 0, 3, 5, 0, 8]]



# iterating through rows and counting zeroes - generates a list with the number of zeroes per row 
def it_rows(array): 
    rows= []
    zeros = 0
    i = 0
    for row in array:
        zeros = row.count(0)
        i += 1
        rows.append(zeros)
    return rows


# iterating through columns and counting zeroes 
def it_cols(array):
    column = []
    columns = []
    
    for i in range (0, 9):
        for row in array:
            column.append(row[i])
        i += 1    
        columns.append(column)
        column = []

    cols = []
    zeros = 0
    i = 0
    for col in columns:
        zeros = col.count(0)
        i += 1
        cols.append(zeros)
    return cols


# iterating through grids and counting zeros

def it_grids(array):
    grid = []
    gridslist = []
    startrow = 0
    startcol = 0
    i = 0
    j = 0

    for startrow in range (0, 7, 3):
        for startcol in range (0, 7, 3):
            for i in range (startrow, startrow + 3):
                for j in range (startcol, startcol + 3):
                    grid.append(c[i][j])
                    j += 1   
                i += 1    
            gridslist.append(grid)
            grid = []
    grids = []
    zeros = 0
    i = 0
    for g in gridslist:
        zeros = g.count(0)
        i += 1
        grids.append(zeros)
    return grids


# placing a number when there is a single space left
def compl_row(array, key):
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = array[key]           # adjust that key to array address (starting with zero, not 1)
    ind = array[key].index(0)  # find the address of the zero
    missing = 0
    
    # find missing numbers in that row
    for i in integers:
        if i not in row:
            missing = i
    array[key][ind] = missing      # replace zero with missing number
    return array


def compl_col(array, key):
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array = c
    col = []

    # find elements in the column and which number is missing 
    for row in array:
        elem = row[key]
        col.append(elem)    
    for i in integers:
        if i not in col:
            missing = i
    # find location of zero, and replace it with missing number
    for row in array:
        if row[key] == 0:
            row[key] = missing
    return array


def compl_grid(array, key):
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    grid = []
    gridkeys = [[1, 0, 0], 
                [2, 0, 3],
                [3, 0, 6],
                [4, 3, 0],
                [5, 3, 3],
                [6, 3, 6],
                [7, 6, 0],
                [8, 6, 3],
                [9, 6, 6]]

    # find elements in the grid
    grid = []
    startrow = gridkeys[key][1]
    startcol = gridkeys[key][2]
    i = 0
    j = 0
    for i in range (startrow, startrow + 3):
        for j in range (startcol, startcol + 3):
            grid.append(array[i][j])
            j += 1   
        i += 1    
    
    # find missing number
    missing = 0
    for num in integers:
        if num not in grid:
            missing = num 
    
    i = 0
    j = 0    
    for i in range (startrow, startrow + 3):
        for j in range (startcol, startcol + 3):             
            if array[i][j] == 0:
                array[i][j] = missing 
            j += 1   
        i += 1    
    return array



# complete a row when there are 2 numbers missing
def compl2_row(array, key):
    row_ind = key
    index_counter = 0
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    missing = []
    indexes = []
    
    # find location of zeros
    for elem in array[row_ind]:
        if elem == 0:
            indexes.append(index_counter)
        index_counter += 1
            
    # find missing numbers 
    for num in integers:
        if num not in array[row_ind]:
            missing.append(num)

    # creates a list = COLUMN OF FIRST CHOICE
    colcontents = []
    for row in array:
        colcontents.append(row[indexes[0]])
        
    # grid list with locations
    g1 = [[0, 1, 2],[0, 1, 2]] 
    g2 = [[3, 4, 5],[0, 1, 2]]
    g3 = [[6, 7, 8],[0, 1, 2]]
    g4 = [[0, 1, 2],[3, 4, 5]]
    g5 = [[3, 4, 5],[3, 4, 5]]
    g6 = [[6, 7, 8],[3, 4, 5]]
    g7 = [[0, 1, 2],[6, 7, 8]]
    g8 = [[3, 4, 5],[6, 7, 8]]
    g9 = [[6, 7, 8],[6, 7, 8]]
    gridlist = [g1, g2, g3, g4, g5, g6, g7, g8, g9]   

    # creates a list = GRID OF FIRST CHOICE
    gridcontents = []
    for grid in gridlist:
        if row_ind in grid[0] and indexes[0] in grid[1]:
            for row in grid[0]:
                for col in grid[1]:
                    gridcontents.append(array[row][col])

            
    # check options against first place column and grid
    if missing[0] in colcontents or missing[0] in gridcontents:    # if first choice is in first place column or grid
        array[row_ind][indexes[0]] = missing[1]                    # swap and place
        array[row_ind][indexes[1]] = missing[0]

    elif missing[1] in colcontents or missing[1] in gridcontents:   # if the second choice is in first place column or grid
        array[row_ind][indexes[0]] = missing[0]                         # must place the first choice here
        array[row_ind][indexes[1]] = missing[1]        
    return array


# complete a col when there are 2 numbers missing
def compl2_col(array, key):
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column = []
    col_ind = key
    missing = []
    indexes = []
    index_counter = 0
    
    # create list with col contents
    for row in array:
        column.append(row[col_ind])
  
    # find location of zeros
    for row in array:
        if row[col_ind] == 0:
            indexes.append(index_counter)
        index_counter += 1  
           
    # find missing numbers 
    for num in integers:
        if num not in column:
            missing.append(num)
       
     # creates a list = ROW OF FIRST CHOICE
    rowcontents = array[indexes[0]]
    
    # grid list with locations
    g1 = [[0, 1, 2],[0, 1, 2]] 
    g2 = [[3, 4, 5],[0, 1, 2]]
    g3 = [[6, 7, 8],[0, 1, 2]]
    g4 = [[0, 1, 2],[3, 4, 5]]
    g5 = [[3, 4, 5],[3, 4, 5]]
    g6 = [[6, 7, 8],[3, 4, 5]]
    g7 = [[0, 1, 2],[6, 7, 8]]
    g8 = [[3, 4, 5],[6, 7, 8]]
    g9 = [[6, 7, 8],[6, 7, 8]]
    gridlist = [g1, g2, g3, g4, g5, g6, g7, g8, g9]   

    # creates a list = GRID OF FIRST CHOICE
    gridcontents = []
    for grid in gridlist:
        if col_ind in grid[1] and indexes[0] in grid[0]:
            for row in grid[0]:
                for col in grid[1]:
                    gridcontents.append(array[row][col])
    
    
    # check options against first place row and grid
    if missing[0] in rowcontents or missing[0] in gridcontents:    # if first choice is in first place row or grid
        array [indexes[0]] [col_ind] = missing[1]                  
        array [indexes[1]] [col_ind] = missing[0]
            
    elif missing[1] in rowcontents or missing[1] in gridcontents:   # if the second choice is in first place row or grid
        array [indexes[0]] [col_ind] = missing[0]                 
        array [indexes[1]] [col_ind] = missing[1]
      
    return array


# complete a grid when there are 2 numbers missing
def compl2_grid(array, key):
    # grid list with locations
    g1 = [[0, 1, 2],[0, 1, 2]] 
    g2 = [[3, 4, 5],[0, 1, 2]]
    g3 = [[6, 7, 8],[0, 1, 2]]
    g4 = [[0, 1, 2],[3, 4, 5]]
    g5 = [[3, 4, 5],[3, 4, 5]]
    g6 = [[6, 7, 8],[3, 4, 5]]
    g7 = [[0, 1, 2],[6, 7, 8]]
    g8 = [[3, 4, 5],[6, 7, 8]]
    g9 = [[6, 7, 8],[6, 7, 8]]
    gridlist = [g1, g2, g3, g4, g5, g6, g7, g8, g9]   
        
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]   
    grid_ind = key
    grid_loc = gridlist[grid_ind]   
    missing = []
    index_i = []
    index_j = []
    grid = []
    
    # finding the locations with zeros in a grid
    for i in grid_loc[0] :
        for j in grid_loc[1]:
            grid.append(array[i][j])
    
    for i in grid_loc[0] :
        for j in grid_loc[1]:
            if array[i][j] == 0:
                index_i.append(i)
                index_j.append(j)
    
    # find missing numbers 
    for num in integers:
        if num not in grid:
            missing.append(num)

    # creates a list = ROW OF FIRST CHOICE
    rowcontents = array[index_i[0]]
    
    # creates a list = COLUMN OF FIRST CHOICE
    colcontents = []
    for row in array:
        colcontents.append(row[index_j[0]])
    
    # check options against first place row and column
    if missing[0] in rowcontents or missing[0] in colcontents:    # if first choice is in first place row or col
        array [index_i[0]] [index_j[0]] = missing[1]                    
        array [index_i[1]] [index_j[1]] = missing[0]
  
    elif missing[1] in rowcontents or missing[1] in colcontents:   # if the second choice is in first place row or col
        array [index_i[0]] [index_j[0]] = missing[0]                         
        array [index_i[1]] [index_j[1]] = missing[1]
     
    return array
    

def compl3_row(array, key):
    row_ind = key
    index_counter = 0
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    missing = []
    indexes = []
    
    # find location of zeros
    for elem in array[row_ind]:
        if elem == 0:
            indexes.append(index_counter)
        index_counter += 1
            
    # find missing numbers 
    for num in integers:
        if num not in array[row_ind]:
            missing.append(num)


    print missing, indexes

    # creates a list = COLUMN OF FIRST CHOICE
    colcontents0 = []
    for row in array:
        colcontents0.append(row[indexes[0]])
    #... COLUMN OF second CHOICE
    colcontents1 = []
    for row in array:
        colcontents1.append(row[indexes[1]])

    colcontents2 = []
    for row in array:
        colcontents2.append(row[indexes[2]])
    # print 'colcontents0', colcontents0
    # print 'colcontents1', colcontents1
    # print 'colcontents2', colcontents2

    # grid list with locations
    g1 = [[0, 1, 2],[0, 1, 2]] 
    g2 = [[3, 4, 5],[0, 1, 2]]
    g3 = [[6, 7, 8],[0, 1, 2]]
    g4 = [[0, 1, 2],[3, 4, 5]]
    g5 = [[3, 4, 5],[3, 4, 5]]
    g6 = [[6, 7, 8],[3, 4, 5]]
    g7 = [[0, 1, 2],[6, 7, 8]]
    g8 = [[3, 4, 5],[6, 7, 8]]
    g9 = [[6, 7, 8],[6, 7, 8]]
    gridlist = [g1, g2, g3, g4, g5, g6, g7, g8, g9]   

    # creates a list = GRID OF FIRST CHOICE
    gridcontents0 = []
    for grid in gridlist:
        if row_ind in grid[0] and indexes[0] in grid[1]:
            for row in grid[0]:
                for col in grid[1]:
                    gridcontents0.append(array[row][col])
    # print 'gridcontents0', gridcontents0
                    
    # creates a list = GRID OF second CHOICE
    gridcontents1 = []
    for grid in gridlist:
        if row_ind in grid[0] and indexes[1] in grid[1]:
            for row in grid[0]:
                for col in grid[1]:
                    gridcontents1.append(array[row][col])
    # print 'row_ind, indexes[1]', row_ind, indexes[1]
    # print 'gridcontents1', gridcontents1

    # creates a list = GRID OF third CHOICE
    gridcontents2 = []
    for grid in gridlist:
        if row_ind in grid[0] and indexes[2] in grid[1]:
            for row in grid[0]:
                for col in grid[1]:
                    gridcontents2.append(array[row][col])
    # print 'gridcontents2', gridcontents2

            
    # check options 
    temp0 = []
    temp1 = []
    temp2 = []

    if missing[0] not in colcontents0 and missing[0] not in gridcontents0:
        temp0.append(missing[0])
    if missing[0] not in colcontents1 and missing[0] not in gridcontents1:
        temp1.append(missing[0])
    if missing[0] not in colcontents2 and missing[0] not in gridcontents2:
        temp2.append(missing[0])
        # array[row_ind][indexes[2]] = missing[0]

    if missing[1] not in colcontents0 and missing[1] not in gridcontents0:
        temp0.append(missing[1])
    if missing[1] not in colcontents1 and missing[1] not in gridcontents1:
        temp1.append(missing[1])
    if missing[01] not in colcontents2 and missing[01] not in gridcontents2: 
        temp2.append(missing[1])
        # array[row_ind][indexes[2]] = missing[1]

    if missing[2] not in colcontents0 and missing[2] not in gridcontents0:
        temp0.append(missing[2])
    if missing[2] not in colcontents1 and missing[2] not in gridcontents1:
        temp1.append(missing[2])
    if missing[2] not in colcontents2 and missing[2] not in gridcontents2:
        temp2.append(missing[2])
        # array[row_ind][indexes[2]] = missing[1]
    print     
    print 'temp0', temp0
    print 'temp1', temp1
    print 'temp2', temp2


    return array


# array[row_ind][indexes[1]] = missing[0]






print compl3_row(c, 3)




















def Sudoku(array):
    print 'initial grids'
    print it_rows(array)
    print
    print it_cols(array)
    print
    print it_grids(array)
    print 
    
    while any(0 in row for row in array):
        
        if 1 in it_rows(array):
            key = it_rows(array).index(1)
            array = compl_row(array, key)
            # break

        if 1 in it_cols(array):
            print 'it_cols 1', it_cols(array)
            key = it_cols(array).index(1)
            array = compl_col(array, key)
            # break 

        if 1 in it_grids(array):
            print 'it_grids 1',it_grids(array)
            key = it_grids(array).index(1)
            array = compl_grid(array, key)   
            # break
        
        else:

            if 2 in it_rows(array):
                print 'it_rows 2', it_rows(array)
                key = it_rows(array).index(2)
                array = compl2_row(array, key)
                print array
                # break

            elif 2 in it_cols(array):
                key = it_cols(array).index(2)
                array = compl2_col(array, key)
                # break

            elif 2 in it_grids(array):
                print 'it_grids 2', it_grids(array)
                key = it_grids(array).index(2)
                array = compl2_grid(array, key)   
                # break
            
            else:
                print 'break'
                break   
      
    return array
            
            
# print Sudoku(c)
# for row in Sudoku(c):
#     print row



