from manim import *
from CircuitanimButForCE.circuit import *

class DrawCircuit(Scene):
  def construct(self):
    res = Resistor()
    cap = Capacitor()
    batt = Battery()
    ind = Inductor()

    batt.rotate(PI/2)
    batt.shift(LEFT)
    res.shift(UP)
    ind.rotate(-PI/2)
    ind.shift(RIGHT)
    cap.shift(DOWN)


    circ = Circuit()
    circ.connect(batt.get_right(),res.get_left())
    circ.connect(res.get_right(),ind.get_left(), pin_top=True)
    circ.connect(cap.get_right(),ind.get_right(), pin_top=True)
    circ.connect(batt.get_left(),cap.get_left())
    circ.render()

    t = Tex(r"suck it patrick I can even do \LaTeX \; if I want")
    t.shift(UP*3)
    
    resLabel = Text("Resistor")
    resLabel.shift(UP*2)

    
    self.play(Create(batt),Create(res),Create(cap),Create(ind), Create(circ), run_time=3)
    self.play(Create(resLabel), run_time=1)
    self.play(Create(t), run_time=3)