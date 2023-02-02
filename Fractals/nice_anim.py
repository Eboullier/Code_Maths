# made in ManimGL
from manim import *

class ParametricCurves1(Scene):
    def construct(self):
        A = 1
        B = 1
        C = 0
        D = 0
        # index_colors = [
        #     [
        #         [4,RED],[12,BLUE],[22,YELLOW]
        #     ],
        #     [
        #         [4,RED],[12,BLUE],[22,YELLOW]
        #     ],
        # ]
        # equation = VGroup(
        #     MathTex(r"\cos(at)+{\cos(bt)\over 2}+{\sin(ct)\over 3}"),
        #     MathTex(r"\sin(at)+{\sin(bt)\over 2}+{\cos(ct)\over 3}")
        # ).scale(0.9).arrange(DOWN,aligned_edge=LEFT)
        # equation.to_corner(UR)
        # print("ok")
        # brace = Brace(equation,LEFT)
        # C_ = brace.get_tex("C")

        # range_ = MathTex(r"t\in[0,2\pi]")
        # range_.next_to(equation,DOWN).align_to(equation,RIGHT)

        values = VGroup(*[
            MathTex(f"{t}=",tex_to_color_map={f"{t}":color}).scale(1.3)
            for t,color in zip(["a","b","c","d"],[RED,BLUE,YELLOW,GREEN])
        ])
        values.arrange(DOWN,aligned_edge=LEFT,buff=1.2)
        values.move_to(RIGHT)

        dn_kwargs = {"unit": r"^\circ"}
        D_A = DecimalNumber(A,**dn_kwargs)
        D_B = DecimalNumber(B,**dn_kwargs)
        D_C = DecimalNumber(C,**dn_kwargs)
        D_D = DecimalNumber(C,**dn_kwargs)
        D_G = VGroup(D_A,D_B,D_C, D_D)
        for d,s in zip(D_G,values):
             d.next_to(s,aligned_edge=DOWN)

        pc = self.get_param_func(A,B,C,D)
        pc.shift(LEFT*3)
        pc.add_updater(
            lambda mob: mob.become(
                self.get_param_func(
                    D_A.get_value(),
                    D_B.get_value(),
                    D_C.get_value(),
                    D_D.get_value()
                )
            ).shift(LEFT*3)
        )

        black_square = Square(
            fill_opacity=1,
            fill_color=BLACK,
            stroke_width=0
        ).set_width(pc.get_width()*1.1).move_to(pc)
        self.add(pc,black_square)

        self.wait(0.3)
        # self.play(
        #     Write(range_)
        # )
        self.wait(0.5)
        self.play(
            # Write(values),
            Write(D_G),
            FadeOut(black_square), run_time =1
        )
        # self.wait(0.5)
        # self.play(
        #     ChangeDecimalToValue(D_B,15),
        #     run_time=15,
        #     rate_func=linear,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_B,1),
        #     run_time=2,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_C,15),
        #     run_time=15,
        #     rate_func=linear,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_C,1),
        #     run_time=2,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_B,30),
        #     run_time=15,
        #     rate_func=linear,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_B,2),
        #     run_time=2,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_C,30),
        #     run_time=15,
        #     rate_func=linear,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_C,25),
        #     run_time=2,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_B,15),
        #     run_time=30,
        #     rate_func=linear,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_B,60),
        #     run_time=30,
        #     rate_func=linear,
        # )
        # self.wait(0.3)
        # self.play(
        #     ChangeDecimalToValue(D_B,30),
        #     ChangeDecimalToValue(D_C,1),
        #     run_time=2,
        # )
        # self.wait(0.3)
        self.play(
            ChangeDecimalToValue(D_A,2),
            run_time=20,
            rate_func=linear,
        )
        self.wait(3)
        self.play(
            ChangeDecimalToValue(D_B,3),
            run_time=20,
            rate_func=linear,
        )
        self.wait(3)
        self.play(
            ChangeDecimalToValue(D_A,6),
            ChangeDecimalToValue(D_B,4),
            run_time=20,
            rate_func=linear,
        )
        self.wait(3)
        self.play(
            ChangeDecimalToValue(D_A,1),
            ChangeDecimalToValue(D_B,1),
            run_time=1,
            rate_func=linear,
        )
        self.play(
            ChangeDecimalToValue(D_B,2),
            run_time=20,
            rate_func=linear,
        )
        self.wait(3)
        self.play(
            ChangeDecimalToValue(D_C,15),
            run_time=30,
            rate_func=linear,
        )
        self.play(
            ChangeDecimalToValue(D_B,1),
            ChangeDecimalToValue(D_C,0),
            run_time=1,
            rate_func=linear,
        )
        self.play(
            ChangeDecimalToValue(D_A,5),
            ChangeDecimalToValue(D_B,3),
            run_time=1,
            rate_func=linear,
        )
        self.wait(3)
        self.play(
            ChangeDecimalToValue(D_D,15),
            run_time=30,
            rate_func=linear,
        )
        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))

    def get_param_func(self, a, b, c, d):
        tol = 1e-9
        # pc = ParametricFunction(
        #     lambda t: np.array([
        #         np.cos(a * t) + np.cos(b * t) / 2 + np.sin(c * t) / 3,
        #         np.sin(a * t) + np.sin(b * t) / 2 + np.cos(c * t) / 3,
        #         0
        #     ]),
        #     t_range=[0,2*PI,0.007],
        #     tolerance_for_point_equality=tol,
        #     dt=tol,
        # )     
        # 
        # x(t) = a * sqrt(2) * cos(t) / (sin(t)^2 + 1)
        #y(t) = a * sqrt(2) * cos(t) * sin(t) / (sin(t)^2 + 1)   
        pc = ParametricFunction(
            lambda t: np.array([
                np.cos(a*t + c),
                np.sin(b*t + d),
                0
            ]),
            t_range=[0,4*PI,0.007],
            tolerance_for_point_equality=tol,
            dt=tol,
        )

        # pc.set_color(color=[RED,YELLOW,BLUE,RED])
        pc.set_color(color=BLUE)
        pc.scale(2)
        return pc