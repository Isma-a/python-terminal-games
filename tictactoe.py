####################
# Tic Tac Toe Game
####################

from random import randint
from random import random
from time import sleep

def init_grid() -> list[list[str]]:
    """ creates an empty 3x3 grid (list of lists)
    Precondition: /
    Example(s):
    $$$ init_grid()
    [['', '', ''], ['', '', ''], ['', '', '']]
    """
    return [['',  '', ''], ['', '', ''], ['', '', '']]

def ask_username(username:str, player:str) -> str:
    """ takes two strings username and player as parameters to ask for the username of the player <player>
    , this one must be different from the one passed as a parameter. Moreover, the username written by the player must not be empty.

    Precondition: /
    Example(s): /
    """
    while True:
        name = input(f'Please write the name of player {player}: ').strip()
        while name == username or name == '':
            print('\nError, incorrect username, please try again\n')
            name = input(f'Please write the name of player {player}: ').strip()
        y_or_n = input(f'Player {player}, do you confirm the name {name}? Y/N: ')
        while y_or_n.lower() not in ['y', 'n']:
            print('\nError, incorrect response, please try again\n')
            y_or_n = input(f'Player {player}, do you confirm the name {name}? Y/N: ')
        if y_or_n == 'Y' or y_or_n == 'y':
            print(f'\nWelcome {name}\n')
            return name
        
def random_or_choice() -> bool:
    """ asks the user if they want to choose the player who starts or if they want it to be random.
    Returns True if the player wants to choose and False if the player wants it random

    Precondition: /
    Example(s): /
    """
    choice = input('\nDo you want to:\n\n\t- Choose which player starts (type "1")\n\t- Random (type "2")\n\nChoice: ')
    while choice not in ('1', '2'):
        print('Error, please only answer with "1" or "2"')
        choice = input('\nDo you want to:\n\n\t- Choose which player starts (type "1")\n\t- Random (type "2")\n\nChoice: ')
    return choice == '1'

def ask_who_starts(names:list[str]) -> bool:
    """ takes a list of strings as parameter and asks the player
    if they want player A (names[0]) or player B (names[1]) to start
    Precondition: len(names) >= 2
    Example(s): /
    """
    choice = input(f'\n\nWhich player starts playing?\n\n\t- Player A: {names[0]} (type "A")\n\t- Player B: {names[1]} (type "B")\n\nChoice: ')
    while choice.upper() not in ['A', 'B']:
        print('Error, please only answer with "A" or "B"')
        choice = input(f'\n\nWhich player starts playing?\n\n\t- Player A: {names[0]} (type "A")\n\t- Player B: {names[1]} (type "B")\n\nChoice: ')
    return choice.upper() == 'A'
          
def who_starts_random(lst:list[str]) -> list[str]:
    """ takes a list of two elements and randomly returns the reversed list or not
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
    print(f'\n{names[0]} will therefore start the game with X\'s, as for {names[1]} you will have O\'s')

def who_starts_general(names:list[str]) -> list[str]:
    """ takes a list of strings names as parameter and returns
    the reversed list or not depending on the player's choice
    Precondition: len(names) == 2
    Example(s): /
    """
    if random_or_choice(): # The player chose to choose who starts
        if ask_who_starts(names): # The player chose that player A starts
            display_who_starts_before_loading(names)
            return names
        else: # The player chose that player B starts
            names = reverse_list2(names) # We reverse so that player B starts
            display_who_starts_before_loading(names)
            return names
    else: # The player chose random
        names = who_starts_random(names) # randomly determines who starts
        display_who_starts_before_loading(names)
        return names
    
    
def reverse_list2(lst:list) -> list:
    """ takes a list of length 2 as parameter and returns it reversed

    Precondition: len(lst) == 2
    Example(s):
    $$$ reverse_list2(['1', '2'])
    ['2', '1']
    """
    lst[0], lst[1] = lst[1], lst[0]
    return lst

def game_loading() -> None:
    """ displays a loading from 0 to 100%
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
    Precondition: len(grid) == len(grid[0]) == len(grid[1]) == len(grid[2]) == 3
    Example(s): /
    """
    print(f"\n   {'1':^7} {'2':^7} {'3':^7}")
    for i in range(3):
        print(f"{i+1}  {grid[i][0]:^7}|{grid[i][1]:^7}|{grid[i][2]:^7}")
        if i < 2:
            print("   -------+-------+-------")
        else:
            print('\n')

def display_current_player(lplayer:list[str]) -> None:
    """ takes a list of strings lplayer as parameter and displays the current player
    Precondition: len(lplayer) > 0
    Example(s): /
    """
    n = randint(0, 2)
    if n == 0:
        print(f'It\'s {lplayer[0]}\'s turn to play')
    elif n == 1:
        print(f'{lplayer[0]}, it\'s your turn')
    else:
        print(f'It\'s {lplayer[0]}\'s turn')
        
def ask_row_index() -> int:
    """ asks the player for the row index where they want to put their symbol on the grid
    Precondition: /
    Example(s): /
    """
    row = input("Choose the row for your symbol: ")
    while row not in ['1', '2', '3']:
        print('Error, the row number must be between 1 and 3')
        row = input("Choose the row for your symbol: ")
    return int(row) - 1
 
def ask_col_index() -> int:
    """ asks the player for the column index where they want to put their symbol on the grid

    Precondition: /
    Example(s): /
    """
    col = input("Choose the column for your symbol: ")
    while col not in ['1', '2', '3']:
        print('Error, the column number must be between 1 and 3')
        col = input("Choose the column for your symbol: ")
    return int(col) - 1

def check_grid_win(grid:list[list[str]]) -> bool:
    """ takes a tictactoe grid and checks if there is a victory (returns True),
    a draw (returns True) or that the game is not over (returns False)
    Precondition: len(grid) == len(grid[0]) == len(grid[1]) == len(grid[2]) == 3
    Example(s):
    $$$ check_grid_win([['', '', ''], ['', '', ''], ['', '', '']])
    False
    $$$ check_grid_win([['X', 'X', 'X'], ['', 'O', ''], ['O', '', '']])
    True
    $$$ check_grid_win([['O', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    True
    $$$ check_grid_win([['', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    False
    $$$ check_grid_win([['O', 'X', 'X'], ['O', 'O', ''], ['O', '', '']])
    True
    $$$ check_grid_win([['O', 'X', 'X'], ['O', 'O', 'X'], ['', 'O', 'X']])
    True
    $$$ check_grid_win([['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']])
    True
    """
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != '':
            return True
        elif grid[0][i] == grid[1][i] == grid[2][i] != '':
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] != '':
        return True
    elif grid[0][2] == grid[1][1] == grid[2][0] != '':
        return True
    for lst in grid:
        if '' in lst:
            return False
    return True

def is_cell_empty(grid:list[list[str]], i_row:int, i_col:int) -> bool:
    """ takes a list of lists of strings grid and two integers i_row and i_col as parameters
    and returns True if the cell at index i_row and i_col is an empty string
    Precondition: 0 <= i_row < 3
                   0 <= i_col < 3
                   len(grid) == len(grid[0]) == len(grid[1]) == len(grid[2]) == 3
    Example(s):
    $$$ is_cell_empty([['', '', ''], ['', '', ''], ['', '', '']], 2, 2)
    True
    $$$ is_cell_empty([['', '', ''], ['', '', ''], ['', '', 'X']], 2, 2)
    False
    $$$ is_cell_empty([['', '', ''], ['', '', ''], ['', '', 'X']], 0, 1)
    True
    $$$ is_cell_empty([['', 'O', ''], ['', '', ''], ['', '', 'X']], 0, 1)
    False
    """
    return grid[i_row][i_col] == ''
    
def grid_index_loop(grid:list[list[str]]) -> list[int]:
    """ takes a list of lists of strings grid as parameter and returns the indices entered by the user
    if they correspond to an empty cell and are within the grid
    Precondition: len(grid) == len(grid[0]) == len(grid[1]) == len(grid[2]) == 3
    Example(s): /
    """
    i_row = ask_row_index()
    i_col = ask_col_index()
    while not is_cell_empty(grid, i_row, i_col):
        print('\nError, you cannot change an already existing sign. Please try again\n')
        i_row = ask_row_index()
        i_col = ask_col_index()
    return [i_row, i_col]
    
def who_won(grid:list[list[str]]) -> int:
    """ takes a tictactoe grid and checks if there is a victory for the player with X's (returns 1), the player with O's (returns 0)
    or a draw (returns -1)
    Precondition: len(grid) == len(grid[0]) == len(grid[1]) == len(grid[2]) == 3
    Example(s):
    $$$ who_won([['O', 'X', 'X'], ['O', 'X', ''], ['O', '', 'X']])
    0
    $$$ who_won([['X', 'X', 'X'], ['', 'O', ''], ['O', '', '']])
    1
    $$$ who_won([['O', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    0
    $$$ who_won([['X', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    1
    $$$ who_won([['O', 'X', 'X'], ['O', 'O', ''], ['O', '', '']])
    0
    $$$ who_won([['O', 'X', 'X'], ['O', 'O', 'X'], ['', 'O', 'X']])
    1
    $$$ who_won([['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']])
    -1
    """
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != '':
            if grid[i][0] == 'X':
                return 1
            return 0
        elif grid[0][i] == grid[1][i] == grid[2][i] != '':
            if grid[0][i] == 'X':
                return 1
            return 0
    if grid[1][1] == grid[2][2] == grid[0][0] != '':
        if grid[0][0] == 'X':
            return 1
        return 0
    elif grid[0][2] == grid[1][1] == grid[2][0] != '':
        if grid[2][0] == 'X':
            return 1
        return 0
    return -1
             
def display_game_result(result:int, name:str) -> None:
    """ takes a result (between -1 and 1 inclusive) and a string name and displays the result with the winner's name (or draw)
    Precondition: result in [-1, 0, 1]
    Example(s): /
    """
    if result == 1:
        print(f'{name} won, three X signs are aligned!')
    elif result == 0:
        print(f'{name} won, three 0 signs are aligned!')
    else:
        print("Draw, there are no more possible moves")
    
def play() -> None:
    """Main function to play tic-tac-toe.
    """
    name_pA = ask_username('', 'A') # ask for player A's name
    names = [name_pA, ask_username(name_pA, 'B')] # ask for player B's name and assign both usernames to names list
    names = who_starts_general(names) # The player chose to choose who starts or let it be random
    grid = init_grid() # Creation of the empty grid
    symbols = ['X', 'O'] # Creation of the symbols
    game_loading() # Fake loading for style

    ### game loop
    while not check_grid_win(grid):
        
        display_grid(grid)
        display_current_player(names)
        indices = grid_index_loop(grid) # asks the player for the indices and checks if the cell is valid (empty cell and in the grid)
        grid[indices[0]][indices[1]] = symbols[0] # The cell chosen by the player becomes the player's symbol
        names, symbols = reverse_list2(names), reverse_list2(symbols) # Change current player
    display_grid(grid)
    result = who_won(grid)
    display_game_result(result, names[1])
    
if __name__ == '__main__':
    play()
