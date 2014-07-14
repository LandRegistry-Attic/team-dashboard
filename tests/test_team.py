import team
import mock
import unittest

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team()

    def test_get_property_calls_api(self):

