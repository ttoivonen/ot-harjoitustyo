from team_member import TeamMember

class Task:
    def __init__(self, task_description: str):
        #description of a content of a task
        self.task_description = task_description
        #one or multiple team members with estimated hours to complete a task, a team member as a key
        #and estimated hours as a value
        self.team_member_estimated_hours = {}

    def add_team_member_and_hours(self, team_member: TeamMember, estimated_hours: int):
        self.team_member_estimated_hours[team_member] = [estimated_hours]