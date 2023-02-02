from manim import * 
from manim.utils.color import RED, ORANGE, YELLOW
import math

config.frame_height, config.frame_width = config.frame_width, config.frame_height
config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height


MAX_COUNT = 10000000
A = 2.879879
B = -0.765145
C = -0.966918
D = 0.744728

class KingDreams(Scene):
    def construct(self):
    #     x=2
    #     y=2
        ax = Axes()
        kingdream = ax.plot_parametric_curve(
            lambda t: np.array(
                [
                    math.sin(A*t)+B*math.sin(A*t),
                    math.sin(C*t)+D*math.sin(C*t),
                    0,
                ]
            ),
            t_range=[-10000, 10000],
            )
        self.add(ax)
        self.play(Create(kingdream))
    #     gradient = color_gradient((RED,ORANGE,YELLOW, BLUE, GREEN),10000)
    #     for i in range (50) : 
    #         dots = VGroup()
    #         for j in range (i*20000,(i+1)*20000):
                
    #             x, y = math.sin(A*x)+B*math.sin(A*y), math.sin(C*x)+D*math.sin(C*y)
    #             new_dot = Dot(radius=0.005, color=gradient[int((x+y)*2400)])
    #             new_dot.shift(x*RIGHT + y*UP)
    #             dots.add(new_dot)
                
    #         self.play(Create(dots))

