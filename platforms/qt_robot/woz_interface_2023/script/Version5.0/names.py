# import rospy
# from woz_interface.msg import NameInfo
# child_name = ""
# adult_name = ""

# table = []
# def name_callback(msg):
#         global child_name
#         global adult_name
#         global table
#         child_name =  msg.first_name
#         last_name = msg.last_name
#         adult_name = msg.teacher_name
#         table = [child_name,adult_name]
#         print("==============================================",adult_name)
#         return 
# rospy.Subscriber('woz/nameinfo', NameInfo, name_callback)

# a = name_callback


