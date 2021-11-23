from project import Project
from app_logic import AppLogic

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
        project.add_team_member(team_member)

for i in project.team_members:
    print(i)