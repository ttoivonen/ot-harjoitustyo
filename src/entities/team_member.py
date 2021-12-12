
class TeamMember:
    """TeamMember class represents a team member in a project.
    A team member is a part of a project, has certain attributes and
    is assigned to perform tasks.

    Attributes:
        name: name of a team member
        role: role of a team member, e.g. project manager, subject matter expert, developer
        int_hour_rate: internal hourly rate, that is a targeted hourly rate for a team member 
        to cover the payroll costs of the team member; used in calculating profitablity
        skills_keywords: list of skills that a team member has, e.g. Python, Java, 
        logistics, accounting
    """

    def __init__(self, name: str, role: str, int_hour_rate: int):
        """constructor to create a TeamMember

        Args:
            name (str): name of a team member
            role (str): role of a team member, e.g. project manager, subject matter expert,
            developer
            int_hour_rate (int): internal hourly rate, that is a targeted hourly rate
            for a team member to cover the payroll costs of the team member;
            used also in calculating profitablity
        """
        self.name = name
        self.role = role
        self.int_hour_rate = int_hour_rate
        self.skills_keywords = []

    def __str__(self):
        """print format of TeamMember object

        Returns:
            str: information of a team member
        """
        if len(self.skills_keywords) == 0:
            skills_prnt = "no listed skills, "
        else:
            skills_prnt = "skilled in "
            for skill in self.skills_keywords:
                skills_prnt += skill + ", "

        return f"{self.name}, role of {self.role}, {skills_prnt}with internal hourly rate EUR {self.int_hour_rate}"
