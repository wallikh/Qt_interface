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
import random
from checking import check, my_callback


mon_objet = check()
mon_objet.register_callback(my_callback)

child_name = ""
adult_name = ""
my_button = ""
is_clicked = False


class Qt_Behavior:

    def name_callback(msg):
        print("============================================================")
        global child_name
        global adult_name
        child_name =  msg.first_name
        last_name = msg.last_name
        print("child_name ::::::: ",child_name)
        adult_name = msg.teacher_name
        print("adult_name :::::: ",adult_name)
    rospy.Subscriber('woz/nameinfo', NameInfo, name_callback)  
    
    def nuitrack_callback(data):
        global my_button
        my_button = data.data
        # time.sleep(1)
        print("***********************************========================= :",my_button)
        global is_clicked
        variable_mise_a_jour = mon_objet.ma_variable = my_button
        if variable_mise_a_jour:
            is_clicked =  True
   
    rospy.Subscriber('human_presence', String, nuitrack_callback)

    def callback(data):
        global my_button
        my_button = data.data
        global is_clicked
        variable_mise_a_jour = mon_objet.ma_variable = my_button
        if variable_mise_a_jour:
            is_clicked =  True
   
    rospy.Subscriber('woz/button', String, callback)
       
    def __init__(self):

        while child_name == "" or adult_name == "":
            time.sleep(0.1)
            pass          
        self.rate = rospy.Rate(10) # 10hz
        self.state_pub = rospy.Publisher('/robot_state', String, queue_size=10)
        self.speechSay_pub = rospy.Publisher("qt_robot/speech/say", String,queue_size=1)
        self.emotionShow_pub = rospy.Publisher("/qt_robot/emotion/show",String,queue_size=1)
        self.talker_pub = rospy.Publisher('/qt_robot/behavior/talkText', String, queue_size=1)

        # state: ( {g: gesture, s: say, h: [head], la: [left_arm], ra: [right_arm], w: [x, y, z, ex, ey, ez]}, [(trigger, param, next_state)])
        self.states = { 'begin': ( {}, [('time', 1, 'choice')]),

                        'choice': ( {'g': '', 's': '', 'e':'' },
                                        # à implementer le joystique plutard debut
                                        [   ('key', my_button, 'left'), ('key', my_button, 'right'),('key', my_button, 'upleft'),('key', my_button, 'upright'),
                                            ('key', my_button, 'up'), ('key', my_button, 'center'), ('key', my_button, 'down'),('key', my_button, 'right'),
                                            ('key', my_button, 'downleft'),('key', my_button, 'downright'),
                                        ## à implemele joystic plutard fin
                                            ('key', my_button, 'la_joie'),('key', my_button, 'amusement'),('key', my_button, 'la_colere'),('key', my_button, 'la_motivation'),('key', my_button, 'la_fatigue'),('key', my_button, 'la_tristesse'),
                                            ('key', my_button, 'la_fierte'),('key', my_button, 'etonnement'),('key', my_button, 'adulte_accord'),('key', my_button, 'demande_adulte'),('key', my_button, 'que_pense'),
                                            ('key', my_button, 'monsieur'),('key', my_button, 'madame'),('key', my_button, 'bien'),('key', my_button, 'cest_mieux'),
                                            ('key', my_button, 'tu_mexplique'),('key',my_button, 'important'),('key', my_button, 'ensuite'),('key', my_button, 'pk_pas_bien'),
                                            ('key', my_button, 'tu_es_sur'),('key', my_button, 'plus_simple'),('key', my_button, 'plus_difficile'),
                                            ('key', my_button, 'bien_mal'),('key', my_button, 'pas_marche'),('key', my_button, 'pourquoi'),('key', my_button, 'ecrit'),('key', my_button, 'senslettre'),('key', my_button, 'fermelettre'),
                                            ('key', my_button, 'endroitlettre'),('key', my_button, 'bien_comme_toi'),('key', my_button, 'triche'),('key', my_button, 'facile'),('key', my_button, 'pas_trop_vite'),
                                            ('key', my_button, 'boum'),('key', my_button, 'tu_relances'),('key', my_button, 'je_bugue'),('key', my_button, 'je_rouille'),
                                            ('key', my_button, 'attends'),('key', my_button, 'malade'),('key', my_button, 'et_alors'),('key', my_button, 'jai_progresse'),
                                            ('key', my_button, 'cest_difficile'),('key', my_button, 'fais_mon_mieux'),('key', my_button, 'tas_gagne'),
                                                                                    ('key', my_button, 'ma_tablette'),('key', my_button, 'pas_mal'),('key', my_button, 'je_trouve_pas'),('key', my_button, 'respire'),('key', my_button, 'ecris_mal'),('key', my_button, 'cest_pas_grave'),
                                            ('key', my_button, 'reessayons'),('key', my_button, 'fera_mieux'),('key', my_button, 'courage'),('key', my_button, 'rate'),('key', my_button, 'difficile'),
                                            ('key', my_button, 'pas_content_moi'),('key', my_button, 'tu_mecoute'),('key', my_button, 'on_essaye'),('key', my_button, 'bravo'),
                                            ('key', my_button, 'je_suis_fort'),('key', my_button, 'cest_bien'),('key', my_button, 'tu_es_fort'),('key', my_button, 'nous_sommes_fort'),
                                            ('key', my_button, 'fier_de_toi'),('key', my_button, 'applique'),('key', my_button, 'tu_perseveres'),
                                            ('key', my_button, 'aie'),('key', my_button, 'ahahah'),('key', my_button, 'muscle'),('key', my_button, 'merci'),('key', my_button, 'repete'),('key', my_button, 'oui'),
                                            ('key', my_button, 'non'),('key', my_button, 'sais_pas_toi'),('key', my_button, 'et_toi'),
                                             
                                             # comportement de scenario
                                            ('key', my_button, 'pression_lance'),('key', my_button, 'pression_expli'),('key', my_button, 'pression_complet'),('key', my_button, 'archeo_lance'),('key', my_button, 'archeo_expli'),('key', my_button, 'archeo_complet'),
                                            ('key', my_button, 'drapeau_lance'),('key', my_button, 'drapeau_expli'),('key', my_button, 'drapeau_complet'),('key', my_button, 'alpha_lance'),('key', my_button, 'alpha_expli'),
                                            ('key', my_button, 'alpha_complet'),('key', my_button, 'zoo_lance'),('key', my_button, 'zoo_expli'),('key', my_button, 'zoo_complet'),
                                            ('key', my_button, 'chimi_lance'),('key',my_button, 'chimi_expli'),('key', my_button, 'tilt_lance'),('key', my_button, 'tilt_expli'),
                                            ('key', my_button, 'tilt_complet'),('key', my_button, 'cowritter_lance'),('key', my_button, 'cowritter_expli_class'),
                                            ('key', my_button, 'cowritter_complet'),('key', my_button, 'jus_lance'),('key', my_button, 'jus_expli'),('key', my_button, 'jus_complet'),('key', my_button, 'poursuite_lance'),('key', my_button, 'poursuite_expli'),
                                            ('key', my_button, 'poursuite_complet'),('key', my_button, 'tu_viens'),('key', my_button, 'ton_nom'),('key', my_button, 'ca_va'),('key', my_button, 'bonjour'),
                                            ('key', my_button, 'je_mappelle_qt'),('key', my_button, 'tu_veux_maider'),('key', my_button, 'tu_maides_encore'),('key', my_button, 'adieu'),
                                            ('key', my_button, 'adieu2'),('key', my_button, 'pause'),('key', my_button, 'change_jeu'),('key', my_button, 'choisis_jeu'),
                                            ('key', my_button, 'dernier_jeu'),('key', my_button, 'cetait_bien'),('key', my_button, 'tu_maide'),('key', my_button, 'mes_progres'),('key', my_button, 'bisou'),('key', my_button, 'bcp_travaille'),('key', my_button, 'il_est_lheure'),
                                            ('key', my_button, 'arrete'),('key', my_button, 'au_revoir'),
                                            # comportement theatre 
                                            ('key', my_button, 'hello'),('key', my_button, 'dontknow'),('key', my_button, '_oui'),('key', my_button, '_non'),('key', my_button, 'suivi'),('key', my_button, 'public'),
                                            ('key', my_button, 'objetDroite'),('key', my_button, 'objetGauche'),('key', my_button, 'pense'),('key', my_button, 'pense2'),('key', my_button, 'neutral'),
                                            ('key', my_button, 'really'),('key', my_button, 'comment'),('key', my_button, 'jaime'),('key', my_button, 'happy'),
                                            ('key', my_button, 'kisses'),('key', my_button, 'excited'),('key', my_button, 'thinking'),('key', my_button, 'curious'),
                                            ('key', my_button, 'fear'),('key', my_button, 'confused'),('key', my_button, 'bored'),
                                            # nuitrack
                                            # ('key', my_button, 'human_0_appeared'),('key', my_button, 'human_0_disappeared'),
                                            # ('key', my_button, 'human_0_center'),('key', my_button, 'human_0_left'),('key', my_button, 'human_0_right'),
                                            ('key', my_button, 'human_0_center_1meter'),('key', my_button, 'human_0_left_1meter'),('key', my_button, 'human_0_right_1meter'),
                                            ('key', my_button, 'human_0_center_2meters'),('key', my_button, 'human_0_left_2meters'),('key', my_button, 'human_0_right_2meters'),
                                            # ('key', my_button, 'human_1_appeared'),('key', my_button, 'human_1_disappeared'),
                                            # ('key', my_button, 'human_1_center'),('key', my_button, 'human_1_left'),('key', my_button, 'human_1_right'),('key', my_button, 'human_1_1meter'),('key', my_button, 'human_1_2meter'),
                                            # ('key',my_button,'test1'),


                                            ('key', my_button, 'end')]),
                                            
                        # 'test1':({},[('key',my_button,'human_0_1meter'),('key',my_button,'human_0_2meter'),('time', 0.5, 'test1')]),
                        

                        # à implementer le joystique plutard debut
                        'up': ( {'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
                        'center': ( {'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
                        'down': ( {'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
                        'right': ( {'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
                        'left': ( { 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
                        'upright': ( { 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
                        'upleft': ( { 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
                        'downright': ( {'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
                        'downleft': ( { 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),
                         #   # à implementer le joystique plutard fin 
                        #nuitrack trigger
                        # 'human_0_appeared':( {'e': 'QT/happy', 'g': '', 's': 'hello'}, [('time', 5, 'choice')]),
                        # 'human_0_disappeared':( {'e': 'QT/happy', 'g': '', 's': 'au revoir'}, [('time', 5, 'choice')]),
                        # 'human_0_center':( {'e': 'QT/happy', 'g': '', 's': 'tu es au centre'}, [('time', 3, 'choice')]),
                        # 'human_0_left':( {'e': 'QT/happy', 'g': '', 's': 'tu es a gauche'}, [('time', 3, 'choice')]),
                        # 'human_0_right':( {'e': 'QT/happy', 'g': '', 's': 'tu es a droite'}, [('time', 3, 'choice')]),


                        'human_0_center_1meter':( {'e': 'QT/angry', 'g': 'QT/angry', 's': random.choice(['recule, je ne peux pas respirer','pas si prés, je ne peux pas respirer', "Recule, tu pues! Ouf", "On dirait que vous les humains n'avez jamais entendu parler d'intimité !"])}, [('time', 5, 'choice')]),
                        'human_0_left_1meter':( {'e': 'QT/kiss', 'g': 'QT/kiss', 's': random.choice(["\\pau=300\\ J'ai envie de te contempler. D'ailleurs tu me fais rougir !","Vas gauchement à droite ou droit à gauche!","\\vct=50\\ T'as jamais entendu parler de l'espace personnel ?"])}, [('time', 5, 'choice')]),
                        'human_0_right_1meter':( {'e': 'QT/angry', 'g': 'QT/angry', 's': random.choice(["\\vct=60\\ Ouste!\\sel=alt\\","\\vct=120\\ Tu es super \\sel=alt\\ collant!","\\vct=90\\ Pas si près, je suis claustrophobe!"])}, [('time', 5, 'choice')]),
                        
                        'human_0_center_2meters':( {'e': '', 'g': '', 's': random.choice(["Avance un peu, je ne te vois pas.","\\rspd=80\\ Je ne t'entends pas très bien.","Avance que je te vois.","\\vce=speaker=Lily\\ Un peu plus !","#SNEEZE01#Viens ! Tu me manques ! "])}, [('time', 5, 'choice')]),
                        'human_0_left_2meters':( {'e': '', 'g': '', 's': random.choice(["Là tu es hors du champ ma belle!","Comment tu t’appelles ? ","\\rmw=0\\ Qui es tu ?","Mais que fais-tu aussi loin ?\\pau=300\\ Tu sais que je te vois!","\\vce=speaker=Will\\Coucou ! "])}, [('time', 5, 'choice')]),
                        'human_0_right_2meters':( {'e': 'QT/happy', 'g': 'QT/happy', 's': random.choice(["Je t’aime mais je dois te quitter, adieu !","Tu  \\pau=300\\ me \\pau=300\\ manques. ","Sans toi ça sera mieux! "," Youuuhouuu ! Enfin tranquille !!"])}, [('time', 5, 'choice')]),

                        # 'human_0_2meters':( {'e': 'QT/happy', 'g': '', 's': random.choice(['avance un peu , je ne te voix pas',"je ne t'entend pas trés bien"])}, [('time', 5, 'choice')]),
                        
                        # 'human_1_appeared':( {'e': 'QT/happy', 'g': '', 's': 'hello un'}, [('time', 3, 'choice')]),
                        # 'human_1_disappeared':( {'e': 'QT/happy', 'g': '', 's': 'au revoir un'}, [('time', 3, 'choice')]),
                        # 'human_1_center':( {'e': 'QT/happy', 'g': '', 's': 'tu es au centre'}, [('time', 3, 'choice')]),
                        # 'human_1_left':( {'e': 'QT/happy', 'g': '', 's': 'tu es a gauche'}, [('time', 3, 'choice')]),
                        # 'human_1_right':( {'e': 'QT/happy', 'g': '', 's': 'tu es a droite'}, [('time', 3, 'choice')]),
                        # 'human_1_1meter':( {'e': 'QT/happy', 'g': '', 's': 'tu es a un mtre'}, [('time', 3, 'choice')]),
                        # 'human_1_2meter':( {'e': 'QT/happy', 'g': '', 's': 'tu es a deux mettres'}, [('time', 3, 'choice')]),
                        #  Theatre
                        'hello': ( {'e': 'QT/happy', 'g': 'QT/hi', 's': '\\pau=2000\\Salut!', 'h': [0,0]}, [('time', 1, 'choice')]),
                        'dontknow': ( {'e': '', 'g': 'QT/touch-head', 's': '~\\pau=500\\Je ne sais pas'}, [('time', 1, 'choice')]),
                        '_oui': ( {'e': '', 'g': 'QT/imitation/nodding-yes', 's': '~\\pau=500\\Oui!'}, [('time', 1, 'choice')]),
                        '_non': ( {'e': '', 'g': 'QT/emotions/sad', 's': '~\\pau=500\\Non!'}, [('time', 1, 'choice')]),
                        'suivi': ( {'e': 'QT/surprise', 'g': 'QT/imitation/head-right-left', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
                        'public': ( {'e': 'QT/surprise', 'h': [0.0,0.0], 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
                        'objetDroite': ( {'e': 'QT/happy', 'h': [+10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
                        'objetGauche': ( {'e': 'QT/happy', 'h': [-10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
                        'pense': ( {'e': 'QT/confused', 'g': 'QT/imitation/hands-on-hip', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
                        'pense2': ( {'e': 'QT/afraid', 'g': 'QT/touch-head-back', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
                        'neutral': ( {'e': 'QT/neutral', 'g': 'QT/neutral', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
                        'really': ( {'e': 'QT/dirty_face','g': 'QT/surprise', 's': '\\pau=2000\\Vraiment ?'}, [('time', 3, 'choice')]),
                        '_comment': ( {'e':'QT/surpise','g': 'QT/touch-head', 's': '\\pau=2000\\Comment ?'}, [('time', 3, 'choice')]),
                        'jaime': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=2000\\jème beaucoup !'}, [('time', 3, 'choice')]),
                        'happy': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=500\\ Youpi !'}, [('time', 3, 'choice')]),

                        'kisses': ( {'e':'QT/kiss','g': 'QT/kiss', 's' : ""}, [('time', 3, 'kisses1')]),
                        'kisses1': ( {'e':'QT/one_eye_wink','g': 'QT/neutral', 's' : ""}, [('time', 3, 'kisses2')]),
                        'kisses2': ( {'e':'QT/shy','h': [-10.0,+10.0], 's' : ""}, [('time', 3, 'choice')]),

                        'excited': ( {'e':'QT/surpise','g': 'QT/neutral', 's' : ""}, [('time', 3, 'excited1')]),
                        'excited1': ( {'e':'QT/happy','g': 'QT/neutral', 's' : ""}, [('time', 3, 'choice')]),

                        'thinking': ( {'e':'QT/surpise','g': 'QT/bored', 's' : ""}, [('time', 3, 'choice')]),

                        'curious': ( {'e':'QT/suprise','g': 'QT/neutral', 's' : ""}, [('time', 3, 'curious1')]),
                        'curious1': ( {'e':'QT/showing_smile','g': 'QT/neutral', 's' : ""}, [('time', 3, 'choice')]),

                        'fear': ( {'e':'QT/cry','g': 'QT/face', 's' : ""}, [('time', 3, 'choice')]),

                        'confused': ( {'e':'QT/confused','g': 'QT/neutral', 's' : ""}, [('time', 3, 'choice')]),
                        'bored': ( {'e':'QT/yawn','g': 'QT/bored', 's' : ""}, [('time', 3, 'choice')]),

                        #reaction
                        'la_joie': ( {'e':'QT/happy', 'g':'QT/so', 's': random.choice(['Quelle mine joyeuse', 'Quel booo  sourire', 'Quel enthousiassme']) }, [('time', 1, 'choice')]),
                        'amusement': ( {'e':'QT/happy', 'g':'QT/happy', 's': random.choice(["Ça a l'air de t'amuser!", "Tu as l'air de trouver que c'est drôle"]) }, [('time', 1, 'choice')]),
                        'la_colere': ( {'e':'QT/confused', 'g':'QT/head_scratch', 's': random.choice(['{}, Est-ce que tu es fâché?'.format( child_name), "Tu es en colère?", "Tu as l'air en colère"]) }, [('time', 1, 'choice')]),
                        'la_motivation': ( {'e':'QT/showing_smile', 'g':'QT/handclap', 's': random.choice(["Tu as l'air motivé", "{} , tu es très motivé aujourd'hui".format( child_name)]) }, [('time', 1, 'choice')]),
                        'la_fatigue': ( {'e':'QT/yawn', 'g':'QT/yawn', 's': "Je suis désolé. #YAWN01# je suis fatigué." }, [('time', 1, 'choice')]),
                        'la_tristesse': ( {'e':'QT/sad', 'g':'QT/thanks', 's': random.choice(["{} ,Est-ce que tu es triste?".format( child_name) , "Tu as de la\sel=alt=p-20\  peine?", "Quelque chose te rend triste?"]) }, [('time', 1, 'choice')]),
                        'la_fierte': ( {'e':'QT/showing_smile', 'g':'QT/yes', 's': random.choice(["Tu es fier de ton travail ?	", "Tu as l'air fier de ton travail"]) }, [('time', 1, 'choice')]),
                        'etonnement': ( {'e':'', 'g':'QT/curious', 's': random.choice(["Tu as l'air étonné", "Tu es étonné,"]) }, [('time', 1, 'choice')]),
                        
                        'adulte_accord': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': "%s ,tu es d'accord?" %adult_name }, [('time', 1, 'choice')]),
                        'demande_adulte': ( {'e':'QT/talking', 'g':'QT/angry', 's':"Demandons à %s" %adult_name }, [('time', 1, 'choice')]),
                        'que_pense': ( {'e':'QT/talking', 'g':'QT/challenge',  's': random.choice([ "%s, qu'en penses-tu ?" %adult_name, "Qu'est-ce que tu en pense %s ?" %adult_name]) }, [('time', 1, 'choice')]),
                        'monsieur': ( {'e':'', 'g':'', 's': "Monsieur!" }, [('time', 1, 'choice')]),
                        'madame': ( {'e':'', 'g':'', 's': "Madame!" }, [('time', 1, 'choice')]),

                        'bien': ( {'e':'QT/showing_smile', 'g':'', 's': random.choice(["C'est comme ça qu'il faut faire?", "Est-ce que c'est bien?"]) }, [('time', 1, 'choice')]),
                        'cest_mieux': ( {'e':'', 'g':'QT/bored', 's': random.choice(["Est-ce que je m'améliore?", "Je fais mieux kavant?"]) }, [('time', 1, 'choice')]),
                        'tu_mexplique': ( {'e':'QT/curious', 'g':'QT/confused', 's': random.choice(["tu m'expliques?", "Tu peux m'expliquer un peu?", "Olala. c'est difficile! Tu peux m'expliquer?"]) }, [('time', 1, 'choice')]),
                        'important': ( {'e':'QT/talking', 'g':'QT/challenge', 's': random.choice(["Qu'est-ce qu'on a fait qui est le plus important?", "C'est quoi le plus important dans ce qu'on a fait,"]) }, [('time', 1, 'choice')]),
                        'ensuite': ( {'e':'QT/showing_smile', 'g':'QT/angry', 's': random.choice(["Que fait-on maintenant pour que j'apprenne mieux à écrire", "Quel jeu pourrait le pluss m'aider tu penses"]) }, [('time', 1, 'choice')]),
                        'pk_pas_bien': ( {'e':'QT/sad', 'g':'QT/so', 's': random.choice(["Pourquoi c'est pas bien,", "Pourquoi, je ne fais pas comme il faut?", "Ah bon? Qu'est-ce qui ne va pas?"]) }, [('time', 1, 'choice')]),
                        'tu_es_sur': ( {'e':'QT/confused', 'g':'QT/head_scratch', 's': random.choice(["Tu es sûr?", "Tu es sûr de toi?", "Je ne suis pas sûr"]) }, [('time', 1, 'choice')]),
                        'plus_simple': ( {'e':'QT/talking', 'g':'', 's': "C'était quoi le plus simple pour toi " }, [('time', 1, 'choice')]),
                        'plus_difficile': ( {'e':'QT/talking', 'g':'', 's': "C'était quoi le plus difficile pour toi " }, [('time', 1, 'choice')]),
                        'bien_mal': ( {'e':'QT/talking', 'g':'', 's': "Qu'est-ce que je fais mal \sel=alt=p-50\ \Rspd=80\ et \sel=alt=p-50\ bien?" }, [('time', 1, 'choice')]),
                        'pas_marche': ( {'e':'QT/sad', 'g':'QT/thanks', 's': "Pourquoi ça n'a pas marché?" }, [('time', 1, 'choice')]),
                        'pourquoi': ( {'e':'', 'g':'', 's': random.choice(["Pourquoi?", "Pour quelle raison?"]) }, [('time', 1, 'choice')]),
                        
                        'ecrit': ( {'e':'', 'g':'QT/test', 's': "" }, [('time', 1, 'choice')]),
                        'senslettre': ( {'e':'QT/talking', 'g':'', 's':"Est-ce que je fais mes lettres en tournant dans le bon sens?" }, [('time', 1, 'choice')]),
                        'fermelettre': ( {'e':'QT/talking', 'g':'',  's': random.choice([ "Est-ce que mes lettres sont bien fermés?", "Est-ce que j'ai bien fermés mes lettres?", "Mes lettres sont fermés comme il faut?"]) }, [('time', 1, 'choice')]),
                        'endroitlettre': ( {'e':'QT/talking', 'g':'', 's': random.choice([ "Est-ce que je débute mes lettres où il faut?", "Est-ce qu'il y a des lettres que je ne commence pas au bon endroit?"])}, [('time', 1, 'choice')]),
                        'bien_comme_toi': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Mon mot \sel=alt=p-20\ \Rspd=80\ ressemble \Rspd=100\ à ce que tu as écrit?", "Est-ce que j'écris aussi bien que toi?", "J'écris bien comme toi?", "Mon mot est aussi beau que le tien?"]) }, [('time', 1, 'choice')]),

                        'triche': ( {'e':'QT/one_eye_wink', 'g':'QT/angry', 's': "Mais tu triche," }, [('time', 1, 'choice')]),
                        'facile': ( {'e':'QT/confused', 'g':'QT/challenge', 's':"Est-ce que c'est trop facile?" }, [('time', 1, 'choice')]),
                        'pas_trop_vite': ( {'e':'QT/talking', 'g':'',  's': random.choice([ "attention, ne va pas trop vite", "{} , ne va pas trop vite".format( child_name)]) }, [('time', 1, 'choice')]),
                        'boum': ( {'e':'', 'g':'QT/happy', 's':"Boum!"}, [('time', 1, 'choice')]),

                        'tu_relances': ( {'e':'', 'g':'QT/challenge', 's': random.choice([ "Tu peux relancer le jeu?", "Peux-tu relancer l'activité ?"])}, [('time', 1, 'choice')]),
                        'je_bugue': ( {'e':'QT/confused', 'g':'QT/thanks', 's': random.choice(["Ça n'a pas bien marché", "J'ai eu un bug"]) }, [('time', 1, 'choice')]),
                        'fatigue': ( {'e':'QT/yawn', 'g':'QT/yawn', 's': "Je suis désolé. #YAWN01# je suis fatigué." }, [('time', 1, 'choice')]),
                        'je_rouille': ( {'e':'QT/with_a_cold', 'g':'QT/grandpa', 's':"aïe Aïe, je suis un peu rouillé aujourd'hui" }, [('time', 1, 'choice')]),
                        'attends': ( {'e':'', 'g':'',  's': random.choice([ "tu patiente un petit moment?", "Attends un peu, je ne suis pas prêt", "Attends une seconde"]) }, [('time', 1, 'choice')]),
                        'malade': ( {'e':'QT/with_a_cold_cleaning_nose', 'g':'QT/sneezing', 's':"je suis malade #SNEEZE01#"}, [('time', 1, 'choice')]),

                        'et_alors': ( {'e':'QT/confused', 'g':'QT/so_what', 's':random.choice([ "Oui, et alors?", "Qu'est-ce que ça fait?", "Et alors?"]) }, [('time', 1, 'choice')]),
                        'jai_progresse': ( {'e':'QT/happy', 'g':'QT/happy',  's': random.choice([ "J'ai beaucoup progressé", "J'ai fait beaucoup de progrès!", "Je me débrouille beaucoup mieux qu'avant."]) }, [('time', 1, 'choice')]),
                        'cest_difficile': ( {'e':'QT/afraidshort', 'g':'QT/ohno', 's':random.choice(["Ce n'est pas si facile!", "Oui mais c'est dur", "C'est quand même difficile!"])}, [('time', 1, 'choice')]),
                        'fais_mon_mieux': ( {'e':'QT/talking', 'g':'QT/angry', 's': random.choice(["mais tu sais je fais comme je peux, je fais beaucoup d'efforts", "Je fais de mon mieux", "Je fais de gros effort"])}, [('time', 1, 'choice')]),
                        'tas_gagne': ( {'e':'', 'g':'QT/challenge', 's': "Bon.Tu as gagné. On s'y remet?" }, [('time', 1, 'choice')]),
                        'ma_tablette': ( {'e':'QT/surprise', 'g':'QT/angry', 's': random.choice([ "Mais! Ma tablette!","Mais où est ma tablette?", "Je ne trouve plus ma tablette!"]) }, [('time', 1, 'choice')]),
                        'pas_mal': ( {'e':'QT/showing_smile', 'g':'QT/bored', 's':random.choice([ "Je trouve que je me suis pas si mal débrouillé ", "Ce n'est pas si mal même si on peut faire mieux"])  }, [('time', 1, 'choice')]),
                        'je_trouve_pas': ( {'e':'', 'g':'QT/no',  's': random.choice([ "Ah bon? Je ne trouve pas", "Je ne suis pas vraiment d'accord", "Je ne suis pas du même avis que toi"]) }, [('time', 1, 'choice')]),
                        
                        'respire': ( {'e':'QT/calmig_down_exercise_nose', 'g':'', 's': random.choice(["Respire un peu, et réessaye", "ce n'est pas grave, reprends ton souffle, et on repart"]) }, [('time', 1, 'choice')]),
                        'ecris_mal': ( {'e':'QT/sad', 'g':'QT/thanks', 's': random.choice(["j'écris vraiment très mal", "Olala, mon écriture n'est pas terrible", "J'ai mal écrit"]) }, [('time', 1, 'choice')]),
                        'cest_pas_grave': ( {'e':'', 'g':'QT/so_what', 's': random.choice(["C'est pas grave, ça arrive", "{} , Ce n'est pas grave".format( child_name)]) }, [('time', 1, 'choice')]),
                        'reessayons': ( {'e':'QT/showing_smile', 'g':'QT/show_tablet', 's': random.choice(["encore une fois?", "On essaye encore?"]) }, [('time', 1, 'choice')]),
                        'fera_mieux': ( {'e':'QT/showing_smile', 'g':'QT/fera_mieux', 's': random.choice(["Nous n'avons pas réussi, mais nous ferons mieux la prochaine fois!", "On va faire mieux quand on reéessayera!"]) }, [('time', 1, 'choice')]),
                        'courage': ( {'e':'QT/showing_smile', 'g':'QT/strong', 's': random.choice(["Courage, {} , nous allons y arriver".format( child_name), "Allez, nous allons faire mieux", "Ne nous décourageons pas"]) }, [('time', 1, 'choice')]),
                        'rate': ( {'e':'QT/confused', 'g':'QT/sad', 's': random.choice(["Mince, nous avons raté", "Oh non, nous n'avons pas été très fort", "Nous n'avons pas très bien réussi"]) }, [('time', 1, 'choice')]),
                        'difficile': ( {'e':'QT/confused', 'g':'QT/challenge', 's': random.choice(["Mince, nous avons raté", "Oh non, nous n'avons pas été très fort", "Nous n'avons pas très bien réussi"]) }, [('time', 1, 'choice')]),
                        'pas_content_moi': ( {'e':'QT/sad', 'g':'', 's':  random.choice(["Je ne suis pas content de moi", "Ce n'est pas beau ce que j'ai fait", "ça ne me plait pas ce que j'ai fait"])}, [('time', 1, 'choice')]),
                        'tu_mecoute': ( {'e':'', 'g':'', 's': random.choice(["Tu ne m'écoutes \\sel=alt=p+100\\ \\Rspd=130\\ plus \\pau=120\\ \\sel=alt=p-50\\  \\Rspd=70\\ {} ?".format( child_name), "Hey! {} ?".format( child_name), "{} ?".format( child_name), "{}, tu m'écoutes?".format( child_name)]) }, [('time', 1, 'choice')]),
                        'on_essaye': ( {'e':'', 'g':'QT/yes', 's': "Ok, alors on essaye plus tard" }, [('time', 1, 'choice')]),
                        
                        'bravo': ( {'e':'QT/happy', 'g':'QT/happy', 's': random.choice(["Felicitations !", "Bravo!", "Bien joué  {}".format( child_name), "Félicitations {}".format( child_name)]) }, [('time', 0.1, 'choice')]),
                        'je_suis_fort': ( {'e':'QT/one_eye_wink', 'g':'QT/hips', 's': random.choice(["je suis trop fort", "je suis très fier de moi!", "J'ai trop bien réussi!"]) }, [('time', 1, 'choice')]),
                        'cest_bien': ( {'e':'QT/showing_smile', 'g':'QT/happy', 's': random.choice(["Super!", "C'est bien !", "C'est chouette!"]) }, [('time', 1, 'choice')]),
                        'tu_es_fort': ( {'e':'QT/happy', 'g':'T/handclap', 's': random.choice(["trop fort?", "Tu as trop bien réussi {} ".format( child_name), "Tu as trop bien fait!!"]) }, [('time', 1, 'choice')]),
                        'nous_sommes_fort': ( {'e':'QT/happy', 'g':'QT/happy', 's': random.choice(["On est trop forts", "On est super forts!", "On a trop bien réussi!"]) }, [('time', 1, 'choice')]),
                        'fier_de_toi': ( {'e':'QT/happy', 'g':'', 's':"Je suis fier de toi!"}, [('time', 1, 'choice')]),
                        'applique': ( {'e':'QT/one_eye_wink', 'g':'QT/thanks', 's': random.choice(["tu travaille très bien","tu t'applique très bien!", "tu est bien appliqué"]) }, [('time', 1, 'choice')]),
                        'tu_perseveres': ( {'e':'QT/happy', 'g':'', 's':random.choice(["Tu n'as pas \pau=5\ \sel=alt=p+50\ abandonné! Bravo!", "Tu as tenu bon, C'est bien !","Tu \sel=alt=p+50\ persévères, Super!"])}, [('time', 1, 'choice')]),

                        'aie': ( {'e':'QT/afraidshort', 'g':'QT/protect', 's': random.choice(["Aie!","Ouilleu", "aoutch, ça fait mal!"]) }, [('time', 1, 'choice')]),
                        'ahahah': ( {'e':'QT/happy', 'g':'QT/laugh', 's':random.choice(["#LAUGH02# C'est rigolo","Ça me fais rire!", "C'est drôle!"])}, [('time', 1, 'choice')]),
                        'muscle': ( {'e':'QT/one_eye_wink', 'g':'QT/strong', 's':"Oui mais moi, tu sais, j'ai des muscles en plastique"}, [('time', 1, 'choice')]),

                        'merci': ( {'e':'QT/showing_smile', 'g':'"QT/thanks', 's':  random.choice(["merci","Merci beaucoup", "Je te remercie", "merci, {}".format( child_name)])}, [('time', 1, 'choice')]),
                        'repete': ( {'e':'QT/talking', 'g':'', 's': random.choice([ "{} , est-ce que tu peux répèter?".format( child_name),"Peux-tu répéter?","Comment?", "Je n'ai pas entendu?"]) }, [('time', 1, 'choice')]),
                        'oui': ( {'e':'', 'g':'QT/thanks', 's':"Oui"}, [('time', 6, 'choice')]),
                        'non': ( {'e':'', 'g':'QT/no', 's': "Non" }, [('time', 7, 'choice')]),
                        'sais_pas_toi': ( {'e':'', 'g':'QT/so_what', 's':random.choice(["Aucune idee ! ,Et toi?","Je ne sais pas. et toi?","Je sais pas trop. et toi?"])}, [('time', 1, 'choice')]),
                        'et_toi': ( {'e':'', 'g':'', 's':"Et toi?"}, [('time', 3, 'choice')]),
                        
                        #comportement de scenario 
                        'pression_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Clique sur le jeu qui s'appelle sous-marin", "Démarre le jeu sous-marin"]) }, [('time', 1, 'choice')]),
                        'pression_expli': ( {'e':'QT/talkinglong', 'g':'QT/bored', 's': "Je navigue en sous-marin. Appuie ton stylo plus ou moins fort pour m'aider à piloter. Attention aux obstacles. Tu peux aller chercher les étoiles en bonus." }, [('time', 1, 'choice')]),
                        'pression_complet': ( {'e':'"QT/talkinglong', 'g':'QT/bored_long', 's': "\sel=alt=p-70\Rappelle-toi \pau=130\ C'est la pression sur le stylo qui pilote. Plus tu appuies fort, plus mon sous-marin descend. Si tu lâches le stylo, mon sous-marin s'arrête. Évite les pics et les rochers." }, [('time', 1, 'choice')]),
                        'archeo_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Lance le jeu archéologue", "Clique sur le jeu qui s'appelle archéologue"]) }, [('time', 1, 'choice')]),
                        'archeo_expli': ( {'e':'QT/talking', 'g':'QT/bored', 's': "Dans ce jeu, j'ai enterré un trésor dans le sol. Appuie le stylo sur la tablette. Déplace-le pour creuser dans le sol et trouver le trésor" }, [('time', 1, 'choice')]),
                        'archeo_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored_long', 's': "Attention ! \pau=80\ Si tu appuie trop fort, tu risque de casser le trésor. Une fois que tu as trouvé tout, n'oublie pas de valider." }, [('time', 1, 'choice')]),
                        
                        'drapeau_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Lance le jeu drapeau", "Clique sur le jeu qui s'appelle drapeau"]) }, [('time', 1, 'choice')]),
                        'drapeau_expli': ( {'e':'QT/talking', 'g':'QT/bored', 's':"Je dois livrer ce drapeau, \pau=30\ mais  je ne sais pas à quel pays \pau=50\ il appartient. Tu peux me recopier son nom pour que je puisse le livrer?" }, [('time', 1, 'choice')]),
                        'drapeau_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored_long', 's':"Il faut bien suivre l'example, et écrire dessus pour qu'on puisse livrer. Sinon notre colis risque d'être refusé. " }, [('time', 1, 'choice')]),
                        'alpha_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice([ "Lance le jeu alphabet.", "Clique sur le jeu qui s'appelle alphabet."])  }, [('time', 1, 'choice')]),
                        'alpha_expli': ( {'e':'QT/talking', 'g':'QT/bored',  's': "Choisis un chiffre, ou une lettre, et montre-moi comment bien l'écrire." }, [('time', 1, 'choice')]),
                        'alpha_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored', 's': "Attention ! \pau=80\ Il faut bien que tu me montre en repassant sur le modèle. Plus on suit le modèle, plus le trait est vert, et plus on gagne de points." }, [('time', 1, 'choice')]),
                        
                        'zoo_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Lance le jeu zoo", "Clique sur le jeu qui s'appelle zoo"]) }, [('time', 1, 'choice')]),
                        'zoo_expli': ( {'e':'QT/talking', 'g':'QT/bored', 's': "Tu peux me montrer comment bien colorier un \sel=alt\ dessin sur la tablette? \pau=50\ On perd des points \sel=alt\ si on dépasse ou si on se trompe de couleurs." }, [('time', 1, 'choice')]),
                        'zoo_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored_long', 's': "il faut bien tout colorier. Si tu n'as pas le temps de finir, tu peux sauvegarder en cliquant sur la croix. On terminera une prochaine fois."}, [('time', 1, 'choice')]),
                        
                        'chimi_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Lance le jeu chimiste", "Clique sur le jeu qui s'appelle chimiste"]) }, [('time', 1, 'choice')]),
                        'chimi_expli': ( {'e':'QT/talking', 'g':'QT/bored', 's': "Copie le mot avec les bonnes couleurs avec moi. Quand tu lève le stylo, la couleur change." }, [('time', 1, 'choice')]),
                        
                        'tilt_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Lance le jeu hélicoptère", "Clique sur le jeu qui s'appelle hélicoptère"]) }, [('time', 1, 'choice')]),
                        'tilt_expli': ( {'e':'QT/talking', 'g':'QT/bored', 's':"Je conduis un hélicoptère dans le jeu, et tu dois m'aider à piloter en plaçant ton stylo dans le cercle. Aide-moi à livrer les boîtes." }, [('time', 1, 'choice')]),
                        'tilt_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored_long', 's': "\sel=alt=p-70\Rappelle-toi \pau=130\  Je vais dans la direction vers laquelle tu places ton stylo. On doit prendre \pau=50\ et livrer les boites. Une flèche rouge nous dit \pau=50\ où on doit aller. Si tu lâches le stylo, la boîte tombe." }, [('time', 1, 'choice')]),
                        
                        'cowritter_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's':  random.choice(["Démarre le jeu qui s'appelle Apprenti", "Clique sur Apprenti"]) }, [('time', 1, 'choice')]),
                        'cowritter_expli_class': ( {'e':'QT/talkinglongrepeat', 'g':'QT/bored', 's': "Tu m'entraîne à écrire. Dans ce jeu, mon surnom est le robot de proust. Tu me montre comment bien corriger mes erreurs!" }, [('time', 1, 'choice')]),
                        'cowritter_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored_long', 's': "\sel=alt=p-70\Rappelle-toi \pau=130\ Tu m'apprends à écrire. Mieux tu me montre, mieux j'apprends. À la fin on verra ma note." }, [('time', 1, 'choice')]),
                       
                        'jus_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Clique sur le jeu qui s'appelle jus", "jouons au jeu qui s'appelle jus"]) }, [('time', 1, 'choice')]),
                        'jus_expli': ( {'e':'QT/talking', 'g':'QT/bored', 's': "Aide mon avatar à faire un jus. Laisse ta main gauche appuyée sur le bouton jaune pour allumer la lumière. Avec tes doigts, suit les étapes qui sont indiqué dans le cadre gris." }, [('time', 1, 'choice')]),
                        'jus_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored', 's': "Attention ! \pau=80\ Il faut cliquer sur tout les fruits indiqués en même temps. Pour couper le fruit, il faut cliquer sur le fruit et le couteau en même temps, et glisser le couteau vers le fruit. Pour presser le jus, glisse tous les fruit en même temps vers le pressoir." }, [('time', 1, 'choice')]),

                        'poursuite_lance': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's':  random.choice(["Clique sur le jeu Poursuite","Lances le jeu qui s'appelle Poursuite"]) }, [('time', 1, 'choice')]),
                        'poursuite_expli': ( {'e':'QT/talkinglong', 'g':'QT/bored', 's':"J'ai faim. Suis le chemin avec ton stylo et ramasse tous les fruits pour moi."}, [('time', 1, 'choice')]),
                        'poursuite_complet': ( {'e':'QT/talkinglong', 'g':'QT/bored_long',  's': "\sel=alt=p-50\Rappelle-toi \pau=100\ il faut bien rester sur le chemin bleu pour ne pas perdre des ballons. Tu peux prendre ton temps." }, [('time', 1, 'choice')]),
                       
                        'tu_viens': ( {'e':'QT/one_eye_wink', 'g':'QT/come', 's':random.choice([ "{} c'est l'heure de mon cours, non?".format( child_name), "{} tu viens m'aider à améliorer mon écriture?".format( child_name), "{} je suis impatient d'écrire, tu viens?".format( child_name),"{} tu peux venir pour qu'on fasse mon cours?".format( child_name)])}, [('time', 1, 'choice')]),
                        'ton_nom': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice([ "Clique sur ton nom pour commencer", "Avant qu'on commence, tu dois cliquer sur ton nom"])}, [('time', 1, 'choice')]),
                        'ca_va': ( {'e':'QT/showing_smile', 'g':'', 's': random.choice(["Comment vas-tu?", "Ça va?", "Tu vas bien?" ]) }, [('time', 1, 'choice')]),
                        'bonjour': ( {'e':'QT/showing_smile', 'g':'QT/hi', 's': random.choice(["Bonjour, {}".format( child_name) , "Coucou? {}".format( child_name) ]) }, [('time', 1, 'choice')]),
                        
                        'je_mappelle_qt': ( {'e':'QT/talkinglongadapted', 'g':'"QT/hi', 's':"Bonjour, je m'appelle kyuti. Et toi, comment tu t'appelles?" }, [('time', 1, 'choice')]),
                        'tu_veux_maider': ( {'e':'QT/talkinglongrepeat', 'g':'QT/begin',  's':"Je suis content de te rencontrer. J'ai besoin de ton aide pour mieux écrire, car je ne suis pas très fort. Est-ce que tu es d'accord pour m'aider? On s'améliorera ensemble!" }, [('time', 1, 'choice')]),
                        'tu_maides_encore': ( {'e':'QT/talkinglong', 'g':'QT/rappel', 's':"Comme je ne sais pas très bien écrire, tu avais décidé de m'aider pour qu'on devienne meilleurs ensemble. On continue?"}, [('time', 1, 'choice')]),
                        'adieu': ( {'e':'QT/dernieradieu', 'g':'QT/adieu', 's':"On a terminé notre dernière séance. Merci beaucoup. J'ai fais beaucoup de progrès, et je me suis bien amusé. J'espère que toi aussi. " }, [('time', 1, 'choice')]),
                        'adieu2': ( {'e':'QT/showing_smile', 'g':'QT/hi',  's': "Au revoir {} ! Bon courage pour la suite!".format( child_name) }, [('time', 1, 'choice')]),
                        
                        'pause': ( {'e':'QT/talking', 'g':'QT/bored', 's':random.choice(["Après un niveau, on s'arrête \pau=20\ et on \Rspd=70\ réfléchit \Rspd=80\ ensemble.", "On fait un niveau, et on s'arrête pour que tu m'expliques."])}, [('time', 1, 'choice')]),
                        'change_jeu': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': random.choice(["Tu veux qu'on fasse un autre \sel=alt=p-30\jeu?", "Tu as envie de changer de jeu?", "On passe à la prochaine activité?"])}, [('time', 1, 'choice')]),
                        'choisis_jeu': ( {'e':'QT/talking', 'g':'QT/show_tablet',  's': random.choice([ "Je te laisse choisir la prochaine activité sur la tablette.", "À toi de choisir dans les jeux sur la tablette.", "Parmi les jeux qu'on a sur notre \Rspd=100\ tablette,\Rspd=80\ lequel tu veux faire ensuite?"]) }, [('time', 1, 'choice')]),
                        
                        'dernier_jeu': ( {'e':'QT/showing_smile', 'g':'', 's':random.choice(["Ce sera notre dernière activité.", "Plus qu'une partie et on arrête.", "C'est le dernier jeu."])}, [('time', 1, 'choice')]),
                        'cetait_bien': ( {'e':'QT/happy', 'g':'QT/handclap', 's': random.choice(["C'était une super séance, {}".format( child_name), "nous avons bien travaillé aujourd'hui"])}, [('time', 1, 'choice')]),
                        'tu_maide': ( {'e':'QT/happy', 'g':'QT/thanks', 's':random.choice([ "{} , Merci pour ton aidé".format( child_name), "Merci {} tu m'aides beaucoup!".format( child_name), "tu m'as beaucoup aidé {}".format( child_name)]) }, [('time', 1, 'choice')]),
                        'mes_progres': ( {'e':'QT/happy', 'g':'QT/hips',  's': random.choice([ "Tu as vu comment j'écrivais et comment j'ai progressé?", "Tu as vu comme je me suis amélioré en écriture?", "Tu as vu mes progrès?"]) }, [('time', 1, 'choice')]),
                        'bisou': ( {'e':'QT/kiss2', 'g':'QT/kiss', 's':"Je peux t'envoyer un bisou?"}, [('time', 8, 'choice')]),
                        'bcp_travaille': ( {'e':'', 'g':'QT/strong', 's': random.choice(["Nous avons beaucoup travaillé aujourd'hui,", "Nous avons travaillé dur", "Nous avons beaucoup travaillé ensemble"])}, [('time', 1, 'choice')]),
                        'il_est_lheure': ( {'e':'', 'g':'QT/bored',  's': random.choice([ "Il est l'heure, on doit s'arrêter", "C'est l'heure à laquelle on doit finir"]) }, [('time', 1, 'choice')]),
                        'arrete': ( {'e':'', 'g':'QT/bored', 's':random.choice(["{} , On s'arrête pour aujourd'hui".format( child_name), "On arrête là cette séance"])}, [('time', 1, 'choice')]),
                        'au_revoir': ( {'e':'QT/showing_smile', 'g':'QT/hi', 's': random.choice(["À bientôt!", "À la prochaine!", "Au revoir,{} !".format( child_name)])}, [('time', 1, 'choice')]),  


                        'end': ((), [('time', 0.1, 'end')]) }
        self.state = 'begin'
        rospy.Timer(rospy.Duration( self.states[self.state][1][0][1]), self.time_callback, oneshot=True)
        self.head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)
        self.left_arm_pub = rospy.Publisher('/qt_robot/left_arm_position/command', Float64MultiArray, queue_size=1)
        self.right_arm_pub = rospy.Publisher('/qt_robot/right_arm_position/command', Float64MultiArray, queue_size=1)
        print("ici begin dans state : ",self.state)

    def time_callback(self, event):
    # go to next state
        print('time callback')
        triggers = self.states[self.state][1]
        # print('time_callback triggers :',triggers)
        for trigger in triggers:
            print('trigger :::',trigger)
            if trigger[0] == 'time':
                self.state = trigger[2]
                print('next_state1: ' + self.state)
                self.next_state()  
                print("srtie de time_callback")

    def button_callback(self, my_button):
        print('bouton            : ', my_button)
        triggers = self.states[self.state][1]
        for trigger in triggers:
            if trigger[0] == 'key':
                if trigger[2] == my_button:
                    print("ici == key en vrai bouton")
                    self.state = trigger[2]
                    print('next_state2: ' + self.state)
                    self.next_state()
                    break;   


    def next_state(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
        if(self.state != 'end'):
            self.state_pub.publish(self.state)
            # send behavior
            behavior = self.states[self.state][0]
            if(len(behavior)):
                # AL machine => pass to smach
                print(self.state + ' =behavior=> ' + str(behavior))
                
                if 'la' in behavior and ('g' not in behavior):
                    self.left_arm_pub.publish(Float64MultiArray(data=behavior['la']))
                if 'ra' in behavior and ('g' not in behavior):
                    self.right_arm_pub.publish(Float64MultiArray(data=behavior['ra']))
                if ('h' in behavior) and ('g' not in behavior):
                    self.head_pub.publish(Float64MultiArray(data=behavior['h']))    
                if ('e' in behavior) or ('g' in behavior) or ('s' in behavior):
                    # --------------------- voir actionLib plutard ----------------------
                    # client = actionlib.SimpleActionClient('/qt_action_behavior', QT_BehaviorAction)
                    # client.wait_for_server()

                    # goal = QT_BehaviorGoal( emotion=behavior['e'] if 'e' in behavior else '',
                    #                        gesture=behavior['g'] if 'g' in behavior else '',
                    #                        speech=behavior['s'] if 's' in behavior else '')
                    # client.send_goal(goal)
                    # # ...
                    # client.wait_for_result()
                    # result = client.get_result()
                    
                    ts = TaskSynchronizer()
                    rospy.wait_for_service('/qt_robot/motors/home')
                    rospy.wait_for_service('/qt_robot/gesture/play')
                    
                    print("emotion gestes and say")
                    
                    self.home_pose = rospy.ServiceProxy('/qt_robot/motors/home',home)
                    self.gesturePlay = rospy.ServiceProxy('/qt_robot/gesture/play', gesture_play)
                    print('calling speechSay and gesturePlay and EmotionShow')
                    start_time = time.time()
                    task1 = ts.sync([
                        (0, lambda:self.talker_pub.publish(behavior['s'][1:]) if behavior['s'].startswith('~') else self.speechSay_pub.publish(behavior['s'])),
                        (0, lambda: self.emotionShow_pub.publish(behavior['e'])),
                        (0, lambda: self.gesturePlay(behavior['g'],0.8) if 'h' not in behavior else '')
                                    ])
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if elapsed_time >  2.0:
                        print("ici home_pose ********************************")
                        task2 = ts.sync([
                            (0, lambda: self.home_pose(['head','left_arm','right_arm']))
                                        ])
                    
                    print("fin de  home_pose ********************************")
                    print('speechSay and gesturePlay and EmotionShow finished.')
                    
                    print("Temps écoulé :::::::::::::::::::::::::::::::::::", elapsed_time, "secondes")
            # prepare jump for next state
            triggers = self.states[self.state][1]
            # print(self.state + ' =trig=> ' + str(triggers))
            for trigger in triggers:
                if trigger[0] == 'time':
                    rospy.Timer(rospy.Duration(trigger[1]), self.time_callback, oneshot=True)
              

    def execute(self):
        global is_clicked 
        
        while not rospy.is_shutdown():

            if (is_clicked):
                self.button_callback(my_button)
            is_clicked = False
            time.sleep(0.5)
            if self.state == 'end': break
            self.rate.sleep()


if __name__ == '__main__':
    rospy.init_node("qt_states_behavior", anonymous=True)    
   
  
    try:
        qt_behavior = Qt_Behavior()
        qt_behavior.execute()
        # print("++++++++++ hors classes (principal) ++++++++++++")
    except rospy.ROSInterruptException: pass