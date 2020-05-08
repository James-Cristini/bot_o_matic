# BOT-O-MAT


## Starting
The bot-o-mat program is a simple, interactive command line program that lets users to create robots and assign them tasks
Users can also destroy one or all of their robots (if so desired) or view the leaderboard among all created robots to see which has completed the most tasks

To start:
* run src/main.py (e.g. `>>> python3 src/main.py`)
* You will be shown some quick introduction instructions, press enter whenever prompted to move the program forward.
* You'll then see a list of choices, type the number associated with the choice you'd like to make and hit enter to proceed
    * Be sure to enter a valid choice when prompted, you cannot continue until a valid listed choice is made!

## Making Choices
```
1: Create a new robot
2: Interact with a robot
3: Destroy a robot
4: Destroy all robots
5: View robot task leaderboard
0: Exit
```
As said above, you will need to type the number associated with the choice you'd like to make and hit enter. Doing so will open up more options related to the initial choice.

## Creating
```
1: Create a new robot
```

Creating a new robot is simple and should be the first thing you do! All you need to do is enter the name when prompted
and then choose the type of robot when asked. Once a robot is created it will be automatically assigned five tasks which
it will begin completing right away. After a robot is created and finishes all of its tasks, you will have the ability
to interact with it, destroy it, or view leaderboards which show the number of tasks completed by all robots.

## Interacting
```
2: Interact with a robot
```

Interacting with a robot can be fun! When choosing this option you will first be asked to pick which robot you'd like to
interact with, once selected you can view a list of all the tasks completed by it or assign it new tasks to complete.
The more tasks a robot completes, the higher it will rank on the leaderboards!

## Destroying
```
3: Destroy a robot
4: Destroy all robots
```
There comes a time in every robot's life where they're just not needed (or wanted :/) anymore. When that time comes all
you need to is make the choice and its gone. You can either destroy a single robot or, if needed, all of them at once.
Its a simple and painless process (at least for you).

## Leaderboards
```
5: View robot task leaderboard
```
As robots complete tasks, their rank on the leaderboard rises. This leaderboard simply ranks the robots from greatest
number of tasks completed to least so make sure your favorite bot is working hard to stay on top!

## Persistant Bots
Everytime you start a new session, the program will attempt to load the previous session via pickling in the robot_save.pkl
file, if the file is present and populated you will see all of your bots from the previous session have survived and are
doing just as well as the last time you saw them! As long as you exit the robot factory properly everytime the end state
is saved for you

## Exiting
```
0: Exit
```
To exit the session, just enter '0' and confirm by typing exit (note that this is not case sensitive).

## Additional Notes
* Most choices are made by typing the corresponding number in the console but sometimes you will need to confirm an action
(when destroying bots or exiting).
    * Typing the confirmation word is not case sensitive
* Everything takes place in the console and there are not additional command lines arguments needed when running, simply
run the main.py script to start
* This program was written in python 3.7 but I've added backward compatibility for 2.7 in case that is needed
* The console's 'clear' command is called often to help make it easier to follow prompts and information but you should
be able to scroll up if you feel you missed anything!
* I included the .env to prevent any issues when trying to run as a package (e.g. in vscode or another IDE's debugger) though
typically .env should be included in the .gitignore

## Have fun!
