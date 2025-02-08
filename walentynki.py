import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def show_popup():
    root = tk.Tk()
    root.title("super swietny mega program")
    center_window(root, 600, 600)

    image_path = os.path.join(os.path.dirname(__file__), "kwiatki.jpg")
    background_image = Image.open(image_path)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    def on_yes():
        thank_you_window()
        root.destroy()

    def on_no():
        root.destroy()
        show_popup()

    def thank_you_window():
        thank_you_win = tk.Toplevel(root)
        thank_you_win.title("DZIEKUJE")
        center_window(thank_you_win, 300, 150)
        
        thank_you_image_path = os.path.join(os.path.dirname(__file__), "image.jpg")
        thank_you_background_image = Image.open(thank_you_image_path)
        thank_you_background_photo = ImageTk.PhotoImage(thank_you_background_image)
        thank_you_background_label = tk.Label(thank_you_win, image=thank_you_background_photo)
        thank_you_background_label.place(relwidth=1, relheight=1)

        header = tk.Label(thank_you_win, text="na gorze <header>", font=("Arial", 12), bg="white")
        header.pack(pady=5)
        
        message = tk.Label(thank_you_win, text="na dole <footer>", font=("Arial", 12), bg="white")
        message.pack(pady=5)

        message = tk.Label(thank_you_win, text="kocham cie bardziej\nniz swoj komputer", font=("Arial", 12), bg="white")
        message.pack(pady=5)

        thank_you_win.mainloop()

    question_label = tk.Label(root, text="Zostaniesz moja walentynka?", bg="white", font=("Arial", 16))
    question_label.pack(pady=20)

    yes_button = tk.Button(root, text="Tak", command=on_yes, font=("Arial", 16))
    yes_button.pack(side=tk.LEFT, padx=20)

    no_button = tk.Button(root, text="Nie", command=on_no, font=("Arial", 16))
    no_button.pack(side=tk.RIGHT, padx=20)

    positions = ["left", "right", "top", "bottom"]
    current_position_index = 0

    def toggle_position(event):
        nonlocal current_position_index
        current_position_index = (current_position_index + 1) % len(positions)
        if positions[current_position_index] == "left":
            no_button.pack(side=tk.LEFT, padx=20)
        elif positions[current_position_index] == "right":
            no_button.pack(side=tk.RIGHT, padx=20)
        elif positions[current_position_index] == "top":
            no_button.pack(side=tk.TOP, pady=20)
        elif positions[current_position_index] == "bottom":
            no_button.pack(side=tk.BOTTOM, pady=20)

    no_button.bind("<Enter>", toggle_position)

    root.mainloop()

show_popup()
