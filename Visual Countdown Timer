import tkinter as tk

hour = 0
min = 0
sec = 0

def inputs():

    global hour, min, sec

    hour = int(entry1.get())

    min = int(entry2.get())

    sec = int(entry3.get())

    if sec > 60:

        timer_end.config(text="Invalid seconds", font=("Times New Roman", 30), fg="red")

    if min > 60:

        timer_end.config(text="Invalid minutes", font=("Times New Roman", 30), fg="red")

    if sec > 60 and min > 60:

        timer_end.config(text="Invalid minutes and seconds", font=("Times New Roman", 30), fg="red")

    if min == 60:

        hour = hour + 1
        min = 0

    if sec == 60:

        sec = 0
        min = min + 1

    if sec <= 60 and min <= 60:

        update_timer()

def update_timer():

    global hour, min, sec

    if hour > 0 or min > 0 or sec >= 0:

        timer_display.config(text=f"{hour:02d} : {min:02d} : {sec:02d}", font=("Times New Roman", 45, "bold"))

        if sec > 0:

            sec -= 1

        elif hour == 0 and min == 0 and sec == 0:

            timer_display.config(text="00 : 00 : 00", font=("Times New Roman", 45, "bold"), fg="red")

            timer_end.config(text="Timer ended!", font=("Times New Roman", 30))
            
        elif sec == 0 and min > 0 and hour >= 0:

            sec = 59

            min = min - 1 
        
        elif min == 0:

            min = 59

            sec = 59

            hour = hour - 1

        root.after(1000, update_timer)


root = tk.Tk()
root.title("Countdown Timer")

label0 = tk.Label(root, text="", width=60, font=("Times New Roman", 10))
label0.pack()

label1 = tk.Label(root, text="Enter the hours", font=("Times New Roman", 27))
label1.pack()

entry1 = tk.Entry(root, width=10, font=("Times New Roman", 19))
entry1.pack()

label2 = tk.Label(root, text="Enter the minutes", font=("Times New Roman", 27))
label2.pack()

entry2 = tk.Entry(root, width=10, font=("Times New Roman", 19))
entry2.pack()

label3 = tk.Label(root, text="Enter the seconds", font=("Times New Roman", 27))
label3.pack()

entry3 = tk.Entry(root, width=10, font=("Times New Roman", 19))
entry3.pack()

label4 = tk.Label(root, text="", font=("Times New Roman", 7))
label4.pack()

button3 = tk.Button(root, text="Start", font=("Times New Roman", 20), command=inputs)
button3.pack()

label5 = tk.Label(root, text="", font=("Times New Roman", 9))
label5.pack()

timer_display = tk.Label(root, text=f"{hour:02d} : {min:02d} : {sec:02d}", font=("Times New Roman", 45, "bold"))
timer_display.pack()

timer_end = tk.Label(root, text="", font=("Times New Roman", 30))
timer_end.pack()

root.mainloop()
