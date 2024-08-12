from manim import *
from AbstractAnim import AbstractAnim
import cvo

class C4Anim(AbstractAnim):
    def construct(self):
        # Level 0: Create the root CVO object (Person)
        p10 = cvo.CVO().CreateCVO("Person", "John Doe")

        # Level 1: Child CVO objects (Age)
        p11 = cvo.CVO().CreateCVO("Age", "36")
        p10.cvolist.append(p11)

        # Level 2: Grandchild CVO object (In Words)
        p12 = cvo.CVO().CreateCVO("In Words", "Thirty Six")
        p11.cvolist.append(p12)

        # Level 2: Another child CVO object (Gender)
        p13 = cvo.CVO().CreateCVO("Gender", "Male")
        p10.cvolist.append(p13)

        # Create the main object and its children with dynamic adjustment to avoid overlaps
        self.construct_object(p10)

if __name__ == "__main__":
    scene = C4Anim()
    scene.render()
