#! /usr/bin/env python
# coding: utf-8
import random
child_name = ""
adult_name = ""
                 
# state: ( {g: gesture, s: say, h: [head], la: [left_arm], ra: [right_arm], w: [x, y, z, ex, ey, ez]}, [(trigger, param, next_state)])
states = { 'begin': ( {}, [('time', 1, 'choice')]),

                'choice': ( {'g': '', 's': '', 'e':'' },
                                # à implementer le joystique plutard debut
                                [   ('entry', None, 'left'), ('entry', None, 'right'),('entry', None, 'upleft'),('entry', None, 'upright'),
                                    ('entry', None, 'up'), 
                                    ('entry', None, 'center'),
                                    ('entry', None, 'down'),('entry', None, 'right'),
                                    ('entry', None, 'downleft'),('entry', None, 'downright'),
                                    
                                    # comportement reactions
                                    ('entry', None, 'la_joie'),('entry', None, 'amusement'),('entry', None, 'la_colere'),('entry', None, 'la_motivation'),('entry', None, 'la_fatigue'),('entry', None, 'la_tristesse'),
                                    ('entry', None, 'la_fierte'),('entry', None, 'etonnement'),('entry', None, 'adulte_accord'),('entry', None, 'demande_adulte'),('entry', None, 'que_pense'),
                                    ('entry', None, 'monsieur'),('entry', None, 'madame'),('entry', None, 'bien'),('entry', None, 'cest_mieux'),
                                    ('entry', None, 'tu_mexplique'),('entry',None, 'important'),('entry', None, 'ensuite'),('entry', None, 'pk_pas_bien'),
                                    ('entry', None, 'tu_es_sur'),('entry', None, 'plus_simple'),('entry', None, 'plus_difficile'),
                                    ('entry', None, 'bien_mal'),('entry', None, 'pas_marche'),('entry', None, 'pourquoi'),('entry', None, 'ecrit'),('entry', None, 'senslettre'),('entry', None, 'fermelettre'),
                                    ('entry', None, 'endroitlettre'),('entry', None, 'bien_comme_toi'),('entry', None, 'triche'),('entry', None, 'facile'),('entry', None, 'pas_trop_vite'),
                                    ('entry', None, 'boum'),('entry', None, 'tu_relances'),('entry', None, 'je_bugue'),('entry', None, 'je_rouille'),
                                    ('entry', None, 'attends'),('entry', None, 'malade'),('entry', None, 'et_alors'),('entry', None, 'jai_progresse'),
                                    ('entry', None, 'cest_difficile'),('entry', None, 'fais_mon_mieux'),('entry', None, 'tas_gagne'),
                                                                            ('entry', None, 'ma_tablette'),('entry', None, 'pas_mal'),('entry', None, 'je_trouve_pas'),('entry', None, 'respire'),('entry', None, 'ecris_mal'),('entry', None, 'cest_pas_grave'),
                                    ('entry', None, 'reessayons'),('entry', None, 'fera_mieux'),('entry', None, 'courage'),('entry', None, 'rate'),('entry', None, 'difficile'),
                                    ('entry', None, 'pas_content_moi'),('entry', None, 'tu_mecoute'),('entry', None, 'on_essaye'),('entry', None, 'bravo'),
                                    ('entry', None, 'je_suis_fort'),('entry', None, 'cest_bien'),('entry', None, 'tu_es_fort'),('entry', None, 'nous_sommes_fort'),
                                    ('entry', None, 'fier_de_toi'),('entry', None, 'applique'),('entry', None, 'tu_perseveres'),
                                    ('entry', None, 'aie'),('entry', None, 'ahahah'),('entry', None, 'muscle'),('entry', None, 'merci'),('entry', None, 'repete'),('entry', None, 'oui'),
                                    ('entry', None, 'non'),('entry', None, 'sais_pas_toi'),('entry', None, 'et_toi'),
                                        
                                    # comportement de scenario
                                    ('entry', None, 'pression_lance'),('entry', None, 'pression_expli'),('entry', None, 'pression_complet'),('entry', None, 'archeo_lance'),('entry', None, 'archeo_expli'),('entry', None, 'archeo_complet'),
                                    ('entry', None, 'drapeau_lance'),('entry', None, 'drapeau_expli'),('entry', None, 'drapeau_complet'),('entry', None, 'alpha_lance'),('entry', None, 'alpha_expli'),
                                    ('entry', None, 'alpha_complet'),('entry', None, 'zoo_lance'),('entry', None, 'zoo_expli'),('entry', None, 'zoo_complet'),
                                    ('entry', None, 'chimi_lance'),('entry',None, 'chimi_expli'),('entry', None, 'tilt_lance'),('entry', None, 'tilt_expli'),
                                    ('entry', None, 'tilt_complet'),('entry', None, 'cowritter_lance'),('entry', None, 'cowritter_expli_class'),
                                    ('entry', None, 'cowritter_complet'),('entry', None, 'jus_lance'),('entry', None, 'jus_expli'),('entry', None, 'jus_complet'),('entry', None, 'poursuite_lance'),('entry', None, 'poursuite_expli'),
                                    ('entry', None, 'poursuite_complet'),('entry', None, 'tu_viens'),('entry', None, 'ton_nom'),('entry', None, 'ca_va'),('entry', None, 'bonjour'),
                                    ('entry', None, 'je_mappelle_qt'),('entry', None, 'tu_veux_maider'),('entry', None, 'tu_maides_encore'),('entry', None, 'adieu'),
                                    ('entry', None, 'adieu2'),('entry', None, 'pause'),('entry', None, 'change_jeu'),('entry', None, 'choisis_jeu'),
                                    ('entry', None, 'dernier_jeu'),('entry', None, 'cetait_bien'),('entry', None, 'tu_maide'),('entry', None, 'mes_progres'),('entry', None, 'bisou'),('entry', None, 'bcp_travaille'),('entry', None, 'il_est_lheure'),
                                    ('entry', None, 'arrete'),('entry', None, 'au_revoir'),
                                    # comportement theatre 
                                    ('entry', None, 'hello'),('entry', None, 'dontknow'),('entry', None, '_oui'),('entry', None, '_non'),('entry', None, 'suivi'),('entry', None, 'public'),
                                    ('entry', None, 'objetDroite'),('entry', None, 'objetGauche'),('entry', None, 'pense'),('entry', None, 'pense2'),('entry', None, 'neutral'),
                                    ('entry', None, 'really'),('entry', None, 'comment'),('entry', None, 'jaime'),('entry', None, 'happy'),
                                    ('entry', None, 'kisses'),('entry', None, 'excited'),('entry', None, 'thinking'),('entry', None, 'curious'),
                                    ('entry', None, 'fear'),('entry', None, 'confused'),('entry', None, 'bored'),
                                    # nuitrack
                                    # ('entry', None, 'human_0_appeared'),('entry', None, 'human_0_disappeared'),
                                    # ('entry', None, 'human_0_center'),('entry', None, 'human_0_left'),('entry', None, 'human_0_right'),
                                    # ('entry', None, 'human_0_center_1meter'),('entry', None, 'human_0_left_1meter'),('entry', None, 'human_0_right_1meter'),
                                    # ('entry', None, 'human_0_center_2meters'),('entry', None, 'human_0_left_2meters'),('entry', None, 'human_0_right_2meters'),
                                    
                                    
                                    ('entry', None, 'replique_1_1'),('entry', None, 'replique_2_1'),
                                    ('entry', None, 'replique_2_2'),('entry', None, 'replique_2_3'),('entry', None, 'replique_3_1'),('entry', None, 'replique_3_2'),('entry', None, 'replique_4_1'),
                                    ('entry',None,'replique_5_1'), ('entry',None,'replique_5_2'), ('entry',None,'replique_6_1'), ('entry',None,'reset_posture'), 
                                    # semi autonome
                                    ('entry',None,'human_0_center_1m'), ('entry',None,'human_0_left_1m'), ('entry',None,'human_0_left_2m'), ('entry',None,'human_0_right_2m'), 
                                    ('entry',None,'human_0_center_2m'),
                                    ('entry',None,'human_0_right_1m'),
                                    # maison
                                    ('entry', None, '_salut'),('entry', None, '_comment_t_appeles_tu'),('entry', None, '_aujourdhui'),

                                    ('entry', None, 'end')]),

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
                                                        
                # 'test1':({},[('entry',None,'human_0_1meter'),('entry',None,'human_0_2meter'),('time', 0.5, 'test1')]),
                

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
                
                'adulte_accord': ( {'e':'QT/talking', 'g':'QT/show_tablet', 's': "%s ,tu es d'accord?" %adult_name }, [('time', 1, 'choice')]),
                'demande_adulte': ( {'e':'QT/talking', 'g':'QT/angry', 's':"Demandons à %s" %adult_name }, [('time', 1, 'choice')]),
                'que_pense': ( {'e':'QT/talking', 'g':'QT/challenge', 's':random.choice(["%s" % adult_name, "%s " % adult_name]) }, [('time', 1, 'choice')]),
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
                '_salut': ( {'e':'QT/showing_smile', 'g':'QT/hi', 's': "Salut! Je m’appelle Cam, on passera un peu de temps ensemble"}, [('time', 1, 'choice')]),  
                '_comment_t_appeles_tu': ( {'e':'', 'g':'', 's': "Comment vous vous appelez ?"}, [('time', 1, 'choice')]),  
                '_aujourdhui': ( {'e':'', 'g':'', 's': "à partir d'aujourd'hui on va se rencontrer régulièrement; quand on sera ensemble tu peux dire tout ce que tu penses. Tu peux le dire aussi en dessinant ou en jouant. Ensemble, on va essayer de comprendre ce qui se passe en toi"}, [('time', 1, 'choice')]),  

                'end': ((), [('time', 0.1, 'end')]) }
    # def choisir(self,l):
    #     if isinstance(l, list) and len(l) > 1:
    #         random.shuffle(l)
    #         choix = random.choice(l)
    #         # print("choix  = ",choix)
    #         return str(choix)
    #     return ""
#     def execute(self):
#          while child_name == "":
#             pass
#             # print("! EN ATTENTE DES NOMS DE L'ENFANT ET DE L'ADULTE !")
#             # time.sleep(2)  # Attente d'une seconde entre chaque itération
# class QtStatesThread(threading.Thread):
#     def run(self):
#         qt_states = Qt_States()
#         qt_states.execute()
        

# thread = QtStatesThread()
# thread.start()

# 's':self.choisir(["%s, qu'en penses-tu ?" % adult_name, "Qu'est-ce que tu en penses %s ?" % adult_name])