from xlsxwriter import *
import xlsxwriter
from entities.phase_task import Task
from entities.project import Project
from entities.team_member import TeamMember
from entities.project_phase import Phase


class ProjectService:
    """The class takes care of the logic and operations
    of building, modifying and displaying a project

    Attributes:
        active_project = a project object created by an user and
        that is build, modified and displayed in the application
    """
    def __init__(self):
        """A constructor to create the service class

        Attributes:
            active_project = a project object created by an user and
            that is build, modified and displayed in the application
        """
        self.active_project = Project(None, None, None, None)

    def create_project(self, project_name: str, customer_name: str,
    project_description: str, hourly_rate: int):
        """To create a project object. Project attributes are given
        in the parameters.

        Args:
            project_name (str): name of the project
            customer_name (str): customer name
            project_description (str): description of the project
            hourly_rate (int): the flat/fixed hourly rated invoiced
            from acustomer

        Returns:
            boolean: True if the operation was successful
        """
        new_project = Project(project_name, customer_name, project_description, hourly_rate)
        self.active_project = new_project
        return True

    def create_team_member(self, tm_name: str, tm_role: str, tm_int_hourly_rate: int,
    tm_skills_keywords: list):
        """To create a team member object to the active project. Team Member attributes
        are given in the parameters.

        Args:
            tm_name (str): team member name
            tm_role (str): role of the team member in the project
            tm_int_hourly_rate (int): internal hourly rate of a team member
            tm_skills_keywords (list): a list of skills of a team member

        Returns:
            boolean: True if the operation was successful
        """
        new_team_member = TeamMember(tm_name, tm_role, tm_int_hourly_rate)
        if len(tm_skills_keywords) > 0:
            new_team_member.skills_keywords = tm_skills_keywords
        self.active_project.team_members.append(new_team_member)
        return True

    def delete_phase(self, phase_index: int):
        """Delete an existing project phase. Application prints existing phases with
            index numbers for each; user provides input as index number
            according to the to be deleted phase

        Args:
            phase_index (int): index number of the to-be deleted phase

        Returns:
            boolean: True if the operation was successful
        """
        try:
            deleted = self.active_project.project_phases.pop(phase_index - 1)
            print(f"Project phase {deleted.description} successfully deleted")
            return True
        except IndexError:
            return False

    def delete_task(self, phase_index: int, task_index):
        """Delete a Task in a Phase. Application prints existing tasks with
            index numbers for each; user provides input as index number
            according to the to be deleted task.

        Args:
            phase_index (int): index number of phase
            task_index ([type]): index number of the to-be deleted task

        Returns:
            boolean: True if the operation was successful
        """
        try:
            delete = self.active_project.project_phases[phase_index - 1].phase_tasks.pop(task_index - 1)
            phase_name = self.active_project.project_phases[phase_index - 1].description
            print(f"Task {delete.task_description} successfully deleted from phase {phase_name}")
            return True
        except IndexError:
            return False

    def print_team_members(self):
        """Prints the existing team members with their respective information

        Returns:
            boolean: True if any team members are existing
        """
        if len(self.active_project.team_members) == 0:
            return False

        for i in range(0, len(self.active_project.team_members)):
            print(f"{i + 1}: {self.active_project.team_members[i]}")
        return True

    def create_project_phase(self, ph_desription: str):
        """To create a project phase.

        Args:
            ph_desription (str): Description to be given for the phase

        Returns:
            boolean: True if the operation was successful.
        """
        self.active_project.project_phases.append(Phase(ph_desription))
        return True

    def print_phases(self):
        """Prints existing project phases.

        Returns:
            boolean: True if any project phases are existing.
        """
        if len(self.active_project.project_phases) == 0:
            return False

        for i in range(0, len(self.active_project.project_phases)):
            print(f"{i + 1}: {self.active_project.project_phases[i].description}")
        return True

    def create_task(self, phase_index: int, task_description: str, estimated_hr: int,
    tm_index: int):
        """To create a Task object. Attributes are given in the parameters, team member
        and phase asre given in index format based on list of existing team members
        and phases.

        Args:
            phase_index (int): phase to which the task is assigned to
            task_description (str): description/content of a task
            estimated_hr (int): estimated hours to complete a task
            tm_index (int): a team member to whom a task is assigned to
        Returns:
            boolean: True if the operation was successful
        """
        self.active_project.project_phases[phase_index - 1].phase_tasks.append((Task(
            task_description,estimated_hr, self.active_project.team_members[tm_index - 1])))
        return True

    def print_tasks(self):
        """Print existing tasks with their respective phase

        Returns:
            boolean: True if any phases with tasks exist
        """
        if len(self.active_project.project_phases) == 0:
            return False
        phase_index = 1
        for phase in self.active_project.project_phases:
            if len(phase.phase_tasks) == 0:
                print(f"Phase {phase.description} has no tasks")
            else:
                print(f"{phase_index} {phase.description}")
                task_index = 1
                for task in phase.phase_tasks:
                    task_tm_name = task.team_member.name
                    task_hours = task.task_estimated_hours()
                    print(f"  {phase_index}.{task_index}: {task.task_description}; team member {task_tm_name}; estimated hours {task_hours}")
                    task_index += 1
            phase_index += 1
        return True


    def print_project_estimates_total(self):
        """Calculate and print an overview of total aggregated time and financial figures
        of a project

        Returns:
            boolean: True if any the operation was successful
        """
        if len(self.active_project.project_phases) == 0:
            return False
        print(self.active_project)
        print(f"Total estimated hours: {self.active_project.calculate_total_hours()}")
        print(f"Total estimated customer costs: EUR {self.active_project.calculate_total_ext_costs()}")
        print(f"Total internal costs: EUR {self.active_project.calculate_total_int_costs()}")
        print(f"Total profitability: EUR {self.active_project.calculate_total_profitability()}")
        return True


    def print_project_estimate_phase(self):
        """Calculate and print project's time and financial information on phase level

        Returns:
            boolean: True if any phases and tasks exists for the calculation
        """
        if len(self.active_project.project_phases) == 0:
            print("No project phases or tasks created.")
            return False
        phase_prnt = "Phase"
        prnt_hours = "Estimated hours"
        prnt_ext_costs = "Customer costs"
        prnt_ext_costs_percentage = "'%' of customer costs"
        prnt_int_costs = "Internal costs"
        prnt_int_costs_percentage = "'%' of internal costs"
        prnt_profitability = "Profitability"
        total_prnt = "TOTAL"
        hourly_rate = self.active_project.hour_rate()
        total_hrs = self.active_project.calculate_total_hours()
        total_ext_costs = self.active_project.calculate_total_ext_costs()
        total_costs_perc = "100.00%"
        total_int_costs = self.active_project.calculate_total_int_costs()
        total_profitability = self.active_project.calculate_total_profitability()
        header1 = f"{phase_prnt:<15}{prnt_hours:<20}{prnt_ext_costs:<20}{prnt_ext_costs_percentage:<25}"
        header2 = f"{prnt_int_costs:<20}{prnt_int_costs_percentage:<25}{prnt_profitability:<20}"
        print(header1+header2)
        for phase in self.active_project.project_phases:
            ext_cost_percentage = "{:.2f}".format(phase.phase_ext_costs(hourly_rate)  / self.active_project.calculate_total_ext_costs() * 100) + "%"
            int_cost_percentage = "{:.2f}".format(phase.phase_int_costs() / self.active_project.calculate_total_int_costs() * 100) + "%"
            output1= f"{phase.description:<15}{phase.phase_hours():<20}{phase.phase_ext_costs(hourly_rate):<20}"
            output2 = f"{ext_cost_percentage:<25}{phase.phase_int_costs():<20}{int_cost_percentage:<25}{phase.phase_profitability(hourly_rate):<20}"
            print(output1+output2)

        print(f"{total_prnt:<15}{total_hrs:<20}{total_ext_costs:<20}{total_costs_perc:<25}{total_int_costs:<20}{total_costs_perc:<25}{total_profitability:<20}")
        return True

    def save_to_xlsx(self, file_name: str):
        """Save project's structure with time and financial estimates
        to an Excel spread sheet. One sheet for estimate breakdown on Phase-Task
        level and another sheet for total aggregated numbers.

        Args:
            file_name (str): name of the to-be created file

        Returns:
            boolean: True if the operation was successful
        """

        path = "src/saved_project_files/" + file_name + ".xlsx"
        workbook = Workbook(path)
        phases_tasks_ws = workbook.add_worksheet("Phases and tasks")
        phases_tasks_ws.set_column(1, 3, 18)
        phases_tasks_ws.write("A1", "No")
        phases_tasks_ws.write("B1", "Phase")
        phases_tasks_ws.write("C1", "Task")
        phases_tasks_ws.write("D1", "Team member")
        phases_tasks_ws.write("E1", "Hours")
        phases_tasks_ws.write("F1", "Int cost")
        phases_tasks_ws.write("G1", "Customer cost")

        index_phase = 1
        row = 1
        for phase in self.active_project.project_phases:
            index_task = 1
            for task in phase.phase_tasks:
                phases_tasks_ws.write(row, 0, f"{index_phase}.{index_task}")
                phases_tasks_ws.write(row, 1, phase.description)
                phases_tasks_ws.write(row, 2, task.task_description)
                phases_tasks_ws.write(row, 3, task.team_member.name)
                phases_tasks_ws.write(row, 4, task.task_estimated_hours())
                phases_tasks_ws.write(row, 5, task.task_estimated_int_cost())
                phases_tasks_ws.write(row, 6,task.task_estimated_hours() * self.active_project.hour_rate())
                index_task += 1
                row += 1
            index_phase += 1
        totals = workbook.add_worksheet("Totals")
        totals.set_column(0,0,24)
        totals.write("A1", "Total estimated hours")
        totals.write("B1", self.active_project.calculate_total_hours())
        totals.write("A2", "Total estimated customer costs")
        totals.write("B2", self.active_project.calculate_total_ext_costs())
        totals.write("A3", "Total estimated internal costs")
        totals.write("B3", self.active_project.calculate_total_int_costs())
        totals.write("A4", "Total profitability")
        totals.write("B4", self.active_project.calculate_total_profitability())
        try:
            workbook.close()
        except xlsxwriter.exceptions.FileCreateError as e:
            print("Error in creating a flie: " + e)
            return False
        return True
