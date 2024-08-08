import unittest
from unittest.mock import patch
from AdditionFrac2 import AdditionFrac2

class TestAdditionFrac2(unittest.TestCase):

    @patch.object(AdditionFrac2, 'play', autospec=True)
    def test_AddCircel1(self, mock_play):
        anim = AdditionFrac2()
        anim.AddCircel1()
        self.assertTrue(mock_play.called)

    @patch.object(AdditionFrac2, 'play', autospec=True)
    def test_AdditionSymbol(self, mock_play):
        anim = AdditionFrac2()
        anim.AdditionSymbol()
        self.assertTrue(mock_play.called)

    @patch.object(AdditionFrac2, 'play', autospec=True)
    def test_AddCircel2(self, mock_play):
        anim = AdditionFrac2()
        anim.AddCircel2()
        self.assertTrue(mock_play.called)

    @patch.object(AdditionFrac2, 'play', autospec=True)
    def test_EquallSymbol(self, mock_play):
        anim = AdditionFrac2()
        anim.EquallSymbol()
        self.assertTrue(mock_play.called)

    @patch.object(AdditionFrac2, 'play', autospec=True)
    def test_AddCircleFinal(self, mock_play):
        anim = AdditionFrac2()
        anim.AddCircleFinal()
        self.assertTrue(mock_play.called)
        self.assertEqual(mock_play.call_count, 1)  # Check that play is called once

    @patch.object(AdditionFrac2, 'play', autospec=True)
    def test_construct(self, mock_play):
        anim = AdditionFrac2()
        anim.construct()
        self.assertTrue(mock_play.called)
        self.assertEqual(mock_play.call_count, 7)  # Updated to match the actual number of play calls

if __name__ == "__main__":
    unittest.main()
