from entities.team_member import TeamMember

class Task:
    """Task class represents an object associated to a phase. It's a sub-component
    of a phase, consisting a project activity in a phase.

    Attributes:
        task_description: description of a content of a task
        estimated_hours: estimated hours to perform the task, i.e.
        how many hours it takes to complete the task
        team_member: a team member who performs the task
    """
    def __init__(self, task_description: str, estimated_hours: int, team_member: TeamMember):
        """constructor to create a new Task

        Args:
            task_description (str): description of a content of a task
            estimated_hours (int): estimated hours to perform the task, i.e.
            how many hours it takes to complete the task
            team_member (TeamMember): a team member who performs the task
        """
        self.task_description = task_description
        self.estimated_hours = estimated_hours
        self.team_member = team_member

    def task_estimated_int_cost(self):
        """calculate estimated internal costs for the Task based on
        team member rate and hours estimated for the Task

        Returns:
            int: estimated internal costs of the Task
        """
        return self.team_member.int_hour_rate * self.task_estimated_hours()

    def task_estimated_hours(self):
        """calculate the estimated hours for the task

        Returns:
            int: estimated hours of the Task
        """
        return self.estimated_hours


    def __str__(self):
        """print format of Task object

        Returns:
            str: Task's description, estimated hours and team member
        """
        return f"{self.task_description} with estimated hours {self.estimated_hours} for team member {self.team_member.name}"
