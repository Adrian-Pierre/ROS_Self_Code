#include <ros/ros.h>
#include <std_msgs/String.h>

void chao_callback(std_msgs::String msg)
{
    ROS_INFO(msg.data.c_str());
}
void yao_callback(std_msgs::String msg)
{
    ROS_WARN(msg.data.c_str());
}

int main(int argc, char *argv[])
{
  //setlocale(LC_ALL,"zh_CH.UTF-8");
    ros::init(argc, argv, "ma_node");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("Adiran_First_Topic", 10, chao_callback);
    ros::Subscriber sub_2 = nh.subscribe("Adiran_Second_Topic", 10, yao_callback);

    while(ros::ok())
    {
        ros::spinOnce();
    }
    
    return 0;
}
