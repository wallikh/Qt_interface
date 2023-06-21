#! /usr/bin/env python3
# coding: utf-8

import roslib
roslib.load_manifest('woz_interface')
import rospy
import rospkg
import actionlib

from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray

from geometry_msgs.msg import Twist
from woz_interface.msg import NaoBehaviorAction
from woz_interface.msg import NaoBehaviorGoal
from woz_interface.msg import NameInfo
import sys, select, termios, tty
import time
import numpy as np
import pandas as pd
import random
from synchroniser import TaskSynchronizer
from checking import check, my_callback

#nao
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
mon_objet = check()
mon_objet.register_callback(my_callback)
child_name = ""
adult_name = ""
last_button = ""
is_clicked = False
stdin_settings = termios.tcgetattr(sys.stdin)

def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, stdin_settings)
    return key


class NaoPlay:
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
  
    def name_callback(msg):
        global child_name
        global adult_name
        child_name =  msg.first_name
        last_name = msg.last_name
        adult_name = msg.teacher_name
        print("==============================================",adult_name)
        
    rospy.Subscriber('woz/nameinfo', NameInfo, name_callback) 
   
    def __init__(self):
        while child_name == "" or adult_name == "":
            time.sleep(0.2)
            pass 
        self.rate = rospy.Rate(10) # 10hz

        self.keyboard_pub = rospy.Publisher('/keyboard', String, queue_size=10)
        self.state_pub = rospy.Publisher('/robot_state', String, queue_size=10)
        

        # state: ( {g: gesture, s: say, h: [head], la: [left_arm], ra: [right_arm], w: [x, y, z, ex, ey, ez]}, [(trigger, param, next_state)])
        self.states = { 'begin': ( {}, [('time', 1, 'choice')]),

                        'choice': ( {'g': '', 's': '' },
                                        [  
                                            # comportement theatre
                                            ('woz', 'z', 'up'), ('woz', 's', 'center'), ('woz', 'x', 'down'),('woz', 'e', 'up_right'),
                                            ('woz', 'q', 'left'), ('woz', 'd', 'right'),('woz', 'a', 'up_left'),
                                            ('woz', 'w', 'down_left'),('woz', 'c', 'down_right'),

                                            ('woz', 'Z', 'LSU'),('woz', 'X', 'LSD'),

                                            ('woz', 'h', 'hello'),('woz', 'k', 'dontknow'),('woz', 'y', '_oui'),('woz', 'n', '_non'),('woz', 'f', 'suivi'),('woz', 'g', 'public'),
                                            ('woz', 'r', 'objetDroite'),('woz', 'l', 'objetGauche'),('woz', 'p', 'pense'),('woz', 'o', 'pense2'),('woz', 'm', 'neutral'),
                                            ('woz', 'R', 'really'),('woz', 'H', '_comment'),('woz','J','jaime'),('woz','b','bored'),('woz','Y','happy'),('woz', 'S', 'sad'),
                                            ('woz', 'u', 'standup'),('woz', 'K', 'kisses'),('woz', 'E', 'excited'),('woz', 't', 'thinking'),('woz', 'C', 'curious'),
                                            ('woz', 'F', 'fear'),('woz', 'O', 'confused'),
                                            
                                            # comportement reactions
                                            ('woz', None, 'la_joie'),('woz', None, 'amusement'),('woz', None, 'la_colere'),('woz', None, 'la_motivation'),('woz', None, 'la_fatigue'),('woz', None, 'la_tristesse'),
                                            ('woz', None, 'la_fierte'),('woz', None, 'etonnement'),('woz', None, 'adulte_accord'),('woz', None, 'demande_adulte'),('woz', None, 'que_pense'),
                                            ('woz', None, 'monsieur'),('woz', None, 'madame'),('woz', None, 'bien'),('woz', None, 'cest_mieux'),
                                            ('woz', None, 'tu_mexplique'),('woz',None, 'important'),('woz', None, 'ensuite'),('woz', None, 'pk_pas_bien'),
                                            ('woz', None, 'tu_es_sur'),('woz', None, 'plus_simple'),('woz', None, 'plus_difficile'),
                                            ('woz', None, 'bien_mal'),('woz', None, 'pas_marche'),('woz', None, 'pourquoi'),('woz', None, 'ecrit'),('woz', None, 'senslettre'),('woz', None, 'fermelettre'),
                                            ('woz', None, 'endroitlettre'),('woz', None, 'bien_comme_toi'),('woz', None, 'triche'),('woz', None, 'facile'),('woz', None, 'pas_trop_vite'),
                                            ('woz', None, 'boum'),('woz', None, 'tu_relances'),('woz', None, 'je_bugue'),('woz', None, 'je_rouille'),
                                            ('woz', None, 'attends'),('woz', None, 'malade'),('woz', None, 'et_alors'),('woz', None, 'jai_progresse'),
                                            ('woz', None, 'cest_difficile'),('woz', None, 'fais_mon_mieux'),('woz', None, 'tas_gagne'),
                                                                                    ('woz', None, 'ma_tablette'),('woz', None, 'pas_mal'),('woz', None, 'je_trouve_pas'),('woz', None, 'respire'),('woz', None, 'ecris_mal'),('woz', None, 'cest_pas_grave'),
                                            ('woz', None, 'reessayons'),('woz', None, 'fera_mieux'),('woz', None, 'courage'),('woz', None, 'rate'),('woz', None, 'difficile'),
                                            ('woz', None, 'pas_content_moi'),('woz', None, 'tu_mecoute'),('woz', None, 'on_essaye'),('woz', None, 'bravo'),
                                            ('woz', None, 'je_suis_fort'),('woz', None, 'cest_bien'),('woz', None, 'tu_es_fort'),('woz', None, 'nous_sommes_fort'),
                                            ('woz', None, 'fier_de_toi'),('woz', None, 'applique'),('woz', None, 'tu_perseveres'),
                                            ('woz', None, 'aie'),('woz', None, 'ahahah'),('woz', None, 'muscle'),('woz', None, 'merci'),('woz', None, 'repete'),('woz', None, 'oui'),
                                            ('woz', None, 'non'),('woz', None, 'sais_pas_toi'),('woz', None, 'et_toi'),
                                            
                                            # comportement de scenario
                                            ('woz', None, 'pression_lance'),('woz', None, 'pression_expli'),('woz', None, 'pression_complet'),('woz', None, 'archeo_lance'),('woz', None, 'archeo_expli'),('woz', None, 'archeo_complet'),
                                            ('woz', None, 'drapeau_lance'),('woz', None, 'drapeau_expli'),('woz', None, 'drapeau_complet'),('woz', None, 'alpha_lance'),('woz', None, 'alpha_expli'),
                                            ('woz', None, 'alpha_complet'),('woz', None, 'zoo_lance'),('woz', None, 'zoo_expli'),('woz', None, 'zoo_complet'),
                                            ('woz', None, 'chimi_lance'),('woz',None, 'chimi_expli'),('woz', None, 'tilt_lance'),('woz', None, 'tilt_expli'),
                                            ('woz', None, 'tilt_complet'),('woz', None, 'cowritter_lance'),('woz', None, 'cowritter_expli_class'),
                                            ('woz', None, 'cowritter_complet'),('woz', None, 'jus_lance'),('woz', None, 'jus_expli'),('woz', None, 'jus_complet'),('woz', None, 'poursuite_lance'),('woz', None, 'poursuite_expli'),
                                            ('woz', None, 'poursuite_complet'),('woz', None, 'tu_viens'),('woz', None, 'ton_nom'),('woz', None, 'ca_va'),('woz', None, 'bonjour'),
                                            ('woz', None, 'je_mappelle_qt'),('woz', None, 'tu_veux_maider'),('woz', None, 'tu_maides_encore'),('woz', None, 'adieu'),
                                            ('woz', None, 'adieu2'),('woz', None, 'pause'),('woz', None, 'change_jeu'),('woz', None, 'choisis_jeu'),
                                            ('woz', None, 'dernier_jeu'),('woz', None, 'cetait_bien'),('woz', None, 'tu_maide'),('woz', None, 'mes_progres'),('woz', None, 'bisou'),('woz', None, 'bcp_travaille'),('woz', None, 'il_est_lheure'),
                                            ('woz', None, 'arrete'),('woz', None, 'au_revoir'),

                                            # walk 
                                            ('woz', '8', 'walk_fwd'),
                                            # ('woz', '5', 'stop'),
                                            ('woz', '2', 'walk_back'),
                                            ('woz', '4', 'strife_left'), ('woz', '6', 'strife_right'),
                                            ('woz', '7', 'rotate_left'), ('woz', '9', 'rotate_right'),


                                            ('woz', 'j', 'end')]),

                        'up': ( {'s': '', 'h': [0.0,-1]}, [('time', 0.1, 'choice')]),
                        'center': ( {'s': '', 'h': [0.0,+0.0]}, [('time', 0.1, 'choice')]),
                        'down': ( {'s': '', 'h': [0.0,+1]}, [('time', 0.1, 'choice')]),
                        'right': ( {'s': '', 'h': [-2,+0.0]}, [('time', 0.1, 'choice')]),
                        'left': ( {'s': '', 'h': [+2,+0.0]}, [('time', 0.1, 'choice')]),
                        'up_right': ( {'s': '', 'h': [-0.5,-5.0]}, [('time', 0.1, 'choice')]),
                        'up_left': ( {'s': '', 'h': [+0.5,-0.5]}, [('time', 0.1, 'choice')]),
                        'down_right': ( {'s': '', 'h': [-0.5,+0.5]}, [('time', 0.1, 'choice')]),
                        'down_left': ( {'s': '', 'h': [+0.5,+0.5]}, [('time', 0.1, 'choice')]),

                        'LSD': ( {'s': '', 'la': [0.5,0,0,0,0,1]}, [('time', 1, 'see')]),
                        'LSU': ( {'s': '', 'la': [-0.5,0,0,0,0,1]}, [('time', 1, 'see')]),
                        'see': ( {'s': 'Did you see ?'}, [('time', 0.1, 'choice')]),



                        'hello': ( {'g': 'hello', 's': '\\pau=4000\\Hello!', 'h': [0,0]}, [('time', 3, 'choice')]),
                        'dontknow': ( {'g': 'dontknow', 's': '\\pau=1000\\I dont know'}, [('time', 3, 'choice')]),
                        '_oui': ( {'g': 'oui', 's': '\\pau=50\\yes!'}, [('time', 3, 'choice')]),
                        '_non': ( {'g': 'non', 's': '\\pau=5\\no!'}, [('time', 3, 'choice')]),
                        'suivi': ( {'g': 'suivi', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
                        'public': ( {'g': 'public', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
                        'objetDroite': ( {'g': 'objetDroite', 's': '\\pau=9500\\Here !'}, [('time', 3, 'choice')]),
                        'objetGauche': ( {'g': 'objetGauche', 's': '\\pau=9500\\Here !'}, [('time', 3, 'choice')]),
                        'pense': ( {'g': 'pense', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
                        'pense2': ( {'g': 'pense2', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
                        'neutral': ( {'g': 'neutral', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
                        'really': ( {'g': 'really', 's': '\\pau=2000\\really ?'}, [('time', 3, 'choice')]),
                        '_comment': ( {'g': 'comment', 's': '\\pau=2000\\how ?'}, [('time', 3, 'choice')]),
                        'jaime': ( {'g':'jaime', 's': '\\pau=1500\\ I love it !'}, [('time', 3, 'choice')]),
                        'bored': ( {'g':'bored', 's': '\\pau=1500\\ Huff'}, [('time', 3, 'choice')]),
                        'happy': ( {'g':'happy', 's': '\\pau=1500\\ YES !'}, [('time', 3, 'choice')]),
                        'sad': ( {'g':'sad', 's': '\\pau=1500\\ oh'}, [('time', 3, 'choice')]),
                        'standup': ( {'g':'standup'}, [('time', 3, 'choice')]),

                        'kisses': ( {'g':'kiss'}, [('time', 3, 'choice')]),
                        'excited': ( {'g':'excited','s': 'yes !'}, [('time', 3, 'choice')]),
                        'thinking': ( {'g':'thinking'}, [('time', 3, 'choice')]),
                        'curious': ( {'g':'curious','s': '\\pau=1500\\ oh'}, [('time', 3, 'choice')]),
                        'fear': ( {'g':'fear'}, [('time', 3, 'choice')]),
                        'confused': ( {'s':'okey','g': 'confused'}, [('time', 3, 'choice')]),

                        #reaction
                        'la_joie': ( {'g':'happy', 's': random.choice(['Quelle mine joyeuse', 'Quel booo  sourire', 'Quel enthousiassme']) }, [('time', 1, 'choice')]),
                        'amusement': ( {'g':'happy', 's': random.choice(["Ça a l'air de t'amuser!", "Tu as l'air de trouver que c'est drôle"]) }, [('time', 1, 'choice')]),
                        'la_colere': ( { 'g':'bored', 's': random.choice(['{}, Est-ce que tu es fâché?'.format( child_name), "Tu es en colère?", "Tu as l'air en colère"]) }, [('time', 1, 'choice')]),
                        'la_motivation': ( { 'g':'chill', 's': random.choice(["Tu as l'air motivé", "{} , tu es très motivé aujourd'hui".format( child_name)]) }, [('time', 1, 'choice')]),
                        'la_fatigue': ( { 'g':'bored', 's': "Je suis désolé. #YAWN01# je suis fatigué." }, [('time', 1, 'choice')]),
                        'la_tristesse': ( { 'g':'sad', 's': random.choice(["{} ,Est-ce que tu es triste?".format( child_name) , "Tu as de la\sel=alt=p-20\  peine?", "Quelque chose te rend triste?"]) }, [('time', 1, 'choice')]),
                        'la_fierte': ( { 'g':'chill', 's': random.choice(["Tu es fier de ton travail ?	", "Tu as l'air fier de ton travail"]) }, [('time', 1, 'choice')]),
                        'etonnement': ( { 'g':'curious', 's': random.choice(["Tu as l'air étonné", "Tu es étonné,"]) }, [('time', 1, 'choice')]),
                        
                        'adulte_accord': ( { 'g':'', 's': "%s ,tu es d'accord?" %adult_name }, [('time', 1, 'choice')]),
                        'demande_adulte': ( {'g':'', 's':"Demandons à %s" %adult_name }, [('time', 1, 'choice')]),
                        'que_pense': ( {'g':'pense', 's':random.choice(["%s,  qu'en penses-tu ?" % adult_name, "Qu'est-ce que tu en pense %s ?" % adult_name]) }, [('time', 1, 'choice')]),
                        'monsieur': ( { 'g':'', 's': "Monsieur!" }, [('time', 1, 'choice')]),
                        'madame': ( { 'g':'', 's': "Madame!" }, [('time', 1, 'choice')]),

                        'bien': ( { 'g':'', 's': random.choice(["C'est comme ça qu'il faut faire?", "Est-ce que c'est bien?"]) }, [('time', 1, 'choice')]),
                        'cest_mieux': ( { 'g':'bored', 's': random.choice(["Est-ce que je m'améliore?", "Je fais mieux kavant?"]) }, [('time', 1, 'choice')]),
                        'tu_mexplique': ( {'g':'confused', 's': random.choice(["tu m'expliques?", "Tu peux m'expliquer un peu?", "Olala. c'est difficile! Tu peux m'expliquer?"]) }, [('time', 1, 'choice')]),
                        'important': ( {'g':'', 's': random.choice(["Qu'est-ce qu'on a fait qui est le plus important?", "C'est quoi le plus important dans ce qu'on a fait,"]) }, [('time', 1, 'choice')]),
                        'ensuite': ( { 'g':'sad', 's': random.choice(["Que fait-on maintenant pour que j'apprenne mieux à écrire", "Quel jeu pourrait le pluss m'aider tu penses"]) }, [('time', 1, 'choice')]),
                        'pk_pas_bien': ( { 'g':'non', 's': random.choice(["Pourquoi c'est pas bien,", "Pourquoi, je ne fais pas comme il faut?", "Ah bon? Qu'est-ce qui ne va pas?"]) }, [('time', 1, 'choice')]),
                        'tu_es_sur': ( {'g':'', 's': random.choice(["Tu es sûr?", "Tu es sûr de toi?", "Je ne suis pas sûr"]) }, [('time', 1, 'choice')]),
                        'plus_simple': ( { 'g':'', 's': "C'était quoi le plus simple pour toi " }, [('time', 1, 'choice')]),
                        'plus_difficile': ( { 'g':'', 's': "C'était quoi le plus difficile pour toi " }, [('time', 1, 'choice')]),
                        'bien_mal': ( { 'g':'', 's': "Qu'est-ce que je fais mal \sel=alt=p-50\ \Rspd=80\ et \sel=alt=p-50\ bien?" }, [('time', 1, 'choice')]),
                        'pas_marche': ( { 'g':'bored', 's': "Pourquoi ça n'a pas marché?" }, [('time', 1, 'choice')]),
                        'pourquoi': ( {'g':'', 's': random.choice(["Pourquoi?", "Pour quelle raison?"]) }, [('time', 1, 'choice')]),
                        
                        'ecrit': ( {'g':'', 's': "" }, [('time', 1, 'choice')]),
                        'senslettre': ( { 'g':'', 's':"Est-ce que je fais mes lettres en tournant dans le bon sens?" }, [('time', 1, 'choice')]),
                        'fermelettre': ( {'g':'',  's': random.choice([ "Est-ce que mes lettres sont bien fermés?", "Est-ce que j'ai bien fermés mes lettres?", "Mes lettres sont fermés comme il faut?"]) }, [('time', 1, 'choice')]),
                        'endroitlettre': ( { 'g':'', 's': random.choice([ "Est-ce que je débute mes lettres où il faut?", "Est-ce qu'il y a des lettres que je ne commence pas au bon endroit?"])}, [('time', 1, 'choice')]),
                        'bien_comme_toi': ( { 'g':'suivi', 's': random.choice(["Mon mot \sel=alt=p-20\ \Rspd=80\ ressemble \Rspd=100\ à ce que tu as écrit?", "Est-ce que j'écris aussi bien que toi?", "J'écris bien comme toi?", "Mon mot est aussi beau que le tien?"]) }, [('time', 1, 'choice')]),

                        'triche': ( { 'g':'sad', 's': "Mais tu triche," }, [('time', 1, 'choice')]),
                        'facile': ( {'g':'really', 's':"Est-ce que c'est trop facile?" }, [('time', 1, 'choice')]),
                        'pas_trop_vite': ( { 'g':'',  's': random.choice([ "attention, ne va pas trop vite", "{} , ne va pas trop vite".format( child_name)]) }, [('time', 1, 'choice')]),
                        'boum': ( { 'g':'happy', 's':"Boum!"}, [('time', 1, 'choice')]),

                        'tu_relances': ( { 'g':'chill', 's': random.choice([ "Tu peux relancer le jeu?", "Peux-tu relancer l'activité ?"])}, [('time', 1, 'choice')]),
                        'je_bugue': ( { 'g':'', 's': random.choice(["Ça n'a pas bien marché", "J'ai eu un bug"]) }, [('time', 1, 'choice')]),
                        'fatigue': ( { 'g':'bored', 's': "Je suis désolé. #YAWN01# je suis fatigué." }, [('time', 1, 'choice')]),
                        'je_rouille': ( { 'g':'bored', 's':"aïe Aïe, je suis un peu rouillé aujourd'hui" }, [('time', 1, 'choice')]),
                        'attends': ( { 'g':'',  's': random.choice([ "tu patiente un petit moment?", "Attends un peu, je ne suis pas prêt", "Attends une seconde"]) }, [('time', 1, 'choice')]),
                        'malade': ( { 'g':'bored', 's':"je suis malade #SNEEZE01#"}, [('time', 1, 'choice')]),

                        'et_alors': ( { 'g':'suivi', 's':random.choice([ "Oui, et alors?", "Qu'est-ce que ça fait?", "Et alors?"]) }, [('time', 1, 'choice')]),
                        'jai_progresse': ( { 'g':'happy',  's': random.choice([ "J'ai beaucoup progressé", "J'ai fait beaucoup de progrès!", "Je me débrouille beaucoup mieux qu'avant."]) }, [('time', 1, 'choice')]),
                        'cest_difficile': ( { 'g':'non', 's':random.choice(["Ce n'est pas si facile!", "Oui mais c'est dur", "C'est quand même difficile!"])}, [('time', 1, 'choice')]),
                        'fais_mon_mieux': ( { 'g':'fear', 's': random.choice(["mais tu sais je fais comme je peux, je fais beaucoup d'efforts", "Je fais de mon mieux", "Je fais de gros effort"])}, [('time', 1, 'choice')]),
                        'tas_gagne': ( { 'g':'', 's': "Bon.Tu as gagné. On s'y remet?" }, [('time', 1, 'choice')]),
                        'ma_tablette': ( { 'g':'bored', 's': random.choice([ "Mais! Ma tablette!","Mais où est ma tablette?", "Je ne trouve plus ma tablette!"]) }, [('time', 1, 'choice')]),
                        'pas_mal': ( { 'g':'bored', 's':random.choice([ "Je trouve que je me suis pas si mal débrouillé ", "Ce n'est pas si mal même si on peut faire mieux"])  }, [('time', 1, 'choice')]),
                        'je_trouve_pas': ( { 'g':'fear',  's': random.choice([ "Ah bon? Je ne trouve pas", "Je ne suis pas vraiment d'accord", "Je ne suis pas du même avis que toi"]) }, [('time', 1, 'choice')]),
                        
                        'respire': ( { 'g':'', 's': random.choice(["Respire un peu, et réessaye", "ce n'est pas grave, reprends ton souffle, et on repart"]) }, [('time', 1, 'choice')]),
                        'ecris_mal': ( { 'g':'dontknow', 's': random.choice(["j'écris vraiment très mal", "Olala, mon écriture n'est pas terrible", "J'ai mal écrit"]) }, [('time', 1, 'choice')]),
                        'cest_pas_grave': ( { 'g':'oui', 's': random.choice(["C'est pas grave, ça arrive", "{} , Ce n'est pas grave".format( child_name)]) }, [('time', 1, 'choice')]),
                        'reessayons': ( { 'g':'', 's': random.choice(["encore une fois?", "On essaye encore?"]) }, [('time', 1, 'choice')]),
                        'fera_mieux': ( { 'g':'jaime', 's': random.choice(["Nous n'avons pas réussi, mais nous ferons mieux la prochaine fois!", "On va faire mieux quand on reéessayera!"]) }, [('time', 1, 'choice')]),
                        'courage': ( { 'g':'excited', 's': random.choice(["Courage, {} , nous allons y arriver".format( child_name), "Allez, nous allons faire mieux", "Ne nous décourageons pas"]) }, [('time', 1, 'choice')]),
                        'rate': ( {'g':'sad', 's': random.choice(["Mince, nous avons raté", "Oh non, nous n'avons pas été très fort", "Nous n'avons pas très bien réussi"]) }, [('time', 1, 'choice')]),
                        'difficile': ( { 'g':'non', 's': random.choice(["Mince, nous avons raté", "Oh non, nous n'avons pas été très fort", "Nous n'avons pas très bien réussi"]) }, [('time', 1, 'choice')]),
                        'pas_content_moi': ( {'g':'', 's':  random.choice(["Je ne suis pas content de moi", "Ce n'est pas beau ce que j'ai fait", "ça ne me plait pas ce que j'ai fait"])}, [('time', 1, 'choice')]),
                        'tu_mecoute': ( { 'g':'', 's': random.choice(["Tu ne m'écoutes \\sel=alt=p+100\\ \\Rspd=130\\ plus \\pau=120\\ \\sel=alt=p-50\\  \\Rspd=70\\ {} ?".format( child_name), "Hey! {} ?".format( child_name), "{} ?".format( child_name), "{}, tu m'écoutes?".format( child_name)]) }, [('time', 1, 'choice')]),
                        'on_essaye': ( {'g':'oui', 's': "Ok, alors on essaye plus tard" }, [('time', 1, 'choice')]),
                        
                        'bravo': ( { 'g':'happy', 's': random.choice(["Felicitations !", "Bravo!", "Bien joué  {}".format( child_name), "Félicitations {}".format( child_name)]) }, [('time', 0.1, 'choice')]),
                        'je_suis_fort': ( { 'g':'chill', 's': random.choice(["je suis trop fort", "je suis très fier de moi!", "J'ai trop bien réussi!"]) }, [('time', 1, 'choice')]),
                        'cest_bien': ( { 'g':'happy', 's': random.choice(["Super!", "C'est bien !", "C'est chouette!"]) }, [('time', 1, 'choice')]),
                        'tu_es_fort': ( { 'g':'happy', 's': random.choice(["trop fort?", "Tu as trop bien réussi {} ".format( child_name), "Tu as trop bien fait!!"]) }, [('time', 1, 'choice')]),
                        'nous_sommes_fort': ( { 'g':'happy', 's': random.choice(["On est trop forts", "On est super forts!", "On a trop bien réussi!"]) }, [('time', 1, 'choice')]),
                        'fier_de_toi': ( { 'g':'', 's':"Je suis fier de toi!"}, [('time', 1, 'choice')]),
                        'applique': ( { 'g':'', 's': random.choice(["tu travaille très bien","tu t'applique très bien!", "tu est bien appliqué"]) }, [('time', 1, 'choice')]),
                        'tu_perseveres': ( {'g':'', 's':random.choice(["Tu n'as pas \pau=5\ \sel=alt=p+50\ abandonné! Bravo!", "Tu as tenu bon, C'est bien !","Tu \sel=alt=p+50\ persévères, Super!"])}, [('time', 1, 'choice')]),

                        'aie': ( { 'g':'', 's': random.choice(["Aie!","Ouilleu", "aoutch, ça fait mal!"]) }, [('time', 1, 'choice')]),
                        'ahahah': ( {'g':'', 's':random.choice(["#LAUGH02# C'est rigolo","Ça me fais rire!", "C'est drôle!"])}, [('time', 1, 'choice')]),
                        'muscle': ( { 'g':'', 's':"Oui mais moi, tu sais, j'ai des muscles en plastique"}, [('time', 1, 'choice')]),

                        'merci': ( { 'g':'"', 's':  random.choice(["merci","Merci beaucoup", "Je te remercie", "merci, {}".format( child_name)])}, [('time', 1, 'choice')]),
                        'repete': ( { 'g':'', 's': random.choice([ "{} , est-ce que tu peux répèter?".format( child_name),"Peux-tu répéter?","Comment?", "Je n'ai pas entendu?"]) }, [('time', 1, 'choice')]),
                        'oui': ( { 'g':'oui', 's':"Oui"}, [('time', 6, 'choice')]),
                        'non': ( { 'g':'non', 's': "Non" }, [('time', 7, 'choice')]),
                        'sais_pas_toi': ( { 'g':'non', 's':random.choice(["Aucune idee ! ,Et toi?","Je ne sais pas. et toi?","Je sais pas trop. et toi?"])}, [('time', 1, 'choice')]),
                        'et_toi': ( { 'g':'', 's':"Et toi?"}, [('time', 3, 'choice')]),

                        #comportement de scenario 
                        'pression_lance': ( {'g':'', 's': random.choice(["Clique sur le jeu qui s'appelle sous-marin", "Démarre le jeu sous-marin"]) }, [('time', 1, 'choice')]),
                        'pression_expli': ( { 'g':'bored', 's': "Je navigue en sous-marin. Appuie ton stylo plus ou moins fort pour m'aider à piloter. Attention aux obstacles. Tu peux aller chercher les étoiles en bonus." }, [('time', 1, 'choice')]),
                        'pression_complet': ( { 'g':'bored', 's': "\sel=alt=p-70\Rappelle-toi \pau=130\ C'est la pression sur le stylo qui pilote. Plus tu appuies fort, plus mon sous-marin descend. Si tu lâches le stylo, mon sous-marin s'arrête. Évite les pics et les rochers." }, [('time', 1, 'choice')]),
                        'archeo_lance': ( { 'g':'', 's': random.choice(["Lance le jeu archéologue", "Clique sur le jeu qui s'appelle archéologue"]) }, [('time', 1, 'choice')]),
                        'archeo_expli': ( { 'g':'bored', 's': "Dans ce jeu, j'ai enterré un trésor dans le sol. Appuie le stylo sur la tablette. Déplace-le pour creuser dans le sol et trouver le trésor" }, [('time', 1, 'choice')]),
                        'archeo_complet': ( { 'g':'bored', 's': "Attention ! \pau=80\ Si tu appuie trop fort, tu risque de casser le trésor. Une fois que tu as trouvé tout, n'oublie pas de valider." }, [('time', 1, 'choice')]),
                        
                        'drapeau_lance': ( { 'g':'', 's': random.choice(["Lance le jeu drapeau", "Clique sur le jeu qui s'appelle drapeau"]) }, [('time', 1, 'choice')]),
                        'drapeau_expli': ( { 'g':'bored', 's':"Je dois livrer ce drapeau, \pau=30\ mais  je ne sais pas à quel pays \pau=50\ il appartient. Tu peux me recopier son nom pour que je puisse le livrer?" }, [('time', 1, 'choice')]),
                        'drapeau_complet': ( { 'g':'bored', 's':"Il faut bien suivre l'example, et écrire dessus pour qu'on puisse livrer. Sinon notre colis risque d'être refusé. " }, [('time', 1, 'choice')]),
                        'alpha_lance': ( { 'g':'', 's': random.choice([ "Lance le jeu alphabet.", "Clique sur le jeu qui s'appelle alphabet."])  }, [('time', 1, 'choice')]),
                        'alpha_expli': ( { 'g':'bored',  's': "Choisis un chiffre, ou une lettre, et montre-moi comment bien l'écrire." }, [('time', 1, 'choice')]),
                        'alpha_complet': ( { 'g':'bored', 's': "Attention ! \pau=80\ Il faut bien que tu me montre en repassant sur le modèle. Plus on suit le modèle, plus le trait est vert, et plus on gagne de points." }, [('time', 1, 'choice')]),
                        
                        'zoo_lance': ( { 'g':'', 's': random.choice(["Lance le jeu zoo", "Clique sur le jeu qui s'appelle zoo"]) }, [('time', 1, 'choice')]),
                        'zoo_expli': ( { 'g':'bored', 's': "Tu peux me montrer comment bien colorier un \sel=alt\ dessin sur la tablette? \pau=50\ On perd des points \sel=alt\ si on dépasse ou si on se trompe de couleurs." }, [('time', 1, 'choice')]),
                        'zoo_complet': ( { 'g':'bored', 's': "il faut bien tout colorier. Si tu n'as pas le temps de finir, tu peux sauvegarder en cliquant sur la croix. On terminera une prochaine fois."}, [('time', 1, 'choice')]),
                        
                        'chimi_lance': ( { 'g':'', 's': random.choice(["Lance le jeu chimiste", "Clique sur le jeu qui s'appelle chimiste"]) }, [('time', 1, 'choice')]),
                        'chimi_expli': ( { 'g':'bored', 's': "Copie le mot avec les bonnes couleurs avec moi. Quand tu lève le stylo, la couleur change." }, [('time', 1, 'choice')]),
                        
                        'tilt_lance': ( { 'g':'', 's': random.choice(["Lance le jeu hélicoptère", "Clique sur le jeu qui s'appelle hélicoptère"]) }, [('time', 1, 'choice')]),
                        'tilt_expli': ( { 'g':'bored', 's':"Je conduis un hélicoptère dans le jeu, et tu dois m'aider à piloter en plaçant ton stylo dans le cercle. Aide-moi à livrer les boîtes." }, [('time', 1, 'choice')]),
                        'tilt_complet': ( { 'g':'bored', 's': "\sel=alt=p-70\Rappelle-toi \pau=130\  Je vais dans la direction vers laquelle tu places ton stylo. On doit prendre \pau=50\ et livrer les boites. Une flèche rouge nous dit \pau=50\ où on doit aller. Si tu lâches le stylo, la boîte tombe." }, [('time', 1, 'choice')]),
                        
                        'cowritter_lance': ( { 'g':'', 's':  random.choice(["Démarre le jeu qui s'appelle Apprenti", "Clique sur Apprenti"]) }, [('time', 1, 'choice')]),
                        'cowritter_expli_class': ( { 'g':'bored', 's': "Tu m'entraîne à écrire. Dans ce jeu, mon surnom est le robot de proust. Tu me montre comment bien corriger mes erreurs!" }, [('time', 1, 'choice')]),
                        'cowritter_complet': ( { 'g':'bored', 's': "\sel=alt=p-70\Rappelle-toi \pau=130\ Tu m'apprends à écrire. Mieux tu me montre, mieux j'apprends. À la fin on verra ma note." }, [('time', 1, 'choice')]),
                        
                        'jus_lance': ( { 'g':'', 's': random.choice(["Clique sur le jeu qui s'appelle jus", "jouons au jeu qui s'appelle jus"]) }, [('time', 1, 'choice')]),
                        'jus_expli': ( { 'g':'bored', 's': "Aide mon avatar à faire un jus. Laisse ta main gauche appuyée sur le bouton jaune pour allumer la lumière. Avec tes doigts, suit les étapes qui sont indiqué dans le cadre gris." }, [('time', 1, 'choice')]),
                        'jus_complet': ( { 'g':'bored', 's': "Attention ! \pau=80\ Il faut cliquer sur tout les fruits indiqués en même temps. Pour couper le fruit, il faut cliquer sur le fruit et le couteau en même temps, et glisser le couteau vers le fruit. Pour presser le jus, glisse tous les fruit en même temps vers le pressoir." }, [('time', 1, 'choice')]),

                        'poursuite_lance': ( { 'g':'', 's':  random.choice(["Clique sur le jeu Poursuite","Lances le jeu qui s'appelle Poursuite"]) }, [('time', 1, 'choice')]),
                        'poursuite_expli': ( { 'g':'bored', 's':"J'ai faim. Suis le chemin avec ton stylo et ramasse tous les fruits pour moi."}, [('time', 1, 'choice')]),
                        'poursuite_complet': ( { 'g':'',  's': "\sel=alt=p-50\Rappelle-toi \pau=100\ il faut bien rester sur le chemin bleu pour ne pas perdre des ballons. Tu peux prendre ton temps." }, [('time', 1, 'choice')]),
                        
                        'tu_viens': ( { 'g':'excited', 's':random.choice([ "{} c'est l'heure de mon cours, non?".format( child_name), "{} tu viens m'aider à améliorer mon écriture?".format( child_name), "{} je suis impatient d'écrire, tu viens?".format( child_name),"{} tu peux venir pour qu'on fasse mon cours?".format( child_name)])}, [('time', 1, 'choice')]),
                        'ton_nom': ( { 'g':'', 's': random.choice([ "Clique sur ton nom pour commencer", "Avant qu'on commence, tu dois cliquer sur ton nom"])}, [('time', 1, 'choice')]),
                        'ca_va': ( { 'g':'', 's': random.choice(["Comment vas-tu?", "Ça va?", "Tu vas bien?" ]) }, [('time', 1, 'choice')]),
                        'bonjour': ( { 'g':'hi', 's': random.choice(["Bonjour, {}".format( child_name) , "Coucou? {}".format( child_name) ]) }, [('time', 1, 'choice')]),
                        
                        'je_mappelle_qt': ( { 'g':'hi', 's':"Bonjour, je m'appelle Nao. Et toi, comment tu t'appelles?" }, [('time', 1, 'choice')]),
                        'tu_veux_maider': ( { 'g':'jaime',  's':"Je suis content de te rencontrer. J'ai besoin de ton aide pour mieux écrire, car je ne suis pas très fort. Est-ce que tu es d'accord pour m'aider? On s'améliorera ensemble!" }, [('time', 1, 'choice')]),
                        'tu_maides_encore': ( { 'g':'sad', 's':"Comme je ne sais pas très bien écrire, tu avais décidé de m'aider pour qu'on devienne meilleurs ensemble. On continue?"}, [('time', 1, 'choice')]),
                        'adieu': ( { 'g':'hello', 's':"On a terminé notre dernière séance. Merci beaucoup. J'ai fais beaucoup de progrès, et je me suis bien amusé. J'espère que toi aussi. " }, [('time', 1, 'choice')]),
                        'adieu2': ( { 'g':'hi',  's': "Au revoir {} ! Bon courage pour la suite!".format( child_name) }, [('time', 1, 'choice')]),
                        
                        'pause': ( { 'g':'bored', 's':random.choice(["Après un niveau, on s'arrête \pau=20\ et on \Rspd=70\ réfléchit \Rspd=80\ ensemble.", "On fait un niveau, et on s'arrête pour que tu m'expliques."])}, [('time', 1, 'choice')]),
                        'change_jeu': ( { 'g':'', 's': random.choice(["Tu veux qu'on fasse un autre \sel=alt=p-30\jeu?", "Tu as envie de changer de jeu?", "On passe à la prochaine activité?"])}, [('time', 1, 'choice')]),
                        'choisis_jeu': ( { 'g':'',  's': random.choice([ "Je te laisse choisir la prochaine activité sur la tablette.", "À toi de choisir dans les jeux sur la tablette.", "Parmi les jeux qu'on a sur notre \Rspd=100\ tablette,\Rspd=80\ lequel tu veux faire ensuite?"]) }, [('time', 1, 'choice')]),
                        
                        'dernier_jeu': ( { 'g':'', 's':random.choice(["Ce sera notre dernière activité.", "Plus qu'une partie et on arrête.", "C'est le dernier jeu."])}, [('time', 1, 'choice')]),
                        'cetait_bien': ( { 'g':'happy', 's': random.choice(["C'était une super séance, {}".format( child_name), "nous avons bien travaillé aujourd'hui"])}, [('time', 1, 'choice')]),
                        'tu_maide': ( { 'g':'jaime', 's':random.choice([ "{} , Merci pour ton aidé".format( child_name), "Merci {} tu m'aides beaucoup!".format( child_name), "tu m'as beaucoup aidé {}".format( child_name)]) }, [('time', 1, 'choice')]),
                        'mes_progres': ( {'g':'jaime',  's': random.choice([ "Tu as vu comment j'écrivais et comment j'ai progressé?", "Tu as vu comme je me suis amélioré en écriture?", "Tu as vu mes progrès?"]) }, [('time', 1, 'choice')]),
                        'bisou': ( { 'g':'kiss', 's':"Je peux t'envoyer un bisou?"}, [('time', 8, 'choice')]),
                        'bcp_travaille': ( { 'g':'happy', 's': random.choice(["Nous avons beaucoup travaillé aujourd'hui,", "Nous avons travaillé dur", "Nous avons beaucoup travaillé ensemble"])}, [('time', 1, 'choice')]),
                        'il_est_lheure': ( { 'g':'bored',  's': random.choice([ "Il est l'heure, on doit s'arrêter", "C'est l'heure à laquelle on doit finir"]) }, [('time', 1, 'choice')]),
                        'arrete': ( { 'g':'bored', 's':random.choice(["{} , On s'arrête pour aujourd'hui".format( child_name), "On arrête là cette séance"])}, [('time', 1, 'choice')]),
                        'au_revoir': ( { 'g':'hi', 's': random.choice(["À bientôt!", "À la prochaine!", "Au revoir,{} !".format( child_name)])}, [('time', 1, 'choice')]),  
                        #  

                        # walk 
                        'walk_fwd': ( {'w': [1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
                        # 'stop': ( {'w': [0,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
                        'walk_back': ( {'w': [-1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
                        'strife_left': ( {'w': [0,1,0,0,0,0]}, [('time', 0.1, 'choice')]),
                        'strife_right': ( {'w': [0,-1,0,0,0,0]}, [('time', 0.1, 'choice')]),
                        'rotate_left': ( {'w': [0,0,0,0,0,1]}, [('time', 0.1, 'choice')]),
                        'rotate_right': ( {'w': [0,0,0,0,0,-1]}, [('time', 0.1, 'choice')]),



                        'end': ((), [('time', 0.1, 'end')]) }

        # print(self.states)

        self.state = 'begin'

        self.angles_pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=10)
        self.walk_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


        rospy.Timer(rospy.Duration( self.states[self.state][1][0][1]), self.time_callback, oneshot=True)
        print(self.state)


    def time_callback(self, event):
        # go to next state
        print('time callback')
        triggers = self.states[self.state][1]
        for trigger in triggers:
            if trigger[0] == 'time':
                self.state = trigger[2]
                print('next_state: ' + self.state)
                self.next_state()
#        self.state = self.states[self.state][2]
#        pass

    def keyboard_callback(self, key):
        print('keyboard callback: ' + key)
        self.keyboard_pub.publish(key)
        triggers = self.states[self.state][1]
        for trigger in triggers:
            if trigger[0] == 'woz':
                if trigger[1] == key:
                    self.state = trigger[2]
                    print('next_state: ' + self.state)
                    self.next_state()
                    # Mettre à jour la valeur de last_button
                    global last_button
                    last_button = key
                    break
                else:
                    if trigger[2] == last_button:
                        self.state = trigger[2]
                        print('next_state2: ' + self.state)
                        self.next_state()
                        break; 
#        pass

    def next_state(self):
        if(self.state != 'end'):
            self.state_pub.publish(self.state)
            # send bhw
            bhw = self.states[self.state][0]
            if(len(bhw)):
                # AL machine => pass to smach
                print(self.state + ' =bhw=> ' + str(bhw))

                if 'h' in bhw:
                    self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['HeadYaw', 'HeadPitch'], joint_angles=bhw['h'], speed=0.25))
                if 'la' in bhw:
                    self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand'], joint_angles=bhw['la'], speed=0.25))
                if 'ra' in bhw:
                    self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand'], joint_angles=bhw['ra'], speed=0.25))
                if ('g' in bhw) or ('s' in bhw):
                    client = actionlib.SimpleActionClient('/nao_behave', NaoBehaviorAction)
                    client.wait_for_server()

                    goal = NaoBehaviorGoal( gesture=bhw['g'] if 'g' in bhw else '',
                                            speech=bhw['s'] if 's' in bhw else '')
                    client.send_goal(goal)
                    # ...
                    client.wait_for_result()
                    result = client.get_result()
                if 'w' in bhw:
                    cmd_vel = Twist()
                    cmd_vel.linear.x=bhw['w'][0]
                    cmd_vel.linear.y=bhw['w'][1]
                    cmd_vel.linear.z=bhw['w'][2]
                    cmd_vel.angular.x=bhw['w'][3]
                    cmd_vel.angular.y=bhw['w'][4]
                    cmd_vel.angular.z=bhw['w'][5]
                    self.walk_pub.publish(cmd_vel) 


            # prepare jump for next state
            triggers = self.states[self.state][1]

            # print(self.state + ' =trig=> ' + str(triggers))
            for trigger in triggers:
                if trigger[0] == 'time':
                    rospy.Timer(rospy.Duration(trigger[1]), self.time_callback, oneshot=True)


    def execute(self):
        while not rospy.is_shutdown():
            if self.state == 'end': break
            global is_clicked
            key = getKey(0.1)
            if (len(key)):
                self.keyboard_callback(key)
            else:
                if is_clicked:
                    self.keyboard_callback(last_button)
            is_clicked = False  
            #     time.sleep(0.5)  
            self.rate.sleep()


if __name__ == '__main__':
    rospy.init_node('nao_play')

    nao_play = NaoPlay()
    nao_play.execute()


