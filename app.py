import random
import time
import tkinter as tk

class Monke():
    """
    A class that creates a GUI for a typing test game.

    Attributes:
    - black (str): A hex code for black color.
    - yellow (str): A hex code for yellow color.
    - grey (str): A hex code for grey color.
    - root (Tk): A tkinter window.
    - canvas (Canvas): A tkinter canvas.
    - label (Label): A tkinter label that displays the sentence to be typed.
    - input (Entry): A tkinter entry for user input.
    - user_input (Label): A tkinter label that displays the user's input.
    - Text (str): A string of words from a text file.
    - Text_as_string (str): A string of 5 randomly selected words from Text.
    - flag (bool): A flag to indicate if the test has started.
    - counter (int): A counter for the number of incorrect characters typed.
    - start_time (float): The time when the test starts.
    - end_time (float): The time when the test ends.
    """

    def __init__(self):
        """
        Initializes the Monke class by creating a tkinter window and GUI elements.
        """
        self.black = "#323437"
        self.yellow = "#E2B714"
        self.grey= "#646665"
        self.flag = True

        self.root = tk.Tk()
        self.root.title("MonkeyType Clone")
        self.root.geometry("800x600")

        self.root.resizable(False, False)
        self.root.configure(bg=self.black)
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg=self.black)
        self.canvas.pack()
        self.canvas.create_text(75, 25, text="monkeytype", fill=self.yellow, font=("Courier", 14, "italic"))
        self.get_sentence()

        button = tk.Button(self.root, text="Reset Test", width=10, bg=self.grey, fg=self.yellow, font=("Courier", 14, "italic"), command=lambda: self.reset_sentence())
        button.place(x=350, y=500)

        self.input = tk.Entry(self.root, width=1, bg=self.black, fg=self.black, font=("Courier", 14, "italic"))
        self.input.place(x=100, y=200)
        
        self.user_input = tk.Label(self.root, text="", bg=self.black, fg=self.yellow, font=("Courier", 14, "italic"))
        self.user_input.place(x=100, y=200)

        self.input.focus_set()
        self.input.bind("<KeyRelease>", lambda event: self.check_input())
        self.input.bind("<Key>", lambda event: self.check_input())
        self.root.bind("<Return>", lambda event: self.reset_sentence())

        self.label = tk.Label(self.root, text=self.Text_as_string, bg=self.black, fg=self.grey, font=("Courier", 14, "italic"))
        self.label.place(x=100, y=200)
        
        self.root.mainloop()

    def check_input(self):
        """
        Checks the user's input and updates the GUI accordingly.
        """
        self.user_input.place_forget()

        self.user_input = tk.Label(self.root, text=self.input.get(), bg=self.black, fg=self.yellow, font=("Courier", 14, "italic"))
        self.user_input.place(x=100, y=200)
        print(self.input.get()) # for debugging
        # Check if the user has started typing

        if self.flag:
            self.counter = 0
            self.flag = False
            self.start_time = time.time()

        # Check if the user has typed the entire sentence
        
        if len(self.input.get()) == len(self.Text_as_string):

            # Disable the input field and unbind the event handler
            self.input["state"] = "disabled"
            self.input.unbind("<KeyRelease>")
            self.input.unbind("<Key>")
            self.user_input.place_forget()

            # Calculate the user's typing speed and accuracy

            for i in range(len(self.Text_as_string)):
                if self.input.get()[i] != self.Text_as_string[i]:
                    self.counter += 1
            
            self.end_time = time.time()

            wpm = self.calculate_wpm()
            accuracy = ((len(self.Text_as_string) - self.counter) / len(self.Text_as_string))* 100
            self.canvas.create_text(400, 300, text=f"WPM: {wpm}", fill=self.yellow, font=("Courier", 14, "italic"))
            self.canvas.create_text(400, 350, text=f"Accuracy: {accuracy:.2f}%", fill=self.yellow, font=("Courier", 14, "italic"))
            self.flag = True
            self.input.delete(0, "end")
        
    def calculate_wpm(self):
        """
        Calculates the user's typing speed in words per minute (WPM).
        """
        time_elapsed = (self.end_time - self.start_time) / 60  # convert to minutes
        words_per_minute = (len(self.Text_as_string))/5 / time_elapsed  # assuming an average word length of 5 characters
        return int(words_per_minute)
        
    def reset_sentence(self):
        """
        Resets the test by generating a new sentence and clearing the user's input.
        """
        # Re-enable the input field and bind the event handler

        self.user_input.place_forget()
        self.label.place_forget()
        self.input.focus_set()
        
        self.flag = True
        
        self.input.bind("<KeyRelease>", lambda event: self.check_input())
        self.input.bind("<Key>", lambda event: self.check_input())
        self.input["state"] = "normal"
        self.input.delete(0, "end")
        
        self.get_sentence()
        
        # Update the GUI
        
        self.canvas.delete("all")
        self.canvas.create_text(75, 25, text="monkeytype", fill=self.yellow, font=("Courier", 14, "italic"))

        self.label = tk.Label(self.root, text=self.Text_as_string, bg=self.black, fg=self.grey, font=("Courier", 14, "italic"))
        self.label.place(x=100, y=200)
        
        self.user_input = tk.Label(self.root, text=self.input.get(), bg=self.black, fg=self.yellow, font=("Courier", 14, "italic"))
        self.user_input.place(x=100, y=200)

        

    def get_sentence(self):
        """
        Selects 5 random words from a text file and creates a string of the words.
        """
        with open("words.txt", "r") as f:
            self.Text = f.read()
        self.Text = self.Text.split("\n")
        self.sentance = [random.choice(self.Text).lower() for i in range(5)]
            
        self.Text_as_string = " ".join(self.sentance)
        

        