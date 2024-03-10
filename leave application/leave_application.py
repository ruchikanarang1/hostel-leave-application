from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
import tkinter as tk
from tkcalendar import DateEntry


def login():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ruchika",
    database="hope"
)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS leave_applications12 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), rollno VARCHAR(255), date_application DATE, date_leaving DATE, going_out_time TIME,am_pm_gt VARCHAR(20),return_time TIME,am_pm_rt VARCHAR(20), reason TEXT)")
    user1=username.get()
    code=passw.get()
     
    # Query the database for the given username
    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (user1,))
    result = cursor.fetchone()

    if result is None:
        messagebox.showerror("Error", "Username not found")
    else:
        if code == result[0]:
            messagebox.showinfo("Success", "Login successful")
            window=Toplevel(root)
            window.geometry('812x450')
            window.resizable(0,0)
            bgimage=ImageTk.PhotoImage(file="bg11.jpg")
            bglabel=tk.Label(window,image=bgimage)
            bglabel.place(x=0,y=0)
            window.title("Hostel Leave Application")

            # Create form labels
            name_label = tk.Label(window, text="Name:",font=('Bodoni MT',22),bg="white")
            rollno_label = tk.Label(window, text="Roll No.:",font=('Bodoni MT',22),bg="white")
            dateapp_label = tk.Label(window, text="Date of Application:",font=('Bodoni MT',22),bg="white")
            dateleave_label = tk.Label(window, text="Date of Leaving:",font=('Bodoni MT',22),bg="white")
            goingtime_label = tk.Label(window, text="Going Out Time:",font=('Bodoni MT',22),bg="white")
            returntime_label = tk.Label(window, text="Return Time:",font=('Bodoni MT',22),bg="white")
            reason_label = tk.Label(window, text="Reason for Going Out:",font=('Bodoni MT',22),bg="white")

            # Create form entry fields
            name_entry = tk.Entry(window,borderwidth=2,relief='solid')
            rollno_entry = tk.Entry(window,borderwidth=2,relief='solid')
            dateapp_entry = DateEntry(window,date_pattern='yyyy-mm-dd')
            dateleave_entry = DateEntry(window,date_pattern='yyyy-mm-dd')
            goingtime_entry_hours = tk.Spinbox(window, from_=0, to=23,width=6)
            goingtime_entry_mins=tk.Spinbox(window, from_=0, to=59,width=6)
            p=['am','pm']
            goingtime_entry_ampm=tk.Spinbox(window,values=p,textvariable=StringVar(window),width=6)
            returntime_entry_hours = tk.Spinbox(window, from_=0, to=23,width=6)
            returntime_entry_mins=tk.Spinbox(window, from_=0, to=59,width=6)
            returntime_entry_ampm=tk.Spinbox(window,values=p,textvariable=StringVar(window),width=6)
            reason_entry = tk.Text(window, height=4, width=25,borderwidth=2,relief='solid')

            def submit_request():
                    name = name_entry.get()
                    roll_no = rollno_entry.get()
                    date_application = dateapp_entry.get()
                    date_leaving = dateleave_entry.get()
                    going_out_time = f"{goingtime_entry_hours.get()}:{goingtime_entry_mins.get()}"
                    return_time =  f"{returntime_entry_hours.get()}:{returntime_entry_mins.get()}"
                    am_pm_gt=goingtime_entry_ampm.get()
                    am_pm_rt=returntime_entry_ampm.get()
                    reason = reason_entry.get("1.0", tk.END)

                    # Insert the form data into the database
                    query = "INSERT INTO leave_applications12 (name, rollno, date_application, date_leaving, going_out_time,am_pm_gt, return_time,am_pm_rt, reason) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
                    values = (name, roll_no, date_application, date_leaving, going_out_time,am_pm_gt,return_time,am_pm_rt,reason)
                    cursor.execute(query, values)
                    db.commit()

    # Display success message
                    messagebox.showinfo("Form Submitted", "Leave application submitted successfully.")

            # Create submit button
            submit_button = tk.Button(window, text="Submit",font=('Bodoni MT',18), command=submit_request, bg='yellow')

            # Grid layout for form elements
            name_label.grid(row=0, column=0, sticky="e")
            name_entry.grid(row=0, column=1)
            rollno_label.grid(row=4, column=0, sticky="e")
            rollno_entry.grid(row=4, column=1)
            dateapp_label.grid(row=8, column=0, sticky="e")
            dateapp_entry.grid(row=8, column=1)
            dateleave_label.grid(row=12, column=0, sticky="e")
            dateleave_entry.grid(row=12, column=1)
            goingtime_label.grid(row=16, column=0, sticky="e")
            goingtime_entry_hours.grid(row=16, column=1)
            goingtime_entry_mins.grid(row=16, column=2)
            goingtime_entry_ampm.grid(row=16, column=3)
            returntime_label.grid(row=20, column=0, sticky="e")
            returntime_entry_hours.grid(row=20, column=1)
            returntime_entry_mins.grid(row=20, column=2)
            returntime_entry_ampm.grid(row=20, column=3)
            reason_label.grid(row=24, column=0, sticky="e")
            reason_entry.grid(row=24, column=1)
            submit_button.grid(row=36, columnspan=2)

            if username.get()=='' or passw.get()=='':
                messagebox.showerror('Error','Fields cannot be empty')
    

            # Start the main event loop
            window.mainloop()

            # Close the database connection
            db.close()
        else:
            messagebox.showerror("Error", "Incorrect password")    
        
def main_screen():
    global root
    global username
    global passw
    root=Tk()
    root.geometry('812x450')
    root.resizable(0,0)
    root.title("Welcome")
    bgimage=ImageTk.PhotoImage(file="bg.jpeg")
    bglabel=Label(root,image=bgimage)
    bglabel.place(x=0,y=0)
    bglabel.grid(row=0,column=0)

    frame=Frame(root,width=320,height=350,bg="white")
    frame.place(x=450,y=30)

    heading=Label(frame,text="User Login",font=('Britannic Bold',32),bg='white')
    heading.place(x=50,y=10)

    def on_enter(e):
         username.delete(0,'end')
    

    username=Entry(frame,width=20,font=('Arial',14),bd=0)
    username.place(x=42,y=150)
    username.insert(0,'Username')
    username.bind('<FocusIn>', on_enter)
    
    
    Frame(frame,width=295,height=2,bg='black').place(x=38,y=177)
               
    passw=Entry(frame,show='*',width=20,font=('Arial',14),bd=0)
    passw.place(x=42,y=220)
    passw.insert(0,'Password')
    
    Frame(frame,width=295,height=2,bg='black').place(x=38,y=240)

    li=Button(frame,width=39,pady=7,text='Log in',bd=0,bg='goldenrod1',cursor='hand2',command=login).place(x=35,y=290)


    root.mainloop()

main_screen()
