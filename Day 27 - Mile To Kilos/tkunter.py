from tkinter import *

window = Tk()
window.title("Weno mecha ine sama ")
window.minsize(width=1500, height=900)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="Turi ip ip ip", font=("Arial", 48, "bold"))
my_label.config(text="wenomechainsama wifenlooof eselifterbraun")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button

def button_clicked():
    print("Ur mom got done")


button = Button(text="Clik to have ur mom done", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Skibidi bop bop yes yes")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=50)
input.grid(column=3, row=2)
print(input.get())

window.mainloop()

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 1, 1, 1, 1))
#
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)
