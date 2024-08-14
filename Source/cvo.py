from manim import *

class CVO:
    def __init__(self):
        self.c1nameposition = None
        self.o1nameposition = None
        self.pos = None
        self.angle = TAU / 4
        self.duration = 1
        self.circle_radius = 0.5
        self.circle_color = BLUE
        self.cname = ""
        self.oname = ""
        self.cvolist = []
        self.cnameMObject = None
        self.onameMObject = None
        self.onameList = []
        self.IsMathText = False
        self.isEllipse = False

    def setPosition(self, pos):
        self.pos = pos
        return self

    def setangle(self, angle):
        self.angle = angle
        return self

    def setc1nameposition(self, c1nameposition):
        self.c1nameposition = c1nameposition
        return self

    def seto1nameposition(self, o1nameposition):
        self.o1nameposition = o1nameposition
        return self

    def setduration(self, duration):
        self.duration = duration
        return self

    def appendOname(self, oname):
        self.onameList.append(oname)
        return self

    def extendOname(self, oname):
        self.onameList.extend(oname)
        return self

    def extendcvo(self, cvoobj):
        self.cvolist.extend(cvoobj)
        return self

    def setcircleradius(self, radius):
        self.circle_radius = radius
        return self

    def SetIsMathText(self, b):
        self.IsMathText = b
        return self

    def CreateCVO(self, cname, oname):
        self.__init__()  # Reinitialize to reset values
        self.cname = cname
        self.oname = oname
        return self

    def adjust_shape_for_text(self):
        """Adjust the shape to an ellipse if the text exceeds the radius."""
        # Create temporary text objects to measure their size
        cname_obj = MathTex(self.cname) if self.IsMathText else Tex(self.cname)
        oname_obj = MathTex(self.oname) if self.IsMathText else Tex(self.oname)

        # Calculate the required width for the ellipse based on the text width
        required_width = max(cname_obj.width, oname_obj.width) + 0.5  # Add padding

        # If the required width exceeds the circle's diameter, switch to an ellipse
        if required_width > 2 * self.circle_radius:
            self.isEllipse = True
            self.ellipse_width = required_width
            self.ellipse_height = 2 * self.circle_radius

    def position_text(self):
        """Position the text over and below the star within the figure."""
        # Star position at the center of the circle/ellipse
        star_position = self.pos

        # Position the object name (oname) over the star
        self.o1nameposition = star_position + UP * 0.01

        # Position the center name (cname) below the star
        self.c1nameposition = star_position + DOWN * 0.01
