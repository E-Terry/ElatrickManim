from manim import *

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
        d1 = Dot(color=BLUE).shift(RIGHT*2)
        d2 = Dot(color=RED)
        tracker = ValueTracker(d1.get_center())
        ln = Line(d1.get_center(), d2.get_center())
        all = VMobject()
        all.add(d2, ln)
        all.add_updater(
            lambda x: x.set_x(tracker.get_value())
            )

        self.add(d1,all,tracker)
        self.wait()
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait()