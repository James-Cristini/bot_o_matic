# Ideally this would be manually reformatted to reduce the extra formatting but left as is for now
base_tasks_orig = [
  {
    'description': 'do the dishes',
    'eta': 1000,
  },{
    'description': 'sweep the house',
    'eta': 3000,
  },{
    'description': 'do the laundry',
    'eta': 10000,
  },{
    'description': 'take out the recycling',
    'eta': 4000,
  },{
    'description': 'make a sammich',
    'eta': 7000,
  },{
    'description': 'mow the lawn',
    'eta': 20000,
  },{
    'description': 'rake the leaves',
    'eta': 18000,
  },{
    'description': 'give the dog a bath',
    'eta': 14500,
  },{
    'description': 'bake some cookies',
    'eta': 8000,
  },{
    'description': 'wash the car',
    'eta': 20000,
  },
]

# Reogranize the above tasks for simpler use in the program
reformatted_tasks = {i['description']:i['eta'] for i in base_tasks_orig}

### Easily add new tasks to either the base list or specific types by modifying the corresponding dictionaries

### Base tasks (see also reformatted_tasks above)
base_tasks = {
  'practice beep-boxing': 8000
}
base_tasks.update(reformatted_tasks)


### UNIPEDAL specific tasks
unipedal_tasks = {
    'show off with a balancing act': 9000,
    'act like a unicycle': 5000,
    }
unipedal_tasks.update(base_tasks)


### BIPEDAL specific tasks
bipedal_tasks = {
    'do some squats': 9000,
    'kick a soccer ball': 2000,
    }
bipedal_tasks.update(base_tasks)


### QUADRUPEDAL specific tasks
quadrupedal_tasks = {
    'run around like a cheetah': 9000,
    'kick two soccer balls at once': 2000,
    }
quadrupedal_tasks.update(base_tasks)


### ARACHNID specific tasks
arachnid_tasks = {
    'walk around creepily': 22000,
    'kick four soccer balls at once': 2000,
    }
arachnid_tasks.update(base_tasks)


### RADIAL specific tasks
radial_tasks = {
    'spin really fast': 12000,
    'do an interesting "dance"?': 19000,
    }
radial_tasks.update(base_tasks)


### AERONAUTICAL specific tasks
aeronautical_tasks = {
    'fly around and do barrel rolls': 17000,
    'partake in a synchronized flying routine': 25000,
    }
aeronautical_tasks.update(base_tasks)