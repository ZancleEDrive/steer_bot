#!/usr/bin/env python3
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def camera_cb(image_msg):
    bridge = CvBridge()
    image = bridge.imgmsg_to_cv2(image_msg, desired_encoding='passthrough')
    cv2.imshow("Camera", image)
    cv2.waitKey(1)
    
def main():
    rospy.init_node('camera_reader', anonymous=True)
    rospy.Subscriber("/steer_bot/rrbot/camera1/image_raw", Image, camera_cb)
    rospy.spin()

if __name__ == '__main__':
    main()