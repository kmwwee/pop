import os
import sys
from tkinter import simpledialog
import pygame
import tkinter as tk
from tkinter.simpledialog import askstring
from ChapterOne import ChapterOne
from gtq import *
from bloch_plot import *
from multiprocessing import Process
import tkinter as tk
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem
import tkinter as tk
from tkinter import messagebox
import pygame_gui
from pygame_gui.elements import UIButton

import random

from tkinter import Scrollbar, Canvas
from tkinter.constants import BOTH, YES, Y

class QuantumChapters:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)  # Make window full screen
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill='both', expand=True)

        self.chapter_names = ['Introduction', 'Basic Concepts', 'Superposition', 'Entanglement', 'Quantum Gates',
                              'Quantum Circuits', 'Quantum Algorithms', 'Quantum Complexity Theory', 'Quantum Error Correction',
                              'Quantum Cryptography']  # Replace with actual chapter names
        
        self.chapter_classes = {
            'Introduction': ChapterOne,
            # Other chapters here...
        }
        self.colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#C0C0C0", "#808080", "#800000", "#808000"]  # List of colors

        # Create a canvas inside the frame to allow scrolling
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side='left', fill='both', expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # Create another frame inside the canvas to hold the content
        self.content_frame = tk.Frame(self.canvas)
        self.canvas.create_window((650, 850), window=self.content_frame, anchor='nw')

        self.buttons = []
        for i in range(10):
            chapter_button = tk.Button(self.content_frame, text=self.chapter_names[i], 
                                       command=lambda i=i: self.on_select(self.chapter_names[i]),
                                       bg=self.colors[i])  # Apply color
            chapter_button.config(height=8, width=48)  # Adjust button dimensions for a smaller square shape
            self.buttons.append(chapter_button)

            # Arrange buttons in a grid layout, 5 per row
            self.buttons[i].grid(row=i//1, column=i%1, sticky='nsew')

        # Add an exit button
        self.exit_button = tk.Button(self.content_frame, text="Exit", command=self.exit, bg="red")
        self.exit_button.grid(row=i//1, column=i//1, sticky='nsew')  # Place the exit button in the bottom right corner
        self.exit_button.config(height=5, width=38)  # Adjust button dimensions for a smaller square shape

    def on_select(self, value):
        selected_class = self.chapter_classes.get(value)
        if selected_class is not None:
            # Create an instance of the selected class
            instance = selected_class(self.master)

        # Here you can add code to show actual learning content.
        # For this example, we just show a message box.
        else:
            messagebox.showinfo("Chapter selected", "You selected " + value)

    def exit(self):
        self.master.destroy()
