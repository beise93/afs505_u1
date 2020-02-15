"""Program designed to run Conway's Game of Life.

..module::game_of_life
    :synopsis: This script is designed to take user inputs from the command to run Conway's Game of Way.

    The inputs from the user indicate the starting cells and the number of 'ticks' or runs the game will run for.


..moduleauthor:: Brian Eisenbarth
..modulereviewer:: Matthew Brousil
"""


def main():
    """Runs the script game_of_life.

    Attributes: Sets up the module argv's to take command line puts from the user.
                Argv0 is the file
                Argv1 is the number of ticks
                Argv2 is the set of cells the user wants to start with

    Return: prints the intial grid the user specifies.
    """
    from sys import argv
    rows = 30
    cols = 80
    coords=argv[2:]
    grid = [[0] * (cols + 1) for i in range(rows + 1)]
    #first input on command line is the file name

    #number of ticks is equal to the second command which is converted to an integer
    ticks = int(argv[1])
    #number of staring cells is the third argv


    #sets the rows and columns for game grid.


    #stores the inital game grid.

    #sets the maximum game length to tick input converted to an integer.
    init_grid(coords, grid)

    print_grid(rows, cols, grid)

    max_ticks = int(argv[1])

    loop_count = 0

    #While loop runs for the number of ticks inputed by a user.
    while loop_count < max_ticks:
        if loop_count == 0:
            new_grid = make_move(grid, cols, rows)

        else:
            new_grid = make_move(new_grid, cols, rows)
        print_grid(rows, cols, new_grid)
        loop_count += 1


#This function takes user input for the cells and returns the intial grid.
def init_grid(coords, grid):
    """
    The intial grid for the game given user input.

    Parameters:
        coords: The starting coordinates given for the cells to be on for the intial grid.
        grid: Passed in blank grid.
    Returns: Displays the cells the user turned on in a grid.
    """

    #corrects for the index starting at 0, so user can input 1 for 0
    for i in range(len(coords)):
        #splits the row and column coords into pair
        rows, cols = coords[i].split(":")
        rows = int(rows)
        cols = int(cols)
        grid[rows-1][cols-1] = 1
        #copies the grid

def make_move(grid, cols, rows):
    """Implements the rules of the Game of life for continued ticks.

        It achieves this by looping through the row and column lists

    Parameters:
        grid: passes in the grid defined above.
        ncol: number of columns.
        nrow: number of rows.
    Returns: Returns a new grid given the rules and prints it.
    """
    #sets up the new grid
    new_grid=[[0]*(cols+1) for i in range(rows+1)]
    #for the element in the row list
    for i in range(rows):
        rows = int(rows)#for the j element in the column list
        for j in range(cols):
            cols = int(cols)#sets upper left neighbor
            upper_left = grid[i-1][j-1]
            #sets upper neighbor
            upper = grid[i-1][j]
            #sets upper right neighbor
            upper_right = grid[i-1][j+1]
            #sets mid left neighbor
            mid_left = grid[i][j-1]
            #sets mid neighbor
            mid = grid[i][j]
            #sets mid right neighbor
            mid_right = grid[i][j+1]
            #sets lower left neighbor
            lower_left = grid[i+1][j-1]
            #sets lower neighbor
            lower = grid[i+1][j]
            #sets lower right neighbor
            lower_right = grid[i][j+1]
            #sets on the on number of neighbors to the sum of the defined variables

            on_nbs = upper_left+upper+upper_right+mid_left+mid+mid_right+lower_left+lower+lower_right
            #loops through the lists and sets cell off if on_nbs is less than 2
            if grid[i][j] == 1 and on_nbs < 2:
                new_grid[i][j] = 0
            #loops through the lists and sets cell on if on_nbs is 2 or 3
            if grid[i][j] == 1 and on_nbs == 2 or on_nbs == 3:
                new_grid[i][j] = 1
            #loops through the lists and sets cell off if on_nbs is greater than 3
            if grid[i][j] == 1 and on_nbs > 3:
                new_grid[i][j] = 0
            #loops through the lists and sets the cell on if on_nbs is 3
            if grid[i][j] == 0 and on_nbs == 3:
                new_grid[i][j] = 1


    #returns the newgrid given the rules
    return new_grid[i][j]
def print_grid(grid, rows, cols):
    """
    The subsequent grid to be displayed as the game runs its ticks.

    Parameters:
        grid: the passed in grid
        rows: number of rows in the grid
        cols: number of columns in the grid
    Returns: Prints the new on and off cells
    """

    for i in range(rows):

        for j in range(cols):

            if grid[i][j] == 0:

                print("-", end = "")

            else:
                 print("X", end = "")
        print()

    print()

main()
