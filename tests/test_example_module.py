import unittest
from hello_world_project.example_module import add_numbers
from hello_world_project.utils import greet_user

class TestHelloWorldProject(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-5, 5), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_greet_user(self):
        self.assertIn("Alice", greet_user("Alice"))
        self.assertIn("User", greet_user(""))

if __name__ == "__main__":
    unittest.main()
