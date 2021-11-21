import unittest
from team_member import TeamMember


class TestTeam_member(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_constructor_works(self):
        team_member_test = TeamMember("Dave Developer", "back-end Developer", 80)
        test_print = str(team_member_test)
        self.assertEqual(test_print, "Dave Developer, role of back-end Developer, no listed skills, with internal hourly rate EUR 80")