# publisher.py
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('topic_name', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        name_str = "naman"
        rospy.loginfo(name_str)
        pub.publish(name_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
