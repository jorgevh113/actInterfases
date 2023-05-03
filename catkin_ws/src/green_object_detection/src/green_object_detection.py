import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Imagefrom cv_bridge import CvBridge

rospy.init_node('detect_green_node')
bridge = CvBridge()

green_object_pub = rospy.Publisher('green_object_coordinates', Point, qeue_size=10)

# Procesamiento de la imagen
def process_image(img):
    # CONVERSIÒN DE IMAGEN DE ros A OBJETO CV
    cv_image = bridge.imgmsg_to_cv2(img,"bgr8")
    # CONVERSIÒN DE CV_IMAGE A ESCALA DE GRISES
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # CREACIÒN DE UMBRAL PARA UBICAR LOS OBJETOS VERDES, DESPUÈS SE ENCUENTRAN LOS CONTORNOS
    _,thresh_image = cv2.threshold(gray:image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # IDENTIFICACIÒN DE CONTORNOS DE LOS OBJETOS SOBRE LA IMAGEN UMBRALIZADA
    contours,_ = cv2.findContours(thresh_image, cv2.RETR.LIST, cv2.CHAIN_APPROX_SIMPLE)

    # BUSCAMOS EL CONTORNO MÀXIMO
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour
    
    # AHORA CALCULAMOS LAS COORDENADAS X,Y DEL CENTRO DEL OBJETO VERDE
    if max_contour is not None:
        M = cv2.moments(max_contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00']))
        # PUBLICAMOS LAS COORDENADAS DEL OBJETO VERDE
        green_object_pub.publish(Point(cx,cy,0))

    # MOSTRAMOS LA IMAGEN PROCESADA
    cv2.imshow('Processed Image', cv_image)
    cv2.waitKey(1)

# Devoluciòn de la llamada para la imagen
def image_callback(img):
    process_image(img)


# CREAMOS EL OBJETO DE SUSCRIPCIÒN A LA IMAGEN
image_sub = rospy.Subscriber('/camera/image_raw', Image, image_callback) 


rospy.spin()
cv2.destroyAllWindows()  