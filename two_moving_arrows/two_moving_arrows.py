from cmath import pi
from manim import *
class MovingArrows(Scene):
    def construct(self):
        starts = [[-5,0,0], [-3,0,0], [-1,0,0], [1,0,0]]
        ends = [[-5,4,0], [-3,4,0], [-1,4,0], [1,4,0]]
        starts1 = [[1,0,0], [3,0,0], [5,0,0], [1,0,0]]
        ends1 = [[1,4,0], [3,4,0], [5,4,0], [1,0,0]]
        n = len(starts)
        for i in range(n):
            arrow = Arrow(starts[i], ends[i])
            arrow1 = Arrow(starts1[i], ends1[i])
            arrow.height = 1
            arrow1.height = 1
            arrow.rotate(pi)
            arrow1.rotate(pi)
            data  = arrow.get_coord(2)
            data1 = arrow1.get_coord(2)
            self.play(Create(arrow), Create(arrow1))
            self.play(FadeOut(arrow), FadeOut(arrow1))

