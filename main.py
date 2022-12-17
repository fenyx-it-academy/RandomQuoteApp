from tkinter import *
import requests

def get_quote():
   
    response = requests.get('http://api.quotable.io/random?tags=inspirational')
    data = response.json()
    author = data['author']
    quote = data['content']

    canvas.itemconfig(quote_text, text=quote)
    canvas.itemconfig(author_text, text=author)



window = Tk()
window.title("Random Quote App")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(
    150,
    180,
    text="Click on the button below to load a random quote.",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

author_text = canvas.create_text(
    150, 320, text="", width=250, font=("Arial", 20, "italic"), fill="white"
)
canvas.grid(row=0, column=0)

button = Button(highlightthickness=0, command=get_quote, text="Get a new quote")
button.grid(row=1, column=0)

window.mainloop()