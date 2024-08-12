# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class C6Anim(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Person","John Doe")
         p11=cvo.CVO().CreateCVO("Age","36")
         p12=cvo.CVO().CreateCVO("In Words","Thirty Six")
         p13=cvo.CVO().CreateCVO("Gender","Male")
         p14=cvo.CVO().CreateCVO("Height","5'9\"")
         p15=cvo.CVO().CreateCVO("Weight","155lb")
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         p10.cvolist.append(p15)
         
         self.construct_object(p10)
         

      
if __name__ == "__main__":
    scene = C6Anim()
    scene.render()