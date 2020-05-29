from scraping import movie_timer
from tkinter import * 

root = Tk()
w = Canvas(root, width=200, height=100)

def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""

    result = myEntry.get()
    result=movie_timer(result)
    resultLabel.config(text=result)
    myEntry.delete(0,END)

# Create the Entry widget
myEntry = Entry(root, width=20)
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()

# Create the Enter button
Label(root, text = 'Movie Time',  
font =('Verdana', 15)).pack(side = TOP, pady = 10)

enterEntry = Button(root, text= "Enter", command=returnEntry).pack(side = TOP) 
#enterEntry.pack(fill=X)

# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)



root.mainloop()