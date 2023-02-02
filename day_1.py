from manim import * 
import math import *

MAX_COUNT = 10000000
A = 2.879879
B = -0.765145
C = -0.966918
D = 0.744728

class FirstExample(Scene):
    def construct(self):
        #Get some axis
        ax = Axes(x_range=(-4,4), y_range=(-4,4))
        for i in range (1000) : 
            x, y = math.sin(A*x)+B*math.sin(A*y), math.sin(C*x)+D*math.sin(C*y)
        curve = ax.plot(lambda x : (x+2)*x*(x-2), color = RED)
        self.add(ax)
        self.add(curve)
        # area = ax.get_area(curve, x_range=(-1,1))
        # self.play(Create(ax, run_time=2))
        # self.play(Create(curve, run_time=4))
        # self.wait(1)
        # self.play(Create(area, run_time=2))
        # self.wait(3)
