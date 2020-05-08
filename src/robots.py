from time import sleep
from random import choice
from collections import OrderedDict

import tasks
from utils import clear_console, press_enter_to_continue, get_user_choice


class Robot(object):
    """ Base robot class, contains all base robot-related logic. """

    all_tasks = {} # overwritten by specific types

    # Shared across all Robots and subclasses
    base_tasks = tasks.base_tasks
    interaction_choices = OrderedDict([
        ('1', 'View completed tasks'),
        ('2', 'Perform a new task'),
        ('0', 'Leave'),
    ])

    def __init__(self, name):
        """ Initialize a robot, each instance with a separate empty tasks_to_perform and tasks_completed lists.
        Population and execution of tasks_to_perform list also happens within this init. """

        self.name = name
        self.msg = '' # Message that will be displayed as tasks are completed

        self.tasks_to_perform = []
        self.tasks_completed = []

        self._current_task = None

        self.populate_todo_list()
        self.perform_all_tasks()

    @property
    def current_task(self):
        """ Current task the robot is working on, may be helpful to have if async is leveraged. """
        return self._current_task

    @property
    def robot_type(self):
        """ Simple way to get the robot types as the type and class names are the same. """
        return self.__class__.__name__

    @property
    def all_tasks_list(self):
        """ List of all tasks that a specific robot can perform. This list varies based on robot type. """
        return list(self.all_tasks.keys())

    @property
    def all_task_choices(self):
        """ An OrderedDict of all tasks with enumeration for choosing specific tasks to perform. """
        task_choices = OrderedDict([(str(e+1), i) for e, i in enumerate(self.all_tasks_list)] + [('0', 'Leave')])
        return task_choices

    @property
    def interactions(self):
        """ Available interaction options a user has with the robot. mapped with self.interaction_choices. """

        return {
            'View completed tasks': self.view_completed_tasks,
            'Perform a new task': self.get_task_to_perform,
        }

    def view_completed_tasks(self):
        """ Prints out the list of tasks completed by the robot. """

        clear_console()
        print('Tasks completed by {0}'.format(self))

        for i in self.tasks_completed: print('- ' + i)

        press_enter_to_continue()
        clear_console()

    def interact_with(self):
        """ Allows the user to interact with the robot by listing out interaction options. """

        while True: # Break when users chooses to '0: Leave'
            clear_console()
            print("*** Interacting with {0} ***\n".format(self))

            # Get the user's interaction choice
            _, action_choice = get_user_choice(self.interaction_choices, 'What would you like to do with {0}'.format(self))

            try:
                self.interactions[action_choice]()
            except KeyError:
                pass # Could break here instead as only hits when '0: Leave' is chosen

            if action_choice == 'Leave':
                break

    def get_task_to_perform(self):
        """ Allows the user to choose a task to perform"""

        clear_console()
        # Get the user's task choice
        _, task_choice = get_user_choice(self.all_task_choices, 'Which task would you like {0} to perform?'.format(self))

        # Rest self.msg as it is very likely it was previously changed
        self.msg = ''

        # Actually perform the chosen task
        self.perform_task(task_choice)

        print("\n*** Task finished! ***\n")

        press_enter_to_continue()
        clear_console()

    def perform_task(self, task):
        """ Performs a single given task, could leverage the self._current task here if we do not want to pass in the task as a param. """

        try: # Attempt to get the task, then perform the task by sleeping for the listed eta duration
            # Get the task eta/duration and convert to seconds for sleep()
            eta = int(self.all_tasks[task]/1000)
        except KeyError:
            pass # Will only occur when '0: Leave' is chosen
        else:
            self.msg += '\nPerforming task: {0}, it will take approximately {1} seconds'.format(task, eta)
            self._current_task = task

            # Clear the console and update the message each iteration to give the impression of ... loading
            for _ in range(eta):
                clear_console()
                self.msg += '.'
                print(self.msg)
                sleep(1)

            # Save the task to completed_tasks list
            self.save_finished_task(task)

    def perform_all_tasks(self):
        """ Starts execution of all tasks listed in tasks_to_perform list. """

        # Reset self.msg as it is starting a new process here
        self.msg = '*** {0} is performing all required tasks, please standby. ***\n'.format(self)

        # Utlize a while loop to safely pop from list while iterating
        while self.tasks_to_perform:
            task = self.tasks_to_perform.pop(0)
            self.perform_task(task)

        print("\n*** {0} has completed all inital tasks! ***\n".format(self))

    def save_finished_task(self, task):
        """ Saves a task to tasks_completed list. """

        self.tasks_completed.append(task)

    def populate_todo_list(self, num_tasks=5):
        """ Randomly chooses (5) tasks from the list of all tasks and populates the robot's tasks_to_perform list. """

        t = set()
        while len(t) < num_tasks:
            task = choice(self.all_tasks_list)
            if task not in t:
                t.add(task)

        self.tasks_to_perform = list(t)

    def __str__(self):
        return '{0} the {1} robot'.format(self.name, self.robot_type)

    def __repr__(self):
        return '{0} the {1} robot'.format(self.name, self.robot_type)


class Unipedal(Robot):
    all_tasks = tasks.unipedal_tasks


class Bipedal(Robot):
    all_tasks = tasks.bipedal_tasks


class Quadrupedal(Robot):
    all_tasks = tasks.quadrupedal_tasks


class Arachnid(Robot):
    all_tasks = tasks.arachnid_tasks


class Radial(Robot):
    all_tasks = tasks.radial_tasks


class Aeronautical(Robot):
    all_tasks = tasks.aeronautical_tasks


# "Exportable" dicts
ROBOT_TYPES = {
    'UNIPEDAL': Unipedal,
    'BIPEDAL': Bipedal,
    'QUADRUPEDAL': Quadrupedal,
    'ARACHNID': Arachnid,
    'RADIAL': Radial,
    'AERONAUTICAL': Aeronautical,
}

ROBOT_TYPE_CHOICES = OrderedDict([
    ('1', 'UNIPEDAL'),
    ('2', 'BIPEDAL'),
    ('3', 'QUADRUPEDAL'),
    ('4', 'ARACHNID'),
    ('5', 'RADIAL'),
    ('6', 'AERONAUTICAL'),
    ('0', 'Leave')
])