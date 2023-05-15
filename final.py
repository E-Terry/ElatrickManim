from manim import *
from math import *

class Testing(Scene):
    def construct(self):

        k= ValueTracker(2.12)
        num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))

        self.play(Create(num))
        self.wait()
        self.play(k.animate.set_value(0))

class testing2(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        label = Dot(radius=1,color=BLUE).add_updater(
            lambda x : x.set_x(tracker.get_value())
            )
        self.add(label)
        self.add(tracker)
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)

class testing3(Scene):
    def construct(self):

        eName2 = MathTex("e^{-}", font_size=50).shift(LEFT*2)
        circle3 = Circle(color=BLUE, fill_opacity=0.2).surround(eName2, buffer_factor=1.5)
        startSize1 = circle3.width
        e1 = VMobject()
        e1.add(eName2, circle3)

        pName2 = MathTex("p^{+}", font_size=50).shift(RIGHT*2)
        circle4 = Circle(color=RED, fill_opacity=0.2).surround(pName2)
        circle4.width = startSize1
        p1 = VMobject()
        p1.add(pName2, circle4)
 
        x1=ValueTracker(2)
        x2=ValueTracker(-2)
        e1.add_updater(lambda z: z.set_x(x1.get_value()))
        p1.add_updater(lambda z: z.set_x(x2.get_value()))

        b = Brace(Line(e1.get_center(),p1.get_center()), color=GREEN, buff=0.6)
        b.add_updater(lambda z: z.become(Brace(Line(e1.get_center(),p1.get_center()), color=GREEN, buff=0.6)))
        distance = str("r")
        bText = b.get_text(distance).add_updater(lambda z: z.become(b.get_text(distance).set_color(GREEN)))
        
        def getDistVal():
            return abs(e1.get_center()[0] - p1.get_center()[0])
        
        distTex = always_redraw(lambda : MathTex(str(round(getDistVal(),2))+ r"\mu m").to_edge(UR))
        
        
        self.add(distTex)
        self.add(e1, p1, b, bText)
        self.play(x1.animate.set_value(5))
        self.play(x2.animate.set_value(-3))
        self.wait()




