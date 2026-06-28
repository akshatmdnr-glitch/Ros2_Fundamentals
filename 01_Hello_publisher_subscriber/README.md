# ROS2 Project 01: Hello Publisher-Subscriber

## Objective

This project demonstrates the fundamental communication architecture of ROS2 using a publisher and subscriber node implemented in Python.

The goal of this project is to understand the following core ROS2 concepts:

- Nodes
- Topics
- Publishers
- Subscribers
- Message Types
- Timers
- Callbacks

---

## System Architecture

```text
Publisher Node
      |
      | publishes
      v
 /hello_topic
      |
      | subscribes
      v
Subscriber Node
```

---

## Project Structure

```text
hello_ros2/
├── package.xml
├── setup.py
├── setup.cfg
└── hello_ros2/
    ├── publisher.py
    └── subscriber.py
```

---

## Publisher Node

The publisher node publishes a message every second to the topic:

```text
/hello_topic
```

Example output:

```bash
Publishing: Hello ROS2 1
Publishing: Hello ROS2 2
Publishing: Hello ROS2 3
```

---

## Subscriber Node

The subscriber node listens to the `/hello_topic` topic and prints received messages.

Example output:

```bash
I heard: Hello ROS2 1
I heard: Hello ROS2 2
I heard: Hello ROS2 3
```

---

## ROS2 Commands Used

Build workspace:

```bash
colcon build
```

Source workspace:

```bash
source install/setup.bash
```

Run publisher:

```bash
ros2 run hello_ros2 publisher
```

Run subscriber:

```bash
ros2 run hello_ros2 subscriber
```

Inspect nodes:

```bash
ros2 node list
```

Inspect topics:

```bash
ros2 topic list
```

Inspect topic information:

```bash
ros2 topic info /hello_topic
```

Echo topic messages:

```bash
ros2 topic echo /hello_topic
```

---

## Concepts Learned

- A Node is an executable process.
- A Topic is a communication channel.
- A Publisher sends data to a topic.
- A Subscriber receives data from a topic.
- ROS2 communication is asynchronous.
- Timers can execute tasks periodically.

---

## Technologies Used

- Ubuntu 24.04
- ROS2 Jazzy Jalisco
- Python
- rclpy
- std_msgs

---
