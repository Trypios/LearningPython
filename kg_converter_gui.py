import tkinter as tk

def from_kg():
	"""converts kg to grams, pounds and ounces then updates tkinter window"""
	num = float(entry_value.get())
	grams = num * 1000

	# reset boxes
	box_grams.delete("1.0", tk.END)
	box_pounds.delete("1.0", tk.END)
	box_ounces.delete("1.0", tk.END)

	# fill boxes
	box_grams.insert(tk.END, f'{grams} grams')
	pounds = num * 2.205
	box_pounds.insert(tk.END, f'{pounds} pounds')
	ounces = num * 35.274
	box_ounces.insert(tk.END, f'{ounces} ounces')


window = tk.Tk()

# main button
button = tk.Button(window, text='Convert', command=from_kg)
button.grid(row=0, column=2)

# entry box
entry_value = tk.StringVar()
entry_label = tk.Label(window, text="Insert Kg:")
entry_label.grid(row=0,column=0)
box_entry = tk.Entry(window, textvariable=entry_value)
box_entry.grid(row=0, column=1)

# results
box_grams = tk.Text(window, height=1, width=20)
box_grams.grid(row=1, column=0)
box_pounds = tk.Text(window, height=1, width=20)
box_pounds.grid(row=1, column=1)
box_ounces = tk.Text(window, height=1, width=20)
box_ounces.grid(row=1, column=2)

window.mainloop()
