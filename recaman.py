from manim import *


class RecamanSequence(MovingCameraScene):

    def construct(self):
        n = 30
        count = 0
        visited = [0] + [None] * n
        arcs = VGroup()

        self.index = 0  # acts as a pointer
        max_width = max(self.index, 3)  # to set the frame width

        for i in range(n):
            index = self.index - count

            if index < 0 or index in visited:
                index = self.index + count

            # defining the start and end of the arc
            start = np.array([visited[count], 0, 0])
            end = np.array([index, 0, 0])

            # defining the angle of arc (i.e., whether it would be an upward arc or downward arc)
            angle = PI if count % 2 else -PI 

            if index < visited[count]:
                angle *= -1

            arc = ArcBetweenPoints(start, end, angle)
            arcs.add(arc)

            # updating variables
            self.index = index
            count += 1
            visited[count] = self.index

        # setting the colors of the arcs
        colors = (RED,YELLOW,BLUE,RED)
        colors = color_gradient(colors, count)
        # VIBGYOR.reverse()
        arcs.set_color_by_gradient(colors)

        # frame = self.camera.frame

        # rendering the sequence
        for i, arc in enumerate(arcs):
            max_width = max(max_width, max(visited[:i + 2]))

            # as the frame width changes, the arcs starts to look thinner, so increasing
            # the stroke width of all arcs as frame width increases.
            arcs.set_stroke(width=arcs.get_stroke_width() * 1.028)

            self.play(
                Create(arc),
                # self.camera.frame.animate.reset_pixel_shape(self.arc.get_heigth(),max_width),
                # self.camera.frame.animate.move_to(max_width / 2 * RIGHT),
                self.frame_j
                # self.camera.auto_zoom(arc, margin=100,only_mobjects_in_frame=False, animate=True),
                rate_func=linear,
                run_time=0.25
            )

