# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *

class CVO:
    """
    Class for creating and managing CVO (Custom Visualization Objects).
    """

    def __init__(self):
        self.c1nameposition = None
        self.o1nameposition = None
        self.oname = ""
        self.cname = ""
        self.circle_radius = 1
        self.circle_color = BLUE
        self.cvolist = []
        self.pos = None
        self.angle = TAU / 4
        self.duration = 1
        self.cnameMObject = None
        self.onameMObject = None
        self.onameList = []
        self.IsMathText = False
        self.speech = ""
        self.isEllipse = False

    def setPosition(self, pos):
        """
        Sets the position of the CVO.
        
        Args:
            pos (list): A list of three coordinates [x, y, z].
        
        Returns:
            CVO: The CVO object with the updated position.
        """
        self.pos = pos
        return self

    def setangle(self, angle):
        """
        Sets the angle of the CVO.
        
        Args:
            angle (list): A list of angles.
        
        Returns:
            CVO: The CVO object with the updated angle.
        """
        self.angle = angle
        return self

    def setc1nameposition(self, c1nameposition):
        """
        Sets the position for the first name of the CVO.
        
        Args:
            c1nameposition (list): Position for the first name.
        
        Returns:
            CVO: The CVO object with the updated first name position.
        """
        self.c1nameposition = c1nameposition
        return self

    def seto1nameposition(self, o1nameposition):
        """
        Sets the position for the second name of the CVO.
        
        Args:
            o1nameposition (list): Position for the second name.
        
        Returns:
            CVO: The CVO object with the updated second name position.
        """
        self.o1nameposition = o1nameposition
        return self

    def setduration(self, duration):
        """
        Sets the duration for the CVO.
        
        Args:
            duration (int): Duration for the CVO.
        
        Returns:
            CVO: The CVO object with the updated duration.
        """
        self.duration = duration
        return self

    def appendOname(self, oname):
        """
        Appends a name to the CVO.
        
        Args:
            oname (str): Name to append.
        
        Returns:
            CVO: The CVO object with the appended name.
        """
        self.onameList.append(oname)
        return self

    def extendOname(self, oname):
        """
        Extends the name list of the CVO.
        
        Args:
            oname (list): List of names to extend.
        
        Returns:
            CVO: The CVO object with the extended name list.
        """
        self.onameList.extend(oname)
        return self

    def extendcvo(self, cvoobj):
        """
        Extends the CVO list.
        
        Args:
            cvoobj (CVO): CVO object to extend.
        
        Returns:
            CVO: The CVO object with the extended CVO list.
        """
        self.cvolist.extend(cvoobj)

    def setcircleradius(self, radius):
        """
        Sets the circle radius for the CVO.
        
        Args:
            radius (float): Circle radius.
        
        Returns:
            CVO: The CVO object with the updated circle radius.
        """
        self.circle_radius = radius

    def SetIsMathText(self, b):
        """
        Sets whether the text is math text.
        
        Args:
            b (bool): Boolean flag indicating math text.
        
        Returns:
            CVO: The CVO object with the updated math text flag.
        """
        self.IsMathText = b
        return self

    def CreateCVO(self, cname, oname):
        """
        Creates a new CVO object with the specified name and content.
        
        Args:
            cname (str): Name of the CVO.
            oname (str): Content of the CVO.
        
        Returns:
            CVO: The created CVO object.
        """
        self.__init__()
        self.cname = cname
        self.oname = oname
        return self
