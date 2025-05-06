#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

def chao_callback(msg):
    rospy.loginfo(msg.data)

def yao_callback(msg):
    rospy.logwarn(msg.data)

if __name__ == "__main__":
    rospy.init_node("ma_node")   #参数为这个节点的名称
    rospy.logwarn("ma_node节点初始化成功！") 

    sub = rospy.Subscriber("Adiran_First_Topic",String,chao_callback,queue_size=10)
    sub1 = rospy.Subscriber("Adiran_Second_Topic",String,yao_callback,queue_size=10)

    rospy.spin()
    