#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("yao_node")   #参数为这个节点的名称
    rospy.logwarn("yao_node节点初始化成功！")

    pub = rospy.Publisher("Adiran_Second_Topic",String,queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("开始发送消息！")
        msg = String()
        msg.data = "Adiran_Second_msg"
        pub.publish(msg)
        rate.sleep()