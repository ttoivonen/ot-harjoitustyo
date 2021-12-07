
from services.project_service import ProjectService

class ProjectManagement:
    
    
    def __init__(self):
        self.service = ProjectService()

    def start(self):
        if len(self.service.projects) == 0:

            print("Start by creating a new project")
            self.define_project()
        else:
            #to be added option to create several projects and to change active project among created/existing projects for modification or deletion
            pass
        while True:
            self.print_main_command_options()
            command = input("Select activity: ")
            if command == "x":
                break
            elif command == "1":     
                self.create_team_member()
            elif command == "2":
                self.create_project_phase()
            elif command == "3":
                self.create_task_to_phase()
            elif command == "4":
                while True:
                    self.print_display_command_options()
                    display_command = input("Select to display: ")
                    if display_command == "x":
                        break
                    elif display_command == "1":
                        if self.service.print_team_members() == False:
                            print("No team members existing to display")
                    elif display_command == "2":
                        if self.service.print_phases() == False:
                            print("No project phases existing to display")
                    elif display_command == "3":
                        if self.service.print_tasks() == False:
                            print("No tasks existing")
                    elif display_command == "4":
                        self.service.print_project_estimate_phase()
                    elif display_command == "5":
                        if self.service.print_project_estimates_total() == False:
                            print("No project phases or tasks created.")
                    else:
                        print("Unknown command")
            else:
                print("Unknown command")

    def define_project(self):
        #hard coded test inputs to save some time in building and testing
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
            while True:
                try:
                    hourly_rate = int(input("Hourly rate (EUR): "))
                    break
                except ValueError:
                    print("Incorrect value. Hourly rate must be a number value (integer).")
        if self.service.create_project(project_name, customer_name, project_description, hourly_rate) == True:
            print(f"Project {project_name} created successfully.")
    
    def create_team_member(self):
        tm_name = input("Team member name: ")
        tm_role = input("Role: ")
        while True:
            try:
                tm_int_rate = int(input("Internal hourly rate (EUR): "))
                break
            except ValueError:
                print("Incorrect value. Internal hourly rate must be a number value (integer).")
        tm_skills_kw = []
        while True:
            tm_skill = input("Add keyword for a skill of the person (enter x to exit): ")
            if tm_skill == "x":
                break
            else:
                tm_skills_kw.append(tm_skill)
        if self.service.create_team_member(tm_name, tm_role, tm_int_rate, tm_skills_kw) == True:
            print(f"Team member {tm_name} successfully created to project {self.service.active_project.project_name}")
        #print(f"Team member {tm_name} successfully created to project {self.active_project.project_name}")

    def create_project_phase(self):
        ph_description = input("A description of the phase: ")
        self.service.create_project_phase(ph_description)

    def create_task_to_phase(self):
        if self.service.print_phases() == False:
            print("No available project phases, create a project phase to assign task(s) to it")
        else:
            select_phase = int(input("Select to which project phase a task is to be created: "))
            if self.service.print_team_members() == False:
                print("No team members existing to perform a task. Create a team member before creating a task.")
                return
            tm_for_task = int(input("Select team member (integer from the list) who performs the task: "))
            task_description = input("Description of the task: ")
            while True:
                try:
                    estimated_hr = int(input("Estimated hours (integer) to complete the task: "))
                    break
                except ValueError:
                    print("Incorrect value. Estimated hours must be a number value (integer).")
            self.service.create_task(select_phase, task_description, estimated_hr, tm_for_task)
        
    def print_main_command_options(self):
        commands_main = {"1": "add team members to the project team", "2": "create a project phase",
        "3": "add a task to a project phase", "4": "show display options", "x": "exit"}
        print("Select action")
        for command_key, command_value in commands_main.items():
            print(f"{command_key} {command_value}")

    def print_display_command_options(self):
        commands_display = {"1": "display team members", "2": "display project phases", "3": "display tasks",
        "4": "display project estimates on phase level", "5": "display total estimates of the project", "x": "return"}
        print("Select display view")
        for command_key, command_value in commands_display.items():
            print(f"{command_key} {command_value}")