import random
import time
import tkinter as tk



black = "#323437"
yellow = "#E2B714"
grey = "#646665"
transparent = "#000000"


def main():
    
    

    
    root = tk.Tk()
    root.title("MonkeyType Clone")
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(bg=black)
    canvas = tk.Canvas(root, width=800, height=600, bg=black)
    canvas.pack()
    canvas.create_text(75, 25, text="monkeytype", fill=yellow, font=("Courier", 14, "italic"))
    


    button = tk.Button(root, text="Start", width=10, bg=grey, fg=yellow, font=("Courier", 14, "italic"), command=lambda: reset_sentence(root, canvas, input))
    button.place(x=350, y=500)


    input = tk.Entry(root, width=55, bg=black, fg=yellow, font=("Courier", 14, "italic"))
    input.place(x=100, y=200)
    input.focus_set()
    input.bind("<KeyPress>", lambda event: check_input(root, canvas, input))

    root.mainloop()

def check_input(root, canvas, input):
    global flag
    global start_time
    if flag:
        flag = False
        start_time = time.time()
        
    if input.get() == " ".join(Text):
        print(start_time, time.time())
        end_time = time.time()
        wpm = calculate_wpm(start_time, end_time, len(Text))
        canvas.create_text(400, 300, text=f"WPM: {wpm}", fill=yellow, font=("Courier", 14, "italic"))
        flag = True
        input.delete(0, "end")
    
def calculate_wpm(start_time, end_time, sentence_length):
    time_elapsed = (end_time - start_time) / 60  # convert to minutes
    words_per_minute = sentence_length / time_elapsed  # assuming an average word length of 5 characters
    return int(words_per_minute)
    
    

def reset_sentence(root, canvas, input):
    global Text
    global flag
    flag = True
    input.delete(0, "end")
    Text = get_sentence()
    canvas.delete("all")
    canvas.create_text(75, 25, text="monkeytype", fill=yellow, font=("Courier", 14, "italic"))
    canvas.create_text(400, 100, text=Text, fill=yellow, font=("Courier", 14, "italic"))



def get_sentence() -> str:
    with open("words.txt", "r") as f:
        text = f.read()
    text = text.split("\n")
    
    sentance = [random.choice(text).lower() for i in range(5)]
    

    return sentance

if __name__ == "__main__":
    main()
