
from services.project_service import ProjectService

class ProjectManagement:
    
    
    def __init__(self):
        self.service = ProjectService()

    def start(self):
        #first mandatory step is to create a project
        print("Start by creating a new project")
        self.define_project_activity()

        while True:
            #this is the main menu where user can choose activities
            #command 4 will move user to display view menu
            self.print_activity_command_options()
            command = input("Select activity: ")
            if command == "x":
                break
            elif command == "1":     
                self.create_team_member_activity()
            elif command == "2":
                self.create_project_phase_activity()
            elif command == "3":
                self.create_task_to_phase_activity()
            elif command == "4":
                self.delete_phase_activity()
            elif command == "5":
                self.delete_task_activity()
            elif command == "6":
                self.save_to_file()
            elif command == "7":
                while True:
                    #display options are below
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
                        if self.service.print_project_estimate_phase() == False:
                            print("No project phases or tasks created.")
                    elif display_command == "5":
                        if self.service.print_project_estimates_total() == False:
                            print("No project phases or tasks created.")
                    else:
                        print("Unknown command")
            else:
                print("Unknown command")

    def define_project_activity(self):
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
    
    def create_team_member_activity(self):
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
            print(f"Team member {tm_name} successfully created to project {self.service.active_project.project_name()}")

    def create_project_phase_activity(self):
        ph_description = input("A description of the phase: ")
        if self.service.create_project_phase(ph_description) == True:
            print(f"Project phase {ph_description} successfully created to project {self.service.active_project.project_name()}")

    def create_task_to_phase_activity(self):
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
            if self.service.create_task(select_phase, task_description, estimated_hr, tm_for_task):
                print(f"Task {task_description} successfully created")
    
    def delete_phase_activity(self):
        if self.service.print_phases() == False:
            print("No existing phases for the project to be deleted")
            return
        while True:
            try:
                delete_index = int(input("Select the phase to be deleted (integer number): "))
                if self.service.delete_phase(delete_index) == False:
                    print("Incorrect value. No project existing for the selected value.")
                break
            except ValueError:
                print("Incorrect value. Selection must be a number value (integer).")

    def delete_task_activity(self):
        if self.service.print_tasks() == False:
            print("No tasks to be deleted due non-existing project phases")
            return
        while True:
            try:
                delete_number = input("Select the task to be deleted (in format [phase].[task], e.g. 1.2): ")
                if delete_number.find(".") < 0:
                    print("Wrong index number")
                    return
                delete_number_parts = delete_number.split(".")
                delete_phase_index = int(delete_number_parts[0])
                delete_task_index = int(delete_number_parts[1])
                if self.service.delete_task(delete_phase_index, delete_task_index) == False:
                    print("Incorrect value. No task existing for the selected value.")
                break
            except ValueError:
                print("Incorrect value. Selection must be in a format [phase].[task], e.g. 1.2.")

    def save_to_file(self):
        file_name = input("Enter file name: ")
        if self.service.save_to_xlsx(file_name) == True:
            print("File " + file_name + ".xlsx created successufully to src/saved_project_files")
        
    def print_activity_command_options(self):
        commands_main = {"1": "add team members to the project team", "2": "create a project phase",
        "3": "add a task to a project phase", "4": "delete a project phase", "5": "delete a task from a phase",
        "6": "save project to a Excel file", "7": "show display options", "x": "exit"}
        print("\nSelect action")
        for command_key, command_value in commands_main.items():
            print(f"{command_key} {command_value}")

    def print_display_command_options(self):
        commands_display = {"1": "display team members", "2": "display project phases", "3": "display tasks",
        "4": "display project estimates on phase level", "5": "display total estimates of the project", "x": "return"}
        print("\nSelect display view")
        for command_key, command_value in commands_display.items():
            print(f"{command_key} {command_value}")
