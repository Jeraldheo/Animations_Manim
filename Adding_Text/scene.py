
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
        start_point=node_1.get_center()+reference_line.get_unit_vector()*radius_n1
        end_point=node_2.get_center()-reference_line.get_unit_vector()*radius_n2
        super().__init__(start_point,end_point,**kwargs)

        
class HelloWorld(Scene):
    def construct(self):
        title = Text("Find Duplicate Number", font_size=30)
        subtitle = Text("Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. \n There is only one repeated number in nums, return this repeated number. \n You must solve the problem without modifying the array nums and uses only constant extra space. ", font_size=20)
        self.play(Write(title))
        self.play(FadeOut(title))

        self.play(Write(subtitle)) 
        self.play(FadeOut(subtitle))

        coord_node_1=[-3,3,0]
        coord_node_2=[0,2,0]
        coord_node_3=[2,0,0]
        coord_node_4=[1,-3,0]
        coord_node_5=[-2,-2,0]
        

        node_1=Node("0",coord_node_1)
        node_2=Node("1",coord_node_2)
        node_3=Node("2",coord_node_3)
        node_4=Node("3",coord_node_4)
        node_5=Node("4",coord_node_5)

        edge1=NArrow(node_1,node_2)
        edge2=NArrow(node_2,node_3)
        edge3=NArrow(node_3,node_4)
        
        


        radius_n5=node_5.get_radius()
        radius_n4=node_4.get_radius()
        reference_line=Line(node_5.get_center(),node_4.get_center())
        start_point=node_5.get_center()+reference_line.get_unit_vector()*radius_n5
        end_point=node_4.get_center()-reference_line.get_unit_vector()*radius_n4
        last_edge = CurvedArrow(start_point, end_point)
        edge4 = CurvedArrow(end_point, start_point)

        self.play(Create(node_1))
        self.play(Create(node_2))
        self.play(Create(node_3))
        self.play(Create(node_4))
        self.play(Create(node_5))
        self.play(Create(edge1))
        self.play(Create(edge2))
        self.play(Create(edge3))
        self.play(Create(edge4))
        self.play(Create(last_edge))



        self.wait(duration=3)
       