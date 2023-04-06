from tkinter import *
import requests
from playsound import playsound


def get_quote():
    res = requests.get(url="https://api.kanye.rest").json()['quote']
    if len(res) > 150:
        canvas.itemconfig(quote_text, text=res, font=("Ariel", 10, "bold"))
    elif len(res) > 70:
        canvas.itemconfig(quote_text, text=res, font=("Ariel", 20, "bold"))
    else:
        canvas.itemconfig(quote_text, text=res, font=("Arial", 30, "bold"))

    playsound('bad-to-the-bone-meme.mp3')
    print('playing sound using 🎸🎸🎸')


window = Tk()
window.title("Ye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, border=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
