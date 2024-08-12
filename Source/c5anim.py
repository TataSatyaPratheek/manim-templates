# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from AbstractAnim import AbstractAnim
import cvo

class C5Anim(AbstractAnim):
    
    def construct(self):
        # Create the CVO objects
        p10 = cvo.CVO().CreateCVO("Person", "John Doe")
        p11 = cvo.CVO().CreateCVO("Age", "36")
        p12 = cvo.CVO().CreateCVO("In Words", "Thirty Six")
        p13 = cvo.CVO().CreateCVO("Gender", "Male")
        p14 = cvo.CVO().CreateCVO("Height", "5'9\"")

        # Establish relationships (parent-child)
        p11.cvolist.append(p12)  # "In Words" is a child of "Age"
        
        p10.cvolist.append(p11)  # "Age" is a child of "Person"
        p10.cvolist.append(p13)  # "Gender" is a child of "Person"
        p10.cvolist.append(p14)  # "Height" is a child of "Person"
        
        # Construct the object starting with the root (Person)
        self.construct_object(p10)
        

if __name__ == "__main__":
    scene = C5Anim()
    scene.render()
