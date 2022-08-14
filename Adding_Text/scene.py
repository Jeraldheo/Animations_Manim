

from manim import *

class Node(VGroup):
    CONFIG={
        "radius":0.5,
        "text_scale":0.3
    }
    def __init__(self,text,position=ORIGIN):
        super().__init__()
        circle = Circle(radius=self.CONFIG['radius'], color='white')
        text_mob = Text(text)
        text_mob.match_width(circle)
        text_mob.scale(self.CONFIG['text_scale'])
        self.add(circle,text_mob)
        self.move_to(position)
        self.text_mob=text_mob

    def get_radius(self):
        return self.CONFIG['radius']

    def get_text(self):
        return self.text_mob

class NArrow(Arrow):
    CONFIG={
        "buff":0
    }
    def __init__(self,node_1,node_2,**kwargs):
        radius_n1=node_1.get_radius()
        radius_n2=node_2.get_radius()
        reference_line=Line(node_1.get_center(),node_2.get_center())
        self.start_point=node_1.get_center()+reference_line.get_unit_vector()*radius_n1
        self.end_point=node_2.get_center()-reference_line.get_unit_vector()*radius_n2
        super().__init__(self.start_point,self.end_point,**kwargs)

    def get_start(self):
        return self.start_point

    def get_end(self):
        return self.end_point
        
class HelloWorld(Scene):
    def construct(self):
        title = Text("Find Duplicate Number", font_size=30)
        subtitle = Text("Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. \n There is only one repeated number in nums, return this repeated number. \n You must solve the problem without modifying the array nums and uses only constant extra space. ", font_size=20)
        self.play(Write(title))
        self.play(FadeOut(title))

        self.play(Write(subtitle)) 
        self.play(FadeOut(subtitle))

        example1 = Table([['1','3','4','2','2'],], include_outer_lines=True)
        self.play(Create(example1))

        indices = [Text(str(i)) for i in range(5)]

        indices = VGroup(indices[0], indices[1], indices[2], indices[3], indices[4]).arrange(5*RIGHT)
        indices.next_to(example1, DOWN, buff=0.5)
        self.play(Create(indices))

        self.play(FadeOut(example1))
        self.play(FadeOut(indices))

        
        coord_nodes = [[-3,3,0], [0,2,0],[2,0,0], [1,-3,0], [-2,-2,0]]
        n = len(coord_nodes)
        nodes = [Node(str(i), coord_nodes[i]) for i in range(n)]

        edges =[NArrow(nodes[i], nodes[i+1]) for i in range(n-1)]
        edges.append(CurvedArrow(edges[3].get_start(), edges[3].get_end()))
        edges.append(CurvedArrow(edges[3].get_end(), edges[3].get_start()))
        
        for i in range(n):
            self.play(Create(nodes[i]))

        for i in range(n+1):
            if i!=3:
             self.play(Create(edges[i]))

        for i in range(n):
            self.play(FadeOut(nodes[i]), run_time=0.1)

        for i in range(n+1):
            if i!=3:
             self.play(FadeOut(edges[i]), run_time=0.1)


        
        example2 = Table([['3','4','1','5','2', '4'],], include_outer_lines=True)
        self.play(Create(example2))

        indices2 = [Text(str(i)) for i in range(6)]

        indices2 = VGroup(indices2[0], indices2[1], indices2[2], indices2[3], indices2[4], indices2[5]).arrange(5*RIGHT)
        indices2.next_to(example2, DOWN, buff=0.5)
        self.play(Create(indices2))

        self.play(FadeOut(example2))
        self.play(FadeOut(indices2))
       