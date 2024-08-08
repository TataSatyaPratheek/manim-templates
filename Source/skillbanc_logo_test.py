import unittest
from unittest.mock import patch
from skillbanc_logo import Skillbanclogo, EllipseWithStars

class TestSkillbancLogo(unittest.TestCase):

    @patch('manim.Scene.play')
    def test_construct(self, mock_play):
        anim = Skillbanclogo()
        anim.construct()
        self.assertTrue(mock_play.called, "play() was not called during construct()")

    @patch('manim.Scene.play')
    def test_RenderSkillbancLogo(self, mock_play):
        anim = Skillbanclogo()
        anim.RenderSkillbancLogo()
        self.assertTrue(mock_play.called, "play() was not called during RenderSkillbancLogo()")

    def test_EllipseWithStars(self):
        num_circles = 5
        ellipse_with_stars = EllipseWithStars(num_circles)
        self.assertEqual(len(ellipse_with_stars.circles), num_circles, "Number of circles in EllipseWithStars is incorrect")

if __name__ == '__main__':
    unittest.main()
