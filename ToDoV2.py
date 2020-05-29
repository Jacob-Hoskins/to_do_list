from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("300x375")
#root.configure(bg="white")


#Globals
ToDoList=[]

#Frames
textframe=LabelFrame(root, text="Text Frame")
textframe.grid(padx=10, pady=10)


def addtolist():
    user_input = input_box.get()
    ToDoList.append(user_input)

    return ToDoList


def updatelist():
    print(ToDoList)
    for task in ToDoList:
        print(task)

def completetask():
    print("Woring")

def textlist():
    print("Working")

input_box = Entry(root, width=30)
input_box.grid(row=0, column=1, columnspan=2, padx=57)

#buttons
addToListButton = Button(root, text="Add To List", command=addtolist)
addToListButton.grid(row=1, column=1, padx=25, ipadx=25)
updateList = Button(root, text="Update List", command=updatelist)
updateList.grid(row=2, column=1, padx=17, ipadx=30)
markTaskComplete = Button(root, text="Mark Complete", command=completetask)
markTaskComplete.grid(row=3, column=1, padx=5, ipadx=14)
textList = Button(root, text="Text List", command=textlist)
textList.grid(row=4, column=1, padx=17, ipadx=33)



root.mainloop()