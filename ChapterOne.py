import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

class ChapterOne:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(self.master)

        # Set window to fullscreen
        self.window.attributes('-fullscreen', True)

        # Set the title of the window
        self.window.title("Introduction")

        self.text_widget = tk.Text(self.window, wrap='word')

        self.text_widget.insert('1.0', "Quantum computing is a type of computation that harnesses the physical "
                                  "phenomena of quantum mechanics. It uses quantum bits, or 'qubits', "
                                  "which can represent and process information in a way that is fundamentally "
                                  "different than classical bits.")
        
        self.scrollbar = tk.Scrollbar(self.window, command=self.text_widget.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.text_widget.configure(yscrollcommand=self.scrollbar.set)
        
        self.image = Image.open('your_image.png')
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.window, image=self.photo)
        self.image_label.pack()
        self.text_widget.pack(expand=True, fill='both')

        self.quiz_button = tk.Button(self.window, text='Start Quiz', command=self.start_quiz)
        self.quiz_button.pack()

    def start_quiz(self):
        question1 = simpledialog.askstring("Question 1", 
                                           "What does a quantum computer use to perform computations?\n"
                                           "a) Bits\n"
                                           "b) Qubits\n"
                                           "c) Bytes\n"
                                           "d) Kilobytes")
        if question1.lower() == "b":
            messagebox.showinfo("Answer", "Correct!")
        else:
            messagebox.showinfo("Answer", "Incorrect. The correct answer is b) Qubits.")

        question2 = simpledialog.askstring("Question 2", 
                                           "Which phenomenon is not associated with quantum mechanics?\n"
                                           "a) Superposition\n"
                                           "b) Entanglement\n"
                                           "c) Decoherence\n"
                                           "d) Gravitational force")
        if question2.lower() == "d":
            messagebox.showinfo("Answer", "Correct!")
        else:
            messagebox.showinfo("Answer", "Incorrect. The correct answer is d) Gravitational force.")
