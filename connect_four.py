####################
# Connect 4 Game
####################

from random import randint
from random import random
from time import sleep

def init_grid() -> list[list[str]]:
    """ create an empty 6x7 grid (list of lists)
    Precondition: /
    Example(s):
    $$$ init_grid()
    [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    """
    return [[' '] * 7, [' '] * 7, [' '] * 7, [' '] * 7, [' '] * 7, [' '] * 7]

def ask_username(username:str, player:str) -> str:
    """ takes two strings username and player as parameters to ask the username of the player <player>
    , this one must be different from the one passed as a parameter. Furthermore, the username written by the player must not be empty.

    Precondition: /
    Example(s): /
    """
    while True:
        name = input(f'Please enter the name for player {player}: ').strip()
        while name == username or name == '':
            print('\nError: invalid username, please try again\n')
            name = input(f'Please enter the name for player {player}: ').strip()
        y_or_n = input(f'Player {player}, do you confirm the name {name}? Y/N: ')
        while y_or_n.lower() not in ['y', 'n']:
            print('\nError: invalid response, please try again\n')
            y_or_n = input(f'Player {player}, do you confirm the name {name}? Y/N: ')
        if y_or_n == 'Y' or y_or_n == 'y':
            print(f'\nWelcome {name}!\n')
            return name
        
def random_or_choice() -> bool:
    """ asks the user if they want to choose the starting player or if they want it to be random.
    Returns True if the player wants to choose and False if the player wants random.

    Precondition: /
    Example(s): /
    """
    choice = input('\nWould you like to:\n\n\t- Choose which player starts (type "1")\n\t- Random (type "2")\n\nChoice: ')
    while choice not in ('1', '2'):
        print('Error, please only answer with "1" or "2"')
        choice = input('\nWould you like to:\n\n\t- Choose which player starts (type "1")\n\t- Random (type "2")\n\nChoice: ')
    return choice == '1'

def ask_who_starts(names:list[str]) -> bool:
    """ takes a list of strings as parameters and asks the player
    if they want Player A (names[0]) or Player B (names[1]) to start
    Precondition: len(names) >= 2
    Example(s): /
    """
    choice = input(f'\n\nWhich player starts playing?\n\n\t- Player A: {names[0]} (type "A")\n\t- Player B: {names[1]} (type "B")\n\nChoice: ')
    while choice.upper() not in ['A', 'B']:
        print('Error, please only answer with "A" or "B"')
        choice = input(f'\n\nWhich player starts playing?\n\n\t- Player A: {names[0]} (type "A")\n\t- Player B: {names[1]} (type "B")\n\nChoice: ')
    return choice.upper() == 'A'
          
def who_starts_random(lst:list[str]) -> list[str]:
    """ takes a list of two elements and randomly returns the list inverted or not
    Precondition: len(lst) >= 2
    Example(s):
    $$$ who_starts_random(['a', 'b'])
    ['a', 'b'] or ['b', 'a']
    """
    i = randint(0, 1)
    lst[i], lst[0] = lst[0], lst[i]
    return lst

def display_who_starts_before_loading(names:list[str]) -> None:
    """ takes a list of strings as parameter and prints the name of the player who will start (the first in the list)
    and the second one as well, specifying their respective symbols
    Precondition: len(names) == 2
    Example(s): /
    """
    print(f'\n{names[0]} will start the game with X, and {names[1]} will have O.')

def who_starts_general(names:list[str]) -> list[str]:
    """ takes a list of strings names as parameter and returns
    the list inverted or not based on the player's choice
    Precondition: len(names) == 2
    Example(s): /
    """
    if random_or_choice(): # The player chose to choose who starts
        if ask_who_starts(names): # The player chose that Player A starts
            display_who_starts_before_loading(names)
            return names
        else: # The player chose that Player B starts
            names = invert_list2(names) # We invert so that Player B starts
            display_who_starts_before_loading(names)
            return names
    else: # The player chose random
        names = who_starts_random(names) # Randomly determines who starts
        display_who_starts_before_loading(names)
        return names
    
    
def invert_list2(lst:list) -> list:
    """ takes a list of length 2 as parameter and returns it inverted

    Precondition: len(lst) == 2
    Example(s):
    $$$ invert_list2(['1', '2'])
    ['2', '1']
    """
    lst[0], lst[1] = lst[1], lst[0]
    return lst

def game_loading() -> None:
    """ displays a loading screen from 0 to 100%
    Precondition: /
    Example(s): /
    """
    print('\n\n\n\nLoading game, please wait\n')
    p = 0
    while p < 100:
        sleep(random())
        print(f'{p}%')
        p += randint(2, 15)
    print('100%')
    print('\nThe game begins!\n')
    
def display_grid(grid:list[list[str]]) -> None:
    """ displays the grid passed as parameter
    Precondition: 6x7 grid
    Example(s): /
    """
    print(f"\n {'1':^8}{'2':^8}{'3':^8}{'4':^8}{'5':^8}{'6':^8}{'7':^8}\n")
    for i in range(7):
        print("+-------+-------+-------+-------+-------+-------+-------+")
        if i < 6:
            print(f"|{grid[i][0]:^7}|{grid[i][1]:^7}|{grid[i][2]:^7}|{grid[i][3]:^7}|{grid[i][4]:^7}|{grid[i][5]:^7}|{grid[i][6]:^7}|")
        else:
            print('\n')

def display_current_player(lplayer:list[str]) -> None:
    """ takes a list of strings lplayer as parameter and displays the current player
    Precondition: len(lplayer) > 0
    Example(s): /
    """
    n = randint(0, 2)
    if n == 0:
        print(f"It is {lplayer[0]}'s turn to play")
    elif n == 1:
        print(f"{lplayer[0]}, it is your turn")
    else:
        print(f"{lplayer[0]}'s turn")
        
def ask_index() -> int:
    """ asks the player for the index of where they want to place their token in the grid
    Precondition: /
    Example(s): /
    """
    column = input("Choose the column to place your token: ") # Asking for the column
    while column not in ['1', '2', '3', '4', '5', '6', '7']:
        print('Error, the column number must be between 1 and 7')
        column = input("Choose the column to place your token: ")
    return int(column) - 1


def check_grid_win(grid:list[list[str]]) -> bool:
    """ takes a Connect 4 grid and checks if there is a win (returns True),
    a draw (returns True), or if the game is not finished (returns False)
    Precondition: 6x7 grid
    Example(s):
    $$$ check_grid_win([[" " for _ in range(7)] for _ in range(6)])
    False
    $$$ horiz = [[" " for _ in range(7)] for _ in range(6)]
    $$$ horiz[5][0], horiz[5][1], horiz[5][2], horiz[5][3] = "X", "X", "X", "X"
    $$$ check_grid_win(horiz)
    True
    $$$ verti = [[" " for _ in range(7)] for _ in range(6)]
    $$$ verti[5][2], verti[4][2], verti[3][2], verti[2][2] = "O", "O", "O", "O"
    $$$ check_grid_win(verti)
    True
    $$$ diag_m = [[" " for _ in range(7)] for _ in range(6)]
    $$$ diag_m[5][0], diag_m[4][1], diag_m[3][2], diag_m[2][3] = "X", "X", "X", "X"
    $$$ check_grid_win(diag_m)
    True
    $$$ diag_d = [[" " for _ in range(7)] for _ in range(6)]
    $$$ diag_d[2][0], diag_d[3][1], diag_d[4][2], diag_d[5][3] = "O", "O", "O", "O"
    $$$ check_grid_win(diag_d)
    True
    $$$ draw = [["X" if (i+j) % 2 == 0 else "O" for j in range(7)] for i in range(6)]
    $$$ check_grid_win(draw)
    True
    """
    for i in range(6):
        for j in range(4):
            if grid[i][j] != " " and grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3]:
                return True
            
    for i in range(3):
        for j in range(7):
            if grid[i][j] != " " and grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j]:
                return True
            
    for i in range(3):
        for j in range(4):
            if grid[i][j] != " " and grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3]:
                return True
            
    for i in range(3, 6):
        for j in range(4):
            if grid[i][j] != " " and grid[i][j] == grid[i-1][j+1] == grid[i-2][j+2] == grid[i-3][j+3]:
                return True
            
    for row in grid:
        if " " in row:
            return False 

    return True

def is_column_empty(grid:list[list[str]], i:int) -> bool:
    """ takes as parameter a list of lists of strings grid and an integer i
    and returns True if the cell at index 0 and column i is an empty string
    Precondition: /
    Example(s): /
    """
    return grid[0][i] == ' '
    
def grid_index_loop(grid:list[list[str]]) -> int:
    """ takes as parameter a list of lists of strings grid and returns the index entered by the user
    if it corresponds to an empty cell within the grid
    Precondition: /
    Example(s): /
    """
    i = ask_index()
    while not is_column_empty(grid, i):
        print('\nError, the column is already full. Please try again\n')
        i = ask_index()
    return i

def add_token_grid(grid:list[list[str]], column:int, symbol:str) -> list[list[str]]:
    for i in range(5, -1, -1):
        if grid[i][column] == " ":  # We assume that the space " " = empty cell
            grid[i][column] = symbol
            return grid
    return grid
             
def display_game_result(result:bool, name:str, symbol:str) -> None:
    """ takes a boolean result and a string name and displays the result with the name of the winner (or draw)
    Precondition: result in [False, True]
    Example(s): /
    """
    if result:
        print(f'{name} won, four {symbol} signs are aligned!')
    else:
        print("Draw, there are no more possible moves")
    
def play() -> None:
    """Main function to play Connect 4.
    """
    name_pA = ask_username('', 'A') # ask player A name
    names = [name_pA, ask_username(name_pA, 'B')] # ask player B name and assign both usernames to names list
    names = who_starts_general(names) # The player chose to choose who starts or let random decide
    grid = init_grid() # Creation of the empty grid
    symbols = ['X', 'O']
    game_loading() # Fake loading for style

    ### game loop
    while not check_grid_win(grid):
        
        display_grid(grid)
        display_current_player(names)
        index = grid_index_loop(grid) # asks the player for indices and checks if the cell is valid (empty cell and in the grid)
        
        add_token_grid(grid, index, symbols[0]) # We drop the player's token
        
        names, symbols = invert_list2(names), invert_list2(symbols) # Change current player
    
    display_grid(grid)
    result = not all(" " not in row for row in grid)
    display_game_result(result, names[1], symbols[1])
    
if __name__ == '__main__':
    # play() 