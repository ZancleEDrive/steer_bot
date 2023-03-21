#!/usr/bin/env python3
import rospy
from track_gazebo.msg import Point_array, Cone

topic = "/cone_position"

def callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node("track_visualizer", anonymous=True)
    rospy.Subscriber(topic, Point_array, callback)