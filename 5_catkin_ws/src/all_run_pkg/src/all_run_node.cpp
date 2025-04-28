#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "all_run_node");

    while(ros::ok())
    {
        ros::spinOnce();
    }
    
    return 0;
}