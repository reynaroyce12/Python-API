from tkinter import *
import requests


# ----------------------------------------API REQUESTS ----------------------------

def get_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()

    data = response.json()
    quote = data['quote']
    canvas.itemconfig(quote_text, text=quote)


# ------------------------------------- UI SETUP ----------------------------------

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg='#000839')

canvas = Canvas(width=300, height=414, bg='#000839', highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"),
                                fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, bg='#000839', highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
