# Project 02: ROS2 Counter Publisher-Subscriber

## Overview

This project demonstrates the basic Publisher-Subscriber communication model in ROS2 using integer messages. A publisher node continuously publishes incrementing integer values, while a subscriber node receives and displays them.

This project builds upon the concepts learned in Project 01 and introduces the concept of maintaining state inside a ROS2 node.

---

## Concepts Learned

* ROS2 Nodes
* ROS2 Topics
* Publishers
* Subscribers
* Message Types
* Timers
* Callback Functions
* State Variables
* Package Structure
* Workspace Building and Sourcing

---

## Project Structure

```text
counter_ros2/
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
│   └── counter_ros2
└── counter_ros2/
    ├── __init__.py
    ├── counter_publisher.py
    └── counter_subscriber.py
```

---

## Node Architecture

```text
Counter Publisher Node
           |
           | publishes Int32 messages
           v
       /counter
           |
           | subscribes
           v
Counter Subscriber Node
```

---

## Message Type Used

```python
std_msgs/msg/Int32
```

Example messages:

```text
1
2
3
4
5
...
```

---

## Counter Publisher

The publisher node:

* Creates a publisher on the `/counter` topic.
* Maintains an internal counter variable.
* Increments the counter every second.
* Publishes the updated value.

Example output:

```text
[counter_publisher]: Publishing: 1
[counter_publisher]: Publishing: 2
[counter_publisher]: Publishing: 3
```

---

## Counter Subscriber

The subscriber node:

* Subscribes to the `/counter` topic.
* Receives integer messages.
* Prints the received values.

Example output:

```text
[counter_subscriber]: Received: 1
[counter_subscriber]: Received: 2
[counter_subscriber]: Received: 3
```

---

## Build Instructions

Navigate to the workspace:

```bash
cd ~/ros2_learning_ws
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## Running the Project

### Terminal 1

```bash
source ~/ros2_learning_ws/install/setup.bash
ros2 run counter_ros2 counter_publisher
```

### Terminal 2

```bash
source ~/ros2_learning_ws/install/setup.bash
ros2 run counter_ros2 counter_subscriber
```

---

## ROS2 Inspection Commands

List active nodes:

```bash
ros2 node list
```

List topics:

```bash
ros2 topic list
```

Inspect the topic:

```bash
ros2 topic info /counter
```

Monitor messages:

```bash
ros2 topic echo /counter
```

---

## Key Takeaways

This project introduced the concept of maintaining state inside a ROS2 node using class variables. It also demonstrated that the ROS2 Publisher-Subscriber architecture remains the same regardless of the data type being transmitted.

---

