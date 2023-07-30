#!/usr/bin/env python3
# --------------nodo suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# Función de callback que se ejecuta cuando se recibe un mensaje en el tópico "floatpub"
def callback(data):
    rospy.loginfo("Resultado redondeado recibido: %f", data.data)

# Inicialización del nodo
rospy.init_node('codigo3_sub', anonymous=True)

# Se crea un suscriptor para el tópico "floatpub" que ejecuta la función de callback
sub = rospy.Subscriber("codigo2_sub_pub", Float64, callback)

# Mantener el nodo en ejecución
rospy.spin()
