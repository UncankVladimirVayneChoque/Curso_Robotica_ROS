#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('pq5_codigo3_point_sub_pub', anonymous=True)	

int_value_1 = 0
int_value_2 = 0
int_value_3 = 0

def callback1(data1):	
    global int_value_1
    int_value_1=data1.data
    # print("Valor1: ", float_value_1)

def callback2(data2):
    global int_value_2
    int_value_2 = data2.data
    # print("Valor2: ", float_value_2)


# se suscribe al topico
sub = rospy.Subscriber("pq5_codigo1_pub", Int32, callback1)
sub = rospy.Subscriber("pq5_codigo2_pub", Int32, callback2)

pub = rospy.Publisher('pq5_codigo3_point_sub_pub', Point, queue_size=10)

rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    int_value_3 = int_value_1 + int_value_2
    punto = Point(int_value_1, int_value_2, int_value_3)
    rospy.loginfo("x: %d", int_value_1)
    rospy.loginfo("y: %d", int_value_2)
    rospy.loginfo("z: %d", int_value_3)
    pub.publish(punto)
    rate.sleep()