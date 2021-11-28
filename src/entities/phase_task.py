from entities.team_member import TeamMember

class Task:
    def __init__(self, task_description: str, estimated_hours: int, team_member: TeamMember):
        #description of a content of a task
        self.task_description = task_description
        #estimated hours to perform the task
        self.estimated_hours = estimated_hours
        #a team member who performs the task
        self.team_member = team_member

    def __str__(self):
        return f"{self.task_description} estimated hours {self.estimated_hours}, team member {self.team_member.name} is performing the task"