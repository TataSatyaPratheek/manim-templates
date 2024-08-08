# AlgebraicAnim_test.py
import unittest
from manim import *
from AlgebraicAnim import AlgebraicAnim

class TestAlgebraicAnim(unittest.TestCase):
    def setUp(self):
        self.anim = AlgebraicAnim()

    def test_Introduction(self):
        self.anim.Introduction()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_Types(self):
        self.anim.Types()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_Polynomials(self):
        self.anim.Polynomials()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_linearpolynomial(self):
        self.anim.linearpolynomial()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_quadraticpolynomial(self):
        self.anim.quadraticpolynomial()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_cubicpolynomial(self):
        self.anim.cubicpolynomial()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_quarticpolynomial(self):
        self.anim.quarticpolynomial()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_quinticpolynomial(self):
        self.anim.quinticpolynomial()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_sexticpolynomial(self):
        self.anim.sexticpolynomial()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_Relations(self):
        self.anim.Relations()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_identities(self):
        self.anim.identities()
        self.assertTrue(len(self.anim.mobjects) > 0)

    def test_construct(self):
        self.anim.construct()
        self.assertTrue(len(self.anim.mobjects) > 0)

if __name__ == '__main__':
    unittest.main()
