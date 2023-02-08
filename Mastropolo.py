from manim import *

class CreateElectron(Scene):
    def construct(self):
     
        electronName = Tex(r"$e^{-}$", color=BLUE, font_size=144)
        circle1 = Circle().surround(electronName)
        circle1.set_color(BLUE)
        circle1.set_fill(BLUE_B, opacity=0.2)
        

        electron = VGroup()
        electron.add(circle1,electronName)

        self.play(Create(electron))
        self.play(electron.animate.shift(LEFT*5))

        coulombVal = Tex(r"$= -1.6 \times 10^{-19} \text{ Mastropolo's}$", font_size=144)
        coulombVal.next_to(electron, RIGHT, buff=0.5)

        self.play(Write(coulombVal))
        self.wait()
        self.play(electron.animate.to_edge(UL), coulombVal.animate.to_edge(UL))

        proton = VGroup()
        protonName = Tex(r"$p^{+}$", color=RED)
        circle2 = Circle().surround(protonName)
        circle2.set_fill(PINK, opacity=0.2)
        proton.add(protonName,circle2)
