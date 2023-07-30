#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

rospy.init_node('codigo4_quaternion_sub_pub', anonymous=True)

joint1_value = 0
joint2_value = 0
joint3_value = 0

def callback(data):
    global joint1_value, joint2_value, joint3_value
    joint1_value = data.x
    joint2_value = data.y
    joint3_value = data.z

sub = rospy.Subscriber("codigo3_point_sub_pub", Point, callback)
pub = rospy.Publisher('codigo4_quaternion_sub_pub', Quaternion, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    x_valor = joint1_value
    y_valor = joint2_value
    z_valor = joint3_value
    w_valor = joint1_value + joint2_value + joint3_value
    quaternion_message = Quaternion(x=x_valor, y=y_valor, z=z_valor, w=w_valor)
    rospy.loginfo("x: %d", joint1_value)
    rospy.loginfo("y: %d", joint2_value)
    rospy.loginfo("z: %d", joint3_value)
    rospy.loginfo("w: %d", w_valor)
    pub.publish(quaternion_message)
    rate.sleep()
