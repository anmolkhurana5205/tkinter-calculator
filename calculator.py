import tkinter as tk
import functools
def press(key):
    entry_var.set(entry_var.get() + key)
#function to evaluate the expression
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except Exception as e:
        entry_var.set('Error')
def clear():
    entry_var.set('')
calc=tk.Tk()
calc.geometry("270x360")
calc.title('My calculator')
entry_var=tk.StringVar()
entry_box=tk.Entry(calc, textvariable=entry_var, font=('calibre', 10, 'bold'), bd=10, insertwidth=2, width=36, borderwidth=4, justify='right')
entry_box.grid(row=0, column=0, columnspan=4, ipady=10)
buttons=['7', '8', '9', '/', 
       '4', '5', '6', '*',
       '1', '2', '3', '-',
       'c', '0', '=', '+']
row_val=1
col_val=0
#loop through button to create and place buttons
for i in buttons:
    if i == '=':
        btn = tk.Button(calc, text=i, padx=20, pady=20, font=('calibre', 15), bg='lightblue', command=calculate)
    elif i == 'c':
        btn = tk.Button(calc, text=i, padx=20, pady=20, font=('calibre', 15), bg='lightcoral', command=clear)
    else:
        btn = tk.Button(calc, text=i, padx=20, pady=20, font=('calibre', 15), command=functools.partial(press, i))
        # or I can use command=lamda b=i press(b) to capture the current value of i in the particular iteration.
    btn.grid(row=row_val, column=col_val)
    col_val+=1
    if col_val > 3:
        col_val=0
        row_val+=1
calc.mainloop()