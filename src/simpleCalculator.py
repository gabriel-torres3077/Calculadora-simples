from tkinter import *
mainWindow = Tk()
mainWindow.geometry("330x440")
mainWindow.resizable(0,0)
mainWindow.columnconfigure(0, weight=1)
mainWindow.title("Simple calculator")

lastValue = StringVar()
firstValue = 0
lastEntry = Label(mainWindow, textvariable=lastValue)
lastEntry.grid(row=0, column=0, columnspan=4, sticky="w")
resultEntry = Entry(mainWindow, borderwidth=5, relief="groove")
resultEntry.grid(row=1, column=0, columnspan=4, pady=15, sticky='we')
def buttonClick(number):
    #resultEntry.delete(0, END)
    current = resultEntry.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(current) + str(number))
def plusFunction():
    global firstValue
    global equation
    global lastValue
    equation = 'plus'
    lastValue.set(resultEntry.get())
    firstValue= int(resultEntry.get())
    resultEntry.delete(0, END)
def minusFunction():
    global firstValue
    global equation
    global lastValue
    equation = 'minus'
    lastValue.set(resultEntry.get())
    firstValue = int(resultEntry.get())
    resultEntry.delete(0, END)
def timesFunction():
    global firstValue
    global equation
    global lastValue
    equation = 'times'
    lastValue.set(resultEntry.get())
    firstValue = int(resultEntry.get())
    resultEntry.delete(0, END)
def dividedFunction():
    global firstValue
    global equation
    global lastValue
    equation = 'divided'
    lastValue.set(resultEntry.get())
    firstValue = int(resultEntry.get())
    print(lastValue)
    resultEntry.delete(0, END)

def equalFunction():
    secondValue = int(resultEntry.get())
    resultEntry.delete(0, END)
    if equation == 'plus':
        resultEntry.insert(0, firstValue + secondValue)
    elif equation == 'minus':
        resultEntry.insert(0, firstValue - secondValue)
    elif equation == 'times':
        resultEntry.insert(0, firstValue * secondValue)
    elif equation == 'divided':
        resultEntry.insert(0, firstValue / secondValue)
    else:
        resultEntry.insert(0, "erro tente novamente")
def clear():
    resultEntry.delete(0, END)

#define all calculator buttons
#1º row
button1 = Button(mainWindow, text="1", padx = 30, pady = 30, command=lambda: buttonClick(1)).grid(row=2, column= 0)
button2 = Button(mainWindow, text="2", padx = 30, pady = 30, command=lambda: buttonClick(2)).grid(row=2, column= 1, padx = 3, pady = 3)
button3 = Button(mainWindow, text="3", padx = 30, pady = 30, command=lambda: buttonClick(3)).grid(row=2, column= 2, padx = 3, pady = 3)
buttonPlus = Button(mainWindow, text="+", padx = 30, pady = 30, command=plusFunction).grid(row=2, column= 3, padx = 3, pady = 3)
#2º row
button4 = Button(mainWindow, text="4", padx = 30, pady = 30, command=lambda: buttonClick(4)).grid(row=3, column= 0, padx = 3, pady = 3)
button5 = Button(mainWindow, text="5", padx = 30, pady = 30, command=lambda: buttonClick(5)).grid(row=3, column= 1, padx = 3, pady = 3)
button6 = Button(mainWindow, text="6", padx = 30, pady = 30, command=lambda: buttonClick(6)).grid(row=3, column= 2, padx = 3, pady = 3)
buttonMinus = Button(mainWindow, text="-", padx = 30, pady = 30, command=minusFunction).grid(row=3, column= 3, padx = 3, pady = 3)
#3º row
button7 = Button(mainWindow, text="7", padx = 30, pady = 30, command=lambda: buttonClick(7)).grid(row=4, column= 0, padx = 3, pady = 3)
button8 = Button(mainWindow, text="8", padx = 30, pady = 30, command=lambda: buttonClick(8)).grid(row=4, column= 1, padx = 3, pady = 3)
button9 = Button(mainWindow, text="9", padx = 30, pady = 30, command=lambda: buttonClick(9)).grid(row=4, column= 2, padx = 3, pady = 3)
buttonTimes = Button(mainWindow, text="x", padx = 30, pady = 30, command=timesFunction).grid(row=4, column= 3, padx = 3, pady = 3)
#4º row
buttonClear = Button(mainWindow, text="clear", pady=30, command=clear).grid(row=5, column=0, padx=3, pady = 3, sticky='we')
button0 = Button(mainWindow, text="0", padx = 30, pady = 30, command=lambda: buttonClick(0)).grid(row=5, column= 1, padx = 3, pady = 3)
buttonEqual = Button(mainWindow, text="=", padx = 30, pady = 30, command=equalFunction).grid(row=5, column= 2, padx = 3, pady = 3)
buttonDivided = Button(mainWindow, text="/", padx = 30, pady = 30, command=dividedFunction).grid(row=5, column= 3, padx = 3, pady = 3)

mainWindow.mainloop()
