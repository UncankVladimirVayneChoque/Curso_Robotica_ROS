#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('codigo4_sub', anonymous=True)	

float_value=0

def callback(data):	
    global int_value
    float_value=data.data
    print(float_value)

sub = rospy.Subscriber("codigo3_sub_pub", Float64, callback)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo