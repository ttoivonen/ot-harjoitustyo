from project import Project
from team_member import TeamMember

class AppLogic:

    def create_project(self):
        project_name = input("Name of the project: ")
        customer_name = input("Customer: ")
        project_description = input("Description of the project: ")
        hourly_rate = input("Hourly rate (EUR): ")
        new_project = Project(project_name, customer_name, project_description, hourly_rate)
        print("A new project created successfully")
        return new_project

    def print_command_options(self):
        commands = {"1": "1 add team members to the project team", "2": "2 create a project phase", "3": "3 add a task to a project phase", "x": "x exit"}
        print("Select action")
        for i in commands.items():
            print(i)

    def create_team_member(self):
        tm_name = input("Team member name: ")
        tm_role = input("Role: ")
        tm_int_rate = input("Internal hourly rate (EUR): ")
        new_team_member = TeamMember(tm_name, tm_role, tm_int_rate)
        while True:
            tm_skill = input("Add keyword for a skill of the person (enter x to exit): ")
            if tm_skill == "x":
                break
            else:
                new_team_member.skills_keywords.append(tm_skill)
        return new_team_member


#testi = AppLogic()

#project = testi.create_project()
#print(project.project_name, project.customer)

