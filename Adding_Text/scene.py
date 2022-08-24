#TODO add sound and sync with video
from cmath import pi

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
        
        self.add_sound('animation_audio.wav')

        subtitle = Text("Given an array of integers containing n + 1 integers where each integer is in the range [1, n] inclusive. \
            \n There is only one repeated number in the array, return this repeated number. \
            \n You must solve the problem without modifying the array and using only constant extra space. ", font_size=21)

        self.play(Create(title))
        self.wait(duration=8)
        self.play(FadeOut(title))

        self.play(Write(subtitle)) 
        self.wait(duration=21)
        self.play(FadeOut(subtitle))

        example1 = Table([['1','3','4','2','2'],], include_outer_lines=True)
        self.play(Create(example1))
        
        indices = [Text(str(i)) for i in range(5)]

        indices = VGroup(indices[0], indices[1], indices[2], indices[3], indices[4]).arrange(5*RIGHT)
        indices.next_to(example1, DOWN, buff=0.5)
        self.play(Create(indices))

        self.wait(duration=25)

        self.play(FadeOut(example1))
        self.play(FadeOut(indices))

        
        coord_nodes = [[-3,3,0], [0,2,0],[2,0,0], [1,-3,0], [-2,-2,0]]
        n = len(coord_nodes)
        nodes = []
        for i in range(n):
            label = i
            if i==2:
                label = 3
            if i == 3:
                label = 2
            nodes.append(Node(str(label), coord_nodes[i]))
                

        edges =[NArrow(nodes[i], nodes[i+1]) for i in range(n-1)]
        edges.append(CurvedArrow(edges[3].get_start(), edges[3].get_end()))
        edges.append(CurvedArrow(edges[3].get_end(), edges[3].get_start()))
        
        for i in range(n):
            self.play(Create(nodes[i]), run_time = 0.5)

        for i in range(n+1):
            if i!=3:
             self.play(Create(edges[i]), run_time = 0.5)

        self.wait(duration=30)

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

        self.wait(duration=15)
        self.play(FadeOut(example2))
        self.play(FadeOut(indices2))

        
        coord_nodes2 = [[-5,0,0], [5,0,0],[3,0,0], [-3,0,0], [1,0,0], [-1,0,0]]

        num = len(coord_nodes2)
        nodes2 = [Node(str(i), coord_nodes2[i]) for i in range(num)]
        
        for i in range(num):
            self.play(Create(nodes2[i]), run_time = 0.2)

        relations = {nodes2[0]: nodes2[3], nodes2[3]: nodes2[5], nodes2[5]: nodes2[4], nodes2[4]: nodes2[2], nodes2[2]: nodes2[1]}

        edges2 =[NArrow(key, value) for key, value in relations.items()]
        value = len(edges2)
        for i in range(value):
             self.play(Create(edges2[i]), run_time=0.2)

        last_edge = NArrow(nodes2[1], nodes2[4])
        last_edge = CurvedArrow(last_edge.get_start(), last_edge.get_end())
        self.play(Create(last_edge))
        self.wait(duration=55)

        starts = [[-5,0,0], [-3,0,0], [-1,0,0], [1,0,0], [3,0,0], [5,0,0]]
        ends = [[-5,3,0], [-3,3,0], [-1,3,0], [1,3,0], [3,3,0], [5,3,0]]
        n = len(starts)
        for i in range(n):
            arrow = Arrow(starts[i], ends[i])
            arrow.height = 1
            arrow.rotate(pi)
            data  = arrow.get_coord(2)
            label = Text(str(i+1)).set_coord(data, 2)
            self.play(Create(arrow), run_time = 0.2)
            label.next_to(arrow, UP)
            self.play(Create(label), run_time = 0.2)
            self.play(FadeOut(arrow), run_time = 0.2)
            self.play(FadeOut(label), run_time = 0.2)
        
        self.wait(duration=10)

        cycle_starts = [[3,0,0], [5,0,0],[1,0,0], [3,0,0]]            
        cycle_ends = [[3,3,0], [5,3,0], [1,3,0], [3,3,0]]
        for i in range(3):
            arrow = Arrow(cycle_starts[i], cycle_ends[i])
            arrow.height = 1
            arrow.rotate(pi)
            data  = arrow.get_coord(2)
            label = Text(str(i+1)).set_coord(data, 2)
            self.play(Create(arrow), run_time = 0.2)
            label.next_to(arrow, UP)
            self.play(Create(label), run_time = 0.2)
            self.play(FadeOut(arrow), run_time = 0.2)
            self.play(FadeOut(label), run_time = 0.2)
        self.wait(duration=5)
        starts = [[-5,0,0], [-3,0,0], [-1,0,0], [1,0,0]]
        ends = [[-5,4,0], [-3,4,0], [-1,4,0], [1,4,0]]
        starts1 = [[1,-1,0], [3,-1,0], [5,-1,0], [1,-1,0]]
        ends1 = [[1,-4,0], [3,-4,0], [5,-4,0], [1,-4,0]]
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
            label1 = Text('S').set_coord(data1, 2)
            label = Text('F').set_coord(data, 2)
            self.play(Create(arrow), Create(arrow1))
            label.next_to(arrow, UP)
            label1.next_to(arrow1, UP)
            self.play(Create(label), Create(label1))
            if i!=n-1:
                self.play(FadeOut(arrow), FadeOut(arrow1))
                self.play(FadeOut(label), FadeOut(label1))
                
        
            