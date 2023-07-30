#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('pq3_codigo3_sub_pub', anonymous=True)	

float_value_1 = 0
float_value_2 = 0

def callback1(data1):	
    global float_value_1
    float_value_1=data1.data
    # print("Valor1: ", float_value_1)

def callback2(data2):
    global float_value_2
    float_value_2 = data2.data
    # print("Valor2: ", float_value_2)


# se suscribe al topico
sub = rospy.Subscriber("pq3_codigo1_pub", Float64, callback1)
sub = rospy.Subscriber("pq3_codigo2_pub", Float64, callback2)
pub = rospy.Publisher('pq3_codigo3_sub_pub', Float64, queue_size=10)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s

while not rospy.is_shutdown():
    resultado =  float_value_1 + float_value_2
    resultado_redondeado = round(resultado, 2)
    print("Resultado codigo3_sub_pub: ", resultado_redondeado)
    pub.publish(resultado_redondeado)
    rate.sleep() # delay de 1 segundo