#!/usr/bin/env python3


import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2


class GreenObjectDetector:

    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.callback)
        self.pub_coord = rospy.Publisher("/green_object_coordinates",Point, queue_size=10)

    def callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_green = (40, 110, 40)
        upper_green = (80, 255, 200)
        mask = cv2.inRange(hsv_image, lower_green, upper_green)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.pub_coord.publish(Point((x+w)/2,(y+h)/2,0))
        cv2.imshow("Green Object Detector", cv_image)
        cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node('green_object_detection_node')
    detector = GreenObjectDetector()
    rospy.spin()