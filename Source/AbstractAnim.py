# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
import cvo
import random

class AbstractAnim(Scene):
    """
    Abstract base class for creating animations using the Manim library.
    Provides utility methods for common animation tasks.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initChoices()
        self.grpAll = VGroup()  # Initialize grpAll here
        self.grp2All = VGroup()
        self.isFadeOutAtTheEndOfThisScene = False  # Initialize the attribute here

    def initChoices(self):
        self.colorChoice = [RED, BLUE, GREEN, PURPLE, ORANGE, YELLOW, LIGHT_PINK, WHITE, LIGHT_GRAY, LIGHT_BROWN, PINK, GRAY_BROWN]
        self.shapeChoice = [Circle, Triangle, Square, Rectangle]
        self.positionChoice = []
        self.angleChoice = [TAU / 5, TAU / 4, TAU / 3, TAU / 2, -TAU / 5, -TAU / 4, -TAU / 3, -TAU / 2]
        self.isRandom = True

    def setNumberOfCirclePositions(self, numberOfCircles: int):
        self.positionChoice = self.calculate_positions(numberOfCircles)

    def setNumberOfAngleChoices(self, numberOfAngles: int):
        self.angleChoice = self.calculate_angles(numberOfAngles)

    def construct(self):
        pass

    def setup(self):
        self.initChoices()

    def calculate_positions(self, number):
        positions = []
        for i in range(number):
            positions.append(self.get_dynamic_position())
        return positions

    def calculate_angles(self, number):
        angles = []
        for i in range(number):
            angles.append(self.get_dynamic_angle_choice())
        return angles

    def get_dynamic_position(self):
        return [random.uniform(-self.camera.frame_width / 2, self.camera.frame_width / 2),
                random.uniform(-self.camera.frame_height / 2, self.camera.frame_height / 2), 0]

    def get_dynamic_angle_choice(self):
        return random.uniform(-TAU / 2, TAU / 2)

    def get_dynamic_color_choice(self):
        return random.choice(self.colorChoice)

    def adjust_shape_size(self, shape, text):
        """
        Adjust the shape size to ensure the text fits inside.
        """
        text_width = text.width
        text_height = text.height
        if isinstance(shape, Ellipse):
            shape.width = text_width + 0.5
            shape.height = text_height + 0.5
        else:  # Circle
            shape.radius = max(text_width, text_height) / 2 + 0.25
        return shape

    def construct1(self, cvo, cvoParent):
        cvo.color = self.get_dynamic_color_choice()
        cvo.pos = cvo.pos or self.get_dynamic_position()

        # Create a circle or ellipse depending on `isEllipse` flag
        shape = Ellipse(width=cvo.circle_radius, height=3, color=cvo.color) if cvo.isEllipse else Circle(radius=cvo.circle_radius, color=cvo.color)
        star = Star(outer_radius=0.1, inner_radius=0.05, color=cvo.color).move_to(shape.get_center())

        c1nameposition = cvo.c1nameposition or shape.get_top()
        cname = MathTex(cvo.cname, color=cvo.color).move_to(c1nameposition).shift(UP * 0.25) if cvo.IsMathText else Tex(cvo.cname, color=cvo.color).move_to(c1nameposition).shift(UP * 0.25)

        o1nameposition = cvo.o1nameposition or star.get_top()
        oname = MathTex(cvo.oname, color=cvo.color).move_to(o1nameposition).shift(UP * 0.15) if cvo.IsMathText else Tex(cvo.oname, color=cvo.color).move_to(o1nameposition).shift(UP * 0.15)

        shape = self.adjust_shape_size(shape, cname)

        self.play(Create(shape, run_time=cvo.duration), Create(cname, run_time=cvo.duration))

        if not cvo.onameList:
            self.play(Create(oname), Create(star))
            grp1 = VGroup(shape, star, cname, oname)
        else:
            grp1 = VGroup(shape, cname)

        grp1.move_to(cvo.pos).shift(UP * 0.16)
        if cvo != cvoParent:
            arrow1 = CurvedArrow(cvoParent.pos, cvo.pos, angle=self.get_dynamic_angle_choice(), stroke_width=1.5)
            arrow1.tip.scale(0.75)
            if not cvo.onameList:
                self.play(Create(arrow1), run_time=cvo.duration)

        for index in range(len(cvo.onameList)):
            starLocal = Star(outer_radius=0.1, inner_radius=0.05, color=cvo.color).move_to(shape.get_top()).shift(LEFT * 0.35, DOWN * 0.25 * (index + 1)).scale(0.5)
            onameLocalText = Tex(cvo.onameList[index], color=cvo.color).scale(0.35).next_to(starLocal).shift(LEFT * 0.20)
            arrow2 = CurvedArrow(cvoParent.pos, starLocal.get_center(), angle=self.get_dynamic_angle_choice(), stroke_width=0.5, tip_length=0.1)
            self.play(Create(starLocal), Create(onameLocalText))
            self.play(onameLocalText.animate.scale(2.0), run_time=1)
            self.play(onameLocalText.animate.scale(0.6).next_to(starLocal).shift(LEFT * 0.20), run_time=1)
            if cvo != cvoParent:
                self.play(Create(arrow2))

        cvo.cnameMObject = cname
        cvo.onameMObject = oname
        self.grpAll.add(grp1)

        if self.isFadeOutAtTheEndOfThisScene:
            self.play(self.grpAll.animate.scale(0))

    def fadeOutCurrentScene(self):
        animations = [FadeOut(mobject) for mobject in self.mobjects]
        if animations:
            self.play(*animations)
        self.initChoices()

    def RenderSkillbancLogo(self):
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI / 2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT * 3),
            Circle(radius=1).rotate(PI / 2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI / 2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT * 3)
        )
        circle1, circle2, circle3 = self.circles

        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU / 4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU / 4)
        )

        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)

        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0), run_time=1)

    def GithubSourceCodeReference(self):
        self.PurchaseSkillbancSubscription()
        self.fadeOutCurrentScene()
        self.SubscribeYoutube()
        self.SetDeveloperList()
        self.SetSourceCodeFileName()

        self.colorChoice = [BLUE, ORANGE, PINK, ORANGE, PURPLE]
        p2 = cvo.CVO().CreateCVO("SOURCE CODE FOR THIS VIDEO", "").setPosition(self.get_dynamic_position())
        p4 = cvo.CVO().CreateCVO("Github URL", "https://github.com/Skillbanc/manim-templates").setPosition(self.get_dynamic_position()).setangle(self.get_dynamic_angle_choice())
        p5 = cvo.CVO().CreateCVO("File Name", self.GetSourceCodeFileName()).setPosition(self.get_dynamic_position()).setangle(self.get_dynamic_angle_choice())
        p6 = cvo.CVO().CreateCVO("Architected By", "Sudhakar Moparthy").setPosition(self.get_dynamic_position()).setangle(self.get_dynamic_angle_choice())
        p7 = cvo.CVO().CreateCVO("Developed By", self.GetDeveloperList()).setPosition(self.get_dynamic_position()).setangle(self.get_dynamic_angle_choice())

        p2.appendOname(p2.cname)
        p2.appendOname(p4.cname + " : " + p4.oname)
        p2.appendOname(p5.cname + " : " + p5.oname)
        p2.appendOname(p6.cname + " : " + p6.oname)
        p2.appendOname(p7.cname + " : " + p7.oname)
        p2.setduration(0.5)
        self.construct2(p2, p2)

    def SubscribeYoutube(self):
        button = RoundedRectangle(corner_radius=0.2, height=1, width=3)
        button.set_fill(PURE_RED, opacity=1)
        button.set_stroke(WHITE, width=2)

        subscribe_text = Text("Subscribe", font_size=36, color=WHITE, font="calibri")
        subscribe_text.move_to(button.get_center())

        subscribe_button = VGroup(button, subscribe_text).move_to(self.get_dynamic_position())

        self.play(GrowFromCenter(subscribe_button))
        self.wait(0.2)

    def PurchaseSkillbancSubscription(self):
        self.colorChoice = [BLUE, ORANGE, PINK, ORANGE, PURPLE]
        self.angleChoice = [-TAU / 3]
        p1 = cvo.CVO().CreateCVO("Need Help?", "We are here to support").setPosition(self.get_dynamic_position())
        p1.setduration(1)
        p1.setcircleradius(5.5)
        p2 = cvo.CVO().CreateCVO("Get Skillbanc Subscription", "https://skillbanc.com/SBstore").setPosition(self.get_dynamic_position())
        p2.setduration(1)
        p2.setcircleradius(7)
        p1.cvolist.append(p2)

        self.setNumberOfCirclePositions(2)
        self.construct5(p1, p1)
        self.play(self.grp2All.animate.scale(1.1))
        self.play(self.grp2All.animate.scale(0.9))

    def GetDeveloperList(self):
        return self.DeveloperList

    def GetSourceCodeFileName(self):
        return self.SourceCodeFileName

    def SetSourceCodeFileName(self):
        pass

    def SetDeveloperList(self):
        pass

    def construct2(self, p10, cvoParent):
        text0 = Tex(p10.onameList[0], color=BLUE)
        text01 = Tex(p10.onameList[0], color=BLUE)

        self.play(Create(text0), run_time=p10.duration)
        grp1 = VGroup(text01)

        for i in range(1, len(p10.onameList)):
            text1 = MathTex(p10.onameList[i], color=BLUE) if p10.IsMathText else Tex(p10.onameList[i], color=BLUE)
            text01 = MathTex(p10.onameList[i], color=BLUE) if p10.IsMathText else Tex(p10.onameList[i], color=BLUE)

            self.play(grp1.animate.shift(UP * 1), run_time=p10.duration)
            self.play(ReplacementTransform(text0, text1), run_time=p10.duration)

            grp1.add(text01)
            text0 = text1

        self.wait(2)

    def construct5(self, cvo, cvoParent):
        colorChoiceIndex = random.randint(0, len(self.colorChoice) - 1) if self.isRandom else 0
        cvo.color = self.colorChoice[colorChoiceIndex]

        positionChoiceIndex = self.get_dynamic_position() if self.isRandom else 0
        if cvo.pos is None:
            cvo.pos = self.positionChoice[positionChoiceIndex]

        shape = Ellipse(width=cvo.circle_radius, height=3, color=self.colorChoice[colorChoiceIndex])
        star = Star(outer_radius=0.1, inner_radius=0.05, color=self.colorChoice[colorChoiceIndex]).move_to(shape.get_center())

        c1nameposition = cvo.c1nameposition or shape.get_top()
        cname = MathTex(cvo.cname, color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25) if cvo.IsMathText else Tex(cvo.cname, color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25)

        o1nameposition = cvo.o1nameposition or star.get_top()
        oname = MathTex(cvo.oname, color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).shift(UP * 0.15) if cvo.IsMathText else Tex(cvo.oname, color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).shift(UP * 0.15)

        shape = self.adjust_shape_size(shape, cname)

        self.add(shape, cname)
        grp2 = VGroup(shape, cname)

        if not cvo.onameList:
            self.add(oname, star)
            grp2.add(star, oname)

        grp2.move_to(cvo.pos).shift(UP * 0.16)

        if cvo != cvoParent:
            angleChoiceIndex = random.randint(0, len(self.angleChoice) - 1) if self.isRandom else 0
            cvo.angle = self.angleChoice[angleChoiceIndex]

            arrow1 = CurvedArrow(cvoParent.pos, cvo.pos, angle=cvo.angle, stroke_width=1.5)
            arrow1.tip.scale(0.75)
            if not cvo.onameList:
                self.add(arrow1)
                grp2.add(arrow1)

        for index in range(len(cvo.onameList)):
            starLocal = Star(outer_radius=0.1, inner_radius=0.05, color=self.colorChoice[colorChoiceIndex]).move_to(shape.get_top()).shift(LEFT * 0.35, DOWN * 0.25 * (index + 1))
            onameLocalText = Tex(cvo.onameList[index], color=self.colorChoice[colorChoiceIndex]).scale(0.35).next_to(starLocal).shift(LEFT * 0.20)
            arrow2 = CurvedArrow(cvoParent.pos, starLocal.get_center(), angle=cvo.angle, stroke_width=0.5, tip_length=0.1)
            self.add(starLocal, onameLocalText, arrow2)

        cvo.cnameMObject = cname
        cvo.onameMObject = oname

        if cvo.pos in self.positionChoice:
            self.positionChoice.remove(cvo.pos)

        if cvo != cvoParent:
            if cvo.angle in self.angleChoice:
                self.angleChoice.remove(cvo.angle)

        if cvo.color in self.colorChoice:
            self.colorChoice.remove(cvo.color)

        if len(cvo.cvolist) > 0:
            for idx in range(len(cvo.cvolist)):
                self.construct5(cvo.cvolist[idx], cvo)

        self.grp2All.add(grp2)

        self.wait(1)
