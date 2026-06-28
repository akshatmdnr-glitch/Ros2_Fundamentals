import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')

        self.publisher = self.create_publisher(
            String,
            'hello_topic',
            10
        )

        self.counter = 0

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

    def publish_message(self):
        msg = String()

        self.counter += 1
        msg.data = f'Hello ROS2 {self.counter}'

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Publishing: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()