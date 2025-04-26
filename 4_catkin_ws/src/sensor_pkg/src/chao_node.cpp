#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "chao_node");

    //printf("Hello World!\n");
    //printf("你好 世界\n");

    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("Adiran_First_Topic",10);

    ros::Rate loop_rate(10);

    while(ros::ok())
    {
        printf("Hello World!\n");
        std_msgs::String msg;
        msg.data = "Adiran_First_msg";
        pub.publish(msg);
        loop_rate.sleep();
    }
    
    return 0;
}
