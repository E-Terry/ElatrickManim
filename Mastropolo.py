from manim import *

class CreateElectron(Scene):
    def construct(self):
        electronName = Tex(r"$e^{-}$", color=RED, font_size=144)
        circle1 = Circle().surround(electronName)
        circle1.set_fill(PINK, opacity=0.2)
        electron = VGroup()
        electron.add(circle1,electronName)

        coulombVal = Tex(r"$= 1.6 \times 10^{-19} \text{ Mastropolo's}$", font_size=144)
        coulombVal.next_to(electron, RIGHT, buff=0.5)
        #still needs to fit on screen


        self.play(Create(electron))
        self.play(Create(coulombVal))
