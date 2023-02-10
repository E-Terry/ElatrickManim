from manim import *

class Testing(Scene):
    def construct(self):

        k= ValueTracker(2.12)
        num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))

        self.play(Create(num))
        self.wait()
        self.play(k.animate.set_value(0))