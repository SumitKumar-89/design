from tkinter import*
#import  lambda  
expression = ""

def press(num):
    
    global expression
    
    expression = expression+str(num)
    
    equation.set(expression)
    
def equalpress():
    
    try:
         global expression
         total = str(eval(expression))
         equation.set(total)
         expression = ""
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression=""
    equation.set("")

if __name__ == "__main__":
    smt=Tk()
    smt.title(" SIMPLE CALCULATOR")
    smt.configure(background="sky Blue")
    smt.geometry("300x300")
    equation = StringVar()
    en=Entry(smt,width=40,textvariable=equation)
    en.place(x=20,y=20)
    btn1=Button(text='1',width=5,command=lambda: press(1))
    btn1.place(x=20,y=50)
    btn2=Button(text='2',width=5, command=lambda: press(2))
    btn2.place(x=70,y=50)
    btn3=Button(text='3',width=5,  command=lambda: press(3))
    btn3.place(x=120,y=50)
    btnn=Button(text='+',width=5,bg="olive",  command=lambda: press("+"))
    btnn.place(x=170,y=50)
    btn4=Button(text='4',width=5, command=lambda: press(4))
    btn4.place(x=20,y=80)
    btn5=Button(text='5',width=5,    command=lambda: press(5))
    btn5.place(x=70,y=80)
    btn6=Button(text='6',width=5,  command=lambda: press(6))
    btn6.place(x=120,y=80)
    btnm=Button(text='-',width=5,bg="olive",command=lambda: press("-"))
    btnm.place(x=170,y=80)
    btn7=Button(text='7',width=5,command=lambda: press(7))
    btn7.place(x=20,y=110)
    btn8=Button(text='8',width=5, command=lambda: press(8))
    btn8.place(x=70,y=110)
    btn9=Button(text='9',width=5,command=lambda: press(9))
    btn9.place(x=120,y=110)
    btnml=Button(text='*',width=5,bg="olive", fg="white",command=lambda: press("*"))
    btnml.place(x=170,y=110)
    btn0=Button(text='0',width=5, command=lambda: press(0))
    btn0.place(x=20,y=140)
    btnc=Button(text='clear',width=5,  command=clear)
    btnc.place(x=70,y=140)
    btne=Button(text="=",width=5,bg="olive", fg="white", command=equalpress)
    btne.place(x=120,y=140)
    btnd=Button(text='/',width=5,bg="olive", fg="white",command=lambda: press("/"))
    btnd.place(x=170,y=140)
    btnp=Button(text='.',width=5,command=lambda: press('.'))
    btnp.place(x=70,y=170)
    
   # btnmod=Button(text='pi',width=5, bg="olive" , fg="white",command=lambda: press("pi"))
   # btnmod.place(x=70,y=170)
    

    btnp1=Button(text='.',width=5,command=lambda: press('.'))
    btnp1.place(x=20,y=170)
    #btnmod1=Button(text='sin',width=5, bg="olive" , fg="white",command=lambda: press("sin"))
    #btnmod1.place(x=120,y=170)

    st=Label(text="---By Sumit",bg="red")
    st.place(x=220,y=220)
    smt.mainloop()


