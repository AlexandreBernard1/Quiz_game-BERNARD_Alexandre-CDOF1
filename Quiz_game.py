import json
import random
import tkinter as tk
from tkinter import simpledialog, messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.score = 0
        self.current_question_index = 0
        self.theme_choisi = self.choisir_theme()
        self.questions = self.charger_questions_depuis_json("questions.json", self.theme_choisi)
        random.shuffle(self.questions)

        self.label_question = tk.Label(master, text="")
        self.label_question.pack(pady=10)

        self.entry_reponse = tk.Entry(master)
        self.entry_reponse.pack(pady=10)

        self.button_valider = tk.Button(master, text="Valider", command=self.valider_reponse)
        self.button_valider.pack(pady=10)

        self.label_score = tk.Label(master, text="Score: 0/0")
        self.label_score.pack(pady=10)

        self.update_question()

    def valider_reponse(self):
        reponse = self.entry_reponse.get().lower()
        question_data = self.questions[self.current_question_index]

        if reponse in question_data["reponses_correctes"]:
            self.score += 1

        self.current_question_index += 1
        self.update_question()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])
            self.label_score.config(text="Score: {}/{}".format(self.score, self.current_question_index))
        else:
            self.fin_du_quiz()

    def fin_du_quiz(self):
        message = "Félicitations! Vous avez gagné avec un score de {}/{}.".format(self.score, len(self.questions)) \
            if self.score >= len(self.questions) // 2 \
            else "Désolé, vous avez perdu avec un score de {}/{}.".format(self.score, len(self.questions))
        messagebox.showinfo("Fin du quiz", message)
        self.master.destroy()

    def charger_questions_depuis_json(self, chemin_fichier, theme):
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as fichier:
                questions = json.load(fichier)
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier {} n'a pas été trouvé.".format(chemin_fichier))
            self.master.destroy()

        questions_du_theme = [q for q in questions if q["theme"] == theme]
        if not questions_du_theme:
            messagebox.showinfo("Fin du quiz", "Aucune question trouvée pour le thème sélectionné.")
            self.master.destroy()

        return questions_du_theme

    def choisir_theme(self):
        themes_possibles = ["geographie", "histoire", "mathematique"]
        theme = ""
        while theme not in themes_possibles:
            theme = simpledialog.askstring("Choisir un thème", "Choisissez un thème parmi {} : ".format(themes_possibles))
            if theme is None:
                exit()
            theme = theme.lower()
        return theme

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
