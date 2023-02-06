from manim import *
from manimlib.imports import *
from circuitanimlib.circuit import *


class DrawCircuit(Scene):
  def construct(self):
    res = Resistor()
    cap = Capacitor()
    batt = Battery()

    batt.rotate(PI/2)
    cap.rotate(-PI/2)
    cap.shift(RIGHT*3)
    res.shift(2*LEFT + UP*3)
    batt.shift(3*LEFT)


    circ = Circuit()
    circ.connect(batt.get_right(),res.get_left())
    circ.connect(res.get_right(),cap.get_left(),pin_top=True)
    circ.connect_right_to_left(cap.get_right(),batt.get_left())
    circ.render()
    
    self.play(Create(batt),Create(res),Create(cap),Create(circ),run_time=3)