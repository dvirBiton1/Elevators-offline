import tkinter as tk
import csv
import time as t

root = tk.Tk()

def readcalls():
    call=[]
    with open("B.csv") as f:
        data = csv.reader(f)
        for line in data:
            call.append(line)
    return call

count=0
canvas = tk.Canvas(root, height=720, width=400,bg="#263D42")
canvas.pack()
size =50
canvas.create_line(200, 0, 200, 900, fill="white")
for i in range(0, 720, 60):
    canvas.create_line(0, i, 700, i)
    count += 1


elev0 =canvas.create_rectangle(200, 600, 250, 540 , fill="green")
elev1 =canvas.create_rectangle(0, 600, 50, 540 , fill="green")
call =readcalls()

for i in range(0, 60, 1):
    canvas.move(elev1, 0,1)
    t.sleep(0.1)
    root.update()


start = tk.Button(root, text="Start now", padx=10, pady=5, fg="white", bg="#263d42")
start.pack()

root.mainloop()