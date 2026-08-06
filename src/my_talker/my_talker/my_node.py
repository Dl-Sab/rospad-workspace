import rclpy                                          # ROS 2 Python library
from rclpy.node import Node                           # base class for every node
from std_msgs.msg import String                       # plain-text message type


class Talker(Node):                                    # our node inherits from Node
    def __init__(self):
        super().__init__('talker')                     # register the node name on the ROS graph
        self.pub   = self.create_publisher(String, '/chatter', 10)  # publish String on /chatter, queue 10
        self.timer = self.create_timer(1.0, self.publish_msg)       # call publish_msg every 1 second
        self.count = 0                                  # counter tracks how many messages sent
        self.get_logger().info('Talker started!')      # print startup message to terminal

    def publish_msg(self):                             # called by the timer every second
        msg = String()                                  # create a blank String message
        msg.data = f'Hello ROS2! count={self.count}'  # fill in the text field
        self.pub.publish(msg)                           # send the message to /chatter
        self.get_logger().info(f'Publishing: {msg.data}')  # echo to terminal
        self.count += 1                                # increment the counter


def main(args=None):
    rclpy.init(args=args)                               # start the ROS 2 runtime
    rclpy.spin(Talker())                                # create node and loop until Ctrl-C
    rclpy.shutdown()                                    # clean up when done