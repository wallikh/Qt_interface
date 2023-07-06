 # maison 
 { 'begin': ( {}, [('time', 1, 'choice')]),
                
                'choice': ( {'g': '', 's': '', 'e':'' }),
                ('woz', None, '_salut'),('woz', None, '_comment_t_appeles_tu'),('woz', None, '_aujourdhui'),('woz', None, 'journee'),('woz', None, 'on_commence'),('woz', None, 'choix_jeu'),
                ('woz', None, 'terminee'),('woz', None, 'regles_mime'),('woz', None, 'cirque'),('woz', None, 'lion'),('woz', None, 'girafe'),
                ('woz', None, 'gazelle'),('woz', None, 'zebre'),('woz', None, 'singe'),('woz', None, 'elephon'),('woz', None, 'guepard'),
                ('woz',None, 'tigre'),('woz', None, 'tortue'),('woz', None, 'panthere'), ('woz', None, 'serpent'),('woz', None, 'chat'),                                     
                ('woz', None, 'manuel_regles'),('woz', None, '_ciel'),('woz', None, 'table'),('woz', None, 'salon'),('woz', None, 'les_animaux'),('woz', None, 'la_mer'), 
                ('woz', None, 'cabane_regles'),('woz', None, 'trois_soleil'),('woz', None, 'lancer_soleil'),
                            
                    # premiere utimisation 
                '_salut': ( {'e':'QT/showing_smile', 'g':'QT/hi', 's': "Salut! Je m’appelle Cam, enchanté de vous rencontrer"}, [('time', 1, 'choice')]),  
                '_comment_t_appeles_tu': ( {'e':'', 'g':'', 's': "~Comment vous vous appelez ?"}, [('time', 1, 'choice')]),  
                '_aujourdhui': ( {'e':'', 'g':'', 's': "~ À partir d’aujourd'hui on va jouer ensemble régulièrement ! Quand on sera ensemble tu seras libre de dire tout ce que tu penses. Tu peux le dire aussi en dessinant ou en jouant, d’accord ? Ensemble, on va essayer de comprendre ce qui se passe en toi. C’est parti ! "}, [('time', 1, 'choice')]),  
                    # debut chaque utilisation 
                'journee': ( {'e':'', 'g':'', 's': "Salut {}, je suis Cam ! \\pau=300\\Tu es prêt ?".format( child_name)}, [('time', 1, 'choice')]),
                'on_commence': ( {'e':'', 'g':'', 's': " Très bien, on commence !"}, [('time', 1, 'choice')]),
                'choix_jeu': ( {'e':'', 'g':'', 's': random.choice([" À quoi tu as envie qu'on joue ensemble aujourd’hui? \\pau=500\\Tu peux choisir un jeux","À quoi on va jouer ?"])}, [('time', 1, 'choice')]),    
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
                'trois_soleil':( {'e':'', 'g':'', 's': "Essaie de me rejoindre pendant que je ferme les yeux. Quand j'ouvrirai les yeux et dirai:\\pau=300\\  soleil,\\pau=300\\ tu devras t'arrêter. Il faut être concentré et rapide ! Si tu réussis à avancer pendant que je garde les yeux fermés, tu auras gagné. Prêt à me rejoindre ?"}, [('time', 1, 'choice')]),
                'lancer_soleil':( {'e':'', 'g':'', 's': "Un, deux , trois "}, [('time', 1, 'montrer_soleil')]),
                'montrer_soleil':( {'e':'Qt/soleil', 'g':'', 's': "Soleil "}, [('time', 1, 'choice')]),         

                 # Activités sociales
                    #S ous-catégorie : Raconter la journée/semaine aux parents ==> à remplir

                # Activités émotionnelles
                    #  Sous-catégorie : jeu symbolique/jeu avec médiateur
                    #  Psychodrame        
                     
                     'end': ((), [('time', 0.1, 'end')]) }