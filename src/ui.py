from project import Project
from app_logic import AppLogic

#the code covers creating a project and any number of team members to the project
application = AppLogic()
print("Create a new project")
project = application.create_project()
while True:
    application.print_command_options()
    command = input("Select to: ")

    if command == "x":
        break
    elif command == "1":
        team_member = application.create_team_member()
        project.team_members.append(team_member)

#test code to ensure team members are saved to project object
for i in project.team_members:
    print(i)