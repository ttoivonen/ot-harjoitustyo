import unittest
from entities.project import Project

class TestProject(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_constructor_works(self):
        test_project = Project("Project Hazard", "Company Oy", "User Acceptance Testing", 100)
        prnt_project = str(test_project)
        self.assertEqual(prnt_project, "Project Hazard for customer Company Oy with objective of User Acceptance Testing")

if __name__ == '__main__':
    
    unittest.main()