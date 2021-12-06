
class Project:

    def __init__(self, project_name: str, customer: str, description: str, flat_hour_rate: int):
        #project's name
        self.project_name = project_name
        #organization who is buying the project and/or to whom to a project is done for
        self.customer = customer
        #a short description of what a project is about, the objective
        self.description = description
        #a fixed and flat hourly EUR rate based on which a customer is invoiced and 
        # fees are incurred
        self.flat_hour_rate = flat_hour_rate
        #team members working in a project
        self.team_members = []
        #project's phases in a list
        self.project_phases = []


    def __str__(self):
        return f"{self.project_name} for customer {self.customer} with objective of {self.description}"
