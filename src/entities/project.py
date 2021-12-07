
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

    def calculate_total_hours(self):
        total_hours = 0
        for phase in self.project_phases:
            total_hours += phase.phase_hours()
        return total_hours

    def calculate_total_ext_costs(self):
        total_ext_costs = self.calculate_total_hours() * self.flat_hour_rate
        return total_ext_costs

    def calculate_total_int_costs(self):
        total_int_costs = 0
        for phase in self.project_phases:
            total_int_costs += phase.phase_int_costs()
        return total_int_costs

    def calculate_total_profitability(self):
        profitability = self.calculate_total_ext_costs() - self.calculate_total_int_costs()
        return profitability

    def __str__(self):
        return f"{self.project_name} for customer {self.customer} with objective of {self.description}"
