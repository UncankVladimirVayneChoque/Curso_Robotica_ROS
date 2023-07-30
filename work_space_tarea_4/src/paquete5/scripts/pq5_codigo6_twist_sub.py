#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('pq5_codigo6_twist_sub', anonymous=True)	

joint1_value = 0
joint2_value = 0
joint3_value = 0
joint4_value = 0
joint5_value = 0
joint6_value = 0

def callback(data):
    global joint1_value,joint2_value,joint3_value,joint4_value,joint5_value,joint6_value
    joint1_value = data.linear.x;
    joint2_value = data.linear.y;
    joint3_value = data.linear.z;
    joint4_value = data.angular.x;
    joint5_value = data.angular.y;
    joint6_value = data.angular.z;
    # print("linear.x: ", joint1_value)
    # print("linear.y: ", joint2_value)
    # print("linear.z: ", joint3_value)
    # print("angular.x: ", joint4_value)
    # print("angular.y: ", joint5_value)
    # print("angular.z: ", joint6_value)

sub = rospy.Subscriber("pq5_codigo5_twist_sub_pub", Twist, callback)
rate = rospy.Rate(1) # 1hz

while not rospy.is_shutdown():
    rospy.loginfo("lineal.x: %d", joint1_value)
    rospy.loginfo("lineal.y: %d", joint2_value)
    rospy.loginfo("lineal.z: %d", joint3_value)
    rospy.loginfo("angular.x: %d", joint4_value)
    rospy.loginfo("angular.y: %d", joint5_value)
    rospy.loginfo("angular.z: %d", joint6_value)
    rate.sleep()