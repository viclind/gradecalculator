import camelot
import tkinter as tk
from tkinter import filedialog
import os
import ctypes
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

root = tk.Tk()
root.withdraw()

#file_path = filedialog.askopenfilename()

#file = os.path.basename(file_path)


file = "intyg.pdf" 

tables = camelot.read_pdf(file, flavor='stream')
table = tables[0].df

values = table.drop([0, 1, 2, 3, 4, 5, table.shape[0]-6, table.shape[0]-5, table.shape[0]-4, table.shape[0]-3, table.shape[0]-2, 
                                                        table.shape[0]-1]).drop(table.columns[[0,3,4]], axis=1).to_dict('records')

points = 0
totalhp = 0

for dict in values:
    if(dict[2] == 'G'):
        continue
    hp = float(dict[1].split(" ")[0].replace(",", "."))
    totalhp += hp
    points += int(dict[2]) * hp


total = round(points / totalhp, 2)


app = QApplication([])
app.setStyle('Fusion')
label = QLabel(str(total))
label.setFixedSize(500, 100)
label.show()
app.exec()
#ctypes.windll.user32.MessageBoxW(0, "Ditt betygssnitt är " + str(total), "Betygssnitt", 1)
