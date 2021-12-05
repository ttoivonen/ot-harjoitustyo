import unittest
from entities.team_member import TeamMember


class TestTeam_member(unittest.TestCase):
    def setUp(self):
        self.team_member_test1 = TeamMember("Dave Developer", "back-end Developer", 80)
        self.test_print1 = str(self.team_member_test1)

        self.team_member_test2 = TeamMember("Mark Manager", "PM", 50)
        self.team_member_test2.skills_keywords.append("Project management")
        self.team_member_test2.skills_keywords.append("JIRA")
        self.test_print2 = str(self.team_member_test2)        

    def test_constructor_works(self):

        self.assertEqual(self.test_print1, "Dave Developer, role of back-end Developer, no listed skills, with internal hourly rate EUR 80")
        self.assertEqual(self.test_print2, "Mark Manager, role of PM, skilled in Project management, JIRA, with internal hourly rate EUR 50")

if __name__ == '__main__':
    
    unittest.main()