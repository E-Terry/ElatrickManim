from manim import *



class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class Circuits(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"""
        \usepackage{circuitikz}
        \usetikzlibrary{decorations.pathreplacing}
        """)
        tex = Tex(
            r"""
        \begin{figure}[h]
            \centering
    
            \begin{tikzpicture}
                \node[inner color=white, outer color=black!30, circle, draw] (C) at (0,0) {$e^{-}$};
                \node[inner color=white, outer color=blue!30, circle, draw] (C) at (3,0) {$p^{+}$};
                \node[inner color=white, outer color=red!30, circle, draw] (C) at (-9,0) {$p^{+}$};
                \draw[red, thick, decorate, decoration={brace, amplitude=5pt, raise=20pt}] (0,0) -- coordinate[midway] node[anchor=north, below=27pt] {$30\mu m$} (-9,0);
                \draw[blue, thick, decorate, decoration={brace, amplitude=5pt, raise=20pt}] (3,0) -- coordinate[midway] node[anchor=north, below=27pt] {$10\mu m$} (0,0);
            \end{tikzpicture}
        \end{figure}
            """,
            tex_template=myTemplate,
            font_size=20,
        )
        self.play(FadeIn(tex))
        self.wait()


class TikzMobject(Tex):
    CONFIG = {
    "stroke_width": 3,
    "fill_opacity": 0,
    "stroke_opacity": 1,
    }