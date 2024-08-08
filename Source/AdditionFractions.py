from manim import *

class Addition(Scene):
    def construct(self):
        self.AdditionOfFractions()
        self.AddSymbol()
        self.AddOfFractionExp2()
        self.EquallSym()
        self.AddOfFractionExp3()

    def AdditionOfFractions(self):
        radius = 1
        side_length = radius * 2
        square1 = Square(side_length=side_length)
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line1 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])
        group1 = VGroup(square1, vertical_line1, horizontal_line1)
        shaded_area1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        group1.add(shaded_area1)
        group1.shift(LEFT * 4)
        print("Calling play in AdditionOfFractions for square1, vertical_line1, horizontal_line1, shaded_area1")
        self.play(Create(square1), Create(vertical_line1), Create(horizontal_line1), Create(shaded_area1))
        text1 = Tex(r"$\frac{1}{4}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        print("Calling play in AdditionOfFractions for text1")
        self.play(Write(text1))

    def AddSymbol(self):
        add_sign = Tex("+").scale(1.5).shift(UP * 0.1 + LEFT * 2.5)
        print("Calling play in AddSymbol for add_sign")
        self.play(Write(add_sign))

    def AddOfFractionExp2(self):
        radius = 1
        side_length = radius * 2
        square2 = Square(side_length=side_length)
        vertical_line2 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line2 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])
        group2 = VGroup(square2, vertical_line2, horizontal_line2)
        shaded_area2 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        group2.add(shaded_area2)
        group2.shift(LEFT * 1)
        print("Calling play in AddOfFractionExp2 for square2, vertical_line2, horizontal_line2, shaded_area2")
        self.play(Create(square2), Create(vertical_line2), Create(horizontal_line2), Create(shaded_area2))
        text2 = Tex(r"$\frac{1}{4}$")
        text2.shift(DOWN * 2 + LEFT * 1)
        print("Calling play in AddOfFractionExp2 for text2")
        self.play(Write(text2))

    def EquallSym(self):
        equals_sign = Tex("=").scale(1.5).shift(UP * 0.1 + RIGHT * 1)
        print("Calling play in EquallSym for equals_sign")
        self.play(Write(equals_sign))

    def AddOfFractionExp3(self):
        radius = 1
        side_length = radius * 2
        square3 = Square(side_length=side_length)
        vertical_line3 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line3 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])
        group3 = VGroup(square3, vertical_line3, horizontal_line3)
        shaded_area3_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area3_2 = Polygon(
            [0, 0, 0], [0, radius, 0], [-radius, radius, 0], [-radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        group3.add(shaded_area3_1, shaded_area3_2)
        group3.shift(RIGHT * 3)
        print("Calling play in AddOfFractionExp3 for square3, vertical_line3, horizontal_line3, shaded_area3_1, shaded_area3_2")
        self.play(Create(square3), Create(vertical_line3), Create(horizontal_line3), Create(shaded_area3_1), Create(shaded_area3_2))
        text3 = Tex(r"$\frac{1}{2}$")
        text3.shift(DOWN * 2 + RIGHT * 3)
        print("Calling play in AddOfFractionExp3 for text3")
        self.play(Write(text3))

if __name__ == "__main__":
    scene = Addition()
    scene.render()
