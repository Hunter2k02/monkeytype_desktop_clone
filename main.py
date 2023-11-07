import random
import time
import tkinter as tk



black = "#323437"
yellow = "#E2B714"
grey = "#646665"
transparent = "#000000"


def main():
    
    
    global input
    global root 
    global label
    global user_input
    root = tk.Tk()
    root.title("MonkeyType Clone")
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(bg=black)
    canvas = tk.Canvas(root, width=800, height=600, bg=black)
    canvas.pack()
    canvas.create_text(75, 25, text="monkeytype", fill=yellow, font=("Courier", 14, "italic"))
    
    

    label = tk.Label(root, text="", bg=black, fg=grey, font=("Courier", 14, "italic"))
    label.place(x=100, y=200)

    button = tk.Button(root, text="Reset Test", width=10, bg=grey, fg=yellow, font=("Courier", 14, "italic"), command=lambda: reset_sentence(root, canvas, input))
    button.place(x=350, y=500)


    input = tk.Entry(root, width=1, bg=black, fg=black, font=("Courier", 14, "italic"))
    input.place(x=100, y=200)
    input.focus_set()
    input.bind("<KeyPress>", lambda event: check_input(root, canvas, input))


    user_input = tk.Label(root, text=input.get(), bg=black, fg=yellow, font=("Courier", 14, "italic"))
    user_input.place(x=100, y=200)


    root.mainloop()

def check_input(root, canvas, input):
    global flag
    global start_time
    global counter 
    global user_input
    global Text_as_string

    
   
    
    user_input.place_forget()
    user_input = tk.Label(root, text=input.get(), bg=black, fg=yellow, font=("Courier", 14, "italic"))
    user_input.place(x=100, y=200)
    canvas.create_text(75, 25, text="monkeytype", fill=yellow, font=("Courier", 14, "italic"))
    


    
    if flag:
        counter = 0
        flag = False
        start_time = time.time()
    
    if len(input.get()) == len(Text_as_string):
        for i in range(len(Text_as_string)):
            if input.get()[i] != Text_as_string[i]:
                counter += 1
                print(counter)
        
        end_time = time.time()

        wpm = calculate_wpm(start_time, end_time, len(Text_as_string))
        accuracy = ((len(Text_as_string) - counter) / len(Text_as_string))* 100
        canvas.create_text(400, 300, text=f"WPM: {wpm}", fill=yellow, font=("Courier", 14, "italic"))
        canvas.create_text(400, 350, text=f"Accuracy: {accuracy:.2f}%", fill=yellow, font=("Courier", 14, "italic"))
        flag = True
        input.delete(0, "end")
    
def calculate_wpm(start_time, end_time, sentence_length):
    time_elapsed = (end_time - start_time) / 60  # convert to minutes
    words_per_minute = (sentence_length)/5 / time_elapsed  # assuming an average word length of 5 characters
    return int(words_per_minute)
    
    

def reset_sentence(root, canvas, input):
    global Text
    global flag
    global label
    global user_input
    global Text_as_string
   
    
    user_input.place_forget()

    flag = True
    input.delete(0, "end")
    label.place_forget()
    Text = get_sentence()
    Text_as_string = " ".join(Text)
    canvas.delete("all")
    canvas.create_text(75, 25, text="monkeytype", fill=yellow, font=("Courier", 14, "italic"))
    
    label = tk.Label(root, text=Text, bg=black, fg=grey, font=("Courier", 14, "italic"))
    label.place(x=100, y=200)

  

    



def get_sentence() -> str:
    with open("words.txt", "r") as f:
        text = f.read()
    text = text.split("\n")
    
    sentance = [random.choice(text).lower() for i in range(5)]
    

    return sentance

if __name__ == "__main__":
    main()
