
class TeamMember:

    def __init__(self, name: str, role: str, int_hour_rate: int):
        #name of a team member
        self.name = name
        #role of a team member, e.g. project manager, subject matter expert, business analyst
        self.role = role
        #internal hourly rate, that is a targeted hourly rate for a team member to cover the payroll costs of the team member
        self.int_hour_rate = int_hour_rate
        #list of skills that a team member has, e.g. Python, Java, logistics, accounting, change management
        self.skills_keywords = []
    
    def __str__(self):
        if len(self.skills_keywords) == 0:
            skills_prnt = "no listed skills, "
        else:
            skills_prnt = "skilled in "
            for skill in self.skills_keywords:
                skills_prnt += skill + ", "

        return f"{self.name}, role of {self.role}, {skills_prnt}with internal hourly rate EUR {self.int_hour_rate}"
