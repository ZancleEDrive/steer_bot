#!/usr/bin/env python3
import rospy
from track_gazebo.msg import Point_array
from geometry_msgs.msg import Point


topic = "/cone_position"

def callback(msg):
    pass

if __name__ == '__main__':
    rospy.Subscriber(topic, Point_array, callback)