import unittest
from unittest.mock import patch
from manim import *
from AboutmeAnim import AboutMe

class TestAboutMeAnim(unittest.TestCase):

    @patch('manim.Scene.play')
    def test_construct(self, mock_play):
        anim = AboutMe()
        anim.construct()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_RenderAboutMe(self, mock_play):
        anim = AboutMe()
        anim.RenderAboutMe()
        self.assertTrue(mock_play.called)

if __name__ == "__main__":
    unittest.main()
