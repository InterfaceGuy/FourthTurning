from manim import *

class RollingCircleScene(Scene):
    def construct(self):
        # Create the large circle
        large_circle = Circle(radius=4, color=WHITE)

        # Create the small circle
        small_circle_radius = 1.5
        small_circle = Circle(radius=small_circle_radius, color=BLUE)
        small_circle.move_to(large_circle.get_top() - small_circle_radius * UP)

        # Point on the small circle
        dot = Dot(small_circle.get_top(), color=RED)

        # Line to trace the path
        trace = VMobject(color=RED)
        trace.set_points_as_corners([dot.get_center(), dot.get_center()])

        # Update function for the rolling and dot position
        def update_small_circle(mob, dt):
            # Rotate the small circle
            angle = dt / small_circle_radius
            mob.rotate(-angle, about_point=large_circle.get_center())

            # Rotate the dot to keep its relative position on the small circle
            dot.rotate(3*angle, about_point=mob.get_center())

            # Update the trace
            trace.add_points_as_corners([dot.get_center()])

        # Add everything to the scene
        self.add(large_circle, small_circle, dot, trace)
        small_circle.add_updater(update_small_circle)

        # Animate
        self.wait(10)  # Duration of the animation
