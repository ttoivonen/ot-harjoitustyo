
import re


class Phase:
    """Phase class represents a phase in a project. There can be multiple phases
    associated to a project. A phase consists of task(s) that are performed
    by team members.

    Attributes:
        description: description of the project phase content, e.g. preparation, sprint 1
        phase_tasks: a list of tasks assigned to a project phase
    """

    def __init__(self, description: str):
        """constructor that creates a new Phase

        Args:
            description (str): description of the project phase content,
            e.g. preparation, sprint 1
        """
        self.description = description
        self.phase_tasks = []

    def phase_hours(self):
        """calculates the total hours associated to the phase

        Returns:
            int: hours of a phase
        """
        hours = 0
        for task in self.phase_tasks:
            hours += task.task_estimated_hours()
        return hours

    def phase_int_costs(self):
        """calculates total internal costs associated
        to the phase

        Returns:
            int: internal costs of a phase
        """
        int_cost = 0
        for task in self.phase_tasks:
            int_cost += task.task_estimated_int_cost()
        return int_cost

    def phase_ext_costs(self, hourly_rate: int):
        """Calculates and returns customer (external) costs for the phase

        Args:
            hourly_rate (int): fixed/flat hourly rate defined on the project level

        Returns:
            int: phase's total customer (external) costs
        """
        return self.phase_hours() * hourly_rate

    def phase_profitability(self, hourly_rate: int):
        """Calculates and returns profitability of the phase

        Args:
            hourly_rate (int): fixed/flat hourly rate defined on the project level

        Returns:
            [type]: phase's total profitability
        """
        return self.phase_ext_costs(hourly_rate) - self.phase_int_costs()
