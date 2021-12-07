from entities.phase_task import Task
from entities.project import Project
from entities.team_member import TeamMember
from entities.project_phase import Phase

class ProjectService:

    def __init__(self):
        self.projects = []
        self.active_project = Project(None, None, None, None)

    def create_project(self, project_name: str, customer_name: str,
    project_description, hourly_rate: int):
        new_project = Project(project_name, customer_name, project_description, hourly_rate)
        self.active_project = new_project
        self.projects.append(new_project)
        return True

    def print_project(self):
        print(self.active_project)

    def create_team_member(self, tm_name: str, tm_role: str, tm_int_hourly_rate: int,
    tm_skills_keywords: list):
        new_team_member = TeamMember(tm_name, tm_role, tm_int_hourly_rate)
        if len(tm_skills_keywords) > 0:
            new_team_member.skills_keywords = tm_skills_keywords
        self.active_project.team_members.append(new_team_member)
        return True


    def print_team_members(self):
        if len(self.active_project.team_members) == 0:
            return False

        for i in range(0, len(self.active_project.team_members)):
            print(f"{i + 1}: {self.active_project.team_members[i]}")

    def create_project_phase(self, ph_desription: str):
        self.active_project.project_phases.append(Phase(ph_desription))
        print(f"Project phase {ph_desription} successfully created to project {self.active_project.project_name}")

    def print_phases(self):
        if len(self.active_project.project_phases) == 0:
            return False

        for i in range(0, len(self.active_project.project_phases)):
            print(f"{i + 1}: {self.active_project.project_phases[i].description}")
        return True

    def create_task(self, phase_index: int, task_description: str, estimated_hr: int,
    tm_index: int):
        self.active_project.project_phases[phase_index - 1].phase_tasks.append((Task(
            task_description,estimated_hr, self.active_project.team_members[tm_index - 1])))
        print("A task successfully assigned to project phase")

    def print_tasks(self):
        if len(self.active_project.project_phases) == 0:
            return False
        for phase in self.active_project.project_phases:
            if len(phase.phase_tasks) == 0:
                print(f"Phase {phase.description} has no tasks")
            else:
                for task in phase.phase_tasks:
                    customer_costs = self.active_project.flat_hour_rate * task.estimated_hours
                    int_cost = task.task_estimated_int_cost()
                    print(f"{task}; customer cost EUR {customer_costs};",
                     f"internal cost EUR {int_cost} (Phase {phase.description})")


    def print_project_estimates_total(self):
        if len(self.active_project.project_phases) == 0:
            return False     
        print(self.active_project)
        print(f"Total estimated hours: {self.active_project.calculate_total_hours()}")
        print(f"Total estimated customer costs: EUR {self.active_project.calculate_total_ext_costs()}")
        print(f"Total internal costs: EUR {self.active_project.calculate_total_int_costs()}")
        print(f"Total profitability: EUR {self.active_project.calculate_total_profitability()}")


    def print_project_estimate_phase(self):
        if len(self.active_project.project_phases) == 0:
            print("No project phases or tasks created.")
            return
        phase_prnt = "Phase"
        prnt_hours = "Estimated hours"
        prnt_ext_costs = "Customer costs"
        prnt_int_costs = "Internal costs"
        prnt_profitability = "Profitability"
        total_prnt = "TOTAL"
        total_hrs = 0
        total_ext_costs = 0
        total_int_costs = 0
        total_profitability = 0
        print(f"{phase_prnt:<15}{prnt_hours:<20}{prnt_ext_costs:<20}{prnt_int_costs:<20}{prnt_profitability:<20}")
        for phase in self.active_project.project_phases:
            print(f"{phase.description:<15}{phase.phase_hours():<20}{phase.phase_hours() * self.active_project.flat_hour_rate:<20}{phase.phase_int_costs():<20}{(phase.phase_hours() * self.active_project.flat_hour_rate) - phase.phase_int_costs():<20}")
            total_hrs += phase.phase_hours()
            total_ext_costs += phase.phase_hours() * self.active_project.flat_hour_rate
            total_int_costs += phase.phase_int_costs()
            total_profitability += (phase.phase_hours() * self.active_project.flat_hour_rate) - phase.phase_int_costs()
        print(f"{total_prnt:<15}{total_hrs:<20}{total_ext_costs:<20}{total_int_costs:<20}{total_profitability:<20}")
