from entities.team_member import TeamMember
from entities.project_phase import Phase
from entities.phase_task import Task

class Project:

    def __init__(self, project_name: str, customer: str, description: str, flat_hour_rate: int):
        #project's name
        self.project_name = project_name
        #organization who is buying the project and/or to whom to a project is done for
        self.customer = customer
        #a short description of what a project is about, the objective
        self.description = description
        #a fixed and flat hourly EUR rate based on which a customer is invoiced and fees are incurred
        self.flat_hour_rate = flat_hour_rate
        #team members working in a project
        self.team_members = []
        #project's phases in a list
        self.project_phases = []

    #adds a team member to a team of a project
    def add_team_member(self, team_member: TeamMember):
        self.team_members.append(team_member)
    #adds/assigns a project phase to a project
    def add_project_phase(self, project_phase: Phase):
        self.project_phases.append(project_phase)

    def __str__(self):
        return f"{self.project_name} for customer {self.customer} with objective of {self.description}"