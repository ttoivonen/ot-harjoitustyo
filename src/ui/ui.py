from services import project_service
from services.project_service import ProjectService

class ProjectManagement:
    
    
    def __init__(self):
        self.service = ProjectService()

    def start(self):
        if len(self.service.projects) == 0:

            print("Start by creating a new project")
            self.define_project()
            self.service.print_project()
        else:
            #to be added option to create several projects and to change active project among created/existing projects for modification or deletion
            pass
        while True:
            self.print_command_options()
            command = input("Select to: ")
            if command == "x":
                break
            elif command == "1":     
                self.create_team_member()
            elif command == "2":
                self.create_project_phase()
            elif command == "3":
                self.create_task_to_phase()

    def define_project(self):
        hard_coded_test_inputs = True
        if hard_coded_test_inputs:
            project_name = "ERP implementation"
            customer_name = "Company Oy"
            project_description = "Implementation of core S4HANA processes"
            hourly_rate = 100
        else:
            project_name = input("Name of the project: ")
            customer_name = input("Customer: ")
            project_description = input("Description of the project: ")
            hourly_rate = int(input("Hourly rate (EUR): "))
        self.service.create_project(project_name, customer_name, project_description, hourly_rate)
    
    def create_team_member(self):
        tm_name = input("Team member name: ")
        tm_role = input("Role: ")
        tm_int_rate = input("Internal hourly rate (EUR): ")
        tm_skills_kw = []
        while True:
            tm_skill = input("Add keyword for a skill of the person (enter x to exit): ")
            if tm_skill == "x":
                break
            else:
                tm_skills_kw.append(tm_skill)
        self.service.create_team_member(tm_name, tm_role, tm_int_rate, tm_skills_kw)

    def create_project_phase(self):
        ph_description = input("A description of the phase: ")
        self.service.create_project_phase(ph_description)

    def create_task_to_phase(self):
        if self.service.print_phases() == False:
            print("No available project phases, create a project phase to assign task(s) to it")
        else:
            select_phase = int(input("Select to which project phase a task is to be created:"))
            if self.service.print_team_members() == False:
                print("No team members existing to perform a task. Create a team member before creating a task.")
                return
            tm_for_task = int(input("Select team member (integer from the list) who performs the task: "))
            task_description = input("Description of the task: ")
            estimated_hr = int(input("Estimated hours (integer) to complete the task: "))
            self.service.create_task(select_phase, task_description, estimated_hr, tm_for_task)
        
    def print_command_options(self):
        commands = {"1": "1 add team members to the project team", "2": "2 create a project phase", "3": "3 add a task to a project phase", "x": "x exit"}
        print("Select action")
        for i, a in commands.items():
            print(a)

