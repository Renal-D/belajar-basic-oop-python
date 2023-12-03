import tkinter

coba = tkinter.Tk()

print(coba.__dict__)
coba.title("My GUI Application")

Label = tkinter.Label(coba, text= "Hello World")
Label.pack()

Button = tkinter.Button(coba, text="Connect", command= coba.destroy)
Button.pack()

Label.mainloop()