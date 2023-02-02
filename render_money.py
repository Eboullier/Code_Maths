from manim import * 


class ways_money(Scene):
    def construct(self):
        def square_text_box(number, square_color, text_color):
            square = Square(side_length=0.7)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text

        
        step_text = MarkupText(r'<span font_family="arial"><b>Example with 4 penny</b></span>', 
                                    color=BLUE_E).scale(0.6)
        step_text.shift(3.5 * UP)

        ways_list = MarkupText(r'<span font_family="arial"><b>Ways list :</b></span>', 
                                    color=BLUE_E).scale(0.6)
        ways_list.shift(2.6* UP, 2*LEFT)

        ways_to_render_0 = square_text_box('1', BLUE_E, WHITE)
        ways_to_render_0.next_to(ways_list, buff=0.5)

        ways_to_render_1 = square_text_box('0', BLUE_E, WHITE)
        ways_to_render_1.next_to(ways_to_render_0, buff=0)

        ways_to_render_2 = square_text_box('0', BLUE_E, WHITE)
        ways_to_render_2.next_to(ways_to_render_1, buff=0)

        ways_to_render_3 = square_text_box('0', BLUE_E, WHITE)
        ways_to_render_3.next_to(ways_to_render_2, buff=0)

        ways_to_render_4 = square_text_box('0', BLUE_E, WHITE)
        ways_to_render_4.next_to(ways_to_render_3, buff=0)
        self.play( Write(step_text))

        self.play(DrawBorderThenFill(ways_to_render_0, run_time = 3),DrawBorderThenFill(ways_to_render_1, run_time = 3), DrawBorderThenFill(ways_to_render_2, run_time = 3), DrawBorderThenFill(ways_to_render_3, run_time = 3),
                  DrawBorderThenFill(ways_to_render_4, run_time = 3), Write(ways_list))
        self.wait(5)