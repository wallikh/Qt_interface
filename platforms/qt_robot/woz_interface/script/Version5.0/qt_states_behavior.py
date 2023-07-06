#! /usr/bin/env python
# coding: utf-8

import roslib
import rospy
roslib.load_manifest('woz_interface')
import actionlib
from woz_interface.msg import NameInfo
from woz_interface.msg import QT_BehaviorAction
from woz_interface.msg import QT_BehaviorGoal
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from qt_gesture_controller.srv import *
from qt_motors_controller.srv import *
from geometry_msgs.msg import Twist
import time
from synchroniser import TaskSynchronizer
from checking import check, my_callback
import qt_states as s 

import names as n
child_name = n.child_name
adult_name = n.adult_name
print(n.table)


mon_objet = check()
mon_objet.register_callback(my_callback)
# child_name = ""
# adult_name = ""
last_button = ""
is_clicked = False

class Qt_Behavior:  
    def human_callback(data):
        global last_button
        last_button = data.data
        global is_clicked
        variable_mise_a_jour = mon_objet.ma_variable = last_button
        if variable_mise_a_jour:
            is_clicked =  True
    rospy.Subscriber('human_presence', String, human_callback)

    def button_callback(data):
        global last_button
        last_button = data.data
        global is_clicked
        variable_mise_a_jour = mon_objet.ma_variable = last_button
        if variable_mise_a_jour:
            is_clicked =  True
    rospy.Subscriber('woz/button', String, button_callback)
  
    # def name_callback(msg):
    #     global child_name
    #     global adult_name
    #     child_name =  msg.first_name
    #     last_name = msg.last_name
    #     adult_name = msg.teacher_name
    #     print("==============================================",adult_name)
        
    # rospy.Subscriber('woz/nameinfo', NameInfo, name_callback) 

    def __init__(self):     
        # while s.child_name == "" or s.adult_name == "":
        #     time.sleep(0.2)
        #     pass       
        self.rate = rospy.Rate(10) # 10hz
        self.state_pub = rospy.Publisher('/robot_state', String, queue_size=10)
        self.speechSay_pub = rospy.Publisher("qt_robot/speech/say", String,queue_size=1)
        self.emotionShow_pub = rospy.Publisher("/qt_robot/emotion/show",String,queue_size=1)
        self.talker_pub = rospy.Publisher('/qt_robot/behavior/talkText', String, queue_size=1)

        self.state = 'begin'
        rospy.Timer(rospy.Duration( s.states[self.state][1][0][1]), self.time_callback, oneshot=True)
        self.head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)
        self.left_arm_pub = rospy.Publisher('/qt_robot/left_arm_position/command', Float64MultiArray, queue_size=1)
        self.right_arm_pub = rospy.Publisher('/qt_robot/right_arm_position/command', Float64MultiArray, queue_size=1)
        print("ici begin dans state : ",self.state)

    def time_callback(self, event):
    # go to next state
        print('time callback')
        triggers = s.states[self.state][1]
        # print('time_callback triggers :',triggers)
        for trigger in triggers:
            print('trigger :::',trigger)
            if trigger[0] == 'time':
                self.state = trigger[2]
                print('next_state1: ' + self.state)
                self.next_state()  
                print("srtie de time_callback")

    def entry_callback(self, last_button):
        print("button module qt_states **********:", last_button)
        # print("s.child_name  +-------------- :",adult_name )
       
        print(n.table)
        print("adult_name à l'ancienne",n.adult_name)
        # a , c = n.table
        # print("split : ",n.a, "split2 " )

        triggers = s.states[self.state][1]
        for trigger in triggers:
            if trigger[0] == 'woz':
                if trigger[2] == last_button:
                    self.state = trigger[2]
                    print('next_state2: ' + self.state)
                    self.next_state()
                    break;   


    def next_state(self):        
        if(self.state != 'end'):
            self.state_pub.publish(self.state)
            # send behavior
            behavior = s.states[self.state][0]

            if(len(behavior)):
                # AL machine => pass to smach
                print(self.state + ' =behavior=> ' + str(behavior))
                ts = TaskSynchronizer()
                if 'la' in behavior and ('g' not in behavior):
                    self.left_arm_pub.publish(Float64MultiArray(data=behavior['la']))
                if 'ra' in behavior and ('g' not in behavior):
                    self.right_arm_pub.publish(Float64MultiArray(data=behavior['ra']))
                if ('h' in behavior) and ('g' not in behavior):
                    self.head_pub.publish(Float64MultiArray(data=behavior['h']))   
                
                if ('e' in behavior) or ('g' in behavior) or ('s' in behavior):
                    rospy.wait_for_service('/qt_robot/motors/home')
                    rospy.wait_for_service('/qt_robot/gesture/play')
                    print("emotion gestes and say")
                    self.home_pose = rospy.ServiceProxy('/qt_robot/motors/home',home)
                    self.gesturePlay = rospy.ServiceProxy('/qt_robot/gesture/play', gesture_play)
                    print('calling speechSay and gesturePlay and EmotionShow')
                    txt = ""
                    if "adult_name" in behavior['s'] :
                        txt = behavior['s'].replace("adult_name",n.adult_name)
                    if "child_name" in behavior['s'] :
                        txt = behavior['s'].replace("child_name",n.child_name)    
                    start_time = time.time()
                    task1 = ts.sync([
                        (0, lambda:self.talker_pub.publish(txt[1:]) if txt.startswith('~') else self.speechSay_pub.publish(txt)),
                        (0, lambda: self.emotionShow_pub.publish(behavior['e'])),
                        (0, lambda: self.gesturePlay(behavior['g'],0.8) if (('h' not in behavior) and ('la' not in behavior) and ('ra' not in behavior) ) else '')
                                    ])
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if elapsed_time >  2.0:
                        print("ici home_pose ********************************")
                        task2 = ts.sync([(0, lambda: self.home_pose(['head','left_arm','right_arm']))])
                    print("fin de  home_pose ********************************")
                    print('speechSay and gesturePlay and EmotionShow finished.')
                    print("Temps écoulé :::::::::::::::::::::::::::::::::::", elapsed_time, "secondes")
            # prepare jump for next state
            triggers = s.states[self.state][1]
            # print(self.state + ' =trig=> ' + str(triggers))
            for trigger in triggers:
                if trigger[0] == 'time':
                    rospy.Timer(rospy.Duration(trigger[1]), self.time_callback, oneshot=True)
              

    def execute(self):
        while not rospy.is_shutdown():
            global is_clicked
            if (is_clicked):
                self.entry_callback(last_button)
            is_clicked = False
            time.sleep(0.5)
            if self.state == 'end': break
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node("qt_states_behavior", anonymous=True)    
    try:
        qt_behavior = Qt_Behavior()
        qt_behavior.execute()
    except rospy.ROSInterruptException: pass