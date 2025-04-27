#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("chao_node")
    rospy.logwarn("chao_node节点初始化成功！")

    pub = rospy.Publisher("Adiran_First_Topic",String,queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("开始发送消息！")
        msg = String()
        msg.data = "Adiran_First_msg"
        pub.publish(msg)
        rate.sleep()
