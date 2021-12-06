
class Phase:

    def __init__(self, description: str):
        #description of the project phase content, e.g. preparation, discovery, sprint 1
        self.description = description
        #list of tasks assigned to a project phase
        self.phase_tasks = []

    def phase_hours(self):
        hours = 0
        for task in self.phase_tasks:
            hours += task.estimated_hours
        return hours

    def phase_int_costs(self):
        int_cost = 0
        for task in self.phase_tasks:
            int_cost += task.task_estimated_int_cost()
        return int_cost
