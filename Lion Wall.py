from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import random

window = Tk()

l = [(255*np.random.rand(250, 250)).astype(np.uint8) for i in range(16)]


background_image = Image.open("OCButton.png")
background_image = background_image.resize((340, 150), Image.ANTIALIAS)  # Adjust the dimensions as needed
background_photo = ImageTk.PhotoImage(background_image)

background_imageC = Image.open("OCButtonCorrect.png")
background_imageC = background_imageC.resize((340, 150), Image.ANTIALIAS)  # Adjust the dimensions as needed
background_photoC = ImageTk.PhotoImage(background_imageC)

background_imageCR = Image.open("OCButtonCORRECTRED.png")
background_imageCR = background_imageCR.resize((340, 150), Image.ANTIALIAS)  # Adjust the dimensions as needed
background_photoCR = ImageTk.PhotoImage(background_imageCR)

background_imageCB = Image.open("OCButtonBLUE.png")
background_imageCB = background_imageCB.resize((340, 150), Image.ANTIALIAS)  # Adjust the dimensions as needed
background_photoCB = ImageTk.PhotoImage(background_imageCB)

background_imageCBL = Image.open("OCButtonLBLUE.png")
background_imageCBL = background_imageCBL.resize((340, 150), Image.ANTIALIAS)  # Adjust the dimensions as needed
background_photoCBL = ImageTk.PhotoImage(background_imageCBL)

win_color = [background_photoCB, background_photoC, background_photoCR, background_photoCBL]

answers = [["Menace", "Vixen", "Beast", "Governess"], ["Comet", "Dancer", "Dasher", "Cupid"], ["Emma Thompson", "Alan Rickman", "Colin Firth", "Hugh Grant"], ["Stephen King", "Pret-A-Manger", "German Shephard", "Darren Star"]]
answer_list = answers.copy()
answer_list = [item for sublist in answers for item in sublist]
random.shuffle(answer_list)
successNum = 0


def click(btn):
    buttons_in_grid = window.grid_slaves(row=0, column=0)

    global successNum

    if btn not in selected:
        selected.append(btn)
        btn.config(image=win_color[successNum])
    else:
        btn.config(image=background_photo)
        selected.remove(btn)
    if len(selected) == 4:
        for i in range(4):
            if (selected[0]["text"]) in answers[i]:
                answers_found = answers[i]
                break

        success = True
        for x in range(4):
            if (selected[x]["text"]) not in answers_found:
                success = False
                break

        if success:
            for i in range(len(selected)):
                info1 = selected[i].grid_info()
                info2 = window.grid_slaves(row=successNum, column=i)[0].grid_info()

                top_button = window.grid_slaves(row=successNum, column=i)[0]

                selected[i].grid(row=info2['row'], column=info2['column'])
                selected[i].config(image=win_color[successNum], command=0)
                top_button.grid(row=info1['row'], column=info1['column'])
                
            successNum += 1
        else:
            for button in selected:
                button.config(image=background_photo)
        selected.clear()

# Countdown bar
countdown_canvas = Canvas(window, width=340*4, height=120)
countdown_canvas.grid(row=len(l)//4, columnspan=4)

def update_countdown(count):
    countdown_canvas.delete("all")
    countdown_canvas.create_rectangle(0, 0, count, 40, fill="green", outline="green")

# Set the initial countdown time
countdown_time = 300
started = False

# Function to update countdown every 100 milliseconds
def countdown():
    global countdown_time
    global started
    update_countdown(countdown_time * 340*4 // 300)
    window.after(300, countdown)
    if(started):
        if countdown_time > 0:
            countdown_time -= 1

def start_game():
    global started
    started = True
    buttons_in_grid = window.grid_slaves()
    for x in range(len(buttons)):
        buttons[x].config(text=answer_list[x])

def solve():
    global selected
    selected = []
    global successNum

    selectButts = []

    for button in window.grid_slaves():
        for answer in answers:
            try:
                if button["text"] in answer:
                    selectButts.append(button)
            except:
                print()            
    
    for i in range(4):
        for button in selectButts:
            if(button["text"] in answers[i]):
                try:
                    button.invoke()
                except:
                    print()
# Start the countdown

buttons = []

countdown()
selected = []
button_width = 340
button_height = 150



for i in range(len(l)):
    btn = Button(window, borderwidth=1, text="", font=("Arial", 24, "bold"), compound="c",
                 image=background_photo, fg="white", highlightthickness=0,
                 width=button_width, height=button_height)

    buttons.append(btn)
    btn.config(command=lambda b=btn: click(b))
    btn.grid(row=i // 4, column=i % 4)


new_button = Button(window, text="Start Timer", command= start_game, width = 20)
new_button.grid(row=len(l)//4, column=0, columnspan=3, pady=0)  # Adjust the row, column, and columnspan as needed

new_button2 = Button(window, text="Solve", command= solve, width = 20)
new_button2.grid(row=len(l)//4, column=1, columnspan=4, pady=0)  # Adjust the row, column, and columnspan as needed
window.geometry("1375x700")
window.title("Only Connect Wall - Lion")



window.mainloop()
