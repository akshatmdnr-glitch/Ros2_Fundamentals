import rclpy
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__('parameter_node')

        # Declare a parameter with a default value
        self.declare_parameter('message', 'Hello ROS2!')

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        message = self.get_parameter('message').value
        self.get_logger().info(message)


def main(args=None):
    rclpy.init(args=args)

    node = ParameterNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()