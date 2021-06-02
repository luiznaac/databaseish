import unittest
from src.action import Action


class TestAction(unittest.TestCase):

    def test_action_with_params(self):
        def function(x, y): return (x * y) == 8
        action_finished = Action(function, (2, 4))
        action_failed = Action(function, (2, 3))

        action_finished.perform()
        action_failed.perform()

        self.assertEqual('finished', action_finished.status)
        self.assertEqual('failed', action_failed.status)

    def test_action_with_succeeding_perform_final_status_should_be_finished(self):
        def function(): return True
        action = Action(function)

        action.perform()

        self.assertEqual('finished', action.status)

    def test_action_with_failing_perform_final_status_should_be_failed(self):
        def function(): return False
        action = Action(function)

        action.perform()

        self.assertEqual('failed', action.status)


if __name__ == '__main__':
    unittest.main()
