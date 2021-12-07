import unittest
from entities.project import Project
from entities.project_phase import Phase
from entities.phase_task import Task
from entities.team_member import TeamMember

class TestProject(unittest.TestCase):
    def setUp(self):
        self.test_project = Project("Project Hazard", "Company Oy", "User Acceptance Testing", 100)
        self.team_member_test = TeamMember("Pekka", "Analyst", 20)
        self.task_test = Task("test", 10, self.team_member_test)
        self.phase_test = Phase("testing")
        self.phase_test.phase_tasks.append(self.task_test)
        self.test_project.project_phases.append(self.phase_test)

    def test_constructor_works(self):
        prnt_project = str(self.test_project)
        self.assertEqual(prnt_project, "Project Hazard for customer Company Oy with objective of User Acceptance Testing")

    def test_calculate_total_hours(self):
        total_hours_test = self.test_project.calculate_total_hours()
        self.assertEqual(total_hours_test, 10)

    def test_calculate_total_ext_costs(self):
        total_ext_costs_test = self.test_project.calculate_total_ext_costs()
        self.assertEqual(total_ext_costs_test, 1000)

    def test_calculate_total_int_costs(self):
        total_int_costs_test = self.test_project.calculate_total_int_costs()
        self.assertEqual(total_int_costs_test, 200)

    def test_calculate_total_profitability(self):
        profitability_test = self.test_project.calculate_total_profitability()
        self.assertEqual(profitability_test, 800)


if __name__ == '__main__':
    
    unittest.main()