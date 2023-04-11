from tkinter import *
import requests
from threading import Thread 

api = "https://api.quotable.io/random"
quotes = []
quote_number = 0
# TODO! 
# make necessary imports for making API calls

def preload_quotes():
    global quotes
    global content
    global author
    print("***loading more quotes ***")
    for x in range(20):
      random_quote = requests.get(api).json()
      content = random_quote["content"]
      author = random_quote["author"]
      quotes = content +"\n\n" + "By" + author
      print(quotes)
      print("**********************************************************")
    

    print("***Finished loading more quotes ! ***")




preload_quotes()
def get_quote():
    global quote_text
    global author_text
    global author
    global content
    global quote_number
    canvas.itemconfig(quote_text, text=content)
    canvas.itemconfig(author_text, text=author)
    quote_number = quote_number + 1 
    print(quote_number)
    if quotes[quote_number] == quotes[1]:
         thread = Thread(target = preload_quotes)
    thread.start()



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
    font=("Arial", 15, "bold"),
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




 #   text_id = quote_text.create_text(10,10, anchor="nw", text="Hello, world")
  #  quote_text.itemconfig( text="New Text")
    # TODO!
    #Make an API call to get a random quote (including exception handling)
    # Requirements of the API call:
        # Make the call to 'http://api.quotable.io' (API documentation => https://github.com/lukePeavey/quotable#readme)
        # Get 1 random quote at a time
        # Specify a category (check out the documentation to learn more about categories and how to use them)
        # Customize your endpoint and parameters according to the requirements above.  
 
    # <YOUR CODE HERE>    
        
    #Parse the response object and store the quote and the author in variables called 'quote' and 'author'

    # <YOUR CODE HERE>    
    
    #Pass the quote variable into the canvas via the 'quote' variable.
  #  canvas.itemconfig(quote_text, text=quote)
    #Pass the author variable into the canvas via the 'author' variable.
   # canvas.itemconfig(author_text, text=author)


