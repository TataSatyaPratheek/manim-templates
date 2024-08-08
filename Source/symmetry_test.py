import unittest
from unittest.mock import patch
from symmetry import SymmetryAnim3

class TestSymmetryAnim3(unittest.TestCase):

    @patch('manim.Scene.play')
    def test_construct(self, mock_play):
        anim = SymmetryAnim3()
        anim.construct()
        self.assertTrue(mock_play.called, "play() was not called during construct()")

    @patch('manim.Scene.play')
    def test_constructDataByCVO(self, mock_play):
        anim = SymmetryAnim3()
        anim.constructDataByCVO()
        self.assertTrue(mock_play.called, "play() was not called during constructDataByCVO()")

    @patch('manim.Scene.play')
    def test_lineandrot(self, mock_play):
        anim = SymmetryAnim3()
        anim.lineandrot()
        self.assertTrue(mock_play.called, "play() was not called during lineandrot()")

    @patch('manim.Scene.play')
    def test_linesymmetry(self, mock_play):
        anim = SymmetryAnim3()
        anim.linesymmetry()
        self.assertTrue(mock_play.called, "play() was not called during linesymmetry()")

    @patch('manim.Scene.play')
    def test_rotsymmetry(self, mock_play):
        anim = SymmetryAnim3()
        anim.rotsymmetry()
        self.assertTrue(mock_play.called, "play() was not called during rotsymmetry()")

    @patch('manim.Scene.play')
    def test_ExamplesLR(self, mock_play):
        anim = SymmetryAnim3()
        anim.ExamplesLR()
        self.assertTrue(mock_play.called, "play() was not called during ExamplesLR()")

    @patch('manim.Scene.play')
    def test_ExamplesLine(self, mock_play):
        anim = SymmetryAnim3()
        anim.ExamplesLine()
        self.assertTrue(mock_play.called, "play() was not called during ExamplesLine()")

    @patch('manim.Scene.play')
    def test_ExamplesRot(self, mock_play):
        anim = SymmetryAnim3()
        anim.ExamplesRot()
        self.assertTrue(mock_play.called, "play() was not called during ExamplesRot()")

if __name__ == '__main__':
    unittest.main()
