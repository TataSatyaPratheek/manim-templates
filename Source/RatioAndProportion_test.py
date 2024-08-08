import unittest
from unittest.mock import patch
from RatioAndProportion import RatioAndProportion

class TestRatioAndProportion(unittest.TestCase):

    @patch('manim.Scene.play')
    def test_construct(self, mock_play):
        anim = RatioAndProportion()
        anim.construct()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Introduction(self, mock_play):
        anim = RatioAndProportion()
        anim.Introduction()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_ratio(self, mock_play):
        anim = RatioAndProportion()
        anim.ratio()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_ratio2(self, mock_play):
        anim = RatioAndProportion()
        anim.ratio2()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_equiratio(self, mock_play):
        anim = RatioAndProportion()
        anim.equiratio()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_squareexample(self, mock_play):
        anim = RatioAndProportion()
        anim.squareexample()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_quantityratio(self, mock_play):
        anim = RatioAndProportion()
        anim.quantityratio()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_proportion(self, mock_play):
        anim = RatioAndProportion()
        anim.proportion()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_proportionderivation(self, mock_play):
        anim = RatioAndProportion()
        anim.proportionderivation()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_unitarymethod(self, mock_play):
        anim = RatioAndProportion()
        anim.unitarymethod()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_unitaryproblem(self, mock_play):
        anim = RatioAndProportion()
        anim.unitaryproblem()
        self.assertTrue(mock_play.called)

if __name__ == '__main__':
    unittest.main()
