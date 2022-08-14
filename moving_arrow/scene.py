from cmath import pi
from manim import *
class MovingArrow(Scene):
    def construct(self):
        starts = [[-5,0,0], [-3,0,0], [-1,0,0], [1,0,0], [3,0,0], [5,0,0]]
        ends = [[-5,4,0], [-3,4,0], [-1,4,0], [1,4,0], [3,4,0], [5,4,0]]
        n = len(starts)
        for i in range(n):
            arrow = Arrow(starts[i], ends[i])
            arrow.height = 1
            arrow.rotate(pi)
            data  = arrow.get_coord(2)
            label = Text(str(i+1)).set_coord(data, 2)
            self.play(Create(arrow))
            label.next_to(arrow, UP)
            self.play(Create(label))
            self.play(FadeOut(arrow))
            self.play(FadeOut(label))

