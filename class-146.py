from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background='snow')

enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label=Label(root,text="namein Ascii:",bg="light yellow",fg="blue")

def asciiConverter():
    input_word=enter_word.get()
    
    for letter in input_word :
        label["text"] +=str(ord(letter))+" "
btn=Button(root,text="Show name in Ascii",command=asciiConverter,bg='gold',fg='pink')
      
label.place(relx=0.5,rely=0.6,anchor=CENTER)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()