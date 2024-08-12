from manim import *
import cvo
import random
import numpy as np

class AbstractAnim(Scene):
    """
    AbstractAnim class for creating complex animations in Manim.
    Inherits from Scene and provides common methods for subclasses.
    """

    grpAll = VGroup()
    isFadeOutAtTheEndOfThisScene = False

    colorChoice = [RED, BLUE, GREEN, PURPLE, ORANGE, YELLOW, LIGHT_PINK, WHITE, LIGHT_GRAY, LIGHT_BROWN, PINK, GRAY_BROWN]

    isRandom = True

    def initChoices(self):
        """Initialize choices for colors and shapes."""
        self.colorChoice = [RED, BLUE, GREEN, PURPLE, ORANGE, YELLOW, LIGHT_PINK, WHITE, LIGHT_GRAY, LIGHT_BROWN, PINK, GRAY_BROWN]

    def determine_position(self, index, num_children, parent_pos, min_distance=1.5, max_distance=5):
        """Determine the position of a child based on the parent position and the number of children, ensuring it stays within screen bounds."""
        angle_step = TAU / num_children
        angle = index * angle_step  # Distribute evenly around the parent
        distance = min_distance

        # Dynamically adjust distance to ensure child stays within screen bounds
        while distance <= max_distance:
            x = parent_pos[0] + distance * np.cos(angle)
            y = parent_pos[1] + distance * np.sin(angle)
            child_pos = np.array([x, y, 0])

            # Check if the position is within bounds and does not overlap with any existing Manim objects
            if self.is_within_bounds_position(child_pos) and not self.check_any_overlap_with_position(child_pos):
                return child_pos

            distance += 0.5  # Increase distance and re-check

        return child_pos  # Return the position even if at max distance

    def check_any_overlap_with_position(self, pos):
        """Check if a given position overlaps with any existing objects in the scene."""
        temp_circle = Circle(radius=0.5).move_to(pos)  # Temporary circle to test overlap
        for other_obj in self.grpAll:
            if self.check_overlap(temp_circle, other_obj):
                return True
        return False

    def determine_initial_parent_position(self, num_children):
        """Determine a dynamic initial position for the parent based on the number of children."""
        bounds = self.get_screen_bounds()

        # Start from the center of the screen
        x = 0
        y = 0

        return np.array([x, y, 0])

    def get_screen_bounds(self):
        """Get the screen boundaries for a 1080p resolution."""
        aspect_ratio = 16 / 9
        vertical_size = 8  # Manim's default frame height is 8 units for 1080p
        horizontal_size = vertical_size * aspect_ratio

        return {
            "left": -horizontal_size / 2,
            "right": horizontal_size / 2,
            "top": vertical_size / 2,
            "bottom": -vertical_size / 2,
        }

    def is_within_bounds_position(self, pos):
        """Check if a given position is within screen bounds."""
        bounds = self.get_screen_bounds()
        return (
            bounds["left"] <= pos[0] <= bounds["right"] and
            bounds["bottom"] <= pos[1] <= bounds["top"]
        )

    def adjust_positions_to_fit(self, objects):
        """Adjust positions to ensure all objects fit within screen bounds."""
        for obj in objects:
            while True:
                obj_position = obj.get_center()  # Get the object's center position
                if self.is_within_bounds_position(obj_position) and not self.check_any_overlap(obj):
                    break  # If within bounds and no overlap, no need to shift

                # Calculate the shift direction
                shift_vector = np.array([random.uniform(-1, 1), random.uniform(-1, 1), 0])
                obj.shift(shift_vector * 0.2)  # Shift in the direction to bring it within bounds

    def check_any_overlap(self, obj):
        """Check if the object overlaps with any other object in grpAll."""
        for other_obj in self.grpAll:
            if obj is not other_obj and self.check_overlap(obj, other_obj):
                return True
        return False

    def check_overlap(self, obj1, obj2) -> bool:
        """Check if two objects overlap."""
        left1, right1, top1, bottom1 = self.get_bounding_box(obj1)
        left2, right2, top2, bottom2 = self.get_bounding_box(obj2)
        return not (right1 < left2 or left1 > right2 or top1 < bottom2 or bottom1 > top2)

    def get_bounding_box(self, obj) -> tuple:
        """Get the bounding box coordinates of an object."""
        left = obj.get_left()[0]
        right = obj.get_right()[0]
        top = obj.get_top()[1]
        bottom = obj.get_bottom()[1]
        return left, right, top, bottom

    def fit_text_in_shape(self, text, shape):
        """Ensure text fits within its associated shape."""
        while text.width > shape.width * 0.8:  # Reduce text size if it's wider than 80% of the shape's width
            text.scale(0.9)
            text.move_to(shape.get_center())  # Center the text in the shape

    def construct_object(self, cvo, cvoParent=None):
        """Construct the animation for an object and its parent, ensuring dynamic positioning."""
        colorChoiceIndex = random.randint(0, len(self.colorChoice) - 1) if self.isRandom else 0
        cvo.color = self.colorChoice[colorChoiceIndex]

        # Automatically determine position if parent exists and this is a child
        if cvoParent:
            num_children = len(cvoParent.cvolist)
            index = cvoParent.cvolist.index(cvo)
            cvo.pos = self.determine_position(index, num_children, cvoParent.pos)
        else:
            # Determine a dynamic position for the parent based on screen space and children
            num_children = len(cvo.cvolist)
            cvo.pos = self.determine_initial_parent_position(num_children)

        # Create the circle, star, and text elements
        if not cvo.isEllipse:
            cir1 = Circle(radius=cvo.circle_radius, color=self.colorChoice[colorChoiceIndex]).move_to(cvo.pos)
        else:
            cir1 = Ellipse(width=cvo.circle_radius * 2.5, height=cvo.circle_radius * 1.5, color=self.colorChoice[colorChoiceIndex]).move_to(cvo.pos)
        
        star = Star(outer_radius=0.1, inner_radius=0.05, color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())

        c1nameposition = cvo.c1nameposition or cir1.get_top()
        cname = MathTex(cvo.cname, color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25) if cvo.IsMathText else Tex(cvo.cname, color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25)

        o1nameposition = cvo.o1nameposition or star.get_top()
        oname = MathTex(cvo.oname, color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).shift(UP * 0.15) if cvo.IsMathText else Tex(cvo.oname, color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).shift(UP * 0.15)

        # Ensure text fits within the shape
        self.fit_text_in_shape(cname, cir1)
        self.fit_text_in_shape(oname, cir1)

        # Set the Manim objects for later use
        cvo.cnameMObject = cname
        cvo.onameMObject = oname
        cvo.starMObject = star

        # Ensure that all elements fit within the screen bounds
        self.adjust_positions_to_fit([cvo.cnameMObject, cvo.onameMObject, star, cir1])

        # Initial creation of the main object
        self.play(Create(cir1, run_time=cvo.duration), Create(star, run_time=cvo.duration), Create(cname, run_time=cvo.duration))

        grp1 = VGroup(cir1, star, cname, oname) if not cvo.isEllipse else VGroup(cir1, cname)

        # Animate text zooming in and out
        self.play(cname.animate.scale(2.0), oname.animate.scale(2.0), run_time=1)
        self.play(cname.animate.scale(0.5), oname.animate.scale(0.3), run_time=1)

        self.grpAll.add(grp1)

        # If there's a parent object, adjust the parent position and draw an arrow from the star of the parent to the star of the child
        if cvoParent is not None:
            arrow1 = CurvedArrow(cvoParent.starMObject.get_center(), cvo.starMObject.get_center(), angle=cvo.angle, stroke_width=1.5)
            arrow1.tip.scale(0.75)
            self.play(Create(arrow1), run_time=cvo.duration)

        for obj in self.grpAll:
            self.add(obj)

        # Recursively create child objects
        for child in cvo.cvolist:
            self.construct_object(child, cvo)

        # Adjust all objects to ensure they fit within the screen bounds
        self.adjust_positions_to_fit(self.grpAll)



    def get_random_position(self) -> int:
        """Get a random position index."""
        if len(self.positionChoice) > 2:
            return random.randint(1, len(self.positionChoice) - 1)
        return 0

    def get_bounding_box(self, obj) -> tuple:
        """Get the bounding box coordinates of an object."""
        left = obj.get_left()[0]
        right = obj.get_right()[0]
        top = obj.get_top()[1]
        bottom = obj.get_bottom()[1]
        return left, right, top, bottom

    def check_overlap(self, obj1, obj2) -> bool:
        """Check if two objects overlap."""
        left1, right1, top1, bottom1 = self.get_bounding_box(obj1)
        left2, right2, top2, bottom2 = self.get_bounding_box(obj2)
        return not (right1 < left2 or left1 > right2 or top1 < bottom2 or bottom1 > top2)

    def fadeOutCurrentScene(self):
        """Fade out all objects in the current scene."""
        animations = [FadeOut(mobject) for mobject in self.mobjects]
        if animations:
            self.play(*animations)
        self.initChoices()


    def RenderSkillbancLogo(self):
        """Render the Skillbanc logo."""
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        circles = VGroup(
            Circle(radius=1).rotate(PI / 2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT * 3),
            Circle(radius=1).rotate(PI / 2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI / 2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT * 3)
        )

        lines = VGroup(
            Arrow(circles[0].get_right(), circles[1].get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circles[1].get_right(), circles[2].get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circles[0].get_top(), circles[2].get_top(), angle=-TAU / 4),
            CurvedArrow(circles[0].get_bottom(), circles[2].get_bottom(), angle=TAU / 4)
        )

        lines[0].put_start_and_end_on(circles[0].get_right(), circles[1].get_left())
        lines[1].put_start_and_end_on(circles[1].get_right(), circles[2].get_left())

        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(circles[0]), Create(circles[1]), Create(circles[2]), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        self.play(Create(text), rate_func=smooth, run_time=0.75)

        logoGroup = VGroup(circles, lines, text)
        self.play(logoGroup.animate.scale(0), run_time=1)

    def GithubSourceCodeReference(self):
        """Display GitHub source code reference."""
        self.PurchaseSkillbancSubscription()
        self.fadeOutCurrentScene()
        self.SubscribeYoutube()
        self.SetDeveloperList()
        self.SetSourceCodeFileName()

        self.colorChoice = [BLUE, ORANGE, PINK, ORANGE, PURPLE]
        p2 = cvo.CVO().CreateCVO("SOURCE CODE FOR THIS VIDEO", "").setPosition([0, 2.5, 0])
        p4 = cvo.CVO().CreateCVO("Github URL", "https://github.com/Skillbanc/manim-templates").setPosition([-4, 1, 0]).setangle(TAU / 3)
        p5 = cvo.CVO().CreateCVO("File Name", self.GetSourceCodeFileName()).setPosition([4, 1, 0]).setangle(TAU / 3)
        p6 = cvo.CVO().CreateCVO("Architected By", "Sudhakar Moparthy").setPosition([5, -2, 0]).setangle(-TAU / 4)
        p7 = cvo.CVO().CreateCVO("Developed By", self.GetDeveloperList()).setPosition([0, -2, 0]).setangle(-TAU / 4)

        p2.appendOname(p2.cname)
        p2.appendOname(f"{p4.cname} : {p4.oname}")
        p2.appendOname(f"{p5.cname} : {p5.oname}")
        p2.appendOname(f"{p6.cname} : {p6.oname}")
        p2.appendOname(f"{p7.cname} : {p7.oname}")
        p2.setduration(0.5)

        self.construct_object(p2, p2)

    def SubscribeYoutube(self):
        """Display a YouTube subscribe button."""
        button = RoundedRectangle(corner_radius=0.2, height=1, width=3)
        button.set_fill(PURE_RED, opacity=1)
        button.set_stroke(WHITE, width=2)

        subscribe_text = Text("Subscribe", font_size=36, color=WHITE, font="calibri")
        subscribe_text.move_to(button.get_center())

        subscribe_button = VGroup(button, subscribe_text).move_to(LEFT * 4 + DOWN * 2.5)
        self.play(GrowFromCenter(subscribe_button))
        self.wait(0.2)

    def PurchaseSkillbancSubscription(self):
        """Display Skillbanc subscription information."""
        self.colorChoice = [BLUE, ORANGE, PINK, ORANGE, PURPLE]
        self.angleChoice = [-TAU / 3]

        p1 = cvo.CVO().CreateCVO("Need Help?", "We are here to support").setPosition([3.5, 1, 0])
        p1.setduration(1)
        p1.setcircleradius(5.5)
        p2 = cvo.CVO().CreateCVO("Get Skillbanc Subscription", "https://skillbanc.com/SBstore").setPosition([-2.5, -1, 0])
        p2.setduration(1)
        p2.setcircleradius(7)

        p1.cvolist.append(p2)
        self.setNumberOfCirclePositions(2)
        self.construct_object(p1, p1)
        self.play(self.grp2All.animate.scale(1.1))
        self.play(self.grp2All.animate.scale(0.9))

    def GetDeveloperList(self) -> str:
        """Get the list of developers."""
        return self.DeveloperList

    def GetSourceCodeFileName(self) -> str:
        """Get the source code file name."""
        return self.SourceCodeFileName

    def SetSourceCodeFileName(self):
        """Set the source code file name. To be implemented."""
        pass

    def SetDeveloperList(self):
        """Set the developer list. To be implemented."""
        pass
