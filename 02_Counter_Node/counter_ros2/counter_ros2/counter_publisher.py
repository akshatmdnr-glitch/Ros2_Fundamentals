import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class CounterPublisher(Node):

    def __init__(self):
        super().__init__('counter_publisher')

        self.publisher = self.create_publisher(
            Int32,
            'counter',
            10
        )

        self.counter = 0

        self.timer = self.create_timer(
            1.0,
            self.publish_counter
        )

    def publish_counter(self):
        msg = Int32()

        self.counter += 1
        msg.data = self.counter

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Publishing: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = CounterPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()