import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class CmdVelWrapper(Node):

    def __init__(self):
        super().__init__('cmd_vel_wrapper')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.publisher = self.create_publisher(Twist, '/commands/velocity', 10)

    def listener_callback(self, msg):
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = CmdVelWrapper()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
