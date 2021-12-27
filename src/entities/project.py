

class Project:
    """Project class represents the highest level in a project structure (Project>Phase>Task) and
    and it included general information about the project, e.g. flat EUR rate for
    invoicing, who is customere etc. Its downstream components are phases, stored in a list.

    Attributes:
        project_name: project's name
        customer: organization who is buying the project and/or to whom to a project is done for
        description: a short description of what a project is about; the objective
        flat_hour_rate: flat (fixed) hourly EUR rate based on which a customer is invoiced and
        fees are incurred
        team_members: people working in the project team
        project_phases: project consist phases to carry out the mission
    """

    def __init__(self, project_name: str, customer: str, description: str, flat_hour_rate: int):
        """Constructor that creates a new Project

        Args:
            project_name (str): project's name
            customer organization who is buying the project and/or to whom to a project is done for
            description (str): a short description of what a project is about; the objective
            flat_hour_rate (int): flat (fixed) hourly EUR rate based on which a customer is 
            invoiced and fees are incurred.
        """
        self.__project_name = project_name
        self.customer = customer
        self.description = description
        self.__flat_hour_rate = flat_hour_rate
        self.team_members = []
        self.project_phases = []

    def hour_rate(self):
        """Returns project's flat hour rate

        Returns:
            int: project hourly rate
        """
        return self.__flat_hour_rate

    def project_name(self):
        """Return project's name

        Returns:
            str: project name
        """
        return self.__project_name

    def calculate_total_hours(self):
        """Calculates the total hours associated the project

        Returns:
            int: total hours of the project
        """
        total_hours = 0
        for phase in self.project_phases:
            total_hours += phase.phase_hours()
        return total_hours

    def calculate_total_ext_costs(self):
        """calculates project's total external costs, i.e.
        the amount of fees for the customer. Total hours * flat hourly rate.

        Returns:
            int: total external EUR costs of the project
        """
        total_ext_costs = self.calculate_total_hours() * self.hour_rate()
        return total_ext_costs

    def calculate_total_int_costs(self):
        """calculates project's total internal costs, i.e. costs
        for the service provider.

        Returns:
            int: total internal EUR costs of the project
        """
        total_int_costs = 0
        for phase in self.project_phases:
            total_int_costs += phase.phase_int_costs()
        return total_int_costs

    def calculate_total_profitability(self):
        """calculate project's profitability; delta between external
        (customer) costs and internal costs

        Returns:
            int: total profitability of the project
        """
        profitability = self.calculate_total_ext_costs() - self.calculate_total_int_costs()
        return profitability

    def __str__(self):
        """print project details summary incl. project name, customer, description

        Returns:
            str: project summary
        """
        return f"{self.__project_name} for customer {self.customer} with objective of {self.description}"
