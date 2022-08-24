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



        
        
                
        
            