import json
import random

def poser_question(question_data):
    print("\n" + question_data["question"])
    reponse = input("Votre réponse : ").lower()
    return reponse in question_data["reponses_correctes"]

def charger_questions_depuis_json(chemin_fichier, theme):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        questions = json.load(fichier)
    
    questions_du_theme = [q for q in questions if q["theme"] == theme]
    return questions_du_theme

def choisir_theme():
    themes_possibles = ["geographie", "histoire", "mathematique"]
    theme = ""
    while theme not in themes_possibles:
        theme = input("Choisissez un thème parmi {} : ".format(themes_possibles)).lower()
    return theme

def jouer_quiz():
    score = 0

    theme_choisi = choisir_theme()
    # Attention, le fichier "questions.json" doit se trouver dans le même dossier que ce script
    questions = charger_questions_depuis_json("questions.json", theme_choisi)
    
    random.shuffle(questions)

    for i, question_data in enumerate(questions, 1):
        print("\nQuestion {}:".format(i))
        if poser_question(question_data):
            print("Bonne réponse!\n")
            score += 1
        else:
            print("Mauvaise réponse.\n")
        
        print("Score actuel : {}/{}".format(score, i))

    print("\nFin du quiz!")
    if score >= len(questions) // 2:
        print("Félicitations! Vous avez gagné avec un score de {}/{}.".format(score, len(questions)))
    else:
        print("Désolé, vous avez perdu avec un score de {}/{}.".format(score, len(questions)))

jouer_quiz()
