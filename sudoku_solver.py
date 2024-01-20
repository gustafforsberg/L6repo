
        #X
grid = [[0, 5, 9, 7, 3, 2, 8, 6, 1], #Y
        [6, 0, 1, 0, 0, 0, 0, 0, 3],
        [0, 8, 0, 6, 9, 1, 0, 7, 5],
        [0, 9, 7, 0, 2, 8, 5, 3, 0],
        [0, 6, 0, 1, 7, 0, 0, 0, 4],
        [0, 2, 4, 0, 5, 6, 7, 1, 0],
        [2, 0, 8, 9, 0, 4, 6, 0, 7],
        [0, 0, 0, 5, 8, 3, 0, 9, 0],
        [0, 0, 0, 0, 6, 7, 3, 4, 8]]




def sort(x, y):
    """Tar emot kordinater och retunerar tre listor 'rad', 'column' och 'cube'"""
    column = []
    row = []
    cube = []
    
    for col in grid:
        column.append(col[x])

    row = grid[y]

    if (x <= 2) & (y <=2):          #cube 1

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

    elif ( x <= 2) & (5 < y < 9):   #cube 7
         for i in range(6, 9):
            cube.append(grid[i][0:3])

    elif ( 2 < x < 6) & (5 < y < 9):#cube 8
         for i in range(6, 9):
            cube.append(grid[i][3:6])

    elif ( 5 < x < 9) & (5 < y < 9):#cube 9
         for i in range(6, 9):
            cube.append(grid[i][6:9])


    

    cube = sum(cube, [])
    return row, column, cube


def find_missing_numbers(list):
   """Tar emot tre listor och retunerar en lista med tal som saknas"""
   missing_numbers_return = []
   missing_numbers_col_return = []

   rad = list[0]
   col = list[1]
   cube = list[2]
  
   for i in range(1,10):
      k = rad.count(i)
      j = col.count(i)
      l = cube.count(i)

      if (k == 0) & (j == 0) & (l == 0):
         #print(i)
         missing_numbers_return.append(i)


      elif k > 1:
         print('FAIL')
      
   return missing_numbers_return




def heal(x,y,num):
    """Tar emot kordinater och en lista med saknade tal 
    om det bara finns ett tal i listan så skrivs talet till sudokut på kordinaternas position"""
    if len(num) < 2:
      grid[y][x] = num[0]

    return



def sudoku_print(grid):
    for outer_element in grid:
        print(outer_element)
    return    


while True:

   if sum(sum(grid,[])) == 405:
       break
   
   for i in range(0, 9):
      y = i
   
      for j in range(0 ,9):
         x = j
         if grid[y][x] == 0:
               print("empty")#ta bort
               missing_num = find_missing_numbers(sort(x,y))
               print(missing_num)#ta bort
               heal(x, y ,missing_num)
   



sudoku_print(grid)
            










