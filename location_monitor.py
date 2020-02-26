import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rospy.loginfo('x: {}, y: {}'.format(x,y))


def main():
    rospy.init_node('location_monitor')
    rospy.Subscriber("/odometry/filtered", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
