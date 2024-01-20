
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


def find_missing_numbers(list):
   """Tar emot en lista och retunerar en lista med tal som saknas"""
   missing_numbers_return = []
   missing_numbers_col_return = []

   rad = list[0]
   col = list[1]
   cube = list[2]
   #print(rad)
   #print(col)


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
    if len(num) < 2:
      grid[y][x] = num[0]

    return

# if grid[y][x] == 0:
#     print("empty")
#     missing_num = find_missing_numbers(sort(x,y))
#     missing_num = missing_num[0]
#     print(missing_num)
#     heal(x, y ,missing_num)
#     print(grid)



i = 0
j = 0


while True:
   for i in range(0, 9):
      y = i
      #print("y = ", y)
      for j in range(0 ,9):
         x = j
         #print("x =", x)
         if grid[y][x] == 0:
               print("empty")
               missing_num =find_missing_numbers(sort(x,y))
               #missing_num = missing_num[0]
               print(missing_num)
               heal(x, y ,missing_num)

      
   print(grid)
            

