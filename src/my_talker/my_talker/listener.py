import rclpy                                          # ROS 2 Python library
from rclpy.node import Node                           # base class for every node
from std_msgs.msg import String                       # plain-text message type


class Listener(Node):
    def __init__(self):
        super().__init__('listener')                   # register this node as 'listener'
        self.sub = self.create_subscription(
            String, '/chatter', self.on_msg, 10)       # subscribe to /chatter, call on_msg each time
        self.get_logger().info('Listener ready — waiting for messages…')

    def on_msg(self, msg):                             # called automatically for each incoming message
        self.get_logger().info(f'Heard: {msg.data}')  # print the received text to terminal


def main(args=None):
    rclpy.init(args=args)                               # start the ROS 2 runtime
    rclpy.spin(Listener())                              # create node and loop until Ctrl-C
    rclpy.shutdown()                                    # clean up when done