# subscriber.py
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s", data.data)

def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('topic_name', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
