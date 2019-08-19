import tkinter as tk

def save_entry_fields():
    global num
    num = e1.get()
    print("Number: %s" % (e1.get()))
    with open("histData.txt", "a") as f:
        if(num.isdigit()):
            f.write(str(num)+"\n")
        else:
            print("Not a valid number")

master = tk.Tk()

tk.Label(master, 
         text="Number of rolls:  ", 
         font = ("Times New Roman", 20)).grid(row=0, column=0)

e1 = tk.Entry(master, 
              font = ("Times New Roman", 16), 
              bd = 5, 
              width = 5)

e1.grid(row=0, column=1)

tk.Label(master,
        text = "  ",
        font = ("Times New Roman", 20)).grid(row=0, column=2)

tk.Button(master, 
          text='Save', 
          command=save_entry_fields, 
          font = ("Times New Roman", 16)).grid(row=0, column=3, sticky=tk.W, pady=4)

tk.mainloop()
