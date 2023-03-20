#!/usr/bin/env python3
import rospy
from track_gazebo.msg import Point_array
from geometry_msgs.msg import Point


topic = "/cone_position"

if __name__ == '__main__':
    while 1:
        cone_pub = rospy.Publisher(topic, Point_array, queue_size=10)
        cone = Point()
        cones = Point_array()
        cone.x = 3
        cone.y = 3
        cones.points.append(cone)
        cone_pub.publish(cones)