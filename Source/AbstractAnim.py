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
    max_adjustments = 100  # Limit for position adjustments to prevent infinite loops

    def initChoices(self):
        """Initialize choices for colors and shapes."""
        self.colorChoice = [RED, BLUE, GREEN, PURPLE, ORANGE, YELLOW, LIGHT_PINK, WHITE, LIGHT_GRAY, LIGHT_BROWN, PINK, GRAY_BROWN]

    def determine_position(self, index, num_children, parent_pos, parent_size, min_distance=2, max_distance=8):
        """
        Determine the position of a child based on the parent position and the number of children,
        ensuring it stays within screen bounds and doesn't overlap with other objects.
        """
        angle_step = TAU / num_children
        angle = index * angle_step  # Distribute evenly around the parent
        distance = min_distance + parent_size  # Start with minimum distance plus the parent size

        # Dynamically adjust distance to ensure child stays within screen bounds and doesn't overlap
        for _ in range(self.max_adjustments):
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
        adjustments_made = 0
        for obj in objects:
            while adjustments_made < self.max_adjustments:
                obj_position = obj.get_center()  # Get the object's center position
                if self.is_within_bounds_position(obj_position) and not self.check_any_overlap(obj):
                    break  # If within bounds and no overlap, no need to shift

                # Calculate the shift direction
                shift_vector = np.array([random.uniform(-1, 1), random.uniform(-1, 1), 0])
                obj.shift(shift_vector * 0.2)  # Shift in the direction to bring it within bounds
                adjustments_made += 1

            if adjustments_made >= self.max_adjustments:
                print("Warning: Max adjustments reached for positioning.")

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
        while text.width > shape.width * 0.75 or text.height > shape.height * 0.75:
            # Reduce text size if it's wider or taller than 75% of the shape's dimensions
            text.scale(0.9)
            text.move_to(shape.get_center())  # Center the text in the shape

    def construct_object(self, cvo, cvoParent=None, calculate_only=False):
        """Construct the animation for an object and its parent, ensuring dynamic positioning."""
        colorChoiceIndex = random.randint(0, len(self.colorChoice) - 1) if self.isRandom else 0
        cvo.color = self.colorChoice[colorChoiceIndex]

        # Automatically determine position if parent exists and this is a child
        if cvoParent:
            num_children = len(cvoParent.cvolist)
            index = cvoParent.cvolist.index(cvo)
            parent_size = cvoParent.circle_radius if not cvoParent.isEllipse else cvoParent.circle_radius * 1.5
            cvo.pos = self.determine_position(index, num_children, cvoParent.pos, parent_size)
        else:
            # Determine a dynamic position for the parent based on screen space and children
            num_children = len(cvo.cvolist)
            cvo.pos = self.determine_initial_parent_position(num_children)

        # Create the circle or ellipse based on the text length
        cir1 = Circle(radius=cvo.circle_radius, color=self.colorChoice[colorChoiceIndex]).move_to(cvo.pos)
        star = Star(outer_radius=0.1, inner_radius=0.05, color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())

        # Positions for object name and center name
        nameposition_scale = 1.2
        c1nameposition = star.get_center() + UP * (1.1 * cvo.circle_radius * nameposition_scale)
        cname = MathTex(cvo.cname, color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition) if cvo.IsMathText else Tex(cvo.cname, color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition)
        cname.scale(0.55)  # Make the center name larger
        o1nameposition = star.get_center() + DOWN * (1.1 * cvo.circle_radius * nameposition_scale) 
        oname = MathTex(cvo.oname, color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition) if cvo.IsMathText else Tex(cvo.oname, color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition)
        oname.scale(0.5)  # Make the center name smaller

        # Check if text fits inside the circle; if not, convert to an ellipse
        max_text_width = max(cname.width, oname.width)
        max_text_height = max(cname.height, oname.height)
        circle_diameter = cvo.circle_radius * 2
        text_scale_factor = 0.75  # Scale factor for text to fit inside circle
        if max_text_width > circle_diameter * text_scale_factor or max_text_height > circle_diameter * text_scale_factor:  # 75% of circle's dimensions
            # Adjust to ellipse to fit the text
            ellipse_width = max_text_width / text_scale_factor  # Set width so text fits inside ellipse
            ellipse_height = 2 * max_text_height / text_scale_factor  # Set height so text fits inside ellipse
            cir1 = Ellipse(width=ellipse_width, height=ellipse_height, color=self.colorChoice[colorChoiceIndex]).move_to(cvo.pos)
            star.move_to(cir1.get_center())  # Reposition the star to the center of the ellipse

            # Adjust text positions again after changing to ellipse
            c1nameposition = star.get_center() + UP * (0.75 * cir1.height * nameposition_scale)
            o1nameposition = star.get_center() + DOWN * (0.75 * cir1.height * nameposition_scale) 
            cname.move_to(c1nameposition)
            oname.move_to(o1nameposition)

        # Set the Manim objects for later use
        cvo.cnameMObject = cname
        cvo.onameMObject = oname
        cvo.starMObject = star

        if calculate_only:
            return [cname, oname, star, cir1]  # Return these for later adjustment

        # Ensure that all elements fit within the screen bounds and do not overlap
        self.adjust_positions_to_fit([cvo.cnameMObject, cvo.onameMObject, star, cir1])

        # Initial creation of the main object
        self.play(Create(cir1, run_time=cvo.duration), Create(star, run_time=cvo.duration), Create(cname, run_time=cvo.duration), Create(oname, run_time=cvo.duration))

        grp1 = VGroup(cir1, star, cname, oname)
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
            self.construct_object(child, cvo, calculate_only)

        # Final adjustment of all objects to ensure they fit within the screen bounds
        self.adjust_positions_to_fit(self.grpAll)

    def prepare_scene(self, cvo):
        """
        Prepares the entire scene by calculating all positions first, 
        ensuring that no overlaps occur and all elements fit within the screen.
        """
        # Step 1: Calculate positions for all objects recursively without rendering
        self.construct_object(cvo, calculate_only=True)

        # Step 2: Adjust positions to avoid overlaps and fit within bounds
        self.adjust_positions_to_fit(self.grpAll)

        # Step 3: Render the scene
        self.construct_object(cvo)
