from manim import *
from AbstractAnim import AbstractAnim
import cvo

class RatioAndProportion(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.ratio()
        self.fadeOutCurrentScene()
        self.ratio2()
        self.fadeOutCurrentScene()
        self.equiratio()
        self.fadeOutCurrentScene()
        self.squareexample()
        self.fadeOutCurrentScene()
        self.quantityratio()
        self.fadeOutCurrentScene()
        self.proportion()
        self.fadeOutCurrentScene()
        self.proportionderivation()
        self.fadeOutCurrentScene()
        self.unitarymethod()
        self.fadeOutCurrentScene()
        self.unitaryproblem()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        text = Text("RATIO AND PROPORTION")
        self.play(Write(text))

    def ratio(self):
        text1 = Text("RATIO")
        text = Text("Ratio can be defined as the comparison between two\nnumbers of the same unit to check how bigger is one\nnumber than the other one.\n\nIt is denoted by ':' symbol.\nFor example, 2:3, 5:6, 3:7, etc.")
        text.scale(0.75)
        text1.to_edge(UP)
        self.play(Write(text1))
        self.play(Write(text), run_time=6)

    def ratio2(self):
        self.setNumberOfCirclePositions(4)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("RATIO", "A:B").setPosition(self.get_dynamic_position())
        p12 = cvo.CVO().CreateCVO("A", "Antecedent").setPosition(self.get_dynamic_position())
        p13 = cvo.CVO().CreateCVO("B", "Consequent").setPosition(self.get_dynamic_position())
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10, p10)

    def equiratio(self):
        text = Text("EQUIVALENT RATIO")
        text1 = Text("Equivalent ratios are those that can be simplified or reduced to the same value.\n\n\n the ratio 30 : 20 and 24 : 16, in lowest form are same as 3 : 2.\nThese are equivalent ratios.")
        text1.scale(0.6)
        text.to_edge(UP)
        self.play(Write(text))
        self.play(Write(text1), run_time=5)

    def squareexample(self):
        text = Text("COMPARING SHADED AND UNSHADED AREA WITH RATIO")
        text.to_edge(UP)
        text.scale(0.6)
        self.play(Write(text))
        self.wait(1)

        large_square = Square(side_length=4)
        large_square.move_to(LEFT * 4)
        small_side_length = 1
        small_squares = [Square(side_length=small_side_length) for _ in range(16)]
        positions = []
        for i in range(4):
            for j in range(4):
                x = -1.5 + j
                y = 1.5 - i
                positions.append(large_square.get_center() + np.array([x, y, 0]))

        shaded_indices = [5, 6, 9, 10]
        for idx, small_square in enumerate(small_squares):
            small_square.move_to(positions[idx])
            if idx in shaded_indices:
                small_square.set_fill(BLUE, opacity=0.5)
            else:
                small_square.set_fill(WHITE, opacity=0)

        self.add(large_square, *small_squares)
        self.wait(1)

        text1 = Text("Shaded Parts=4\n\nUnshaded Parts=12\n\nRatio= 4:12\n\nSimplest Ratio=1:3")
        text1.scale(0.5)
        self.play(text1.animate.shift(RIGHT * 3))
        self.wait(3)

    def quantityratio(self):
        text = Text("Division of a given quantity in a given ratio")
        text.scale(0.75)
        text.to_edge(UP)
        text1 = Text("A goldsmith mixes gold and copper in the ratio 7:2 to prepare an ornament.\nIf the ornament weighs 45gms, find the weight of gold and copper in it.")
        text1.scale(0.5)
        text1.shift(UP * 2)
        text2 = Text(" Ratio of gold and copper = 7: 2\n\nSum of the ratio terms = 7+2 = 9\n\nWeight of 9 parts  = 45 gm\n\nWeight of Each part   = 45 ÷ 9 = 5 gm\n\nPart of gold weighs = 7 parts × 5 gm = 35 gm\n\nPart of copper weighs = 2 parts × 5 gm = 10 gm")
        text2.scale(0.5)
        text2.shift(DOWN)
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)

    def proportion(self):
        text = Text("PROPORTION")
        text1 = Text("Proportion is an equation that defines that the two given ratios are equivalent to each other.")
        text2 = Text("In general if the ratio of 'a' and 'b' is equal to the ratio of 'c' and 'd', we say that they\nare in proportion. This is represented as a : b : : c : d.")
        text.to_edge(UP)
        text1.scale(0.5)
        text1.shift(UP)
        text2.scale(0.5)
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)

    def proportionderivation(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("PROPORTION", "A:B::C:D").setPosition(self.get_dynamic_position())
        p12 = cvo.CVO().CreateCVO("", "A/B=C/D").setPosition(self.get_dynamic_position())
        p13 = cvo.CVO().CreateCVO("", "AD=BC").setPosition(self.get_dynamic_position())
        p14 = cvo.CVO().CreateCVO("AD", "Product of Means").setPosition(self.get_dynamic_position())
        p15 = cvo.CVO().CreateCVO("BC", "Product of Extremes").setPosition(self.get_dynamic_position())
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        p13.cvolist.append(p15)
        self.construct1(p10, p10)

    def unitarymethod(self):
        text = Text("UNITARY METHOD")
        text1 = Text("The method in which we first find the value of one unit and then the value of the required\nnumber of units is known as the unitary method.")
        text.to_edge(UP)
        text1.scale(0.5)
        text1.shift(UP)
        self.play(Write(text))
        self.play(Write(text1))
        self.wait(3)

    def unitaryproblem(self):
        text = Text("UNITARY METHOD EXAMPLE")
        text1 = Text("If the cost of 12 pencils is 24, then find the cost of 10 pencils.")
        text2 = Text("First we find the cost of 1 pencil by dividing 24 by 12.\n\nCost of 12 pencils = 24\n\nCost of 1 pencil = 24 ÷ 12 = 2\n\nCost of 10 pencils = 2 × 10 = 20\n\nCost of 10 pencils is 20.")
        text.scale(0.75)
        text.to_edge(UP)
        text1.scale(0.5)
        text1.shift(UP * 2)
        text2.scale(0.5)
        text2.shift(DOWN)
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)

    def SetDeveloperList(self):
        self.DeveloperList = "SURADHYA REDDY"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "RatioAndProportion.py"

if __name__ == "__main__":
    scene = RatioAndProportion()
    scene.render()
