from phase_task import Task

class Phase:
    
    def __init__(self, description: str):
        #description of the project phase content, e.g. preparation, discovery, sprint 1
        self.description = description
        #list of tasks assigned to a project phase
        self.phase_tasks = []

    def add_task(self, task: Task):
        self.phase_tasks.append(task)