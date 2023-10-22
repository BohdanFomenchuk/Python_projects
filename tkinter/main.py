import tkinter

window = tkinter.Tk()
window.title("Miles to kilometers converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)

input_bar = tkinter.Entry(width=10)
input_bar.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
km_count = tkinter.Label(text="0")
km_count.grid(column=1, row=1)
# Label
def kilometres():
    miles = input_bar.get()
    km_count = tkinter.Label(text=round(int(miles)*1.609))
    km_count.grid(column=1, row=1)


button = tkinter.Button(text="Calculate", command=kilometres)
button.grid(column=1, row=2)







window.mainloop()
