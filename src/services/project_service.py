from entities.phase_task import Task
from entities.project import Project
from entities.team_member import TeamMember
from entities.project_phase import Phase

class ProjectService:
    

    def __init__(self):
        self.projects = []
        self.active_project = Project(None, None, None, None)

    
    def create_project(self, project_name: str, customer_name: str, project_description, hourly_rate: int):
        new_project = Project(project_name, customer_name, project_description, hourly_rate)
        self.active_project = new_project
        self.projects.append(new_project)

    def print_project(self):
        print(self.active_project)

    def create_team_member(self, tm_name: str, tm_role: str, tm_int_hourly_rate, tm_skills_keywords: list):
        new_team_member = TeamMember(tm_name, tm_role, tm_int_hourly_rate)
        if len(tm_skills_keywords) > 0:
            new_team_member.skills_keywords = tm_skills_keywords
        self.active_project.team_members.append(new_team_member)
        print(f"Team member {tm_name} successfully created to project {self.active_project.project_name}")

    def print_team_members(self):
        if len(self.active_project.team_members) == 0:
            
            return False
        else:
            for i in range(0, len(self.active_project.team_members)):
                print(f"{i + 1}: {self.active_project.team_members[i]}")

    def create_project_phase(self, ph_desription: str):
        self.active_project.project_phases.append(Phase(ph_desription))
        print(f"Project phase {ph_desription} successfully created to project {self.active_project.project_name}")

    def print_phases(self):
        if len(self.active_project.project_phases) == 0:
            return False
        else:
            for i in range(0, len(self.active_project.project_phases)):
                print(f"{i + 1}: {self.active_project.project_phases[i].description}")
            return True

    def create_task(self, phase_index: int, task_description: str, estimated_hr: int, tm_index: int):
        self.active_project.project_phases[phase_index - 1].add_task((Task(task_description, estimated_hr, self.active_project.team_members[tm_index - 1])))
        print("A task successfully assigned to project phase")

    def print_tasks(self):
        for i in self.active_project.project_phases:
            for a in i.phase_tasks:
                print(a)
