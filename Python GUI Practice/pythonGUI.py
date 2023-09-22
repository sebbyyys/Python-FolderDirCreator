from tkinter import *
from tkinter import filedialog
import os

# initialise tkinter
root = Tk()
bottomrow = (root)
bottom.pack()


#window information
root.geometry("600x400")
root.eval('tk::PlaceWindow . center')

# script for geting directory path and assigning it to variable file_path





# make a window and place it at the center of a screen


# nonresizable script root.resizable(0,0)

# labels
l1 = Label(
    root,
    text = "Please copy and paste in the filepath of where you want to make folders: ",
    bg='red',
    fg='blue',
    font =('Arial',10, 'bold')
)

l2 = Label(
    root,
    text = "Please input each folder name followed by a semicolon.\n (1;2;3;4 is a valid input): ",
    bg='blue',
    fg='white',
    font =('Arial',10, 'bold')
)    

def FileCreator():
    print("yes")

b1 = Button(
    root,
    text="Submit",
    font=('Courier',15,'bold'),
    command=FileCreator
    )

# l1.pack(side = LEFT, padx = 50, pady = 15)
# l2.pack(side = LEFT, padx = 50, pady = 15)

# l1.pack(expand=1)
# l2.pack(expand=1)
# b1.pack(side = BOTTOM, padx = 50, pady = 15, fill = BOTH)


l1.place(x= 10, y = 40)
l2.place(x= 10, y = 70)
b1.pack(side = BOTTOM, expand= 1)

root.mainloop()






#l1.place(x = 0.03, rely = 0.1)
# l1.pack_propagate(0)
# l1.pack(expand=1)
# l2.place(relx = 0.03, rely = 0.2)
# l2.pack_propagate(0)
# l2.pack(expand=1)

# l2.grid(row = 0, column = 0, padx=(100, 10))


# entries

# e1 = Entry(root, bd=5)
# e2 = Entry(root, bd=5)
# e1.place(x=60,y=10)
# e2.place(x=60,y=50)