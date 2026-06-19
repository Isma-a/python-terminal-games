####################
# Game of Nim
####################

from random import randint

def get_name() -> str:
    """ Prompts for a non-empty name from the keyboard, as many
    times as necessary.

    Precondition: /
    Example(s): /
    """
    name = input('Please enter the name of player A: ')
    while name == '':
        print('\n/!\\ Incorrect player name /!\\ \n')
        name = input('Please enter the name of player A (you must enter at least one character): ')
    return name


def get_different_name(player_a_name: str) -> str:
    """ Prompts for a non-empty name from the keyboard that is different from the one in the parameter, as many
    times as necessary.
    
    Precondition: /
    Example(s): /
    """
    name = input('Please enter the name of player B: ')
    while name == '' or name == player_a_name:
        if name == player_a_name:
            print('\nThe name ' + name + ' already exists.\n')
            name = input('Please enter the name of player B (must be different from player A): ')
        else:
            print('\n/!\\ Incorrect player name /!\\ \n')
            name = input('Please enter the name of player B (please enter at least one character): ')
    return name
    
    
def get_max_possible_to_take(num_matches: int) -> int:
    """ Takes an int num_matches and returns the max amount of matches to take
    Precondition: 
    Example(s): num_matches >= 0
    $$$ get_max_possible_to_take(10)
    3
    $$$ get_max_possible_to_take(2)
    2
    $$$ get_max_possible_to_take(1)
    1
    $$$ get_max_possible_to_take(3)
    3
    """
    if num_matches < 3:
        return num_matches
    return 3

def get_num_matches_taken(max_val) -> int:
    """ Asks the player for the number of matches they want to take and returns this value as an int
    Precondition: /
    Example(s): / 
    """
    prompt_text = "How many matches are you taking? "
    res = input(prompt_text)
    while int(res) not in range(1, max_val + 1):
        print("The entered number is invalid.")
        res = input(prompt_text)
    return res

def get_other_player_index(player_index: int):
    """ Takes the current player's index and returns the other player's index

    Precondition: player_index in (0, 1)
    Example(s):
    $$$ get_other_player_index(0)
    1
    $$$ get_other_player_index(1)
    0
    """
    if player_index == 1:
        return 0
    else:
        return 1

# Uncomment and complete the given signature then do the rest
def play() -> None:
    """ Function that codes the game of Nim
    """
    #### Game state initialization
    num_matches = 16

    name_pA = get_name()

    name_pB = get_different_name(name_pA)
    
    player_list = [name_pA, name_pB]
    
    current_player_index = randint(0, 1)
    
    #### Game loop
    while num_matches != 0:
        
        print(f'Number of matches: {num_matches}')

        print(player_list[current_player_index] + ': your turn!')
        
        max_to_take = get_max_possible_to_take(num_matches)

        matches_taken = get_num_matches_taken(max_to_take)
        
        current_player_index = get_other_player_index(current_player_index)

        num_matches -= int(matches_taken)
    
    current_player_index = get_other_player_index(current_player_index)
    
    final = "No more matches! " + player_list[current_player_index] + " has won!"
            
    print(final)

if __name__ == '__main__':
    play()