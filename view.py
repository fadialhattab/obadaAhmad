from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from functools import partial
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database = "electric"
)
cur = conn.cursor()


kwh_price = 0.086
wh = 0
cost = float

def insert_data(r_id,d_id,d_n,w,h,cost):
    kwh_price = 0.086
    wh = 0
    wats = (w.get())
    hours = (h.get())
    wh = int(wats) * int(hours) / 1000
    cost = wh * kwh_price
    Label(text="your electricy cost is %d JOD"% cost).place(x=350,y=220)
    sql1 = "INSERT INTO devices(room_id,device_id,device_name,device_load,use_hours,room_cost)VALUES(%s,%s,%s,%s,%s,%s) " 
    room_id = (r_id.get())
    serial = (d_id.get())
    name = (d_n.get())
    val1 = [room_id,serial,name,wats,hours,cost]
    cur.execute(sql1,val1)
    conn.commit()
    Label(text="your data is saved").place(x=350,y=250)

def search_data():
    Label(text="we will activate this feature in the new version").place(x=335,y=387)


win = Tk()
style = ttk.Style()
win.geometry("1000x1000")
serial = StringVar()
name = StringVar()
wats = StringVar()
hours = StringVar()
room_id = StringVar()
label_wel = Label(win, text="adding data",font="roman", foreground="black")
label_wel.place(x=416 , y= 20)
room_lbl = Label(win,text="enter the room number").place(x=100,y=80)
room_entry = Entry(win,textvariable=room_id).place(x=350,y=80)
serial_lbl = Label(win,text="enter the device serial num").place(x=100, y=100)
serial_entry = Entry(win,textvariable=serial).place(x=350,y=100)
name_lbl = Label(win,text="enter the device name").place(x=100, y=120)
name_entry = Entry(win,textvariable=name).place(x=350,y=120)
kw_lbl = Label(win,text="enter the kws of the device").place(x=100,y=140)
kw_entry = Entry(win,textvariable=wats).place(x=350,y=140)
time_lbl = Label(win,text="enter time of turnning on").place(x=100,y=160)
time_entry = Entry(win,textvariable=hours).place(x=350,y=160)
insert_data = partial(insert_data,room_id,serial,name,wats,hours,cost)
btn_save = Button(win,text="electricy cost",command=insert_data).place(x=350,y=200)
search = StringVar()
search_lbl =Label(win,text="search for device spec").place(x=360,y=325)
search_entry = Entry(win,textvariable=search,width=35).place(x=320,y=342.5)
btn_search = Button(win,text="Go!",command=search_data).place(x=375,y=365)
                                                        






win.mainloop()
