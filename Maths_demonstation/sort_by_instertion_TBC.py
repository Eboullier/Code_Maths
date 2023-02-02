from manim import *


class SortFunction(Scene):
    def construct(self):

        def square_text_box(number, square_color, text_color):
            square = Square(side_length=0.7)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text

        def square_swap(color_name):
            square_fill2 = Square(side_length=0.7)
            square_fill2.set_stroke(color=color_name, width=0)
            square_fill2.set_fill(color=color_name, opacity=0.5)

            return square_fill2
        




        bubs_text41 = square_text_box('41', BLUE_E, GREEN_E)
        bubs_text41.shift(0* UP, 2.5* LEFT)

        bubs_text9 = square_text_box('9', BLUE_E, GREEN_E)
        bubs_text9.next_to(bubs_text41, buff=0)

        bubs_text3 = square_text_box('3', BLUE_E, GREEN_E)
        bubs_text3.next_to(bubs_text9, buff=0)

        bubs_text25 = square_text_box('25', BLUE_E, GREEN_E)
        bubs_text25.next_to(bubs_text3, buff=0)

        bubs_text28 = square_text_box('28', BLUE_E, GREEN_E)
        bubs_text28.next_to(bubs_text25, buff=0)

        bubs_text39 = square_text_box('39', BLUE_E, GREEN_E)
        bubs_text39.next_to(bubs_text28, buff=0)

        bubs_text19 = square_text_box('19', BLUE_E, GREEN_E)
        bubs_text19.next_to(bubs_text39, buff=0)

        bubs_text47 = square_text_box('47', BLUE_E, GREEN_E)
        bubs_text47.next_to(bubs_text19, buff=0)

        bubs_text_right = MarkupText(r'<span font_family="arial"><b>Insertion Sort</b></span>', 
                                    color=BLUE_E)

        bubs_text_right.shift(1* UP)

        self.play(DrawBorderThenFill(bubs_text41, run_time = 3), DrawBorderThenFill(bubs_text9, run_time = 3), DrawBorderThenFill(bubs_text3, run_time = 3),
                  DrawBorderThenFill(bubs_text25, run_time = 3),
                  DrawBorderThenFill(bubs_text47, run_time = 3), DrawBorderThenFill(bubs_text19, run_time = 3), DrawBorderThenFill(bubs_text39, run_time = 3),
                  DrawBorderThenFill(bubs_text28, run_time = 3), Write(bubs_text_right))

                #  ------------step 1 ------------------------- 

        step_text = MarkupText(r'<span font_family="arial"><b>STEP 1 :</b></span>', 
                                    color=BLUE_E).scale(0.6)
        step_text.shift(3 * UP)

        self.play(Write(step_text), run_time=2)

        step_text_explanation_1 = MarkupText(r'<span font_family="arial"><b>We start by comparing the second number of the list with the first.</b></span>', 
                                    color=WHITE).scale(0.4)
        step_text_explanation_1.shift(2.6 * UP)
        step_text_explanation_2 = MarkupText(r'<span font_family="arial"><b>If it is smaller, we swap places</b></span>',
                                    color=WHITE).scale(0.4)
        step_text_explanation_2.shift(2.2 * UP)
        
        step_text_explanation_3 = MarkupText(r"""<span font_family="arial"><b>Here 9 is less than 41, so let's swap places </b></span>""",
                                    color=WHITE).scale(0.4)
        step_text_explanation_3.shift(1.8 * UP)
        self.play(Write(step_text_explanation_1), run_time=3)
        self.play(Write(step_text_explanation_2), run_time=3)
        self.play(Write(step_text_explanation_3), run_time=3)
        self.wait(1.5)
        self.play(CyclicReplace(bubs_text41, bubs_text9))
    
                #  ------------step 2 ------------------------- 
        self.play(FadeOut(step_text), FadeOut(step_text_explanation_1), FadeOut(step_text_explanation_2), FadeOut(step_text_explanation_3))
        step_text = MarkupText(r'<span font_family="arial"><b>STEP 2 :</b></span>', 
                                    color=BLUE_E).scale(0.6)
        step_text.shift(3 * UP)

        self.play(Write(step_text), run_time=2)
        step_text_explanation_1 = MarkupText(r'<span font_family="arial"><b>Now we compare the third digit with the second and first. </b></span>', 
                                    color=WHITE).scale(0.4)
        step_text_explanation_1.shift(2.6 * UP)
        step_text_explanation_2 = MarkupText(r"""<span font_family="arial"><b>3 is less than 41, so let's swap places</b></span>""",
                                    color=WHITE).scale(0.4)
        step_text_explanation_2.shift(2.2 * UP)
        self.play(Write(step_text_explanation_1), run_time=3)
        self.play(Write(step_text_explanation_2), run_time=3)  
        self.wait(1.5)
        self.play(CyclicReplace(bubs_text41, bubs_text3))     
        step_text_explanation_3 = MarkupText(r'<span font_family="arial"><b>But 3 is also less than 9, so we swap places again.</b></span>',
                                    color=WHITE).scale(0.4)
        step_text_explanation_3.shift(1.8 * UP)
        self.play(Write(step_text_explanation_3), run_time=3)  
        self.wait(1.5)
        self.play(CyclicReplace(bubs_text9, bubs_text3))    
         #  ------------step 3 ------------------------- 
        self.play(FadeOut(step_text), FadeOut(step_text_explanation_1), FadeOut(step_text_explanation_2), FadeOut(step_text_explanation_3))
        step_text = MarkupText(r'<span font_family="arial"><b>STEP 3 :</b></span>', 
                                    color=BLUE_E).scale(0.6)
        step_text.shift(3 * UP)
        self.play(Write(step_text), run_time=2)
        step_text_explanation_1 = MarkupText(r'<span font_family="arial"><b>We repeat the process for the fourth, fifth, ...</b></span>', 
                                    color=WHITE).scale(0.4)
        step_text_explanation_1.shift(2.2 * UP)
        self.play(Write(step_text_explanation_1), run_time=3)
        self.play(CyclicReplace(bubs_text41, bubs_text25))
        self.wait(1) 
        self.play(CyclicReplace(bubs_text41, bubs_text28))
        self.wait(1) 
        self.play(CyclicReplace(bubs_text41, bubs_text39))
        self.wait(1) 
        self.play(CyclicReplace(bubs_text41, bubs_text19))
        self.wait(1) 
        self.play(CyclicReplace(bubs_text39, bubs_text19))
        self.wait(1) 
        self.play(CyclicReplace(bubs_text28, bubs_text19))
        self.wait(1) 
        self.play(CyclicReplace(bubs_text25, bubs_text19))
        self.wait(1) 
         #  ------------step final ------------------------- 
        self.play(FadeOut(step_text), FadeOut(step_text_explanation_1))
        step_text = MarkupText(r'<span font_family="arial"><b>FINAL STEP :</b></span>', 
                                    color=BLUE_E).scale(0.6)
        step_text.shift(3 * UP)

        self.play(Write(step_text), run_time=2)
        step_text_explanation_1 = MarkupText(r'<span font_family="arial"><b>When we reach the last position in the list, the sort is complete</b></span>', 
                                    color=WHITE).scale(0.4)
        step_text_explanation_1.shift(2.2 * UP)
        self.play(Write(step_text_explanation_1), run_time=3)
        self.play(FadeOut(step_text), FadeOut(step_text_explanation_1))
        self.play(FadeOut(bubs_text41, run_time = 3), FadeOut(bubs_text9, run_time = 3), FadeOut(bubs_text3, run_time = 3),
                  FadeOut(bubs_text25, run_time = 3),
                  FadeOut(bubs_text47, run_time = 3), FadeOut(bubs_text19, run_time = 3), FadeOut(bubs_text39, run_time = 3),
                  FadeOut(bubs_text28, run_time = 3), FadeOut(bubs_text_right))