import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from countdown_action.action import Countdown


class CountdownServer(Node):

    def __init__(self):
        super().__init__('countdown_server')

        self._action_server = ActionServer(
            self,
            Countdown,
            'countdown',
            self.execute_callback
        )

        self.get_logger().info("Countdown Action Server Started")

    def execute_callback(self, goal_handle):

        self.get_logger().info(
            f"Received countdown goal: {goal_handle.request.seconds}"
        )

        feedback_msg = Countdown.Feedback()

        for i in range(goal_handle.request.seconds, 0, -1):

            feedback_msg.remaining = i

            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(
                f"Remaining: {i}"
            )

            time.sleep(1)

        goal_handle.succeed()

        result = Countdown.Result()
        result.success = True

        return result


def main(args=None):

    rclpy.init(args=args)

    node = CountdownServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()