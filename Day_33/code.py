from tkinter import *
import requests
#
def get_quote():

    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()

    data = response.json()["quote"]
    canvas.itemconfig(quote_text, text=data)
    return data

window = Tk()
window.title("Naruto says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)

canvas.create_image(150, 207)
quote_text = canvas.create_text(150, 207, text="Naruto says...", width=250, font=("Arial", 30, "bold"), fill="Black")
canvas.grid(row=0, column=0)


kanye_button = Button(highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()