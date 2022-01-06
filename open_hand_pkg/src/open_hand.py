#!/usr/bin/env python
import rospy
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory

jointCommands = JointTrajectory()
point = JointTrajectoryPoint()

rospy.init_node('open_hand_node', anonymous=True)
pub = rospy.Publisher('/hand_controller/command', JointTrajectory, queue_size=1)
rate = rospy.Rate(1)

# Message Data
jointCommands.joint_names = ['H1_F1J1', 'H1_F1J2', 'H1_F1J3', 'H1_F2J1', 'H1_F2J2', 'H1_F2J3', 'H1_F3J1', 'H1_F3J2', 'H1_F3J3']

"""
Create target joint positions. Setting the joint positions of a finger to 
0.0 will raise it up.

""" 
point.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

point.velocities = []
point.accelerations = []
point.effort = [] 
point.time_from_start.secs = 1
point.time_from_start.nsecs = 0

# Append target position to jointCommands message
jointCommands.points.append(point)

def open_robot_hand():
    while not rospy.is_shutdown():
        pub.publish(jointCommands)
        # rate.sleep()

if __name__ == "__main__":
    try:
        open_success_info = "Gripper opened!"
        rospy.loginfo(open_success_info)
        open_robot_hand()
        rate.sleep()

    except rospy.ROSInterruptException:
        pass