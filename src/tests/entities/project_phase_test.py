import unittest
from entities.project_phase import Phase
from entities.phase_task import Task
from entities.team_member import TeamMember

class TestPhase(unittest.TestCase):
    def setUp(self):
        self.phase_test = Phase("discovery")
        self.tm_test = TeamMember("Dave Developer", "Developer", 50)
        self.phase_test.phase_tasks.append(Task("draft design", 15, self.tm_test))
        self.phase_test.phase_tasks.append(Task("workshop materials", 5, self.tm_test))

    def test_constructor_works(self):
        print_test = self.phase_test.description
        self.assertEqual(print_test, "discovery")

    def test_calculate_hours(self):
        hours_test = self.phase_test.phase_hours()
        self.assertEqual(hours_test, 20)

    def test_calculate_int_costs(self):
        int_cost_test = self.phase_test.phase_int_costs()
        self.assertEqual(int_cost_test, 1000)