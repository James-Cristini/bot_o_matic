from __future__ import print_function
from builtins import input

import os
import pickle


def clear_console():
    """ Simply runs the clear/cls command on the console to make it easier to read what is going on. """

    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter_to_continue():
    """ Simply 'pauses' the console and waits for user to hit enter to continue. """

    input('\nPress enter to continue\n')


def get_user_choice(choices_dict, message="Please choose from the list of optiions."):
    """ Takes in an 'enumerated' dict object (preferably an OrdereDict),
    lists the choices then gets (and validates) the user's input.
    returns the chosen key and value from the dict. """

    # Breaks only when a valid choice is made via returning it
    while True:
        print(message)
        # Print out the key/value pairs for a user to choose from
        for k, v in choices_dict.items(): print('{0} : {1}'.format(k, v))

        # Accept user input to be evaluated below
        choice = input('Your choice: ')

        try:
            # Check that the input matches a key in the choices dict
            choices_dict[choice]
        except KeyError:
            # If it is not a valid selection, let the user know and let the loop continue
            clear_console()
            print('*** Not a valid option! ***\n')
        else:
            # Return a valid choice
            return choice, choices_dict[choice]


def load_from_pickle(fn='robot_save.pkl'):
    """ Loads objects from pickle file and stores them in a list to send back. """

    # List to store all saved robot objects
    objs = []
    with open(fn, 'rb') as pkl_file:
        # Iterate through and load all objects until EOF (signifies no more objects to load)
        while pkl_file:
            try:
                r = pickle.load(pkl_file)
                objs.append(r)
            except EOFError:
                break
    return objs


def save_to_pickle(objs, fn='robot_save.pkl'):
    """ Saves a list of objects to a pickle file. """

    # Dump each object in the list to the .pkl
    with open(fn, 'wb') as pkl_file:
        for obj in objs:
            pickle.dump(obj, pkl_file, protocol=2)

    return True # Not necessary but could leverage the return value to confirm success