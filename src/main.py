"""
Python Version: 3.7 (2.7 support as well)
Author: James Cristini
Description: An interactive command line 'game' that allows users to create robots and assign them tasks
Created: 7/23/2019
"""

from __future__ import print_function
from builtins import input

from collections import OrderedDict

from robot_factory import RobotFactory
from utils import clear_console, press_enter_to_continue, get_user_choice


# ACTION_CHOICES are the primary actions that will be presented to a user at the start
# these will be mapped to RobotFactory methods after it is instantiated below
# An OrderedDict is used so that choices can always be displayed in the same order
ACTION_CHOICES = OrderedDict([
            ('1', 'Create a new robot'),
            ('2', 'Interact with a robot'),
            ('3', 'Destroy a robot'),
            ('4', 'Destroy all robots'),
            ('5', 'View robot task leaderboard'),
            ('0', 'Exit'),
    ])


def run_session():
    clear_console() # <- clears the console, makes following prompts and information easier

    # Factory used as a context manager to ensure load and save methods are run
    with RobotFactory() as rf:

        # Choices from ACTION_CHOICES above mapped to actual methods
        actions_map = {
                'Create a new robot':           rf.create_robot,
                'Interact with a robot':        rf.interact_with_robot,
                'Destroy a robot':              rf.destroy_a_robot,
                'Destroy all robots':            rf.destroy_all_robots,
                'View robot task leaderboard':  rf.view_robot_leaderboard,
                # Exit' is not mapped so that it passes choice validation and still exits
        }

        # Primary user interaction loop runs until a user chooses to exit
        while True:
            # Below function gets user input based on dict of choices
            _, choice = get_user_choice(ACTION_CHOICES, 'What would you like to do?')

            try:
                actions_map[choice]() # <- Call the method on the fly
            except KeyError:
                clear_console()
                pass # Only hits KeyError if '0' : Exit is chosen

            if choice == 'Exit':
                # Have user confirm exit with case insensitve typed input
                if input('Type EXIT to quit if you are sure you want to leave.\n').upper() == 'EXIT':
                    clear_console()
                    break

        print('\n*** You are now leaving the robot factory! ***\n')
    print('\n*** Your robots have been saved, goodbye! ***\n')


if __name__ == "__main__":
    run_session()

    ### Potential enchancements:
    # could leverage object.__class__.__name__ and/or object.__doc__ for choice mappings? this would negate the need for 2 dictionaries to map abstract (number) choices to objects/methods
    # add a manual save option and maybe an chance to save on KeyboardInterrupt?
    # allow users to queue up tasks for a robot to complete (instead of one at a time)
    # leverage async so mutliple robots could run multiple tasks at once
    # let a user upgrade bots so they can perform tasks more quickly! (could earn upgrade points through completing more tasks)

