# Dragon Fractal

from manim import *


class DragonFractal(MovingCameraScene):
    CONFIG = {
        "colors": [RED, ORANGE, GREEN_B, BLUE_D, BLUE, PURPLE]
    }

    def construct(self):
        # self.colors.reverse()
        self.camera.frame.save_state()
        line = Line(DOWN, UP)
        self.offset = 1.4

        self.dragon = VMobject()
        self.dragon.set_stroke(width=20)
        self.dragon.set_points(line.get_points())
        # self.dragon.set_color(next(self.colors))

        
        self.camera.frame.set_height(self.dragon.get_height() * self.offset)
        self.camera.frame.move_to(self.dragon.get_center())

        self.last_point = self.dragon.get_last_point()

        self.play(Create(self.dragon.copy()))

        for i in range(22):
            self.copy_and_rotate(i)
        self.wait()

    def copy_and_rotate(self, i):
        colors_list = [RED, ORANGE, GREEN_B, BLUE_D, BLUE, PURPLE]
        dragon = self.dragon.copy()
        dragon.set_color(colors_list[i%6])
        dragon.generate_target()
        dragon.target.rotate(PI / 2, about_point=self.last_point)

        self.bring_to_back(dragon)
        self.dragon.set_points(
            np.vstack((self.dragon.get_points(), dragon.target.get_points()))
        )

        self.play(
            MoveToTarget(dragon,path_arc=PI / 2),
            # self.camera.frame.animate.set(height = self.dragon.get_height() * self.offset*10),
            # self.camera.frame.animate.move_to(self.dragon.get_center())
            self.camera.auto_zoom(self.dragon, margin=10,only_mobjects_in_frame=True, animate=True),
            run_time=1.5,
            rate_func=linear,
        )

        self.last_point = self.dragon.get_points()[len(self.dragon.get_points()) // 2]