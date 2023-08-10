var groupsList = [
	["static/images/face/partage_sentiments.png", "Jeux symboliques avec médiateur"],
	["static/images/face/theatre_emotions.png", "QT partage ses sentiments"],
	["static/images/face/stars.png", "Renforcements positifs et encouragements"],
	["static/images/face/theatre_a_definir_3.png","QT clos la scéance"],
	["static/images/face/maison_debut_activite1.png", "QT ouvre la scéance"],
	["static/images/face/presentation2.png", "QT se présente pour la première fois"],
	["static/images/face/questionne.png", "QT et le jeu de mimes"],
	["static/images/face/mimes2.png", "Réactions pour le jeu de mimes"],
	["static/images/face/ghghgh.png", "QT et le travail manuel"],
	["static/images/face/manuel.png", "Réactions pour pour les travaux manuels"],	
	["static/images/face/wink.png", "QT et 1, 2, 3 soleil"],	
	["static/images/face/happy.png", "On raconte sa journée ?"],
]

var infoList = [
	["static/images/arrow/bleu1.png", ""],
	["static/images/arrow/bleu2.png", ""],
	["static/images/arrow/orange.png", ""],
	["static/images/arrow/hautplein.png", ""],
	["static/images/arrow/ah.png", ""],
	["static/images/arrow/vert1.png", ""],
	["static/images/arrow/rouge.png", ""],
	["static/images/arrow/vert2.png", ""],
	["static/images/arrow/peau.png", ""],
	["static/images/arrow/basgauche.png", ""],
	["static/images/arrow/jaune.png", ""],
	["static/images/arrow/gaucheplume.png", ""], 
]

var textList = [
	["", "Jeux symboliques avec médiateur"],
	["", "QT partage ses sentiments"],
	["", "Renforcements positifs et encouragements"],
	["","QT clos la scéance"],
	["", "QT  ouvre la scéance"],
	["", "QT se présente pour la première fois"],
	["", "QT et le jeu de mimes"],
	["", "Réactions pour le jeu de mimes"],
	["", "QT et le travail manuel"],
	["", "Réactions pour pour les travaux manuels"],
	["", "QT et 1, 2, 3 soleil"],
	["", "On raconte sa journée ?"]
]

var commandsList = [
	// ["", "Jeux symboliques avec médiateur"],
	["#C09BF5", [	["Et alors ?", "",0],
					["Ça doit être dur pour lui", "",0],
					["Je comprends", "",0],
					["C'est drôle", "",0],
					["Pourquoi il fait ça ?", "",0],
					["Comment il se sent ?", "",0],
					["Tu peux m'expliquer ?", "",0],
					["Comment ça s'est passé ?", "",0],
					["Tu es sûr ?", "",0],
					["Envie de jouer ?", "",0],
					["Réessayons !", "",0],
					["C'est trop difficile ?", "",0]	]	],
	// ["", "QT partage ses sentiments"],					
	["#5EEBF4", [	["QT surpris !", "",0],
					["QT exprime la peur", "",0],
					["QT dégouté", "",0],
					["QT en colère !", "",0],
					["QT est heureux!", "",0],
					["QT exprime sa tristesse", "",0],
					["QT est fatigué", "",0],
					["QT réfléchit !", "",0] ]       ],
	// ["", "Renforcements positifs et encouragements"],				
	["#FFEE11", [	["Bravo", "",0],
					["C'est bien", "",0],
					["Tu as bien fait", "",0],
					["On est fort", "",0],
					["Je suis fier de toi", "",0],
					["Merci", "",0],
					["Courage", "",0],
					["Ce n'est pas grave", "",0],
					["Respire et recommence", "",0],
					["Tu as l'air de t'amuser !", "",0],
					["Quelle mine joyeuse !", "",0],
					["Tu t'appliques bien !", "",0]]	],
	// ["","QT clos la scéance"],
	["#56a0ff",	[	["Fin des activités ","terminee",0],
					["QT fatigué","qt_fatigue",0] ]	],
	//QT  ouvre la scéance				
	["#866d4f",	[	["Salut ","journee",0],
					["Etes vous prêts ?","on_est_prets",0],
					["Es tu prêt ?", "tu_es_pret",0],
					["Pourquoi tu ne veux pas ?","pourquoi_non",0],
					["On va s'amuser !","rassure_toi",0],
					["Je t'attend","previens_moi",0],
					["Choisir un jeu", "choix_activite",0],
					["On commence","on_commence",0] ]	],
	// QT se présente pour la première fois
	["#d0d0d0", [	["Je me présente", "_salut",0],
					["Quel est ton nom ?", "_comment_t_appeler",0],
					["Et tes parents ?", "_comment_t_appeler",0],
					["Ce qu'on va faire", "_aujourdhui",0]  ]	],
	// QT et le jeu de mimes
	["#83a2fe", [	["Expliquer les règles", "regles_mime",0],
					["Le lion", "lion",0],
					["La girafe", "girafe",0],
					["Le zebre", "zebre",0],
					["Le singe", "singe",0],
					["L'éléphon", "elephon",0],
					["La tortue", "tortue",0],
					["Le serpent", "serpent",0],
					["Le chat", "chat",0],
					["Le chien", "chien",0],
					["Le chameau", "chameau",0],
					["La grenouille", "grenouille",0]		]	],
	// Réactions pour le jeu de mimes
	["#F2838C", [	["Quelle peur !", "quelle_peur",0],
					["Il est féroce !", "feroce",0],
					["C'est drôle", "drole",0],
					["Qu'il est mignon !", "mignon",0],
					["Bravo!", "_bravo",0],
					["Tu es fort !", "tres_fort",0],
					["Tu imites bien", "imites_bien",0],
					["Réflechis", "reflechis",0],
					["Un conseil à tes parents ?", "tes_parents",0],
					["Essaye encore", "essaye_encore",0],
					["Essaye un autre", "un_autre",0],
					["On reprend ?", "on_reprend",0]	]	],
	// QT et le travail manuel
	["#C0F971", [	["Pâte à modeler", "soleil_regles",0],	
					["Le ciel", "",0],
					["La table", "",0],
					["Le salon", "",0],
					["Les animaux", "",0],
					["La mer", "",0],
					["Construire un puzzle", "",0],
					["Construire une cabane", "",0],
					["Le sol","",0],
					["Les murs","",0],
					["Le toit", "",0],
					["La porte", "",0]	]	],
	//Réactions pour pour les travaux manuels"				
	["#5cd788", [	
					["Génial !", "",0],
					["C'est joli !", "",0],
					["C'est reussi !", "",0],
					["Tu t'en sors bien !", "",0],
					["Tu es rapide !", "",0],
					["Fais de ton mieux", "",0],
					["Essayes encore", "",0],
					["Essayes un autre", "",0],
					["Sois patient","",0],
					["Puzzle : commencer","",0],
					["C'est un bon début","",0],
					["Observe bien les morceaux !", "",0]	]	],
	//QT et 1, 2, 3 soleil				
	["#F98443", [	["Régles du jeu", "",0],
					["Lancer !", "",0],
					["bravo", "",0],
					["J'ai gagné", "",0]	]	],
	//On raconte sa journée ?				
	["#F5D39B", [	["Comment ça va ?", "",0],
					["Et ta journee ?", "",0],
					["Envie de nous raconter ?", "",0],
					["De belles choses à raconter ?", "",0],
					["Quelque chose t'a inquieté ?", "",0],
					["Tu as joué avec tes amis ?", "",0],
					["Et à l'école ?", "",0],
					["Vraiment ?", "",0],
					["Pourquoi ?", "",0],
					["Et après ?", "",0],
					["Ah bon !", "",0]	]	]
]


// icon position
var ellipseGroupList = [
	[14.9, 3.7],
	[10.2, 6],
	[5.2, 7.1],
	[-4.6, 7.1],
	[-10.4, 6],
	[-15.3, 3],
	[-14.9,	-4.2],
	[-10.2,	-6.5],
	[-2.9, -7.6],
	[2.5, -7.6],
	[10.2, -6.5],
	[14.9, -4.2]
]

// arrow position
var ellipseInfoList = [
	[19.8, 5],
	[14.7, 9.8],
	[7, 12.5],
	[-4.2, 12.5],
	[-12.5, 10.5],
	[-21, 5],
	[-19.8, -6],
	[-14.8, -9.5],
	[-3.1, -12.2],
	[5.2, -11.8],
	[13.3, -10.5],
	[19.8, -6]
]

	
	



// text position
var ellipseTextList = [
	[22.3, 9.0],
	[17.3, 13.8],
	[8, 17],
	[-4.7, 15.5],
	[-16.3, 11],
	[-26.5, 3.3],
	[-22.5, -8.8],
	[-13.5, -13],
	[-1.1, -15],
	[9.5, -12.3],
	[18.6, -9.7],
	[22.3, -6.8]
]

// button position
var ellipseCommandList = [
	[23.55, 4.4],
	[18.41, 10.05],
	[7.63, 12.67],
	[-7.63, 12.67],
	[-18.4, 10.04],
	[-23.55, 4.54],
	[-24.25, -3.4],
	[-19.21, -8.95],
	[-10.63, -12.67],
	[10.63, -12.67],
	[19.21, -8.95],
	[24.25, -3.4],
]
