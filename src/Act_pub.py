#!/usr/bin/env python2
import rospy
import sys


from std_msgs.msg import String
from std_msgs.msg import Int32
#from dynamixel_workbench_msgs.msg import DynamixelStateList

#from dynamixel_workbench_msgs.srv import DynamixelCommand

if __name__=='__main__':
    try:
	x=0
	rospy.init_node('Gesture_pub',anonymous=True)
        pub=rospy.Publisher('/Gesture_Info',Int32,queue_size=1)
        while not rospy.is_shutdown():
		print('1: Namaste')
		print('2: Handshake')
		print('3: Hi')
		print('4: Dab')
		print('5:Defence')
		print('Any other choice will go to Home Position')
		try:
			x=int(input("Enter a choice: "))
		except:
			print('Please give a integer input')
		pub.publish(x)
	    	rospy.sleep(2)
    except rospy.ROSInterruptException:
        rospy.loginfo('Execution Interrupted.Try again')

