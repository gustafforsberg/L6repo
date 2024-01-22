#!/usr/bin/python3

########################################
# SudokuSolver.py 
# Gustaf Forsberg
# Ei22
########################################

import sys

####### Funktionsdeklerationer #######

def sudoku_input():
    """Läser in en valfri .csv-fil  som ett command-line-argument, skapar en 2D-lista med "intar" och skriver ut den formaterad i terminalen"""
    csv_file = str(sys.argv[1])
    f = open(csv_file, mode = 'r')
    sudoku_string_list = []

    for line in f:
        sudoku_string_list.append(line.split(','))

    for outer_element in sudoku_string_list:
        sudoku_grid.append([int(i) for i in outer_element])

    f.close()
    print(f'Unsolved sudoku from file: {csv_file}')
    for outer_element in sudoku_grid:
        print(', '.join(str(element) for element in outer_element))
    return 


def row_column_cube_sort(x, y):
    """Tar emot kordinater till en position i sudokut och retunerar en 2D-lista med tre listor 'rad', 'column' och 'cube' beroende på position"""
    column = []
    row = []
    cube = []
    
    for col in sudoku_grid:
        column.append(col[x])

    row = sudoku_grid[y]

    if (x <= 2) & (y <= 2):          #cube 1

     for i in range(3):
        cube.append(sudoku_grid[i][0:3])

    elif (2 < x < 6) & (y < 2):     #cube 2
       for i in range(3):
            cube.append(sudoku_grid[i][3:6])

    elif (5 < x < 9) & (y < 2):     #cube 3
         for i in range(3):
            cube.append(sudoku_grid[i][6:9])
    
    elif (x <= 2) & (2 < y < 6):    #cube 4
         for i in range(3, 6):
            cube.append(sudoku_grid[i][0:3])
            
    elif (2 < x < 6) & (2 < y < 6): #cube 5
         for i in range(3, 6):
            cube.append(sudoku_grid[i][3:6])

    elif (5 < x < 9) & (2 < y < 6): #cube 6
        for i in range(3, 6):
            cube.append(sudoku_grid[i][6:9])

    elif ( x <= 2) & (5 < y < 9):   #cube 7
         for i in range(6, 9):
            cube.append(sudoku_grid[i][0:3])

    elif ( 2 < x < 6) & (5 < y < 9):#cube 8
         for i in range(6, 9):
            cube.append(sudoku_grid[i][3:6])

    elif ( 5 < x < 9) & (5 < y < 9):#cube 9
         for i in range(6, 9):
            cube.append(sudoku_grid[i][6:9])


    cube = sum(cube, [])
    return row, column, cube


def find_missing_numbers(lists):
   """Tar emot en 2D-lista med tre listor (row, column, cube) som delas upp. 
   Om tal mellan 1-9 inte finns i listorna och retunerar en lista med tal som saknas"""
   
   missing_numbers_return = []

   for i in range(1,10):
      row_nr_check= lists[0].count(i)
      column_nr_check = lists[1].count(i)
      cube_nr_check = lists[2].count(i)

      if (row_nr_check == 0) & (column_nr_check == 0) & (cube_nr_check  == 0):
         missing_numbers_return.append(i)

   return missing_numbers_return


def heal(x, y, missing_numbers_list):
    """Tar emot kordinater och en lista med saknade tal 
    om det bara finns ett tal i listan så skrivs talet till sudokut på kordinaternas position. 
    Finns det fler möjliga tal så görs ingenting"""
    if len(missing_numbers_list) == 1:
      sudoku_grid[y][x] = missing_numbers_list[0]

    return


def print_solved_sudoku(sudoku_grid):
    """Skriver ut 2D-listan som en sträng med rätt formaterning och skriver den till en filen 'solved.csv' """
    print('\nSolved sudoku:')
    f = open('solved.csv', mode = 'w')
    for outer_element in sudoku_grid:
        print(', '.join(str(element) for element in outer_element))
        f.writelines(', '.join(str(element) for element in outer_element) + '\n')
    f.close()
    print('Written to file: solved.csv ')
    return


####### program start #######

#skapar en lista för sudokut
sudoku_grid = []

#Läser in en .csv-fil som commandline argument och sparar den som en 2D-lista i 'sudoku_grid'
sudoku_input()

# I en while-loop körs en nästlad for-loop som räknar upp kordinaterna för x och y position i sudokut, från väsnster till höger, uppifrån och ner. 
# Varje position testats, om det finns en "0" i positionen listats möjliga kandidater för positionen
# Finns det bara en kandidat så skrivs nollan över med den nya siffran. 
# While-loopen körs så länge summan av sudokut inte är 405.
while True:

   if sum(sum(sudoku_grid,[])) == 405:
       break
   else:
    for y in range(0, 9):
        for x in range(0 ,9):
            if sudoku_grid[y][x] == 0:
                heal(x, y ,find_missing_numbers(row_column_cube_sort(x, y)))
   
       
# När sudokut är löst skrivs det ut i terminalen, samt skapar en .csv-fil med det lösta sudokut.
print_solved_sudoku(sudoku_grid)
            










