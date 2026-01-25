import tkinter as tk

root=tk.Tk()
root.configure(bg="#FFFFFF")
root.title("cat")
root.geometry("500x500")

label=tk.Label(root,text="free RAM no scam",bg="#FDFDFD")
label.pack()

def buton():
    print("jk nu primesti RAM. e prea scump🥀")

def schimba_label():
    text=entry.get()
    label.config(text="jk u aint getting RAM")
    
button=tk.Button(root,text="puneti emailul si parola aici pentru RAM gratis",command=schimba_label,bg="#383838",fg="#000000")
button.pack()
entry=tk.Entry(root,width=30)
entry.pack()


root.mainloop()