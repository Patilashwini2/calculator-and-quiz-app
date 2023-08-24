import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.questions = [
            {
                "prompt": "What is the capital of France?",
                "options": ["Paris", "Madrid", "Berlin", "Rome"],
                "correct": "Paris"
            },
            {
                "prompt": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct": "Mars"
            },
            {
                "prompt": "What is 7 * 8?",
                "options": ["45", "56", "64", "57"],
                "correct": "56"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="")
        self.question_label.pack()
        
        self.option_buttons = []
        for _ in range(4):
            button = tk.Button(root, text="", command=lambda: self.check_answer(button.cget("text")))
            self.option_buttons.append(button)
            button.pack(fill="both", padx=10, pady=5)
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["prompt"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            self.current_question += 1
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz completed! You scored {self.score} out of {len(self.questions)}")
            self.root.quit()
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question - 1]["correct"]
        if selected_option == correct_answer:
            self.score += 1
        self.next_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
