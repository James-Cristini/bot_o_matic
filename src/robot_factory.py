from __future__ import print_function
from builtins import input

from collections import OrderedDict
from robots import ROBOT_TYPES, ROBOT_TYPE_CHOICES
from utils import (
    save_to_pickle,
    load_from_pickle,
    get_user_choice,
    clear_console,
    press_enter_to_continue
)


class RobotFactory(object):
    """ Functions as a factory, container, and context manager within which the user can create, destroy, and interact with robots. """

    robots = {} # <- Primary container for all created robots

    @property
    def robot_name_choices(self):
        """ Generates a quick enumerated 'map' of the existing robots, easier for user to make choices with number selection. """

        # Enumeration starts at 1 and the 0: Leave option is tacked on at the end
        robot_choices = OrderedDict([(str(n+1), bot) for n, bot in enumerate(self.robots.keys())] + [('0', 'Leave')])
        return robot_choices

    def __enter__(self):
        """ Load previous bots and run intro text when starting. """

        self._load()

        print("Welcome to the robot factory! You can create a robot to perform various tasks! And if one robot is not enough, you can create more!")
        print("Once created, robots are automatically assigned 5 random tasks which they will complete right away.")
        print("After they have finished their tasks you can decide to either create a new robot, destroy a robot (or all of them), or assign new tasks to existing robots.")
        press_enter_to_continue()
        clear_console()
        return self

    def __exit__(self, type, value, traceback):
        """ Makes sure to save when exiting! """

        self._save()

    def _load(self):
        """ Load previous robot objects, currently using pickle. """

        try:
            robot_list = load_from_pickle()
        except IOError:
            pass # Just pass, self.robots need not be modified
        else:
            # Update instead of assignmet in case loading somehow happens after some bots are already created
            self.robots.update({bot.name: bot for bot in robot_list})

    def _save(self):
        """ Save all robot objects, using pickle. """ ### XXX better just save the factory itself instead?

        # Send a list of objects to save
        robot_list = [self.robots[k] for k in self.robots.keys()]
        save_to_pickle(robot_list)

    def view_robot_leaderboard(self):
        """ Sorts all robots by number of tasks completed and prints out the results. """

        clear_console()

        # Nothing to do if no robots have been created yet
        if not self.robots:
            print("There are no robots! Please create one first")
            press_enter_to_continue()
            clear_console()
            return

        # Create a list tuples consisting of robots and the number of tasks completed by each
        leaderboard_list = [(bot, len(bot.tasks_completed)) for bot in list(self.robots.values())]

        # Sort by most tasks completed
        leaderboard_list = sorted(leaderboard_list, key=lambda x: -x[1])

        # Printed out in a table-like view
        print("*** Leaderboard for tasks completed by each robot ***\n")
        print("Tasks | Robot")
        print("------|----------")
        for robot, num_tasks_completed in leaderboard_list:
            spaces = 4 - len(str(num_tasks_completed))
            print("{0}{1}  | {2}".format(' ' * spaces, num_tasks_completed, robot))

        press_enter_to_continue()
        clear_console()

    def create_robot(self):
        """ Create a new robot based on user input for name and robot type. """

        clear_console()
        print('*** Entering robot creation room ***\n')
        robot_name = input("What is you robot's name?\n")

        # Some name validation, we want unique names so other robots are not lost/overwritten by new bots with the same name
        while not robot_name or robot_name in self.robots:
            clear_console()
            print("*** Sorry that name is not valid or is already taken, please try another. ***\n")
            robot_name = input("What is you robot's name?\n")

        clear_console()

        _, robot_class = get_user_choice(ROBOT_TYPE_CHOICES, 'What type of robot is {0}'.format(robot_name))

        try:
            robot = ROBOT_TYPES[robot_class](robot_name) # <- instantiate on the fly
        except KeyError:
            print('\n*** Leaving Robot Creation room ***\n')
        else:
            # Store new robots in class-level dict
            self.robots[robot_name] = robot
        finally:
            press_enter_to_continue()
            clear_console()

    def interact_with_robot(self):
        """ Allows for interaction with a robot."""

        clear_console()
        print('*** Entering robot interaction room ***\n')

        # Nothing to do if no robots have been created yet
        if not self.robots:
            print("No robots to interact with, please create one first!")
            press_enter_to_continue()
            clear_console()
            return

        # Get user's robot-to-interact-with choice
        _, robot_name = get_user_choice(self.robot_name_choices, 'Choose a robot to interact with.')

        try:
            bot = self.robots[robot_name]
        except KeyError:
             # Only occurs when 0: exit is selected or no robots exist yet
            print('\n*** Leaving Robot Interaction room ***\n')
        else:
            bot.interact_with()
        finally:
            press_enter_to_continue()
            clear_console()

    def destroy_a_robot(self):
        """ Destroys a robot based on it's name. """

        clear_console()
        print('*** Entering robot destruction room ***\n')

        # Nothing to do if no robots have been created yet
        if not self.robots:
            print("No robots to destroy, please create one first!")
            press_enter_to_continue()
            clear_console()
            return

        # Get user's robot-to-destroy choice
        _, robot_name = get_user_choice(self.robot_name_choices, 'Choose a robot to destroy.')

        try:
            robot = self.robots[robot_name]
        except KeyError:
            # Only occurs when 0: exit is selected or no robots exist yet
            print("\n*** Leaving robot destruction room ***\n")
        else:
            # Confirrm that the user actually wants to destroy the bot
            clear_console()
            if input('Type DESTROY if you are sre you want to destroy {0} (not case sensitive)\n'.format(robot)).upper() == 'DESTROY':
                del self.robots[robot_name]
                print('\n*** {0} has been destroyed! ***\n'.format(robot_name))
            else:
                print('\n*** {0} was NOT destroyed! ***\n'.format(robot_name))
        finally:
            press_enter_to_continue()
            clear_console()

    def destroy_all_robots(self):
        """ Destroy all currently existing robots in this container. """

        clear_console()
        print('*** Entering super serious robot destruction room ***\n')

        # Nothing to do if no robots have been created yet
        if not self.robots:
            print("No robots to destroy, please create one first!")
            press_enter_to_continue()
            clear_console()
            return

        # Get user confirmation to actually destroy all robots
        if input('Type DESTORY if you are sure you want to destroy ALL robots (not case sensitive)\n').upper() == 'DESTROY':
            self.robots = {}
            print("\n*** All robots have been destroyed! ***\n")
        else:
            print("\n*** Robots were NOT destroyed! ***\n")

        print("\n*** Leaving robot destruction room ***\n")
        press_enter_to_continue()
        clear_console()