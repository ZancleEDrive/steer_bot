#!/usr/bin/env python3
import rospy
from track_gazebo.msg import Point_array, Cone

topic = "/cone_position"

if __name__ == '__main__':
    while 1:
        rospy.init_node("track_generator", anonymous=True)
        cone_pub = rospy.Publisher(topic, Point_array, queue_size=10)
        cone = Cone()
        cones = Point_array()
        cone.x = 3
        cone.y = 3
        cone.color = 0
        cones.points.append(cone)
        cone_pub.publish(cones)