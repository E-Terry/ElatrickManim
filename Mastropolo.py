from manim import *

class ShowCharges(Scene):
    def construct(self):
     
        eName = Tex(r"$e^{-}$", color=BLUE, font_size=144)
        circle1 = Circle(color=BLUE, fill_opacity=0.2).surround(eName)
        electron = VMobject()
        electron.add(eName, circle1)

        self.play(Create(electron))
        self.play(electron.animate.shift(LEFT*5))

        coulombVal1 = Tex(r"$= -1.6 \times 10^{-19}$", " Mastropolos", font_size=75)
        coulombVal1.next_to(electron, RIGHT, buff=0.25)
        eC = Tex(" C")
        eC.next_to(coulombVal1[0], RIGHT)

        self.play(Write(coulombVal1), run_time=0.5)
        self.wait()

        #I got the "Mastroplos" to change to a "C" but I did it in probably the worst way possible
        self.play(Transform(coulombVal1[1], eC))

        electron.add(coulombVal1)

        #I don't know a better way to make 2 animations happen at once
        def toSide(mob):
            mob.scale(0.5)
            mob.to_edge(UL)
            return mob
        self.play(ApplyFunction(toSide, electron))

        proton = VGroup()
        pName = Tex(r"$p^{+}$", color=RED)
        circle2 = Circle(color=RED, fill_opacity=0.2).surround(pName)
        #for the life of me I can't do anything about this circles radius
        #Eventually I want it to follow the same behavior as the electron
        circle2.radius=5
        proton.add(pName,circle2)

        self.play(Create(proton))
        self.play(proton.animate.shift(LEFT*5))

        coulombVal2 = Tex(r"$= 1.6 \times 10^{-19} \text{ Mastropolos}$", font_size=75)
        coulombVal2.next_to(proton, RIGHT, buff=0.25)

        self.play(Write(coulombVal2), run_time=0.5)
        self.wait()

        proton.add(coulombVal2)

        def unders(mob):
            mob.scale(0.5)
            mob.next_to(electron, DOWN)
            return mob
