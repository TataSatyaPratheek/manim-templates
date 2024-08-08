import unittest
from unittest.mock import patch
from manim import *
from add import add

class TestAddAnim(unittest.TestCase):

    @patch('manim.Scene.play')
    def test_construct(self, mock_play):
        anim = add()
        anim.construct()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Introduction(self, mock_play):
        anim = add()
        anim.Introduction()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Addition(self, mock_play):
        anim = add()
        anim.Addition()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Subtraction(self, mock_play):
        anim = add()
        anim.Subtraction()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Multiplication(self, mock_play):
        anim = add()
        anim.Multiplication()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Division(self, mock_play):
        anim = add()
        anim.Division()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_prop(self, mock_play):
        anim = add()
        anim.prop()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_Rules(self, mock_play):
        anim = add()
        anim.Rules()
        self.assertTrue(mock_play.called)

    @patch('manim.Scene.play')
    def test_ending(self, mock_play):
        anim = add()
        anim.ending()
        self.assertTrue(mock_play.called)

if __name__ == "__main__":
    unittest.main()
