
# Guess the Number
# Develop a game where the computer randomly selects a number, and the user has to guess it.
import random
from tkinter import *
import tkinter as tk
from tkinter import IntVar
from tkinter import messagebox

def pick_randomNum():
    global target_num
    target_num = int(random.uniform(0,100))

min = 0
max = 100


def check_number():
    global min, max
   
    guessing_num_var = int(guessing_num.get())

    try:
        # guessing_num = int(input("guess a number  "))
        if 0 <= guessing_num_var <= 100:
            if guessing_num_var == target_num:
                tk.messagebox.showinfo('message', 'Correct!!!')
            else: 
                if guessing_num_var > target_num:
                    max=guessing_num_var
                    print("range from ", min,"to", guessing_num_var)
                    tk.messagebox.showerror('message', f'Range from {min} to {guessing_num_var}')
                    # check_number()
                elif guessing_num_var < target_num:
                    min = guessing_num_var
                    print("range from ", guessing_num_var,"to", max)
                    tk.messagebox.showwarning('message', f'Range from {guessing_num_var} to {max}')
                    # check_number()
        else:
            tk.messagebox.showwarning('message', 'Wrong number, outside of the range')
            print("Wrong number, outside of the range")
    except:
        tk.messagebox.showwarning('message', 'pick a number first')

window = tk.Tk()
window.title("Number guessing")
window.resizable(False,False)
window.geometry('380x200')
window.iconbitmap('icon.ico')

# a button to pick a random number as a key. This stays as first raw
random_pick = tk.Button(window, text= "Pick Random Number",width=20, height = 5, bg="Black",fg="red",font=('arial', 12, 'bold'), command=lambda:pick_randomNum(),justify=CENTER,padx=3)
# random_pick.grid(row=0,column=0)
random_pick.pack()

# a label for guessing a number
label_guess = tk.Label(window, text="please guess", width=10,height=2)
# label_guess.grid(row=1,column=0)
label_guess.pack()

guessing_num = tk.StringVar()
# an entry to guessing number. 
input_num_text = tk.Entry(window, width=15, textvariable = guessing_num,font=('arial', 20, 'bold'),highlightbackground= "white",highlightthickness=2)
# input_num_text.grid(row=1,column=1)
input_num_text.pack()

input = tk.Button(window, text= "Enter",width=20, height = 3, bg="Black",font=('arial', 10, 'bold'), command=lambda:check_number(),justify="center",padx=2,pady=2)
# input.grid(row=2,column=0)
input.pack()

window.mainloop()
# if __name__=="__main__":
#     pick_randomNum()
#     check_number()

