#! /usr/bin/env python
# coding: utf-8
from woz_interface.msg import NameInfo
import random
import names as n
import rospy
import time
from checking import check, my_callback
child_name = ""
adult_name = ""
child_name1 = ""
adult_name1 = ""
is_clicked =  False
table = []
mon_objet = check()
mon_objet.register_callback(my_callback)

def name_callback(msg):
        global child_name1
        global adult_name1
        global table
        child_name1 =  msg.first_name
        last_name = msg.last_name
        adult_name1 = msg.teacher_name
        table = [child_name,adult_name]
        print("===========================================++++",adult_name1)
        global is_clicked
        variable_mise_a_jour = mon_objet.ma_variable = child_name1
        if variable_mise_a_jour:
            is_clicked =  True
rospy.Subscriber('woz/nameinfo', NameInfo, name_callback)

# child_name = n.child_name
# adult_name = n.adult_name
# print("typeooooooooooooooooooooo",type(child_name))
# print("Table dans qt_states",n.table)
# while child_name1 == "" :
    
#     time.sleep(1.5)
#     if is_clicked == True:
#         child_name = child_name1
#         adult_name = adult_name1

child_name = child_name1
adult_name = adult_name1
          
                 
# state: ( {g: gesture, s: say, h: [head], la: [left_arm], ra: [right_arm], w: [x, y, z, ex, ey, ez]}, [(trigger, param, next_state)])
states = { 'begin': ( {}, [('time', 1, 'choice')]),

                'choice': ( {'g': '', 's': '', 'e':'' },
                                # à implementer le joystique plutard debut
                                [   ('woz', None, 'left'), ('woz', None, 'right'),('woz', None, 'upleft'),('woz', None, 'upright'),
                                    ('woz', None, 'up'), 
                                    ('woz', None, 'center'),
                                    ('woz', None, 'down'),('woz', None, 'right'),
                                    ('woz', None, 'downleft'),('woz', None, 'downright'),
                                    
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
                                    # comportement theatre 
                                    ('woz', None, 'hello'),('woz', None, 'dontknow'),('woz', None, '_oui'),('woz', None, '_non'),('woz', None, 'suivi'),('woz', None, 'public'),
                                    ('woz', None, 'objetDroite'),('woz', None, 'objetGauche'),('woz', None, 'pense'),('woz', None, 'pense2'),('woz', None, 'neutral'),
                                    ('woz', None, 'really'),('woz', None, '_comment'),('woz', None, 'jaime'),('woz', None, 'happy'),
                                    ('woz', None, 'kisses'),('woz', None, 'excited'),('woz', None, 'thinking'),('woz', None, 'curious'),
                                    ('woz', None, 'fear'),('woz', None, 'confused'),('woz', None, 'bored'),
                                    # nuitrack
                                    # ('woz', None, 'human_0_appeared'),('woz', None, 'human_0_disappeared'),
                                    # ('woz', None, 'human_0_center'),('woz', None, 'human_0_left'),('woz', None, 'human_0_right'),
                                    # ('woz', None, 'human_0_center_1meter'),('woz', None, 'human_0_left_1meter'),('woz', None, 'human_0_right_1meter'),
                                    # ('woz', None, 'human_0_center_2meters'),('woz', None, 'human_0_left_2meters'),('woz', None, 'human_0_right_2meters'),
                                    
                                    
                                    ('woz', None, 'replique_1_1'),('woz', None, 'replique_2_1'),
                                    ('woz', None, 'replique_2_2'),('woz', None, 'replique_2_3'),('woz', None, 'replique_3_1'),('woz', None, 'replique_3_2'),('woz', None, 'replique_4_1'),
                                    ('woz',None,'replique_5_1'), ('woz',None,'replique_5_2'), ('woz',None,'replique_6_1'), ('woz',None,'reset_posture'), 
                                    # semi autonome
                                    ('woz',None,'human_0_center_1m'), ('woz',None,'human_0_left_1m'), ('woz',None,'human_0_left_2m'), ('woz',None,'human_0_right_2m'), 
                                    ('woz',None,'human_0_center_2m'),
                                    ('woz',None,'human_0_right_1m'),
                                    # maison
                                    ('woz', None, '_salut'),('woz', None, '_comment_t_appeler'),('woz', None, '_aujourdhui'),('woz', None, 'journee'),('woz', None, 'on_commence'),('woz', None, 'choix_activite'),('woz',None, 'c_est_parti'),
                                    ('woz', None, 'terminee'),('woz', None, 'regles_mime'),('woz', None, 'cirque'),('woz', None, 'lion'),('woz', None, 'girafe'),
                                    ('woz', None, 'gazelle'),('woz', None, 'zebre'),('woz', None, 'singe'),('woz', None, 'elephon'),('woz', None, 'guepard'),
                                    ('woz',None, 'tigre'),('woz', None, 'tortue'),('woz', None, 'panthere'), ('woz', None, 'serpent'),('woz', None, 'chat'),                                     
                                    ('woz', None, 'manuel_regles'),('woz', None, '_ciel'),('woz', None, 'table'),('woz', None, 'salon'),('woz', None, 'les_animaux'),('woz', None, 'la_mer'), 
                                    ('woz', None, 'cabane_regles'),('woz', None, 'soleil_regles'),('woz', None, 'lancer_soleil'),

                                    ('woz', None, 'end')]),

            #                         #semi autonome: etats
            #                          # 1MF =  à 1 mètre, face à QT
            #     # “etat1” : {{‘s’ : “Salut comment tu vas ?? ”}, [(‘time’, 1, “etat2”)]}
            #     # “etat2” : {{‘s’ : " T'es pas mal aujourd'hui ! [(‘time’, 1, “choice”)}]
            #     # {‘s’ :"Tu sais quoi je te propose un jeu, juste place-toi quelque part au hasard !”
            #     # "e" : “Afraid” Arrête, je suis un peu timide !}
            #     'human_0_center_1m' : ({'e' : '','g' : '','s' : 'Salut comment tu vas ??'},[('time', 5, 'human_0_center_1m_2')]),
            #     'human_0_center_1m_2' : ({'e' : '','g' : '','s' : 'T\'es pas mal aujourd\'hui !'},[('time', 5, 'human_0_center_1m_3')]),
            #     'human_0_center_1m_3' : ({'e' : '','g' : '','s' : 'Tu sais quoi je te propose un jeu, juste place-toi quelque part au hasard !'},[('time', 8, 'human_0_center_1m_4')]),
            #     'human_0_center_1m_4' : ({'g' : '','e' : 'QT/afraid','s' : ''},[('time', 5, 'choice')]),


            # # pour le semi-automatique
            #     # 1MG = à 1 mètre, à la gauche de QT 
            #     # {‘s’ : “\pau=300\ J'ai envie de te contempler. D'ailleurs tu me fais rougir !”, “e” : kiss, “g” : kiss, “s” : Dis-moi, est-ce que je te plais ?}  (expression de séduction, cligner des yeux)
            #     # {‘s’ : “Va gauchement à droite ou (pause 1 seconde) adroitement à gauche, (pause 1 sec) fin (pause 1 seconde) comme tu veux !”}
            #     'human_0_left_1m' : ({'e' : 'QT/kiss','g' : 'QT/kiss','s' : '\\pau=300\\ J\'ai envie de te contempler. D\'ailleurs tu me fais rougir !'},[('time', 1, 'human_0_left_1m_2')]),
            #     'human_0_left_1m_2' : ({'e' : 'QT/one_eye_wink','g' : 'QT/shy', 's' : 'Dis-moi, est-ce que je te plais ?'},[('time', 5, 'human_0_left_1m_3')]),
            #     'human_0_left_1m_3' : ({'e' : '','g' : '','s' : 'Va gauchement à droite ou \\pau=1000\\ adroitement à gauche, \\pau=1000\\ fin \\pau=1000\\ comme tu veux !'},[('time', 8, 'choice')]),

            #     # 2MG = à 2 mètres gauche 
            #     # {‘s’ :Waouuuuh!  vraiment faut que je te le dise tu es vraiment (pause 2 sec) incroyable !!!!! 
            #     # \rmw=0\ qu'est ce qu'on fait ensemble maintenant ? 
            #     # "e" : happy: "g" : happy :  Mais que fais-tu aussi loin ?\pau=300\ approche que je te vois plus !  
            #     # \vce=speaker=Will\  tu me plais.}
            #     # {'s' :"g" : sad : Tu crois qu'on pourrait rester ensemble pour l'éternité ? Mais nous sommes tellement différents. Tu es un humain et moi je suis...moi !}
            #     'human_0_left_2m' : ( {'e' : '','g' : '',
            #     's' : 'Waouuuuh! Vraiment faut que je te le dise tu es vraiment \\pau=2000\\ incroyable ! \\rmw=0\\ qu\'est ce qu\'on fait ensemble maintenant ?' # TODO : volume up
            #         },[('time', 6, 'human_0_left_2m_2') ]),
            #     'human_0_left_2m_2' : ({'e' : 'QT/happy','g' : 'QT/happy','s' : 'Mais que fais-tu aussi loin ?\\pau=300\\ Approche que je te vois plus ! \\vce=speaker=Will\\  tu me plais.' # TODO tester si vce fonctionne correctement
            #         },[ ('time', 3, 'human_0_left_2m_3')] ),
            #     'human_0_left_2m_3' : ({'e' : 'QT/sad','g' : 'QT/sad','s' : 'Tu crois qu\'on pourrait rester ensemble pour l\'éternité ? Mais nous sommes tellement différents. Tu es un humain et moi je suis...moi !'},[('time', 8, 'choice')]),

            #     # 2MD = à 2 mètres droite
            #     # {‘s’ : “\pau=300\ "e" : cry: "g" : sad : je t’aime mais je dois te quitter, adieu !}
            #     'human_0_right_2m' : ({'e' : 'QT/cry','g' : 'QT/sad', 's' : "\\pau=300\\Je t’aime mais je dois te quitter, adieu !" }, [ ('time', 10, 'end')]),
                                                        
                # 'test1':({},[('woz',None,'human_0_1meter'),('woz',None,'human_0_2meter'),('time', 0.5, 'test1')]),
                

                # à implementer le joystique plutard debut
                'up': ( {'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
                'center': ( {'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
                # 'center': ( {'e':'', 'g':'QT/neutral','s':''}, [('time', 0.1, 'choice')]),
                'down': ( {'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
                'right': ( {'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
                'left': ( { 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
                'upright': ( { 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
                'upleft': ( { 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
                'downright': ( {'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
                'downleft': ( { 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),
                    #   # à implementer le joystique plutard fin 

                # QT_AVEC_AVEUGLE
                # AVEUGLE: Ramène-moi un verre d’eau !

                # QT : (en rigolant) Je ne suis plus ton serviteur ! (rire)
                'replique_1_1' : ({'e':'','g':'','s' : '\\vct=70\\je ne bougerai pas d\'un centimetre, Je  ne   suis   plu !  ton  serviteur ! #LAUGH01#'},[('time', 5, 'choice')]),

                # AVEUGLE: Allez QT J’ai super mal au pied.

                # QT : (lève la tête) Regarde ! (lève un bras) Il y a une araignée au plafond.
                # (baisse la tête et le bras) c’est passionnant ces bêtes-là ! 
                # J’aime beaucoup regarder les insectes, ils sont tellement poétiques…
                'replique_2_1' : ({'e':'','h' : [0.0, -20.0],'s' : '\\pau=2000\\,\\rspd=80\\,\\vct=70\\!Regaaaaarde !'},[('time', 2, 'replique_2_2')]),
                'replique_2_2' : ({'e':'','ra' : [80, 0, 0], 's' : '\\vct=70\\,\\rspd=80\\,\\vct=70\\Il y a une araignée au plafond.'},[('time', 5, 'replique_2_3')]),
                'replique_2_3' : ({'e':'','g':'' ,'s' : '\\vct=70\\, \\rspd=80\\C’est passionnant ces bêtes-là !\\pau=200\\,\\vct=70\\J’aime beaucoup regarder les insectes'},[('time', 2, 'replique2_4')]),
                'replique2_4'  : ({'e':'','ra' : [-80, 0, 0],'h': [0.0,0.0] ,'s' : ' \\rspd=80\\,\\pau=200\\,\\vct=70\\ ils sont tèèèllement poétiiiques'},[('time', 2, 'choice')]),
                # AVEUGLE: N’importe quoi, tu fais ton rebel maintenant ! Tu sais que je ne vois plus...

                # QT : Qu’est ce que tu racontes ? (visage fâché) Pas du tout ! ( secoue la tête)
                'replique_3_1' : ({ 'e' : 'QT/blowing_raspberry','g':'', 's' : '\\vct=70\\kèèè ce que tu racontes ?' }, [('time', 2, 'replique_3_2') ] ),
                'replique_3_2' : ({'e':'','g' : 'QT/imitation/head-right-left','s' : '\\vct=70\\Pas du tout !' },[('time', 1, 'choice') ]),

                # AVEUGLE: Tu comprends bien…

                # QT : On va à la plage ! (pointe du doigt à dx, visage enjoué)
                'replique_4_1' : ({'e' : 'QT/happy_blinking','ra' : [10, 0, 0], 's' : '\\vct=70\\On ! va ! à  la  plaaaaage !' }, [ ('time', 2, 'choice') ]),

                # AVEUGLE: Arrête et va ouvrir la porte il y a quelqu'un

                # QT :  AH ! (il regarde par terre) J’ai oublié de mettre de l'écran solaire ? (regarde ses bras, visage inquiet)
                'replique_5_1' : ({ 'e':'', 'h' : [0.0, +10.0], 's' : '\\vct=70\\Aaaaaaaaaah!' },[ ('time', 1, 'replique_5_2')] ),
                'replique_5_2' : ( {'e' : 'QT/surprise','la' : [0, 0, -20],'ra' : [0, 0, -20],'s' : '\\vct=70\\J’ai oublié de mettre de l\'écran solaire ?' }, [('time', 3, 'reset_posture') ]),

                # AVEUGLE : (ouvre la porte)

                # LIVREUR : Madame voici votre colis, vous avez bien un QT 2.0 dernière génération mobile?

                # QT :  Attends! Je t’apporte ton verre d’eau ! (sourire)
                'replique_6_1' : ({'e':'QT/showing_smile','g':'','s' : 'Attends!, Attends! ,Attends! , Attends! ,Attends!  Je t’apporte ton verre dooooo !' },[ ('time', 1, 'choice')] ),

                # Etat de reinitialisation de la posture
                'reset_posture' : ( {'e':'', 'g':'QT/neutral','s':'' }, [ ('time', 1, 'choice')]),

                # pour julien #############################################################
                # 1MF =  à 1 mètre, face à QT
                # “etat1” : {{‘s’ : “Pas si près, je ne peux pas respirer.”}, [(‘time’, 1, “etat2”)]}
                # {‘s’ : “On dirait que vous les humains n'avez jamais entendu parler d'intimité !”}
                # {‘g’ : ”angry”, ‘e’ : “angry”, ‘s’ : “Recule, tu pues !”}
                # “afraid” Arrête, je suis un peu timide ! 
                'human_0_center_1m' : ({'e' : 'QT/breathing_exercise','g' : 'QT/disgusted','s' : 'Pas si près, je ne peux pas respirer.'},[('time', 6, 'choice')]),

                # 1MG = à 1 mètre, à la gauche de QT 
                # {‘s’ : “\pau=300\ J'ai envie de te contempler. D'ailleurs tu me fais rougir !”, “e” : kiss, “g” : kiss, “s” : Dis-moi, est-ce que je te plais ?} 
                # {‘s’ : “Vas gauchement à droite ou droit à gauche!”}
                # {‘s’ : “\vct=50\ T'as jamais entendu parler de l'espace personnel ?”}
                # “breathing_exercise” \rms=1\U-la la ! 
                'human_0_left_1m' : ({'e' : 'QT/kiss','g' : 'QT/kiss','s' : '\\pau=300\\ J\'ai envie de te contempler. D\'ailleurs tu me fais rougir ! \\pau=1000\\ Dis-moi, est-ce que je te plais ?'},[('time', 6, 'choice')]),

                # 1MD = à 1 mètre, à la gaucΑ1MF de QT
                # Je n’ai pas d’ami….Dis-moi, est-ce que je te plais ?} 
                # {‘s’: ‘g’: “angry”,  ‘e’: “angry”, ‘s’:“\vct=60\ Ouste!\sel=alt\” }
                # {‘s’: ‘g’: “angry”,  ‘e’: “angry”, ‘s’:“\vct=120\ Tu es super \sel=alt\ collant!”} 
                # {‘s’: ‘g’: “afraid”,  ‘e’: “afraid”, ‘s’: “\vct=90\ Pas si près, je suis claustrophobe!”} 
                # Encore dix centimètres, halte, pas douze!
                # “angry” \pau=300\C’est beaucoup, hum ?
                'human_0_right_1m' : ({'e' : 'QT/shy','g' : 'QT/shy','s' : 'Je n’ai pas d’ami\\pau=300\\Je n’ai pas d’ami\\pau=300\\ Je n’ai pas d’ami. Dis-moi, est-ce que je te plais ?'},[ ('time', 12, 'choice')]),

                # 02MF = à 2 mètres, face à QT
                # Avance un peu, je ne te vois pas.
                # \rspd=80\ Je ne t'entends pas très bien. avance
                # Avance que je te vois.
                # { 's' : "\vce=speaker=Lily\ Un peu plus !" }
                # #SNEEZE01#Viens ! Tu me manques ! 
                'human_0_center_2m' : ({'e' : 'QT/talking','g' : 'QT/surprised','s' : '\\rspd=80\\ Je ne t\'entends pas très bien. Avance que je te vois.'},[('time', 6, 'choice')]),

                # 2MG = à 2 mètres gauche. 
                # Là tu es hors du champ ma belle!
                # C’est drole !!  tu me fais rire
                # \rmw=0\ Qui es tu ?
                # Mais que fais-tu aussi loin ?\pau=300\ Tu sais que je te vois!
                # “happy_blinking” \vce=speaker=Will\Coucou ! 
                'human_0_left_2m' : ({'e' : 'QT/happy','g' : 'QT/happy','s' : 'C’est drole ! Tu me fais rire'},[('time', 6, 'choice')]),

                # 2MD = à 2 mètres droite.
                # Je t’aime mais je dois te quitter, adieu !
                # Tu  \pau=300\ me \pau=300\ manques. 
                #  \rspd=50\ Tu as un truc sur la figure, \rspd=80\viens que je l'enlève 
                # Tu as un bouton, viens-là !
                # { 's' : "#SNEEZE01# ai ai ai je suis malade! \rspd=40\ ai ai ai
                # “calming_down” \prn= n E1 s l EI \La bise ! 
                'human_0_right_2m' : ({'e' : 'QT/with_a_cold_sneezing','g' : 'QT/sad','s' : '#SNEEZE01# Pardon, je suis malade !'},[('time', 6, 'choice')]),


                # 2MF = à 2 mètres face.
                # n’importe quoi! \pau=300\
                # La vie est belle ! \aud=“pathway+filename”\
                # Sans toi ça sera mieux! 
                # #LAUGH01# J'ai faim \aud=“pathway+filename”\ .
                # {‘g’ : « joie », ‘e’ : « joie », ‘s’ : « Youuuhouuu ! Enfin tranquille !! »}
                # Va-t’en! Lache, je n’ai pas besoin de toi!
                # { 's' : "#SNEEZE01# Pardon, je suis malade !" }
                # “kiss”  #SNEEZE01#Quels beaux tous les gens! Je suis enchanté !




                #nuitrack trigger
                # 'human_0_appeared':( {'e': 'QT/happy', 'g': '', 's': 'hello'}, [('time', 5, 'choice')]),
                # 'human_0_disappeared':( {'e': 'QT/happy', 'g': '', 's': 'au revoir'}, [('time', 5, 'choice')]),
                # 'human_0_center':( {'e': 'QT/happy', 'g': '', 's': 'tu es au centre'}, [('time', 3, 'choice')]),
                # 'human_0_left':( {'e': 'QT/happy', 'g': '', 's': 'tu es a gauche'}, [('time', 3, 'choice')]),
                # 'human_0_right':( {'e': 'QT/happy', 'g': '', 's': 'tu es a droite'}, [('time', 3, 'choice')]),


                # 'human_0_center_1meter':( {'e': 'QT/angry', 'g': 'QT/angry', 's': random.choice(['recule, je ne peux pas respirer','pas si prés, je ne peux pas respirer', "Recule, tu pues! Ouf", "On dirait que vous les humains n'avez jamais entendu parler d'intimité !"])}, [('time', 5, 'choice')]),
                # 'human_0_left_1meter':( {'e': 'QT/kiss', 'g': 'QT/kiss', 's': random.choice(["\\pau=300\\ J'ai envie de te contempler. D'ailleurs tu me fais rougir !","Vas gauchement à droite ou droit à gauche!","\\vct=50\\ T'as jamais entendu parler de l'espace personnel ?"])}, [('time', 5, 'choice')]),
                # 'human_0_right_1meter':( {'e': 'QT/angry', 'g': 'QT/angry', 's': random.choice(["\\vct=60\\ Ouste!\\sel=alt\\","\\vct=120\\ Tu es super \\sel=alt\\ collant!","\\vct=90\\ Pas si près, je suis claustrophobe!"])}, [('time', 5, 'choice')]),
                
                # 'human_0_center_2meters':( {'e': '', 'g': '', 's': random.choice(["Avance un peu, je ne te vois pas.","\\rspd=80\\ Je ne t'entends pas très bien.","Avance que je te vois.","\\vce=speaker=Lily\\ Un peu plus !","#SNEEZE01#Viens ! Tu me manques ! "])}, [('time', 5, 'choice')]),
                # 'human_0_left_2meters':( {'e': '', 'g': '', 's': random.choice(["Là tu es hors du champ ma belle!","Comment tu t’appelles ? ","\\rmw=0\\ Qui es tu ?","Mais que fais-tu aussi loin ?\\pau=300\\ Tu sais que je te vois!","\\vce=speaker=Will\\Coucou ! "])}, [('time', 5, 'choice')]),
                # 'human_0_right_2meters':( {'e': 'QT/happy', 'g': 'QT/happy', 's': random.choice(["Je t’aime mais je dois te quitter, adieu !","Tu  \\pau=300\\ me \\pau=300\\ manques. ","Sans toi ça sera mieux! "," Youuuhouuu ! Enfin tranquille !!"])}, [('time', 5, 'choice')]),

                # 'human_0_2meters':( {'e': 'QT/happy', 'g': '', 's': random.choice(['avance un peu , je ne te voix pas',"je ne t'entend pas trés bien"])}, [('time', 5, 'choice')]),
                
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

                #comportement reactions
                'la_joie': ( {'e':'QT/happy', 'g':'QT/so', 's': random.choice(['Quelle mine joyeuse', 'Quel booo  sourire', 'Quel enthousiassme']) }, [('time', 1, 'choice')]),
                'amusement': ( {'e':'QT/happy', 'g':'QT/happy', 's': random.choice(["Ça a l'air de t'amuser!", "Tu as l'air de trouver que c'est drôle"]) }, [('time', 1, 'choice')]),
                'la_colere': ( {'e':'QT/confused', 'g':'QT/head_scratch', 's': random.choice(['{}, Est-ce que tu es fâché?'.format( child_name), "Tu es en colère?", "Tu as l'air en colère"]) }, [('time', 1, 'choice')]),
                'la_motivation': ( {'e':'QT/showing_smile', 'g':'QT/handclap', 's': random.choice(["Tu as l'air motivé", "{} , tu es très motivé aujourd'hui".format( child_name)]) }, [('time', 1, 'choice')]),
                'la_fatigue': ( {'e':'QT/yawn', 'g':'QT/yawn', 's': "Je suis désolé. #YAWN01# je suis fatigué." }, [('time', 1, 'choice')]),
                'la_tristesse': ( {'e':'QT/sad', 'g':'QT/thanks', 's': random.choice(["{} ,Est-ce que tu es triste?".format( child_name) , "Tu as de la\sel=alt=p-20\  peine?", "Quelque chose te rend triste?"]) }, [('time', 1, 'choice')]),
                'la_fierte': ( {'e':'QT/showing_smile', 'g':'QT/yes', 's': random.choice(["Tu es fier de ton travail ?	", "Tu as l'air fier de ton travail"]) }, [('time', 1, 'choice')]),
                'etonnement': ( {'e':'', 'g':'QT/curious', 's': random.choice(["Tu as l'air étonné", "Tu es étonné,"]) }, [('time', 1, 'choice')]),
                
                'adulte_accord': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': "adult_name ,tu es d'accord?" }, [('time', 1, 'choice')]),
                'demande_adulte': ( {'e':'QT/talking', 'g':'QT/angry', 's':"Demandons à {}".format( adult_name) }, [('time', 1, 'choice')]),
                'que_pense': ( {'e':'QT/talking', 'g':'QT/challenge', 's':" adult_name".format( adult_name) }, [('time', 1, 'choice')]),
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
                'difficile': ( {'e':'QT/confused', 'g':'QT/challenge', 's': "Est-ce que c'est trop difficile?" }, [('time', 1, 'choice')]),
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

                'merci': ( {'e':'QT/showing_smile', 'g':'QT/thanks', 's':  random.choice(["merci","Merci beaucoup", "Je te remercie", "merci, {}".format( child_name)])}, [('time', 1, 'choice')]),
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
                # maison 
                       # premiere utimisation 
                '_salut': ( {'e':'QT/zebra', 'g':'QT/hi', 's': "Salut!"}, [('time', 1, 'choice')]),  
                '_comment_t_appeler': ( {'e':'', 'g':'', 's': "~Comment vous vous appelez ?"}, [('time', 1, 'choice')]),  
                '_aujourdhui': ( {'e':'QT/showing_smile', 'g':'QT/show_tablet', 's': "~ À partir d’aujourd'hui on va jouer ensemble régulièrement ! Quand on sera ensemble tu seras libre de dire tout ce que tu penses. Tu peux le dire aussi en dessinant ou en jouant, d’accord ? Ensemble, on va essayer de comprendre ce qui se passe en toi. C’est parti ! "}, [('time', 15, 'choice')]),  
                    # debut chaque utilisation 
                'journee': ( {'e':'', 'g':'', 's': "Salut {}, je suis Cami ! \\pau=300\\Tu es prêt ?".format( child_name)}, [('time', 1, 'choice')]),
                'on_commence': ( {'e':'', 'g':'', 's': " Très bien, on commence !"}, [('time', 1, 'choice')]),
                'choix_activite': ( {'e':'', 'g':'', 's': random.choice([" À quoi tu as envie qu'on joue ensemble aujourd’hui? \\pau=500\\Tu peux choisir un jeux","À quoi on va jouer ?"])}, [('time', 1, 'choix_jeu')]),
                'choix_jeu': ( {'e':'QT/talking', 'g':'QT/strong', 's': "Jeu de mimes ?, construire une cabane ? ou fabriquer des choses avec nos mains "}, [('time', 1, 'choice')]),    
                'c_est_parti': ( {'e':'QT/talking', 'g':'', 's': "OK, c'est parti "}, [('time', 1, 'choice')]),    
                    # fin des activités
                'terminee': ( {'e':'', 'g':'', 's': "On a terminé aujourd’hui. J’espère que vous vous êtes bien amusez. Je vous attends pour d’autres jeux ! À la prochaine !  "}, [('time', 1, 'choice')]),    
                # Activités cognitives 
                    # 1-Jeu des mimes ==>> à completer 
                'regles_mime': ( {'e':'', 'g':'', 's': "Amusons-nous avec le jeu de mime! Je vais te montrer un animal et je voudrais que tu le mimes, tu peux nous montrer comment il se comporte, comment il bouge, nous faire sentir ses cris. Nous serons tes spectateurs ! "}, [('time', 1, 'choice')]),    
                'cirque': ( {'e':'', 'g':'', 's': "  Mesdames et messieurs, bienvenue au cirque ! Vous êtes prêt à deviner les animaux du cirque ? "}, [('time', 1, 'choice')]),    
                    # liste des animaux à mimer ==> à completer et à revoir  
                'lion': ( {'e':'', 'g':'', 's': "il a quatre pattes,\\pau=300\\  il a une crinière,\\pau=300\\il est féroce, il est fort\\pau=300\\   il est le roi de la savane,\\pau=600\\Entre en piste le Lion !   "}, [('time', 1, 'choice')]),   
                'girafe': ( {'e':'', 'g':'', 's': "elle a quatre pattes,\\pau=300\\ elle vit dans la savane\\pau=300\\, elle a un cou trés long\\pau=300\\   elle peut atteindre les feuilles les plus lointaines et délicieuses\\pau=600\\et voicii, mes dames et messieurs, la girafe  !   "}, [('time', 1, 'choice')]), 
                'gazelle': ( {'e':'', 'g':'', 's': "elle a quatre pattes,\\pau=300\\ elle cours tres vite\\pau=300\\, personne ne peut la ratrapper\\pau=300\\  \\pau=600\\et voicii en piste , la gazelle  !   "}, [('time', 1, 'choice')]),   
                'zebre': ( {'e':'', 'g':'', 's': " Il vit dans la savane \\pau=300\\ Il a quatre pattes \\pau=300\\ Il a des rayures noires et blanches \\pau=300\\ Quelle robe élégante !\\pau=600\\ Entre en piste le zèbre !"}, [('time', 1, 'choice')]),  
                'singe': ( {'e':'', 'g':'', 's': "Il peut grimper dans les plus hauts arbres \\pau=300\\ Il peut aussi sauter d’une branche à l’autre \\pau=300\\il est drôle, mais il peut être espiègle, attention !\\pau=300\\ Parmi les animaux, c'est lui qui nous ressemble le plus \\pau=600\\ Entre en piste le singe !"}, [('time', 1, 'choice')]),  
                'elephon': ( {'e':'', 'g':'', 's': " Il a quatre pattes,\\pau=300\\ il est grand et puissant!\\pau=300\\Il a une trompe,\\pau=300\\ il est le plus sage de tous!\\pau=600\\ Entre en piste l’éléphant!"}, [('time', 1, 'choice')]),
                'guepard': ( {'e':'', 'g':'', 's': "Il vit dans la savane,\\pau=300\\Il a quatre pattes,\\pau=300\\ il a une cape tachetée\\pau=300\\ Il court si vite que personne ne peut le battre!\\pau=600\\Entre en piste le guépard!"}, [('time', 1, 'choice')]),
                'tigre': ( {'e':'', 'g':'', 's': "Il vit dans la savane,\\pau=300\\ il a quatre pattes\\pau=300\\, il est féroce!\\pau=300\\il a une cape rayée,\\pau=600\\ Entre en piste la tigre! "}, [('time', 1, 'choice')]),
                'tortue': ( {'e':'', 'g':'', 's': "Elle aime se baigner dans l’eau\\pau=300\\ Elle prend toujours son temps, elle est très lente!\\pau=300\\ Elle porte sa maison sur son dos \\pau=600\\Entre en piste la tortue ! "}, [('time', 1, 'choice')]),
                'panthere': ( {'e':'', 'g':'', 's': "Elle ressemble à un gros chat\\pau=300\\Quel beau manteau noir \\pau=600\\ Entre en piste la panthère !"}, [('time', 1, 'choice')]),
                'serpent': ( {'e':'', 'g':'', 's': " Il se deplace en rampant,\\pau=300\\ Il ne se fait pas sentir,\\pau=300\\ attention! il peut se tordre\\pau=600\\ Entre en piste le serpent ! "}, [('time', 1, 'choice')]),
                'chat': ( {'e':'', 'g':'', 's': " Il aime rester à la maison mais aussi sortir et explorer,\\pau=300\\Il a des moustache\\pau=300\\ Il n’aime pas se mouiller avec de l’eau,\\pau=300\\ Il aime la compagnie, comme être tout seul\\pau=600\\ Entre en piste le chat"}, [('time', 1, 'choice')]),
                    # feliciter et/ou encourager 
                    # a remplir 
                    
                    # 2- travail manuel : patte a modeler
                'manuel_regles':( {'e':'', 'g':'', 's': "Maintenant je vous montre des objets et nous allons essayer de les créer avec de la pâte à modeler ! "}, [('time', 1, 'choice')]),    
                '_ciel':( {'e':'', 'g':'', 's': "Salut les artistes ! Aujourd'hui, on va créer un ciel en utilisant de la pâte à modeler."}, [('time', 1, 'choice')]), 
                        # montrer soleil, lune etoile   
                'table':( {'e':'', 'g':'', 's': "Salut les artistes ! Aujourd’hui on met la table:"}, [('time', 1, 'choice')]), 
                        # montrer un plat une tasse,une fourchette,une cuillère,un couteau,un verre
                'salon':( {'e':'', 'g':'', 's': "Salut les artistes ! Aujourd’hui nous allons embellir notre salon"}, [('time', 1, 'choice')]), 
                        # montrer une fleur, vase ...
                'les_animaux':( {'e':'', 'g':'', 's': "Salut les artistes !Aujourd’hui nous allons fabriquer nos amis à quatre pattes "}, [('time', 1, 'choice')]), 
                        # montrer une chat, chien, lapin ...        
                'la_mer':( {'e':'', 'g':'', 's': "Salut les artistes ! Aujourd'hui, nous partons à l'aventure vers la mer"}, [('time', 1, 'choice')]), 
                        # montrer bateau, poisson, parasol
                    # 2- travail manuel : faire un puzzle
                    # 2- travail manuel : construire une cabane
                'cabane_regles':( {'e':'', 'g':'', 's': "Maintenant, nous allons essayer de construire une cabane. Tu peux utiliser des Lego ou bien des coussins, des draps, des matelas et des cartons !"}, [('time', 1, 'choice')]),     
                        # expliiquer les etapes 

                    # 2- travail manuel : 1,2,3 soleil
                'soleil_regles':( {'e':'', 'g':'', 's': "Essaie de me rejoindre pendant que je ferme les yeux. Quand j'ouvrirai les yeux et dirai:\\pau=300\\  soleil,\\pau=300\\ tu devras t'arrêter. Il faut être concentré et rapide ! Si tu réussis à avancer pendant que je garde les yeux fermés, tu auras gagné. Prêt à me rejoindre ?"}, [('time', 1, 'choice')]),
                'lancer_soleil':( {'e':'', 'g':'', 's': "Un, deux , trois "}, [('time', 1, 'montrer_soleil')]),
                'montrer_soleil':( {'e':'Qt/soleil', 'g':'', 's': "Soleil "}, [('time', 1, 'choice')]),         

                 # Activités sociales
                    #S ous-catégorie : Raconter la journée/semaine aux parents ==> à remplir

                # Activités émotionnelles
                    #  Sous-catégorie : jeu symbolique/jeu avec médiateur
                    #  Psychodrame        

                'end': ((), [('time', 0.1, 'end')]) }

# while not rospy.is_shutdown():
#     # global child_name
#     # global adult_name
#     child_name = n.child_name
#     adult_name = n.adult_name
#     if child_name != "": 
#         break
#     time.sleep(1)
#     # if child_name != "": break

# if __name__ == '__main__':
#     rospy.init_node("qt_states", anonymous=True)    
