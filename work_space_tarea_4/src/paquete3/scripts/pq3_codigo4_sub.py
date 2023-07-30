#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('pq3_codigo4_sub', anonymous=True)	

float_value=0

def callback(data):	
    global int_value
    float_value=data.data
    

sub = rospy.Subscriber("pq3_codigo3_sub_pub", Float64, callback)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    print("codigo4_sub: ", float_value)
    rate.sleep() # delay de 1 segundo