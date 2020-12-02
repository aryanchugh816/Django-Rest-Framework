# Files that contains unit tests should always be names "tests.py"
from django.test import TestCase

from app.calc import add, subtract

# Create classes for tests of different modules (In this case calc module), this inherits from "TestCase class" of django.test


class CaclTests(TestCase):

    # Each test function with start with word "test" adn nothing else or it won't run
    def test_add_numbers(self):
        "Test that two numbers are added together"
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        "Test that two numbers are subtracted"
        self.assertEqual(subtract(5, 11), 6)
