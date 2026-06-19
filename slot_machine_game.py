from random import choice

def get_name() -> str:
    """ prompts for a name and returns it as a str

    Precondition: /
    """
    return input('Enter your name: ')
    
def display_welcome_message(name: str) -> None:
    """ takes a name as a str parameter and prints a welcome message as a str

    Precondition: /
    Example(s):
    """
    print(name + ', Welcome to the Slot Machine game\n')


def get_starting_bet() -> int:
    """ prompts for a starting bet and returns it as an int
    Precondition: /
    """
    bet = input('What is your starting bet? : ')
    while not bet.isdigit():
        print("Please enter an integer only")
        bet = input('What is your starting bet? : ')
    return int(bet)



def spin_reel() -> str:
    """ randomly draws a character from '$%#~&' and returns it

    Precondition: /
    """
    symbols = '$%#~&' 
    return choice(symbols)


def calculate_winnings(bet: int, char1: str, char2: str, char3: str) -> int:
    """ takes three characters and the starting bet and returns the amount won

    Precondition: char1 in '$%#~&'
                  char2 in '$%#~&'
                  char3 in '$%#~&'
    Example(s):
    $$$ calculate_winnings(100, '$', '$', '$')
    25000
    $$$ calculate_winnings(500, '&', '%', '%')
    0
    $$$ calculate_winnings(5000, '$', '~', '&')
    10000
    $$$ calculate_winnings(10, '%', '%', '%')
    1500
    $$$ calculate_winnings(10, '#', '#', '#')
    500
    """
    symbols = [char1, char2, char3]
    dollar_count = symbols.count('$') # calculation of the total number of $
    
    # IMPROVED LOGIC: Any 3 identical symbols trigger a win
    if char1 == char2 == char3:
        if char1 == '$':
            return bet * 250    # Jackpot
        elif char1 == '%':
            return bet * 150    # Second best tier
        else:
            return bet * 50     # Base payout for any other 3-of-a-kind
            
    # If not 3-of-a-kind, $ symbols still give a small payout
    elif dollar_count == 2:
        return bet * 5
    elif dollar_count == 1:
        return bet * 2
        
    return 0


def get_reels_representation(char1: str, char2: str, char3: str) -> str:
    """ takes three characters as parameters and returns a representation of three reels displaying the parameter characters

    Precondition: /
    """
    return f'+------+------+------+\n|{char1:^6}|{char2:^6}|{char3:^6}|\n+------+------+------+'

def display_reels(reels_txt: str) -> None:
    """ Displays the reels
    Precondition: /
    """
    print("\n\n")
    print(reels_txt)


def display_win_or_loss_message(winnings: int) -> None:
    """ takes an integer as a parameter and prints a win or loss phrase depending on the amount won

    Precondition: winnings >= 0
    Example(s):
    """
    if winnings == 0: # in case of loss
        print('\nYou lost!')
    else: # in case of win so winnings > 0
        print(f'\nYou won €{winnings}!')
    
    
def final_balance(starting_bet: int, winnings: int) -> None:
    """ takes a starting bet and winnings and prints a summary string with the final balance

    Precondition: winnings >= 0
    """
    net_balance = winnings - starting_bet
    if net_balance <= 0:
        print(f'Balance:  -€{abs(net_balance)}')
    else:
        print(f'Balance:  +€{net_balance}!')
    
    

if __name__ == "__main__":
    name = get_name() # prompts for the player's name
    display_welcome_message(name) # displays a welcome message with the player's name
    bet_int = get_starting_bet() # prompts the player for a starting bet, stored in bet_int
    
    reel_1 = spin_reel() # random assignment of the 1st character for reel 1
    reel_2 = spin_reel() # random assignment of the 2nd character for reel 2
    reel_3 = spin_reel() # random assignment of the 3rd character for reel 3
    
    display_reels(get_reels_representation(reel_1, reel_2, reel_3)) # displays the three reels with their results
    winnings = calculate_winnings(bet_int, reel_1, reel_2, reel_3) # calculates winnings based on reel characters
    display_win_or_loss_message(winnings) # displays a win or loss message based on the winnings
    final_balance(bet_int, winnings) # displays (winnings - initial bet)
    
    