#!/usr/bin/env python3
#--------------publicador de Float64--------------
import rospy
from std_msgs.msg import Float64
import random

#el codigo se identifica ante ros
rospy.init_node('codigo2_pub', anonymous=True)

#se crea el publicador
pub = rospy.Publisher('codigo2_pub', Float64, queue_size=1)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    valor=round(random.uniform(10, 100), 2) #valor random con 2 decimales
    print("valor2: ", valor)
    pub.publish(valor) # se publica el valor
    rate.sleep() # delay de 1 segundo