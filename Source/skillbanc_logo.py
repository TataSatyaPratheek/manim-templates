from manim import *
from AbstractAnim import AbstractAnim

class EllipseWithStars(VGroup):
    def __init__(self, num_circles, **kwargs):
        super().__init__(**kwargs)
        self.circles = [Circle(radius=1).shift(RIGHT * i) for i in range(num_circles)]
        self.add(*self.circles)

class Skillbanclogo(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()

if __name__ == "__main__":
    s = Skillbanclogo()
    s.render()
