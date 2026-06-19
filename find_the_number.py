from random import randint

def input_integer_in_range(the_min: int, the_max: int) -> int:
    """prompts for an integer between `the_min` and `the_max`, as long as the input
    is incorrect.

    Precondition: the_min <= the_max
    """
    correct_input = False
    while not correct_input:
        integer = int(input(f"enter an integer between {the_min} and {the_max} inclusive: "))
        correct_input = (the_min <= integer and integer <= the_max)
    return integer


def compare(num1: int, num2: int) -> int:
    """Returns -1 if num1 < num2 ; 1 if num1 > num2 and 0 if num1 == num2.

    Precondition: none
    Example(s):
    $$$ compare(-8, 4)
    -1
    $$$ compare(8, 4)
    1
    $$$ compare(8, 8)
    0
    """
    res = 1
    if num1 < num2:
        res = -1
    elif num1 == num2:
        res = 0
    return res

def guess_a_number(max_attempts: int, max_val: int) -> None:
    """Plays the game with `max_attempts` attempts and a
    value drawn between 1 and `max_val` inclusive.

    Precondition: max_attempts > 0, max_val >= 1
    """
    secret = randint(1, max_val)
    attempts = 0 # number of attempts already made by the player
    found = False # the player has found the num
    
    while not found and attempts < max_attempts:
        guess = input_integer_in_range(1, max_val)
        attempts = attempts + 1
        res = compare(guess, secret)
        
        if res == -1:
            print('Greater!')
        elif res == 1:
            print('Smaller!')
        else:
            print(f'Won in {attempts} guesses!')
            found = True
            
    if not found:
        print('Lost!')
        

if __name__ == '__main__':
    guess_a_number(3, 10)