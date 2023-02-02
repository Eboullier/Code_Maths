from manim import *


class SortFunctionSelection(Scene):
    def construct(self):

        def square_text_box(number, square_color, text_color):
            square = Square(side_length=0.7)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text
        
        bubs_text41 = square_text_box('41', BLUE_E, WHITE)
        bubs_text41.shift(0* UP, 2.5* LEFT)

        bubs_text9 = square_text_box('9', BLUE_E, WHITE)
        bubs_text9.next_to(bubs_text41, buff=0)

        bubs_text3 = square_text_box('3', BLUE_E, WHITE)
        bubs_text3.next_to(bubs_text9, buff=0)

        bubs_text25 = square_text_box('25', BLUE_E, WHITE)
        bubs_text25.next_to(bubs_text3, buff=0)

        bubs_text28 = square_text_box('28', BLUE_E, WHITE)
        bubs_text28.next_to(bubs_text25, buff=0)

        bubs_text39 = square_text_box('39', BLUE_E, WHITE)
        bubs_text39.next_to(bubs_text28, buff=0)

        bubs_text19 = square_text_box('19', BLUE_E, WHITE)
        bubs_text19.next_to(bubs_text39, buff=0)

        bubs_text47 = square_text_box('47', BLUE_E, WHITE)
        bubs_text47.next_to(bubs_text19, buff=0)

        box_group = VGroup(bubs_text41, bubs_text9, bubs_text3, bubs_text25, bubs_text28, bubs_text39, bubs_text19, bubs_text47)
        box_group.add()
    
        bubs_text_right = MarkupText(r'<span font_family="arial"><b>Selection Sort</b></span>', 
                                    color=BLUE_E)

        bubs_text_right.shift(1* UP)

        self.play(Create(box_group), Write(bubs_text_right))
        self.wait(1)
        self.play(bubs_text3.animate.shift(1.2*DOWN))
        self.wait(5)
        self.play(bubs_text41.animate.shift(0.35*RIGHT), bubs_text9.animate.shift(0.35*RIGHT), bubs_text25.animate.shift(0.35*LEFT), bubs_text28.animate.shift(0.35*LEFT), bubs_text39.animate.shift(0.35*LEFT), bubs_text19.animate.shift(0.35*LEFT), bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text3.animate.shift(1.2*DOWN))
        self.wait(5)
             #  ------------step 2 -------------------------   
            
        self.play(bubs_text9.animate.shift(1.2*DOWN))  
        self.wait(5)
        self.play(bubs_text41.animate.shift(0.35*RIGHT), bubs_text25.animate.shift(0.35*LEFT), bubs_text28.animate.shift(0.35*LEFT), bubs_text39.animate.shift(0.35*LEFT), bubs_text19.animate.shift(0.35*LEFT), bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text9.animate.shift(1.05*RIGHT,1.2*DOWN))
        self.wait(5)


             #  ------------step 3 -------------------------   
            
        self.play(bubs_text19.animate.shift(1.2*DOWN))  
        self.wait(5)
        self.play(bubs_text41.animate.shift(0.35*RIGHT), bubs_text25.animate.shift(0.35*RIGHT), bubs_text28.animate.shift(0.35*RIGHT), bubs_text39.animate.shift(0.35*RIGHT), bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text19.animate.shift(0.7*LEFT,1.2*DOWN))
        self.wait(5)

             #  ------------step 4 -------------------------   
            
        self.play(bubs_text25.animate.shift(1.2*DOWN)) 
        self.wait(5) 
        self.play(bubs_text41.animate.shift(0.35*RIGHT), bubs_text28.animate.shift(0.35*LEFT), bubs_text39.animate.shift(0.35*LEFT), bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text25.animate.shift(1.75*RIGHT,1.2*DOWN))
        self.wait(5)
             #  ------------step 5 -------------------------   
            
        self.play(bubs_text28.animate.shift(1.2*DOWN))  
        self.wait(5)
        self.play(bubs_text41.animate.shift(0.35*RIGHT), bubs_text39.animate.shift(0.35*LEFT), bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text28.animate.shift(1.75*RIGHT,1.2*DOWN), bubs_text3.animate.shift(0.35*LEFT), bubs_text9.animate.shift(0.35*LEFT), bubs_text19.animate.shift(0.35*LEFT), bubs_text25.animate.shift(0.35*LEFT))
        self.wait(5)
             #  ------------step 6 -------------------------   
            
        self.play(bubs_text39.animate.shift(1.2*DOWN))  
        self.wait(5)
        self.play(bubs_text41.animate.shift(0.35*RIGHT), bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text39.animate.shift(1.75*RIGHT,1.2*DOWN), bubs_text3.animate.shift(0.35*LEFT), bubs_text9.animate.shift(0.35*LEFT), bubs_text19.animate.shift(0.35*LEFT), bubs_text25.animate.shift(0.35*LEFT),bubs_text28.animate.shift(0.35*LEFT))

        self.wait(5)

             #  ------------step 7 -------------------------   
            
        self.play(bubs_text41.animate.shift(1.2*DOWN))  
        self.wait(5)
        self.play(bubs_text47.animate.shift(0.35*LEFT))
        self.play(bubs_text41.animate.shift(2.45*RIGHT,1.2*DOWN), bubs_text3.animate.shift(0.35*LEFT), bubs_text9.animate.shift(0.35*LEFT), bubs_text19.animate.shift(0.35*LEFT), bubs_text25.animate.shift(0.35*LEFT),bubs_text28.animate.shift(0.35*LEFT), bubs_text39.animate.shift(0.35*LEFT))
        self.wait(5)

             #  ------------step 8 -------------------------   
            
        self.play(bubs_text47.animate.shift(1.2*DOWN))  
        self.play(bubs_text47.animate.shift(2.45*RIGHT,1.2*DOWN), bubs_text3.animate.shift(0.35*LEFT), bubs_text9.animate.shift(0.35*LEFT), bubs_text19.animate.shift(0.35*LEFT), bubs_text25.animate.shift(0.35*LEFT),bubs_text28.animate.shift(0.35*LEFT), bubs_text39.animate.shift(0.35*LEFT), bubs_text41.animate.shift(0.35*LEFT))
        self.wait(5)
    
        self.play(bubs_text47.animate.shift(2.4*UP), bubs_text3.animate.shift(2.4*UP), bubs_text9.animate.shift(2.4*UP), bubs_text19.animate.shift(2.4*UP), bubs_text25.animate.shift(2.4*UP),bubs_text28.animate.shift(2.4*UP), bubs_text39.animate.shift(2.4*UP), bubs_text41.animate.shift(2.4*UP))
        self.wait(5)