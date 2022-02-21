#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String
from std_msgs.msg import Int32
#sys.path.append('~/ajit_ws/src/dynamixel_workbench_msgs/msg')
#sys.path.append('~/ajit_ws/src/dynamixel_workbench_msgs/msg')

from dynamixel_workbench_msgs.msg import DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand,DynamixelCommandRequest
Ajit_Pose_client=rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command',DynamixelCommand)

gesture=0
def command(m_id,val):
	Ajit_Pose=DynamixelCommandRequest()
	Ajit_Pose.id=m_id
	Ajit_Pose.addr_name='Goal_Position'
	Ajit_Pose.value=val
	a=Ajit_Pose_client(Ajit_Pose)
def Namaste():
	l=[(10,1292),(11,2299),(12,2967),(13,2912),(14,2877),(20,2661),(21,1829),(22,1222),(23,1114),(24,1429)]
 	for i in l:
		command(i[0],i[1])
def Hi():
	l=[(10,2048),(11,2048),(12,2048),(13,2048),(14,2048),(20,3246),(21,2601),(22,1339),(23,1363),(24,1700)]
 	for i in l:
		 command(i[0],i[1])
def Handshake():
	l=[(10,2048),(11,2048),(12,2048),(13,2048),(14,2048),(20,2523),(21,1911),(22,1886),(23,1420),(24,2036)]
 	for i in l:
	    	command(i[0],i[1])
def Dab():
	l=[(10,1882),(11,672),(12,1963),(13,2051),(14,2042),(20,3103),(21,1971),(22,1353),(23,1037),(24,2103)]
 	for i in l:
	    	command(i[0],i[1])
def Attack():
	l=[(10,1048),(11,2299),(12,2312),(13,2625),(14,2043),(20,2776),(21,1870),(22,1230),(23,722),(24,1939)]
 	for i in l:
	    	command(i[0],i[1])
def Safe():
	l=[(10,2048),(11,2048),(12,2048),(13,2048),(14,2048),(20,2048),(21,2048),(22,2048),(23,2048),(24,2048)]
	for i in l:
		command(i[0],i[1])

def AjitCallback(info):
	global gesture
	gesture=info.data
	print(gesture)
	if gesture==1:
		Safe()
	    	print('Executing Namaste')
          	Namaste()
            	rospy.sleep(2)
        elif gesture==2:
		Safe()
	    	print('Executing Handshake')
            	Handshake()
            	rospy.sleep(2)
        elif gesture==3:
		Safe()
		print('Executing Hi')
            	Hi()
		gesture=0
            	rospy.sleep(2)
        elif gesture==4:
		Safe()
		print('Executing Dab')
            	Dab()
		gesture=0
            	rospy.sleep(2)
	elif gesture==5:
		Safe()
		print('Executing Defence')
            	Attack()
		gesture=0
            	rospy.sleep(2)
	else:
		print('Going to home position')
	    	Safe()
	    	rospy.sleep(2)


if __name__=='__main__':
	try:
		while not rospy.is_shutdown():
        		rospy.init_node('Gesture_sub',anonymous=True)
        		rospy.Subscriber('/Gesture_Info',Int32,AjitCallback)
			rospy.spin()
        		
		#rospy.spin()
    	except:
        	pass
