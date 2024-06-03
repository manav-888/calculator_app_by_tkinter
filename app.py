from tkinter import *
import ast


root = Tk()

i=0
def display_number(num):
    global  i
    display.insert(i,num)
    i += 1

def display_operator(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length

def all_clear():
    display.delete(0,END)

def calculate():
    entire_string= display.get()
    try:
        code= ast.parse(entire_string, mode='eval')
        result = eval( compile(code, '', mode='eval') )
        all_clear()
        display.insert(0,result)
    except:
        all_clear()
        display.insert(0,"Error")

def undo():
    save_string = display.get()
    if len(save_string) != 0:
        new_string = save_string[:-1]
        all_clear()
        display.insert(0,new_string)
    else:
        all_clear()
        display.insert(0,"")


display = Entry(root)
display.grid(row=1, columnspan=6)

numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root , text = button_text , width = 2, height=2  , command= lambda text = button_text : display_number(text) )
        button.grid(row =x+2 , column= y)
        counter +=1

button =Button(root , text = "0" , width =2, height=2 , command = lambda: display_number(0))
button.grid(row = 5 , column= 1 )


count =0
operation =[ ' + ', ' - ', ' * ', ' / ' , ' * 3.14 ' ,' % ' ,' ** ' ,' ( ' , ' ) ', ' **2 ']
for x in range(4):
    for y in range(3):
        if count < len(operation):
            button = Button(root , text = operation[count] , width =2 , height=2 , command= lambda text =operation[count]:display_operator(text))
            count += 1
            button.grid(row = x+2, column =  y+4)


button_all_clear=Button(root,text="AC",width =2 , height= 2,command = all_clear )
button_all_clear.grid(row = 5, column=0)

button_cal=Button(root,text="=", width =2 , height= 2 , command=calculate )
button_cal.grid(row = 5, column=2)

button_undo= Button(root, text="<--", width =2, height=2,command= undo )
button_undo.grid(row= 5  , column=6)


status = Frame(root, bg='White', padx=2, pady=3)
status.grid(row = 6, columnspan = 7)
designed = Label(status, text='Manav Calculator')
designed.grid(row=0, column=0, padx= 5, pady=3)



root.mainloop()