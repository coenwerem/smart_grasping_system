#!/usr/bin/env python
import rospy
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory

jointCommands = JointTrajectory()
point = JointTrajectoryPoint()

rospy.init_node('close_hand_node', anonymous=True)
pub = rospy.Publisher('/hand_controller/command', JointTrajectory, queue_size=1)
rate = rospy.Rate(1)

# Message Data
jointCommands.joint_names = ['H1_F1J1', 'H1_F1J2', 'H1_F1J3', 'H1_F2J1', 'H1_F2J2', 'H1_F2J3', 'H1_F3J1', 'H1_F3J2', 'H1_F3J3']

"""
Create target joint positions. J2: 1.05, J3: 1.57

""" 
point.positions = [0.0, 1.05, 1.57, 0.0, 1.05, 1.57, 0.0, 1.05, 1.57]

point.velocities = []
point.accelerations = []
point.effort = [] 
point.time_from_start.secs = 1
point.time_from_start.nsecs = 0

# Append target position to jointCommands message
jointCommands.points.append(point)

def close_robot_hand():
    while not rospy.is_shutdown():
        pub.publish(jointCommands)

if __name__ == "__main__":
    try:
        close_success_info = "Gripper closed!"
        rospy.loginfo(close_success_info)
        close_robot_hand()
        rate.sleep()

    except rospy.ROSInterruptException:
        pass