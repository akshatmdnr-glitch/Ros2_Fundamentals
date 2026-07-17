import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from countdown_action.action import Countdown


class CountdownClient(Node):

    def __init__(self):
        super().__init__('countdown_client')

        self._client = ActionClient(
            self,
            Countdown,
            'countdown'
        )

    def send_goal(self, seconds):

        goal_msg = Countdown.Goal()
        goal_msg.seconds = seconds

        self._client.wait_for_server()

        self._send_goal_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        self._send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return

        self.get_logger().info("Goal accepted")

        self._result_future = goal_handle.get_result_async()

        self._result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f"Remaining: {feedback.remaining}"
        )

    def result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f"Finished: {result.success}"
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = CountdownClient()

    node.send_goal(10)

    rclpy.spin(node)


if __name__ == '__main__':
    main()