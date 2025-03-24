from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("300x400")


def one():
    inp.insert(END,'1')

def two():
    inp.insert(END,'2')

def three():
    inp.insert(END,'3')

def four():
    inp.insert(END,'4')

def five():
    inp.insert(END,'5')

def six():
    inp.insert(END,'6')

def seven():
    inp.insert(END,'7')

def eight():
    inp.insert(END,'8')

def nine():
    inp.insert(END,'9')

def zero():
    inp.insert(END,'0')

def add():
    inp.insert(END,'+')

def sub():
    inp.insert(END,'-')

def multi():
    inp.insert(END,'*')

def div():
    inp.insert(END,'/')

def two():
    inp.insert(END,'2')

def two():
    inp.insert(END,'2')

def equ():
    try:
        val = inp.get()
        result = eval(val)
        inp.delete(0, END)
        inp.insert(END, str(result))
    except Exception as e:
        inp.delete(0, END)
        inp.insert(0, "Error")


inp=Entry(window,width=13,borderwidth=5,highlightthickness=0,font=("Arial",20))


btn1=Button(window,text="1",width=5,height=2,command=one)
btn2=Button(window,text="2",width=5,height=2,command=two)
btn3=Button(window,text="3",width=5,height=2,command=three)
btn4=Button(window,text="4",width=5,height=2,command=four)
btn5=Button(window,text="5",width=5,height=2,command=five)
btn6=Button(window,text="6",width=5,height=2,command=six)
btn7=Button(window,text="7",width=5,height=2,command=seven)
btn8=Button(window,text="8",width=5,height=2,command=eight)
btn9=Button(window,text="9",width=5,height=2,command=nine)
btn10=Button(window,text="0",width=5,height=2,command=zero)
btn11=Button(window,text="+",width=5,height=2,command=add)
btn12=Button(window,text="-",width=5,height=2,command=sub)
btn13=Button(window,text="*",width=5,height=2,command=multi)
btn14=Button(window,text="/",width=5,height=2,command=div)
btn15=Button(window,text="=",width=5,height=2,command=equ)
clr=Button(window,text="Clear",width=5,height=2,command=lambda: inp.delete(0, END))

inp.place(x=10,y=10)
btn1.place(x=10,y=90)
btn2.place(x=60,y=90)
btn3.place(x=120,y=90)
btn4.place(x=180,y=90)
btn5.place(x=240,y=90)
btn6.place(x=10,y=160)
btn7.place(x=60,y=160)
btn8.place(x=120,y=160)
btn9.place(x=180,y=160)
btn10.place(x=240,y=160)
btn11.place(x=10,y=230)
btn12.place(x=60,y=230)
btn13.place(x=120,y=230)
btn14.place(x=180,y=230)
btn15.place(x=240,y=230)
clr.place(x=240,y=10)




window.mainloop()