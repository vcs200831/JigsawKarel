"""
Karel has picked up a new hobby: doing puzzles! Karel is trying to complete this puzzle made up of beepers.
To reiterate, you should write the sequence of commands so that Karel will:
•Move to and pick up the last puzzle piece (the beeper in row 1, column 3)
•Put the puzzle piece in place (row 3, column 4)
• Return Karel to her initial position
"""
from stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_right()
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_right()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    run_karel_program()