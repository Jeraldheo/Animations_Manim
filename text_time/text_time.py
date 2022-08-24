from manim import *


class TextTime(Scene):
    def construct(self):
        data  = Text('Hello World')
        self.play(Create(data))
        self.wait(duration=10)