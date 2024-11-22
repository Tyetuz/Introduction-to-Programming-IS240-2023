# from tkinter import *
# window = Tk()

# window.title("Button Example")  
# btnCalculate = Button(window, text = "Calculate", fg = "pink", bg = "green")

# btnCalculate.grid(padx = 75, pady = 15)

# window.mainloop()

# from tkinter import *

# def toggleColor():
#     if btnCalculate["fg"] == "green":
#         btnCalculate["fg"] = "pink"
#         btnCalculate["bg"] = "green"
#     else:
#         btnCalculate["fg"] = "green"
#         btnCalculate["bg"] = "pink"

# window = Tk()

# window.title("Button Example")
# btnCalculate = Button(window, text = "Calculate", fg = "pink", bg = "green", command = toggleColor)

# btnCalculate.grid(padx = 75, pady = 15)

# window.mainloop()   

# from  tkinter import *
# window = Tk()

# window.title("Label Example")
# lblPrice = Label(window, text = "Price")
# lblPrice.grid(padx = 100, pady = 15)

# window.mainloop()   

# from tkinter import *  
# window = Tk()   

# window.title("Entry Example")
# entName = Entry(window, width = 20)
# entName.grid(padx = 100, pady = 15)

# window.mainloop()   

# from tkinter import *

# def changeColor(event):
#     if entName["fg"] == "black":
#         entName["fg"] = "red"
#     else:
#         entName["fg"] = "black"

# window = Tk()

# window.title("Entry Example")
# entName = Entry(window, width = 20)
# entName.grid(padx = 100, pady = 15)
# entName.bind("<Button-3>", changeColor)

# window.mainloop()

# from tkinter import *

# def convertToUpper(event):
#     conOFentName.set(conOFentName.get().upper())

# window = Tk()

# window.title("Entry Example")
# conOFentName = StringVar()
# entName = Entry(window, textvariable = conOFentName)
# entName.grid(padx = 100, pady = 15)
# entName.bind("<Button-3>", convertToUpper)

# window.mainloop()

# from tkinter import *

# window = Tk()

# window.title("Read Only Example")
# conOFentOutput = StringVar()
# entName = Entry(window, textvariable = conOFentOutput, state = "readonly")
# entName.grid(padx = 100, pady = 15)
# conOFentOutput.set("Python Rocks!")

# window.mainloop()   

from tkinter import *
window = Tk()   

def changeWindowColor(entity):
    window["bg"] = lstColors.get(lstColors.curselection())

window.title("Listbox Example")
L= ["red", "green", "blue", "pink", "purple", "black"]  

conOfListColors = StringVar()
lstColors = Listbox(window, width=10, height=6, listvariable=conOfListColors)
lstColors.grid(padx = 100, pady = 15)

conOfListColors.set(tuple(L))
lstColors.bind("<<ListboxSelect>>", changeWindowColor)

window.mainloop()   