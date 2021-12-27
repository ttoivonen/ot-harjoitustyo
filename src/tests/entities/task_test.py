import unittest
from entities.project_phase import Phase
from entities.phase_task import Task
from entities.team_member import TeamMember

class TestTask(unittest.TestCase):
    def setUp(self):
        self.tm_test = TeamMember("Dave Developer", "Developer", 50)
        self.task_test = Task("draft design", 15, self.tm_test)

    def test_constructor(self):
        prnt_test = f"draft design with estimated hours 15 for team member Dave Developer"
        self.assertEqual(prnt_test, str(self.task_test))