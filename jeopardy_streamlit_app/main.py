import tkinter as tk
from tkinter import messagebox, simpledialog

# Sample wedding-themed categories and questions
categories = {
    "The Bride": {
        100: "What is Sara's favorite TV show?",
        200: "How tall is Sara?",
        300: "True or False: Sara made the first move on Zach?",
        400: "What is the first memorable gift Sara received from Zach?",
        500: "What exact date did Sara move to Texas?"
    },
    "The Couple": {
        100: "What restaurant did Sara and Zach meet at?",
        200: "What is Sara and Zach's anniversary?",
        300: "What is the height difference between Sara and Zach (in inches)?",
        400: "What is Sara and Zach's favorite thing to do together?",
        500: "How many children do Sara and Zach want to have?"
    },
    "The Bridesmaids": {
        200: "Where did Andre and Sara first meet?",
        201: "What is Jacqui and Sara's go-to car song?",
        202: "What was the first ever abandoned location Sara took Brina?",
        203: "What fandoms do Pohai and Sara have in common?",
        204: "How old was Michelle when Sara started colorguard?"
    },
    "The Groom": {
        100: "What is Zach's favorite sport?",
        200: "What is Zach's favorite thing about Sara?",
        300: "True or False: Zach is the better cook?",
        400: "What is one thing Zach does that annoys Sara?",
        500: "If Zach could swap with Sara for the day, what is one thing he would be excited to do?"
    }
}

answers = {
    "The Bride": {
        100: "Friends",
        200: "5'1",
        300: "True",
        400: "The necklace Sara wears everyday",
        500: "August 13th, 2016"
    },
    "The Couple": {
        100: "Whistle Britches",
        200: "March 8th, 2022",
        300: "17 inches",
        400: "Drinking margaritas and going Pokemon Go hunting",
        500: "2"
    },
    "The Bridesmaids": {
        200: "Black Gold rehearsal in 2016",
        201: "MCR - The Black Parade",
        202: "Profanity Houses",
        203: "3: Lord of the Rings, Harry Potter, Game of Thrones",
        204: "4 years old"
    },
    "The Groom": {
        100: "Basketball",
        200: "The way she cares about things",
        300: "False, unless he is cooking protein then it is true",
        400: "Sing annoying songs all day long",
        500: "Zach would hide in the smallest place ever and scare Sara"
    }
}

team_a_score = 0
team_b_score = 0
questions_answered = 0
total_questions = len(categories) * 5

# UI setup
root = tk.Tk()
root.title("Wedding Jeopardy 💍")
root.configure(bg="#C3C3C3")
root.geometry("1000x700")

# Title
title = tk.Label(root, text="Wedding Jeopardy!", font=("Edwardian Script ITC", 40), fg="#b76e79", bg="#C3C3C3")
title.pack(pady=20)

# Scoreboard
score_frame = tk.Frame(root, bg="#C3C3C3")
score_frame.pack(side="left", fill="y", padx=20)
team_a_label = tk.Label(score_frame, text=f"Team A:\n{team_a_score}", font=("Georgia", 20), fg="#6b4c4c", bg="#C3C3C3")
team_a_label.pack(pady=20)

team_b_label = tk.Label(score_frame, text=f"Team B:\n{team_b_score}", font=("Georgia", 20), fg="#6b4c4c", bg="#C3C3C3")
team_b_label.pack(pady=20)


# Game board frame
board_frame = tk.Frame(root, bg="#C3C3C3")
board_frame.pack(expand=True)

# Celebration label
celebration_label = tk.Label(root, text="", font=("Edwardian Script ITC", 32), fg="#b76e79", bg="#C3C3C3")
celebration_label.place(relx=0.5, rely=0.9, anchor="center")

def show_answer_popup(question, correct_answer, value):
    popup = tk.Toplevel(root)
    popup.title("Question")
    popup.configure(bg="#f4f4f4")
    popup.geometry("600x350")  # Increased width and height

    tk.Label(popup, text=question, font=("Georgia", 14), wraplength=550, bg="#f4f4f4", fg="#222222").pack(pady=20)

    def reveal():
        tk.Label(popup, text=f"Answer: {correct_answer}", font=("Georgia", 12, "italic"),
                 fg="#6b4c4c", bg="#f4f4f4", wraplength=550).pack(pady=10)  # Increased wraplength
        # confirm_btn.config(state="normal")

    def confirm(team):
        global team_a_score, team_b_score, questions_answered
        popup.destroy()
        if team == "A":
            team_a_score += value
            team_a_label.config(text=f"Team A:\n{team_a_score}")
            messagebox.showinfo("Team A", f"Team A earned {value} points!")
        elif team == "B":
            team_b_score += value
            team_b_label.config(text=f"Team B:\n{team_b_score}")
            messagebox.showinfo("Team B", f"Team B earned {value} points!")
        else:
            messagebox.showinfo("No Points", "No team earned points.")
        questions_answered += 1
        if questions_answered == total_questions:
            final_jeopardy()


    tk.Button(popup, text="Reveal Answer", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
              activebackground="#f4e1d2", command=reveal).pack(pady=10)

    button_frame = tk.Frame(popup, bg="#f4f4f4")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Team A Correct", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
            activebackground="#f4e1d2", command=lambda: confirm("A")).pack(side="left", padx=5)

    tk.Button(button_frame, text="None", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
            activebackground="#f4e1d2", command=lambda: confirm("None")).pack(side="left", padx=5)

    tk.Button(button_frame, text="Team B Correct", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
            activebackground="#f4e1d2", command=lambda: confirm("B")).pack(side="left", padx=5)



def ask_question(category, value, button):
    button.config(state="disabled", bg="#C3C3C3")
    question = categories[category][value]
    correct_answer = answers[category][value]
    score_value = 200 if category == "The Bridesmaids" else value
    show_answer_popup(question, correct_answer, score_value)


def final_jeopardy():
    question = "What is the exact number of days Sara and Zach have known each other?"
    correct_answer = "1,265 to 1,292 days"
    final_value = 1000  # Fixed point value for Final Jeopardy

    popup = tk.Toplevel(root)
    popup.title("Final Jeopardy 💍")
    popup.configure(bg="#f4f4f4")
    popup.geometry("500x300")

    # Final Jeopardy Title
    tk.Label(popup, text="Final Jeopardy!", font=("Georgia", 18, "bold"), fg="#b76e79", bg="#f4f4f4").pack(pady=10)

    # Question
    tk.Label(popup, text=question, font=("Georgia", 14), wraplength=450, bg="#f4f4f4", fg="#222222").pack(pady=10)

    def reveal():
        tk.Label(popup, text=f"Answer: {correct_answer}", font=("Georgia", 12, "italic"),
                 fg="#6b4c4c", bg="#f4f4f4").pack(pady=10)
        # confirm_btn.config(state="normal")

    def confirm(team):
        global team_a_score, team_b_score
        popup.destroy()
        if team == "A":
            team_a_score += final_value
            team_a_label.config(text=f"Team A:\n{team_a_score}")
            celebration_label.config(text="💖 Team A nailed Final Jeopardy! 💖")
        elif team == "B":
            team_b_score += final_value
            team_b_label.config(text=f"Team B:\n{team_b_score}")
            celebration_label.config(text="💖 Team B nailed Final Jeopardy! 💖")
        else:
            celebration_label.config(text="Better luck next time 💐")


    tk.Button(popup, text="Reveal Answer", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
              activebackground="#f4e1d2", command=reveal).pack(pady=10)

    button_frame = tk.Frame(popup, bg="#f4f4f4")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Team A Correct", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
            activebackground="#f4e1d2", command=lambda: confirm("A")).pack(side="left", padx=5)

    tk.Button(button_frame, text="None", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
            activebackground="#f4e1d2", command=lambda: confirm("None")).pack(side="left", padx=5)

    tk.Button(button_frame, text="Team B Correct", font=("Georgia", 12), bg="#fffaf5", fg="#6b4c4c",
            activebackground="#f4e1d2", command=lambda: confirm("B")).pack(side="left", padx=5)



def restart_game():
    confirm = messagebox.askyesno("Restart Game", "Are you sure you want to restart?")
    if confirm:
        global team_a_score, team_b_score, questions_answered
        team_a_score = 0
        team_b_score = 0
        questions_answered = 0
        team_a_label.config(text=f"Team A:\n{team_a_score}")
        team_b_label.config(text=f"Team B:\n{team_b_score}")
        celebration_label.config(text="")
        for widget in board_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="normal", bg="#fffaf5")


# Create category headers and buttons
for col, category in enumerate(categories.keys()):
    tk.Label(board_frame, text=category, font=("Georgia", 16, "bold"), fg="#b76e79", bg="#C3C3C3", width=15).grid(row=0, column=col, padx=5, pady=5)
    for i, value in enumerate(categories[category].keys()):
        display_value = 200 if category == "The Bridesmaids" else value
        btn = tk.Button(board_frame, text=f"${display_value}", font=("Georgia", 14), width=15, height=2,
                        bg="#fffaf5", fg="#6b4c4c", activebackground="#f4e1d2",
                        command=lambda c=category, v=value, b=None: ask_question(c, v, b))
        btn.grid(row=i+1, column=col, padx=5, pady=5)
        btn.config(command=lambda c=category, v=value, b=btn: ask_question(c, v, b))

        

# Restart button
restart_btn = tk.Button(root, text="Restart", font=("Georgia", 12), width=10, height=1,
                        bg="#fffaf5", fg="#6b4c4c", activebackground="#f4e1d2",
                        command=restart_game)
restart_btn.place(relx=0.9, rely=0.05)

root.mainloop()
