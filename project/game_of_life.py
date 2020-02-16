"""Program designed to run Conway's Game of Life.

..module::game_of_life
    :platform: Windows
    :synopsis: This script is designed to take user inputs from the command to run Conway's Game of Way.

    The inputs from the user indicate the starting cells and the number of 'ticks' or runs the game will run for.


..moduleauthor:: Brian Eisenbarth brian.eisenbarth@wsu.edu
..modulereviewer:: Matthew Brousil Grade on intial review 58/100
"""


def main():
    """Runs the script game_of_life.

    Sets up the module argv's to take command line puts from the user; creates an intial blank grid(2D array);
    and sets up the while loop for how long the game will run.


    :return: prints the intial grid the user specifies.
    :rtype: a 2D list
    """
    from sys import argv
    #sets the amount of row to 30
    rows = 30
    #sets the amount of columns to 80
    cols = 80
    #sets the user's input for starting cells as coords
    coords=argv[2:]
    #Creates the intial grid as 2D list of zeros
    grid = [[0] * (cols + 1) for i in range(rows + 1)]

    #stores the inital game grid.

    #main funcntion will call init_grid function with coords and grid as passing arguments
    init_grid(coords, grid)
    #calls print_grid with rows, cols, and grid as passing arguments
    print_grid(rows, cols, grid)

    #maxium number of ticks is equal to the second command which is converted to an integer
    max_ticks = int(argv[1])
    #sets intial loop_count
    loop_count = 0

    #While loop runs for the number of ticks inputed by a user.
    while loop_count < max_ticks:

        if loop_count == 0:
            #new_grid is equal to make_move with intial grid, cols, and rows as passing arguments
            new_grid = make_move(grid, cols, rows)

        else:
            #for every other tick the new grid is equal the subsequent new_grid
            new_grid = make_move(new_grid, cols, rows)
        #calls the print_grid function with rows, cols, and new_grid as passing arguments
        print_grid(rows, cols, new_grid)
        #sets loop_count iteratoins
        loop_count += 1

print(main.__doc__)

def init_grid(coords, grid):
    """The intial grid for the game given user input.

    :param coords: The user indicated starting cells
    :type amount: int
    :param grd: Passed in blank grid
    :type: list of lists

    :returns: Displays the cells the user turned on in a grid.
    :rtype: integer
    """

    #corrects for the index starting at 0, so user can input 1 for 0
    for i in range(len(coords)):
        #splits the row and column coords into pair
        rows, cols = coords[i].split(":")
        #converts rows to integer
        rows = int(rows)
        #converts cols to integer
        cols = int(cols)
        #sets grid equal to 1
        grid[rows - 1][cols - 1] = 1

print(init_grid.__doc__)
def make_move(grid, cols, rows):
    """Implements the rules of the Game of life for continued ticks.

        It achieves this by looping through the row and column lists.


    :param grid: passes in the grid defined above.
    :type list: list of lists
    :param cols: passes in number of columns
    :type list: list of lists
    :param rows: passes in number of rows
    :type list: list of cols


    :return: Returns a new grid given the rules and prints it.
    :rtype: a list of lists of new cells
    """
    #sets up the new grid
    new_grid=[[0]*(cols+1) for i in range(rows+1)]
    #for the element in the row list
    for i in range(rows):
        #for the j element in the column list
        for j in range(cols):
            #sets upper left neighbor
            upper_left = grid[i-1][j-1]
            #sets upper neighbor
            upper = grid[i-1][j]
            #sets upper right neighbor
            upper_right = grid[i-1][j+1]
            #sets mid left neighbor
            mid_left = grid[i][j-1]
            #sets mid right neighbor
            mid_right = grid[i][j+1]
            #sets lower left neighbor
            lower_left = grid[i+1][j-1]
            #sets lower neighbor
            lower = grid[i+1][j]
            #sets lower right neighbor
            lower_right = grid[i+1][j+1]

            #sets on the on number of neighbors to the sum of the defined variables

            on_nbs = upper_left+upper+upper_right+mid_left+mid_right+lower_left+lower+lower_right
            #loops through the lists and sets cell off if on_nbs is less than 2
            if grid[i][j] == 1 and on_nbs <2:
                new_grid[i][j] = 0
            #loops through the lists and sets cell on if on_nbs is 2 or 3
            elif grid[i][j] == 1 and on_nbs == 2:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and on_nbs == 2 or on_nbs == 3:
                new_grid[i][j] = 1
            #loops through the lists and sets cell off if on_nbs is greater than 3
            elif grid[i][j] == 1 and on_nbs > 3:
                new_grid[i][j] = 0
            #loops through the lists and sets the cell on if on_nbs is 3
            elif grid[i][j] == 0 and on_nbs == 3:
                new_grid[i][j] = 1


    #returns the newgrid given the rules
    return new_grid
print(make_move.__doc__)
def print_grid(rows, cols, grid):
    """The subsequent grid to be displayed as the game runs its ticks.

    :param rows: passes in number of rows.
    :type rows: list of rows
    :param cols: passes in number of columns.
    :type cols: list of cols
    :param grid: passes in the grid
    :type grid: list of lists


    :returns: prints the new on and off cells as it loops through the rows and colums of the grid.
    :rtype: 2d list
    """
    # for loop through row index
    for i in range(rows):
        # for loop thhrough the column index
        for j in range(cols):
            #conditional statement for any off cells
            if grid[i][j] == 0:
                #if cell is off print it as "-"
                print("-", end = "")
            #conditional statement for any on cells
            else:
                #else if the cell is on print it as "X"


                 print("X", end = "")
        #prints the elements for the for- loop for j in range(cols)
        print()
    #prints the elements for the for- loop for in range(rows)
    print()
#calls the main function
main()

print(print_grid.__doc__)
