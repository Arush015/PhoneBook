from Tkinter import *
import intro_me  #importing the file into_me to show the information about myself
from tkMessageBox import *
import tkFont
import sqlite3
root=Tk()  #main root window
con=sqlite3.Connection('PHONEBOOK_DATABASE1') #connection with database
cur=con.cursor()
cur.execute("PRAGMA foreign_keys=ON")  #creating tables
cur.execute("create table if not exists contact(contactid integer primary key autoincrement,fname varchar(15),mname varchar(15),lname varchar(15),company varchar(15),address varchar(30),city varchar(15),pin integer,website varchar(15),dob varchar(8))")
cur.execute("create table if not exists phone(contactid integer, contype varchar(15),phno number(10),primary key(contactid,phno),foreign key(contactid) references contact(contactid) on delete cascade)")
cur.execute("create table if not exists email(contactid integer,emailidtype varchar(15),emailid varchar(15),primary key(contactid,emailid),foreign key(contactid) references contact(contactid) on delete cascade)")
photo=PhotoImage(file="phonebook.gif")
photoimage = photo.subsample(5, 5)
Label(root, text = '', image = photoimage).grid(row=0,column=0)
root.title('Phonebook')
Label(root,text='PHONEBOOK',relief='ridge',font='times 30 bold italic',bg='gold').grid(row=0,column=2)  #gui design
Label(root,text='FIRST NAME',font='times 10').grid(row=2,column=0)
e1=Entry(root)
e1.grid(row=2,column=2)
Label(root,text='MIDDLE NAME',font='times 10').grid(row=3,column=0)
x=Entry(root)
x.grid(row=3,column=2)
Label(root,text='LAST NAME',font='times 10').grid(row=4,column=0)
e2=Entry(root)
e2.grid(row=4,column=2)
Label(root,text='COMPANY NAME',font='times 10').grid(row=5,column=0)
e3=Entry(root)
e3.grid(row=5,column=2)
Label(root,text='ADDRESS',font='times 10').grid(row=6,column=0)
e4=Entry(root)
e4.grid(row=6,column=2)
Label(root,text='PIN CODE',font='times 10').grid(row=7,column=0)
e5=Entry(root)
e5.grid(row=7,column=2)
Label(root,text='CITY',font='times 10').grid(row=8,column=0)
e6=Entry(root)
e6.grid(row=8,column=2)
Label(root,text='WEBSITE URL',font='times 10').grid(row=9,column=0)
e7=Entry(root)
e7.grid(row=9,column=2)
Label(root,text='DOB',font='times 10').grid(row=10,column=0)
e8=Entry(root)
e8.grid(row=10,column=2)
root.geometry('650x500')
Label(root,text='Select Phone Type:').grid(row=11,column=0)
v1=IntVar()
r=Radiobutton(root,text='Home',variable=v1,value=1)
r.grid(row=11,column=1)
r1=Radiobutton(root,text='Office',variable=v1,value=2)
r1.grid(row=11,column=2)
r2=Radiobutton(root,text='Mobile',variable=v1,value=3)
r2.grid(row=11,column=3)
Label(root,text='Phone number',font='times 10',fg='blue').grid(row=12,column=0)
e9=Entry(root)
e9.grid(row=12,column=2)
Button(root,text='+').grid(row=12,column=3)
Label(root,text='Select Email Type:',fg='blue').grid(row=13,column=0)
v2=IntVar()
r2=Radiobutton(root,text='Office',variable=v2,value=1)
r2.grid(row=13,column=1)
r3=Radiobutton(root,text='Personal',variable=v2,value=2)
r3.grid(row=13,column=2)
Label(root,text='Email Id',font='times 10').grid(row=14,column=0)
e10=Entry(root)
e10.grid(row=14,column=2)
d={1:'Home',2:'Office',3:'Mobile'}
e={1:'Office',2:'Personal'}
def new():  #function to save contact into database
    if len(e1.get())== 0 and len(x.get())== 0 and len(e2.get()) == 0 and len(e3.get()) == 0 and len(e4.get()) == 0 and len(e5.get())== 0 and len(e6.get())== 0 and len(e7.get())== 0 and len(e8.get())== 0 and len(e9.get())== 0 and len(e10.get())== 0 :
        showerror("Wrong info","every entry cannot be empty")
    else:
        cur.execute("insert into contact(fname,mname,lname,company,address,city,pin,website,dob) values(?,?,?,?,?,?,?,?,?)",(e1.get(),x.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()))
        cur.execute("select contactid curval from contact")
        qwe=cur.fetchall()
        le=len(qwe)-1
        cur.execute("insert into phone(contactid,contype,phno) values(?,?,?)",(qwe[le][0],d.get(v1.get()),e9.get()))
        cur.execute("insert into email(contactid,emailidtype,emailid) values(?,?,?)",(qwe[le][0],e.get(v2.get()),e10.get()))
        con.commit()
        cur.execute("select * from phone")
        showinfo("info","contact successfully saved")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        x.delete(0,END)
        v1.set(0)
        v2.set(0)

def search_sort():  #searching a contact
    root3=Tk()
    root3.title('Search')
    root3.geometry('550x700')
    Label(root3,text='Enter name to search:').grid(row=1,column=0,columnspan=5,sticky=W)
    g=Entry(root3)
    g.grid(row=1,column=0)
    fon=tkFont.Font(size=10)
    Lb=Listbox(root3,height='30',width='90',font=fon)
    Lb.grid()
    cur.execute("select contactid,fname,mname,lname from contact")
    s=cur.fetchall()
    global az
    az=s
    
    def showval(e=1): #to search the contact whena character is typed
        Lb.delete(0,END)
        cur.execute("select contactid,fname,mname,lname from contact where (fname like (?) or mname like (?) or lname like (?)) order by fname,mname,lname",('%'+g.get()+'%','%'+g.get()+'%','%'+g.get()+'%'))
        global az
        az=cur.fetchall()
        for i in range(len(az)):
            
            #if az[i][0]!='':
            Lb.insert(i,az[i][1]+" "+az[i][2]+" "+az[i][3])
    def fun(e=1):   #displaying the selected contact from database
        def delete_fun():
            cur.execute('delete from contact where contactid=?',(iq,))
            cur.execute('delete from phone where contactid=?',(iq,))
            cur.execute('delete from email where contactid=?',(iq,))
            con.commit()
            showinfo('Delete','Contact Removed Successfully')
            close_()
        Button(root3,text='Delete',command=delete_fun).grid(row=4,column=0)
        temp=Lb.curselection()
        iq=az[temp[0]][0]
        cur.execute("select fname,mname,lname ,company,address,city,pin,website,dob from contact where contactid=?",(iq,))
        li2=cur.fetchall()
        cur.execute("select contype,phno from phone where contactid=?",(iq,))
        li3=cur.fetchall()
        cur.execute("select emailidtype,emailid from email where contactid=?",(iq,))
        li4=cur.fetchall()
        Lb.delete(0,END)
        Lb.insert(0,"FIRST NAME     :  "+(str)(li2[0][0]))
        Lb.insert(1,"MIDDLE NAME     :  "+(str)(li2[0][1]))
        Lb.insert(2,"LAST NAME     :  "+(str)(li2[0][2]))
        Lb.insert(3,"COMPANY     :  "+(str)(li2[0][3]))
        Lb.insert(4,"ADDRESS    :  "+(str)(li2[0][4]))
        Lb.insert(5,"CITY    :  "+(str)(li2[0][5]))
        Lb.insert(6,"PIN     :  "+(str)(li2[0][6]))
        Lb.insert(7,"WEBSITE URL     :  "+(str)(li2[0][7]))
        Lb.insert(8,"DATE OF BIRTH     :  "+(str)(li2[0][8]))


        Lb.insert(9,"Phone details............")   
        Lb.insert(10,(str)(li3[0][0])+"   : "+(str)(li3[0][1]))
        Lb.insert(11,"Email Addresses............")
        Lb.insert(12,(str)(li4[0][0])+"   : "+(str)(li4[0][1]))
        
        
    cur.execute('select contactid curval from contact')
    q=cur.fetchall()
    l=len(q)
    
    
    for i in range(l):   # loop to print all the contacts in the listbox
        cur.execute("select fname,mname,lname from contact  where contactid=? order by fname,mname,lname",(q[i][0],))
        s=cur.fetchall()
        if s[0][0]!='':
            Lb.insert(i,s[0])

    Lb.bind("<Double-Button-1>",fun)
    g.bind("<KeyRelease>",showval)
    def close_(e=1):   
        root3.destroy()
    Button(root3,text='close',command=close_).grid(row=3,column=0)
    root3.mainloop()


    


Button(root,text='save',command=new).grid(row=17,column=0)
Button(root,text='search',command=search_sort).grid(row=17,column=1)
def close_main(e=1):
    root.destroy()
Button(root,text='close',command=close_main).grid(row=17,column=2)
def edit():   #function to edit the saved contacts
    root4=Tk()
    root4.title('Search a contact to edit')
    root4.geometry('550x700')
    Label(root4,text='Enter name to search and edit:').grid(row=1,column=0,columnspan=5,sticky=W)
    g=Entry(root4)
    g.grid(row=1,column=0)
    fon=tkFont.Font(size=10)
    Lb1=Listbox(root4,height='30',width='90',font=fon)
    Lb1.grid()
    cur.execute("select contactid,fname,mname,lname from contact")
    s=cur.fetchall()
    global az
    az=s
    def showval1(e=1):
        Lb1.delete(0,END)
        cur.execute("select contactid,fname,mname,lname from contact where (fname like (?) or mname like (?) or lname like (?)) order by fname,mname,lname",('%'+g.get()+'%','%'+g.get()+'%','%'+g.get()+'%'))
        global az
        az=cur.fetchall()
        for i in range(len(az)):
            #if az[i][0]!='':
            Lb1.insert(i,az[i][1]+" "+az[i][2]+" "+az[i][3])
    cur.execute('select contactid curval from contact')
    q=cur.fetchall()
    l=len(q)
    for i in range(l):
        cur.execute("select fname,mname,lname from contact  where contactid=? order by fname,mname,lname",(q[i][0],))
        s=cur.fetchall()
        if s[0][0]!='':
            Lb1.insert(i,s[0])
    def new_window(e=1):  #edit window
        root5=Tk()
        root5.title('EDIT WINDOW')
        Label(root5,text='EDIT CONTACT',relief='ridge',font='times 30 bold italic',bg='gold').grid(row=0,column=2)
        Label(root5,text='FIRST NAME',font='times 10').grid(row=2,column=0)
        e1=Entry(root5)
        e1.grid(row=2,column=2)
        Label(root5,text='MIDDLE NAME',font='times 10').grid(row=3,column=0)
        x=Entry(root5)
        x.grid(row=3,column=2)
        Label(root5,text='LAST NAME',font='times 10').grid(row=4,column=0)
        e2=Entry(root5)
        e2.grid(row=4,column=2)
        Label(root5,text='COMPANY NAME',font='times 10').grid(row=5,column=0)
        e3=Entry(root5)
        e3.grid(row=5,column=2)
        Label(root5,text='ADDRESS',font='times 10').grid(row=6,column=0)
        e4=Entry(root5)
        e4.grid(row=6,column=2)
        Label(root5,text='PIN CODE',font='times 10').grid(row=7,column=0)
        e5=Entry(root5)
        e5.grid(row=7,column=2)
        Label(root5,text='CITY',font='times 10').grid(row=8,column=0)
        e6=Entry(root5)
        e6.grid(row=8,column=2)
        Label(root5,text='WEBSITE URL',font='times 10').grid(row=9,column=0)
        e7=Entry(root5)
        e7.grid(row=9,column=2)
        Label(root5,text='DOB',font='times 10').grid(row=10,column=0)
        e8=Entry(root5)
        e8.grid(row=10,column=2)
        root5.geometry('650x500')
        Label(root5,text='Select Phone Type:').grid(row=11,column=0)
        v1=IntVar()
        r=Radiobutton(root5,text='Home',variable=v1,value=1)
        r.grid(row=11,column=1)
        r1=Radiobutton(root5,text='Office',variable=v1,value=2)
        r1.grid(row=11,column=2)
        r2=Radiobutton(root5,text='Mobile',variable=v1,value=3)
        r2.grid(row=11,column=3)
        Label(root5,text='Phone number',font='times 10',fg='blue').grid(row=12,column=0)
        e9=Entry(root5)
        e9.grid(row=12,column=2)
        Label(root5,text='Select Email Type:',fg='blue').grid(row=13,column=0)
        v2=IntVar()
        r2=Radiobutton(root5,text='Office',variable=v2,value=1)
        r2.grid(row=13,column=1)
        r3=Radiobutton(root5,text='Personal',variable=v2,value=2)
        r3.grid(row=13,column=2)
        Label(root5,text='Email Id',font='times 10').grid(row=14,column=0)
        e10=Entry(root5)
        e10.grid(row=14,column=2)
        d={1:'Home',2:'Office',3:'Mobile'}
        e={1:'Office',2:'Personal'}
        
        temp=Lb1.curselection()
        iq=az[temp[0]][0]
        cur.execute("select fname,mname,lname ,company,address,city,pin,website,dob from contact where contactid=?",(iq,))
        li2=cur.fetchall()
        cur.execute("select contype,phno from phone where contactid=?",(iq,))
        li3=cur.fetchall()
        cur.execute("select emailidtype,emailid from email where contactid=?",(iq,))
        li4=cur.fetchall()
        e1.insert(0,(li2[0][0]))
        x.insert(0,(li2[0][1]))
        e2.insert(0,(li2[0][2]))
        e3.insert(0,(li2[0][3]))
        e4.insert(0,(li2[0][4]))
        e5.insert(0,(li2[0][5]))
        e6.insert(0,(li2[0][6]))
        e7.insert(0,(li2[0][7]))
        e8.insert(0,(li2[0][8]))
        e9.insert(0,(li3[0][1]))
        e10.insert(0,(li4[0][1]))
        def fillup():  #refilling the selected contact into the entry box
            fn=e1.get()
            mn=x.get()
            ln=e2.get()
            com=e3.get()
            add=e4.get()
            cit=e5.get()
            pin=e6.get()
            web=e7.get()
            dob=e8.get()
            pn=e9.get()
            em=e10.get()
            iq=az[temp[0]][0]
            cur.execute("update contact set fname=(?) ,mname=(?),lname=(?),company=(?),address=(?),city=(?),pin=(?),website=(?),dob=(?) where contactid=(?)",(fn,mn,ln,com,add,cit,pin,web,dob,iq))
            cur.execute("update phone set phno=(?) where contactid=(?)",(pn,iq))
            cur.execute("update email set emailid=(?) where contactid=(?)",(em,iq))
            con.commit()
            showinfo('UPDATED',"contact updated successfully")
            
        Button(root5,text='save',command=fillup).grid(row=17,column=0)
        
    Lb1.bind("<Double-Button-1>",new_window)
    g.bind("<KeyRelease>",showval1)
    def close_1(e=1):   
        root4.destroy()
    Button(root4,text='close',command=close_1).grid(row=3,column=0)
    root4.mainloop()
    
Button(root,text='edit',command=edit).grid(row=17,column=3)
root.mainloop()
