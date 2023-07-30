#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('pq2_codigo2_sub_pub', anonymous=True)	

float_value=0

#se crea la funcion para recibir el mensaje del topico
def callback(data):	
    global float_value
    float_value=data.data
    # print("el valor recibido es: ", float_value)

# se suscribe al topico
sub = rospy.Subscriber("random_float", Float64, callback)
pub = rospy.Publisher('pq2_codigo2_sub_pub', Float64, queue_size=10)
# el codigo float_pub.py publica al topico 'random_float'

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    resultado =  float_value * float_value
    resultado_redondeado = round(resultado, 2)
    print("Resultado codigo_sub_pub: ", resultado_redondeado)
    pub.publish(resultado_redondeado)
    rate.sleep() # delay de 1 segundo