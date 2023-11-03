import random
import time
import tkinter as tk


def main():
    
    

    black = "#323437"
    yellow = "#E2B714"
    grey = "#646665"

    root = tk.Tk()
    root.title("MonkeyType Clone")
    root.geometry("800x600")
    root.configure(bg=black)
    canvas = tk.Canvas(root, width=800, height=600, bg=black)
    canvas.pack()
    canvas.create_text(75, 25, text="monkeytype", fill=yellow, font=("Courier", 14, "italic"))
    
    
    
    
    Button = tk.Button(root, text="Start", width=10, height=2, bg=grey, fg=yellow, font=("Courier", 14), command=lambda:get_sentence(inputBox))
    Button.place(x=350, y=450)
    inputBox = tk.Entry(root, width=47, bg=black, text = get_sentence(), fg=yellow, font=("Courier", 18))
    inputBox.place(x=75, y=100)
    
    
    

    
    
    root.mainloop()

    

def get_sentence() -> str:
        
        sentencesForTest = ["The quick brown fox jumps over the lazy dog.",
                          "The five boxing wizards jump quickly.",
                            "Pack my box with five dozen liquor jugs.",
                            "Jackdaws love my big sphinx of quartz.",
                            "The five boxing wizards jump quickly.",
                            "How vexingly quick daft zebras jump!",
                            "Bright vixens jump; dozy fowl quack.",
                            "Quick zephyrs blow, vexing daft Jim.",
                            "Sphinx of black quartz, judge my vow.",
                            "Waltz, bad nymph, for quick jigs vex.",
                            "Glib jocks quiz nymph to vex dwarf.",
                            ]
        text = random.choice(sentencesForTest)
        
        
        return text

if __name__ == "__main__":
    main()
