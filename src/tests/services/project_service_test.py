import unittest
from entities.project_phase import Phase
from entities.team_member import TeamMember
from services.project_service import ProjectService
from entities.project import Project

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.service_test = ProjectService()
        name_test = "Software design"
        customer_test = "Company Oy"
        description_test = "Plan a software"
        hourly_rate_test = 100
      
        self.service_test.create_project(name_test, customer_test, description_test, hourly_rate_test)

    def test_create_project(self):
        name_test = "Software design"
        customer_test = "Company Oy"
        description_test = "Plan a software"
        hourly_rate_test = 100

        test_boolean = self.service_test.create_project(name_test, customer_test, description_test, hourly_rate_test)
        self.assertEqual(test_boolean, True)

    def test_create_team_member(self):
        tm_name_test = "Dave Daveloper"
        tm_role_test = "Developer"
        tm_int_rate_test = 50
        tm_skills_test = ["Python", "Java", "project management"]
        boolean_test_create = self.service_test.create_team_member(tm_name_test, tm_role_test, tm_int_rate_test, tm_skills_test)
        tm_headcount = len(self.service_test.active_project.team_members)
        self.assertEqual(tm_headcount, 1)
        self.assertEqual(boolean_test_create, True)
        self.assertEqual(self.service_test.print_team_members(), True)

    def test_create_project_phase(self):
        phase_description_test = "Preparation"
        boolean_test = self.service_test.create_project_phase(phase_description_test)
        phase_amount_test = len(self.service_test.active_project.project_phases)
        self.assertEqual(boolean_test, True)
        self.assertEqual(self.service_test.print_phases(), True)
        self.assertEqual(phase_amount_test, 1)

    def test_create_task(self):
        self.service_test.create_project_phase("Testing")
        self.service_test.create_team_member("Dave Developer", "Developer", 10, ["Python"])

        boolean_test = self.service_test.create_task(1, "test task", 10, 1)
        self.assertEqual(True, boolean_test)

    def test_print_tasks(self):
        self.service_test.create_project_phase("Testing")
        self.service_test.create_team_member("Dave Developer", "Developer", 10, ["Python"])
        print_ok_test = self.service_test.print_tasks()
        self.assertEqual(True, print_ok_test)

    def test_delete_task(self):
        self.service_test.create_project_phase("Testing")
        self.service_test.create_team_member("Dave Developer", "Developer", 10, ["Python"])
        self.service_test.create_task(1, "Testing", 10, 1)
        delete_ok = self.service_test.delete_task(1, 1)
        self.assertEqual(True, delete_ok)

    def test_delete_phase(self):
        self.service_test.create_project_phase("Testing")
        delete_ok = self.service_test.delete_phase(1)
        self.assertEqual(True, delete_ok)

    def test_print_project_estimate_phase(self):
        self.service_test.create_project_phase("Testing")
        self.service_test.create_team_member("Dave Developer", "Developer", 10, ["Python"])
        self.service_test.create_task(1, "Testing", 10, 1)
        print_ok = self.service_test.print_project_estimate_phase()
        self.assertEqual(True, print_ok)

    def test_save_to_xlsx(self):
        self.service_test.create_project_phase("Testing")
        self.service_test.create_team_member("Dave Developer", "Developer", 10, ["Python"])
        self.service_test.create_task(1, "Testing", 10, 1)
        saving_ok = self.service_test.save_to_xlsx("test_file")
        self.assertEqual(True, saving_ok)