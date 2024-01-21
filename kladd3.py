
# grid = [[0, 5, 9, 7, 3, 2, 8, 6, 1],
#         [6, 0, 1, 0, 0, 0, 0, 0, 3],
#         [0, 8, 0, 6, 9, 1, 0, 7, 5],
#         [0, 9, 7, 0, 2, 8, 5, 3, 0],
#         [0, 6, 0, 1, 7, 0, 0, 0, 4],
#         [0, 2, 4, 0, 5, 6, 7, 1, 0],
#         [2, 0, 8, 9, 0, 4, 6, 0, 7],
#         [0, 0, 0, 5, 8, 3, 0, 9, 0],
#         [0, 0, 0, 0, 6, 7, 3, 4, 8]]


grid = []

def sudoku_input():

    f = open('sudukoComa.csv', mode = 'r')
    sudoku_string_list = []

    for line in f:
        sudoku_string_list.append(line.split(','))

    print(sudoku_string_list)

    for outer_element in sudoku_string_list:
        grid.append([int(i) for i in outer_element])

    f.close()
    for outer_element in grid:
        print(', '.join(str(element) for element in outer_element))
    return



def print_solves_sudoku(grid):
    print('\nSolved Sudoku!!: \n')
    f = open('solved_sudoku.csv', mode='w')

    for outer_element in grid:
        print(', '.join(str(e) for e in outer_element))

        f.writelines(', '.join(str(e) for e in outer_element) + '\n')


    f.close()
    return

sudoku_input()

print_solves_sudoku(grid)