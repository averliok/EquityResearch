import GUI
from tkinter import filedialog
from pandas import DataFrame

root = tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def export_CSV():
    global df
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv(export_file_path, index=None, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV)
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()