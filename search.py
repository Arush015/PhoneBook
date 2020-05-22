def search_s():
    root3=Tk()
    root3.title('Search')
    root3.geometry('550x700')
    Label(root3,text='Enter name to search:').grid(row=1,column=0,columnspan=5,sticky=W)
    g=Entry(root3)
    g.grid(row=1,column=0)
    fon=tkFont.Font(size=10)
    Lb=Listbox(root3,height='30',width='90',font=fon)
    Lb.grid()
    
    def fun(e=1):
        q=(Lb.get(ACTIVE))
        cur.execute("select contactid from contact where fname =?",q)
    cur.execute('select contactid from contact')
    q=cur.fetchall()
    l=len(q)
    for i in range(l):
        cur.execute("select fname from contact where contactid=?",(i+1,))
        s=cur.fetchall()
        if s[0][0]!='':
            Lb.insert(i,s[0])
    def showval(e=1):
        u=unicode(g.get())
        u=("%"+u+"%",)
        Lb.delete(0,END)
        cur.execute("select fname from contact where fname like ?",u)
        az=cur.fetchall()
        for i in range(len(az)):
            if az[i][0]!='':
                Lb.insert(i,az[i])
        Lb.bind("<Double-Button-1>",fun)
    g.bind("<KeyRelease>",showval)
    def close_(e=1):
        root3.destroy()
    Button(root3,text='close',command=close_).grid(row=3,column=0)
    root3.mainloop()
