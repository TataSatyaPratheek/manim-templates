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
