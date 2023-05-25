#! /usr/bin/env python3
# coding: utf-8

# import roslib
# roslib.load_manifest('woz_interface')
# import rospy
# import rospkg
# import actionlib

# from std_msgs.msg import String
# from std_msgs.msg import Float64MultiArray

# from geometry_msgs.msg import Twist
# from theatre.msg import NaoBehaviorAction
# from theatre.msg import NaoBehaviorGoal

# import sys, select, termios, tty
# import numpy as np
# import pandas as pd
# #####################

# import roslib

# import rospy
# import actionlib
# from woz_interface.msg import NameInfo

# from std_msgs.msg import String
# from std_msgs.msg import Float64MultiArray
# from geometry_msgs.msg import Twist
# import time
# from synchroniser import TaskSynchronizer
# import random
# from checking import check, my_callback
# #######################""

# #nao
# from naoqi_bridge_msgs.msg import JointAnglesWithSpeed

# mon_objet = check()
# mon_objet.register_callback(my_callback)

# child_name = ""
# adult_name = ""
# my_button = ""
# is_clicked = False



# class NaoBehaviour:
#     def name_callback(msg):
#         print("============================================================")
#         global child_name
#         global adult_name
#         child_name =  msg.first_name
#         last_name = msg.last_name
#         print("child_name ::::::: ",child_name)
#         adult_name = msg.teacher_name
#         print("adult_name :::::: ",adult_name)
#     rospy.Subscriber('woz/nameinfo', NameInfo, name_callback)  
    
    

#     def callback(data):
#         global my_button
#         my_button = data.data
#         global is_clicked
#         variable_mise_a_jour = mon_objet.ma_variable = my_button
#         if variable_mise_a_jour:
#             is_clicked =  True
   
#     rospy.Subscriber('woz/button', String, callback)

#     def __init__(self):
#         self.rate = rospy.Rate(10) # 10hz

       


#         # state: ( {g: gesture, s: say, h: [head], la: [left_arm], ra: [right_arm], w: [x, y, z, ex, ey, ez]}, [(trigger, param, next_state)])
#         self.states = { 'begin': ( {}, [('time', 1, 'choice')]),

#                         'choice': ( {'g': '', 's': '' },
#                                         [    ('key', my_button, 'left'), ('key', my_button, 'right'),('key', my_button, 'upleft'),('key', my_button, 'upright'),
#                                             ('key', my_button, 'up'), ('key', my_button, 'center'), ('key', my_button, 'down'),('key', my_button, 'right'),
#                                             ('key', my_button, 'downleft'),('key', my_button, 'downright'),

#                                             ('key', 'Z', 'LSU'),('key', 'X', 'LSD'),

#                                             ('key', my_button, 'hello'),('key', my_button, 'dontknow'),('key', my_button, 'oui'),('key', my_button, 'non'),('key', my_button, 'suivi'),('key', my_button, 'public'),
#                                             ('key', my_button, 'objetDroite'),('key', my_button, 'objetGauche'),('key', my_button, 'pense'),('key', my_button, 'pense2'),('key', my_button, 'neutral'),
#                                             ('key', my_button, 'really'),('key', my_button, 'comment'),('key',my_button,'jaime'),('key',my_button,'bored'),('key',my_button,'happy'),('key', my_button, 'sad'),
#                                             ('key', my_button, 'standup'),('key', my_button, 'kisses'),('key', my_button, 'excited'),('key', my_button, 'thinking'),('key', my_button, 'curious'),
#                                             ('key', my_button, 'fear'),('key', my_button, 'confused'),

#                                             ('key', my_button, 'walk_fwd'), ('key', my_button, 'stop'), ('key', my_button, 'walk_back'),
#                                             ('key', my_button, 'strife_left'), ('key', my_button, 'strife_right'),
#                                             ('key', my_button, 'rotate_left'), ('key', my_button, 'rotate_right'),

#                                             ('key', my_button, 'end')]),

#                         'up': ( {'s': '', 'h': [0.0,-1]}, [('time', 0.1, 'choice')]),
#                         'center': ( {'s': '', 'h': [0.0,+0.0]}, [('time', 0.1, 'choice')]),
#                         'down': ( {'s': '', 'h': [0.0,+1]}, [('time', 0.1, 'choice')]),
#                         'right': ( {'s': '', 'h': [-2,+0.0]}, [('time', 0.1, 'choice')]),
#                         'left': ( {'s': '', 'h': [+2,+0.0]}, [('time', 0.1, 'choice')]),
#                         'up_right': ( {'s': '', 'h': [-0.5,-5.0]}, [('time', 0.1, 'choice')]),
#                         'up_left': ( {'s': '', 'h': [+0.5,-0.5]}, [('time', 0.1, 'choice')]),
#                         'down_right': ( {'s': '', 'h': [-0.5,+0.5]}, [('time', 0.1, 'choice')]),
#                         'down_left': ( {'s': '', 'h': [+0.5,+0.5]}, [('time', 0.1, 'choice')]),

#                         'LSD': ( {'s': '', 'la': [0.5,0,0,0,0,1]}, [('time', 1, 'see')]),
#                         'LSU': ( {'s': '', 'la': [-0.5,0,0,0,0,1]}, [('time', 1, 'see')]),
#                         'see': ( {'s': 'Did you see ?'}, [('time', 0.1, 'choice')]),



#                         'hello': ( {'g': 'hello', 's': '\\pau=4000\\Hello!', 'h': [0,0]}, [('time', 3, 'choice')]),
#                         'dontknow': ( {'g': 'dontknow', 's': '\\pau=1000\\I dont know'}, [('time', 3, 'choice')]),
#                         '_oui': ( {'g': 'oui', 's': '\\pau=50\\yes!'}, [('time', 3, 'choice')]),
#                         '_non': ( {'g': 'non', 's': '\\pau=5\\no!'}, [('time', 3, 'choice')]),
#                         'suivi': ( {'g': 'suivi', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
#                         'public': ( {'g': 'public', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
#                         'objetDroite': ( {'g': 'objetDroite', 's': '\\pau=9500\\Here !'}, [('time', 3, 'choice')]),
#                         'objetGauche': ( {'g': 'objetGauche', 's': '\\pau=9500\\Here !'}, [('time', 3, 'choice')]),
#                         'pense': ( {'g': 'pense', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
#                         'pense2': ( {'g': 'pense2', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
#                         'neutral': ( {'g': 'neutral', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
#                         'really': ( {'g': 'really', 's': '\\pau=2000\\really ?'}, [('time', 3, 'choice')]),
#                         '_comment': ( {'g': 'comment', 's': '\\pau=2000\\how ?'}, [('time', 3, 'choice')]),
#                         'jaime': ( {'g':'jaime', 's': '\\pau=1500\\ I love it !'}, [('time', 3, 'choice')]),
#                         'bored': ( {'g':'bored', 's': '\\pau=1500\\ Huff'}, [('time', 3, 'choice')]),
#                         'happy': ( {'g':'happy', 's': '\\pau=1500\\ YES !'}, [('time', 3, 'choice')]),
#                         'sad': ( {'g':'sad', 's': '\\pau=1500\\ oh'}, [('time', 3, 'choice')]),
#                         'standup': ( {'g':'standup'}, [('time', 3, 'choice')]),

#                         'kisses': ( {'g':'kiss'}, [('time', 3, 'choice')]),
#                         'excited': ( {'g':'excited','s': 'yes !'}, [('time', 3, 'choice')]),
#                         'thinking': ( {'g':'thinking'}, [('time', 3, 'choice')]),
#                         'curious': ( {'g':'curious','s': '\\pau=1500\\ oh'}, [('time', 3, 'choice')]),
#                         'fear': ( {'g':'fear'}, [('time', 3, 'choice')]),
#                         'confused': ( {'s':'okey','g': 'confused'}, [('time', 3, 'choice')]),


#                         'walk_fwd': ( {'w': [1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
#                         'stop': ( {'w': [0,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
#                         'walk_back': ( {'w': [-1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
#                         'strife_left': ( {'w': [0,1,0,0,0,0]}, [('time', 0.1, 'choice')]),
#                         'strife_right': ( {'w': [0,-1,0,0,0,0]}, [('time', 0.1, 'choice')]),
#                         'rotate_left': ( {'w': [0,0,0,0,0,1]}, [('time', 0.1, 'choice')]),
#                         'rotate_right': ( {'w': [0,0,0,0,0,-1]}, [('time', 0.1, 'choice')]),



#                         'end': ((), [('time', 0.1, 'end')]) }

#         # print(self.states)

#         self.state = 'begin'

#         self.angles_pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=10)
#         self.walk_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


#         rospy.Timer(rospy.Duration( self.states[self.state][1][0][1]), self.time_callback, oneshot=True)
#         print(self.state)


#     def time_callback(self, event):
#         # print("child_name   loop:  5 ", child_name)
#         # print("adult_name   loop:  6 ", adult_name)
#         # print("************************************************************",self.child_name1)

#     # go to next state
#         print('time callback')
#         triggers = self.states[self.state][1]
#         # print('time_callback triggers :',triggers)
#         for trigger in triggers:
#             print('trigger :::',trigger)
#             if trigger[0] == 'time':
#                 self.state = trigger[2]
#                 print('next_state1: ' + self.state)
#                 self.next_state()  
#                 print("srtie de time_callback")

#     def button_callback(self, my_button):
#         # print("child_name   loop:   ", child_name)
#         # print("adult_name   loop:   ", adult_name)
#         # print("child_name   loop: 7  ", child_name)
#         # print("adult_name   loop:  8 ", adult_name)
#         print('bouton            : ', my_button)
#         triggers = self.states[self.state][1]
#         # print('keyboard_callback triggers :',triggers)
#         for trigger in triggers:
#             # print('trigger :::',trigger)
#             if trigger[0] == 'key':
#                 # print("ici == key en str")
#                 # print(" trigger[1] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", trigger[1])
#                 if trigger[2] == my_button:
#                     print("ici == key en vrai bouton")
#                     self.state = trigger[2]
#                     print('next_state2: ' + self.state)
#                     self.next_state()
#                     break;   
# #        pass

#     def next_state(self):
#         if(self.state != 'end'):
#             self.state_pub.publish(self.state)
#             # send bhw
#             bhw = self.states[self.state][0]
#             if(len(bhw)):
#                 # AL machine => pass to smach
#                 print(self.state + ' =bhw=> ' + str(bhw))

#                 if 'h' in bhw:
#                     self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['HeadYaw', 'HeadPitch'], joint_angles=bhw['h'], speed=0.25))
#                 if 'la' in bhw:
#                     self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand'], joint_angles=bhw['la'], speed=0.25))
#                 if 'ra' in bhw:
#                     self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand'], joint_angles=bhw['ra'], speed=0.25))
#                 if ('g' in bhw) or ('s' in bhw):
#                     client = actionlib.SimpleActionClient('/qt_action_behavior', NaoBehaviorAction)
#                     client.wait_for_server()

#                     goal = NaoBehaviorGoal( gesture=bhw['g'] if 'g' in bhw else '',
#                                             speech=bhw['s'] if 's' in bhw else '')
#                     client.send_goal(goal)
#                     # ...
#                     client.wait_for_result()
#                     result = client.get_result()
#                 if 'w' in bhw:
#                     cmd_vel = Twist()
#                     cmd_vel.linear.x=bhw['w'][0]
#                     cmd_vel.linear.y=bhw['w'][1]
#                     cmd_vel.linear.z=bhw['w'][2]
#                     cmd_vel.angular.x=bhw['w'][3]
#                     cmd_vel.angular.y=bhw['w'][4]
#                     cmd_vel.angular.z=bhw['w'][5]
#                     self.walk_pub.publish(cmd_vel) 


#             # prepare jump for next state
#             triggers = self.states[self.state][1]

#             print(self.state + ' =trig=> ' + str(triggers))
#             for trigger in triggers:
#                 if trigger[0] == 'time':
#                     rospy.Timer(rospy.Duration(trigger[1]), self.time_callback, oneshot=True)


#     def execute(self):
#         global is_clicked 
        
#         while not rospy.is_shutdown():

#             if (is_clicked):
#                 self.button_callback(my_button)

#                 # print("child_name   loop:  13 ", child_name)
#                 # print("adult_name   loop:   14", adult_name)
#             is_clicked = False
#             time.sleep(0.5)
#             if self.state == 'end': break
#             self.rate.sleep()





# if __name__ == '__main__':
#     rospy.init_node("qt_states_behavior", anonymous=True)    

#     nao_play = NaoBehaviour()
#     nao_play.execute()
