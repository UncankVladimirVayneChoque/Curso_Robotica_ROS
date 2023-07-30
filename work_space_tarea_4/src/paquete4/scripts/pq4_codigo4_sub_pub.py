#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('pq4_codigo3_sub_pub', anonymous=True)	

float_value_1 = 0
float_value_2 = 0
float_value_3 = 0

def callback1(data1):	
    global float_value_1
    float_value_1=data1.data
    # print("Valor1: ", float_value_1)

def callback2(data2):
    global float_value_2
    float_value_2 = data2.data
    # print("Valor2: ", float_value_2)

def callback3(data3):
    global float_value_3
    float_value_3 = data3.data


# se suscribe al topico
sub = rospy.Subscriber("pq4_codigo1_pub", Float64, callback1)
sub = rospy.Subscriber("pq4_codigo2_pub", Float64, callback2)
sub = rospy.Subscriber("pq4_codigo3_pub", Float64, callback3)

pub = rospy.Publisher('pq4_codigo4_sub_pub', Point, queue_size=10)

rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    punto = Point(float_value_1, float_value_2, float_value_3)
    print(float_value_1, " ", float_value_2, " ", float_value_3)

    pub.publish(punto)

    rate.sleep()