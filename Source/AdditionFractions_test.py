import unittest
from AdditionFractions import Addition

class TestAddition(unittest.TestCase):

    def test_AdditionOfFractions(self):
        anim = Addition()
        anim.AdditionOfFractions()
        # Verify expected behaviors here, such as the presence of certain objects on the scene

    def test_AddSymbol(self):
        anim = Addition()
        anim.AddSymbol()
        # Verify expected behaviors here, such as the presence of the "+" symbol

    def test_AddOfFractionExp2(self):
        anim = Addition()
        anim.AddOfFractionExp2()
        # Verify expected behaviors here, such as the presence of certain objects on the scene

    def test_EquallSym(self):
        anim = Addition()
        anim.EquallSym()
        # Verify expected behaviors here, such as the presence of the "=" symbol

    def test_AddOfFractionExp3(self):
        anim = Addition()
        anim.AddOfFractionExp3()
        # Verify expected behaviors here, such as the presence of certain objects on the scene

    def test_construct(self):
        anim = Addition()
        anim.construct()
        # Verify expected behaviors here, such as the full construction of the scene

if __name__ == "__main__":
    unittest.main()
