#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from woz_interface.msg import NameInfo
from checking import check, my_callback
mon_objet = check()
mon_objet.register_callback(my_callback)
is_clicked = False
import time
fname = ""
def name_callback(msg):
        print("============================================================")
        global fname
        fname =  msg.first_name
        print("fname :::::::_-_-_-_-_ ",fname)
        # rospy.loginfo("Last name: %s", msg.last_name)
        fname2 = msg.teacher_name
        print("fname2 ::::::_-_-_-_-_-_ ",fname2)
        global is_clicked
        variable_mise_a_jour = mon_objet.ma_variable = fname
        if variable_mise_a_jour:
            is_clicked =  True

def callback2(data):
    global button_data
    button_data = data.data
    print(data.data)
  

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('woz/button', String, callback2)
    rospy.Subscriber('woz/nameinfo', NameInfo, name_callback) 
    print(is_clicked) 
   
       
    if is_clicked:
        f = fname
        print("fname ++++++++++++++++",f)
    rospy.spin()

if __name__ == '__main__':
   listener()


# def execute(self):

# global my_button
# last_modified_time = os.stat(chemin_fichier).st_mtime
# while not rospy.is_shutdown():
#     if os.stat(chemin_fichier).st_mtime != last_modified_time:
#         my_button = woz_button()
#         print("°°°°°°°°°°°°°°° Le fichier de configuration a été modifié °°°°°°°°°°°°°°°°°°")
#         print("--------- ",my_button," ------------")
#         last_modified_time = os.stat(chemin_fichier).st_mtime
#         if (my_button != ""):
#             self.button_callback(my_button)
#     time.sleep(1)
#     if self.state == 'end': break
#     self.rate.sleep()




# def execute(self):
#         last_button_value = ""
#         counter =[]
        
#         # print("counter : ", counter, "size_counter : ",size_counter)
#         while not rospy.is_shutdown():
#             size_counter = len(counter)
#             # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   :::  ",rospy.Subscriber('woz/button', String, self.callback))
#             if ((my_button != last_button_value) or ( len(counter) != size_counter)):
                
#                 counter.append(my_button)
#                 print("Le bouton a été modifié :", my_button)
#                 last_button_value = my_button
#                 self.button_callback(my_button)
#                 print("counter : ", counter, "size_counter : ",size_counter)
#                 print("len(counter) ++++++++++++++++++++++++ : ", len(counter), "size_counter : ",size_counter)
                

                
#             time.sleep(1)
#             if self.state == 'end': break
#             self.rate.sleep()