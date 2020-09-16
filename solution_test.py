import model
import unittest


class SolutionTest(unittest.TestCase):

    def test_answer_at_the_beginning_no_factor_is_selected(self):
        s = model.Solution()
        self.assertEqual([False] * 16, s.answer)  # expected, actual

    def test_answer_after_selecting_factor_0_factor_0_is_selected(self):
        s = model.Solution()
        s.toggle_factor(0)
        self.assertTrue(s.answer[0])
        self.assertFalse(s.answer[1])

    def test_random_exercise_with_16_random_factors(self):
        f = model.Solution().exercise[1]
        self.assertEqual(len(f), 16)
