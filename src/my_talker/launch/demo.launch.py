import math                                            # for cos() and sin()
import rclpy                                          # ROS 2 Python library
from rclpy.node import Node                           # base class for every node


class TurtleCircle(Node):
    def __init__(self):
        super().__init__('turtle_circle')             # register node name
        # Use raw rosBus to publish turtlesim pose (bypasses rclpy message types)
        import js                                       # access the browser JavaScript environment
        self.bus = js.window.rosBus                    # rosBus is the in-browser ROS message bus
        self.t   = 0.0                                 # elapsed time (drives the circle parameter)
        self.timer = self.create_timer(0.05, self.step)  # update pose at 20 Hz
        self.get_logger().info('Turtle circle started!')

    def step(self):                                    # called every 0.05 s
        self.t += 0.05                                 # advance the parameter
        x     = 5.5 + 3.0 * math.cos(self.t)         # x centre ± 3 units radius
        y     = 5.5 + 3.0 * math.sin(self.t)         # y centre ± 3 units radius
        theta = self.t + math.pi / 2                  # heading = tangent to the circle
        self.bus.publish(
            '/turtle1/pose', 'turtlesim/Pose',        # topic and message type
            {'x': x, 'y': y, 'theta': theta,
             'linear_velocity': 1.0, 'angular_velocity': 1.0}  # position + speed
        )


def main(args=None):
    rclpy.init(args=args)                               # start the ROS 2 runtime
    rclpy.spin(TurtleCircle())                          # create node and loop until Ctrl-C
    rclpy.shutdown()                                    # clean up