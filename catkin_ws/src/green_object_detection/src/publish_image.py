#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def camera_publisher():
    # Inicializar el nodo de ROS
    rospy.init_node('camera_publisher', anonymous=True)

    # Crear un objeto CvBridge
    bridge = CvBridge()

    # Crear un objeto VideoCapture para capturar imágenes desde la cámara
    cap = cv2.VideoCapture(0)

    # Crear un objeto ImagePublisher para publicar imágenes en el tópico de ROS
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)

    # Definir la frecuencia de publicación
    rate = rospy.Rate(10) # 10 Hz

    while not rospy.is_shutdown():
        # Capturar la imagen desde la cámara
        ret, frame = cap.read()

        # Comprobar si la captura de la imagen fue exitosa
        if not ret:
            rospy.logwarn("Error al capturar la imagen desde la cámara")
            continue

        # Convertir la imagen de OpenCV a un mensaje de imagen de ROS
        image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        # Publicar el mensaje de imagen en el tópico de ROS
        image_pub.publish(image_msg)

    # Liberar los recursos
    cap.release()

if __name__ == '__main__':
    try:
        camera_publisher()
    except rospy.ROSInterruptException:
        pass
