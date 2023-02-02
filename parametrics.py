from manim import *
import numpy as np
## WIP

class SierpinskiTriangle(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        ax = Axes(x_range=(-6,6), y_range=(-6,6))
        nice_plot = ax.plot_parametric_curve(
            lambda t: np.array(
                [
                    t-1.6*np.cos(24*t),
                    t-1.6*np.cos(25*t),
                    0,
                ]
            ),
            t_range=[-6, 6],
            color="#0FF1CE",

            )
        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(nice_plot.t_min, nice_plot), color=BLUE)
        dot_1 = Dot(ax.i2gp(nice_plot.t_min, nice_plot))
        dot_2 = Dot(ax.i2gp(nice_plot.t_max, nice_plot))
        self.add(ax)   
        self.add(ax, nice_plot, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot), run_time=5)   

        self.play(MoveAlongPath(moving_dot, nice_plot, rate_func=linear), run_time=30)

        self.play(Restore(self.camera.frame))        