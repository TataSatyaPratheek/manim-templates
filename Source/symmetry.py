from AbstractAnim import AbstractAnim
import cvo

class SymmetryAnim3(AbstractAnim):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.isFadeOutAtTheEndOfThisScene = True

    def construct(self):
        self.constructDataByCVO()

    def constructDataByCVO(self):
        p10 = cvo.CVO().CreateCVO("Example", "This is an example")
        self.construct1(p10, p10)

    def lineandrot(self):
        p20 = cvo.CVO().CreateCVO("Line and Rotational Symmetry", "")
        self.construct1(p20, p20)

    def linesymmetry(self):
        p14 = cvo.CVO().CreateCVO("Line Symmetry", "")
        self.construct1(p14, p14)

    def rotsymmetry(self):
        p17 = cvo.CVO().CreateCVO("Rotational Symmetry", "")
        self.construct1(p17, p17)

    def ExamplesLR(self):
        example1 = cvo.CVO().CreateCVO("Example LR", "")
        self.construct1(example1, example1)

    def ExamplesLine(self):
        example1 = cvo.CVO().CreateCVO("Example Line", "")
        self.construct1(example1, example1)

    def ExamplesRot(self):
        example1 = cvo.CVO().CreateCVO("Example Rot", "")
        self.construct1(example1, example1)
