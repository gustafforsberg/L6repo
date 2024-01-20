

grid = [[0, 5, 9, 7, 3, 2, 8, 6, 1],
        [6, 0, 1, 0, 0, 0, 0, 0, 3],
        [0, 8, 0, 6, 9, 1, 0, 7, 5],
        [0, 9, 7, 0, 2, 8, 5, 3, 0],
        [0, 6, 0, 1, 7, 0, 0, 0, 4],
        [0, 2, 4, 0, 5, 6, 7, 1, 0],
        [2, 0, 8, 9, 0, 4, 6, 0, 7],
        [0, 0, 0, 5, 8, 3, 0, 9, 0],
        [0, 0, 0, 0, 6, 7, 3, 4, 8]]




def sort(x, y):
    column = []
    row = []
    cube = []
    
    for col in grid:
        column.append(col[x])

    row = grid[y]

    if (x <= 2) & (y <=2):      #cube 1

     for i in range(3):
        cube.append(grid[i][0:3])

    elif (2 < x < 6) & (y < 2):     #cube 2
       for i in range(3):
            cube.append(grid[i][3:6])

    elif (5 < x < 9) & (y < 2):     #cube 3
         for i in range(3):
            cube.append(grid[i][6:9])
    
    elif (x <= 2) & (2 < y < 6):    #cube 4
         for i in range(3, 6):
            cube.append(grid[i][0:3])
            
    elif (2 < x < 6) & (2 < y < 6): #cube 5
         for i in range(3, 6):
            cube.append(grid[i][3:6])

    elif (5 < x < 9) & (2 < y < 6): #cube 6
        for i in range(3, 6):
            cube.append(grid[i][6:9])

    elif ( x <= 2) & (5 < y < 9):     #cube 7
         for i in range(6, 9):
            cube.append(grid[i][0:3])

    elif ( 2 < x < 6) & (5 < y < 9):     #cube 8
         for i in range(6, 9):
            cube.append(grid[i][3:6])

    elif ( 5 < x < 9) & (5 < y < 9):     #cube 9
         for i in range(6, 9):
            cube.append(grid[i][6:9])


    

    cube = sum(cube, [])
    return row, column, cube


print(sort(2, 2))








