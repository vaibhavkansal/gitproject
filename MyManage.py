from tkinter import *
from tkinter import ttk
import PyPDF2
from operator import add
from tkinter import filedialog  # to import a file name so that we can use that file
import xlrd
import xlsxwriter
import sqlite3
import tkinter.messagebox as tsmg
from datetime import date

root = Tk()
root.minsize(1200, 680)
root.maxsize(1200, 680)
# describing frames
root.title("Stocks")
global f2
global f4

f1 = Frame(root, background="bisque", height=100, borderwidth=6, relief=SUNKEN)
f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)

f1.grid(row=0, column=0, sticky="nsew", rowspan=2)
f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
f3.grid(row=0, column=2, sticky="nsew")
f4.grid(row=1, column=2, sticky="nsew")
Label(f2, text="                      ", bg="pink").pack()
root.grid_columnconfigure(0)
root.grid_columnconfigure(1)
root.grid_columnconfigure(2, weight=10)
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=1)


def createtable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
        Type VARCHAR(40),
        den_size VARCHAR(40),
        THKREMARK VARCHAR(30),
        BUNDLE VARCHAR(30) PRIMARY KEY,
        COVER VARCHAR(30),
        STM VARCHAR(30),
        R2 VARCHAR(30),
        PCS VARCHAR(30),
        MM VARCHAR(30),
        KG VARCHAR(30),
        PACKINGLIST VARCHAR(30),
        DATE VARCHAR(30),
        STATUS VARCHAR(30));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()

    pass


def showstock(events):
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM stockfinal634")
    d = crsr.fetchall()
    connection.close()

    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def showsoldstock():
        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        treev = ttk.Treeview(f3, selectmode='browse', height=19)
        treev.pack()
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev.configure(xscrollcommand=scrollbar.set)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=250, anchor='c')
        treev.column("2", width=300, anchor='c')
        treev.column("3", width=150, anchor='c')
        treev.column("4", width=80, anchor='c')
        treev.column("5", width=110, anchor='c')
        treev.column("6", width=100, anchor='c')
        treev.column("7", width=60, anchor='c')
        treev.column("8", width=60, anchor='c')
        treev.column("9", width=60, anchor='c')
        treev.column("10", width=60, anchor='c')
        treev.column("11", width=60, anchor='c')
        treev.column("12", width=100, anchor='c')
        treev.column("13", width=100, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="TYPE")
        treev.heading("2", text="DENSIZE")
        treev.heading("3", text="THK REMARK")
        treev.heading("4", text="BUNDLENO")
        treev.heading("5", text="COVER")
        treev.heading("6", text="STM")
        treev.heading("7", text="R2")
        treev.heading("8", text="PCS")
        treev.heading("9", text="MM")
        treev.heading("10", text="KGS")
        treev.heading("11", text="PACKINGLIST")
        treev.heading("12", text="DATE")
        treev.heading("13", text="STATUS")
        # Inserting the items and their features to the
        # columns built
        for row in d:
            s = tuple(row)
            if (s[12] == 'SOLD'):
                treev.insert("", 'end', values=s, tags=(s[12],))
        treev.tag_configure('SOLD', background='light green')
        treev.tag_configure('SPLIT', background='light blue')

        pass

        pass

    def showinstock():

        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        treev = ttk.Treeview(f3, selectmode='browse', height=19)
        treev.pack()
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev.configure(xscrollcommand=scrollbar.set)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=250, anchor='c')
        treev.column("2", width=300, anchor='c')
        treev.column("3", width=150, anchor='c')
        treev.column("4", width=80, anchor='c')
        treev.column("5", width=110, anchor='c')
        treev.column("6", width=100, anchor='c')
        treev.column("7", width=60, anchor='c')
        treev.column("8", width=60, anchor='c')
        treev.column("9", width=60, anchor='c')
        treev.column("10", width=60, anchor='c')
        treev.column("11", width=60, anchor='c')
        treev.column("12", width=100, anchor='c')
        treev.column("13", width=100, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="TYPE")
        treev.heading("2", text="DENSIZE")
        treev.heading("3", text="THK REMARK")
        treev.heading("4", text="BUNDLENO")
        treev.heading("5", text="COVER")
        treev.heading("6", text="STM")
        treev.heading("7", text="R2")
        treev.heading("8", text="PCS")
        treev.heading("9", text="MM")
        treev.heading("10", text="KGS")
        treev.heading("11", text="PACKINGLIST")
        treev.heading("12", text="DATE")
        treev.heading("13", text="STATUS")
        # Inserting the items and their features to the
        # columns built
        for row in d:
            s = tuple(row)
            if (s[12] != "SOLD"):
                treev.insert("", 'end', values=s, tags=(s[12],))
        treev.tag_configure('SOLD', background='light green')
        treev.tag_configure('SPLIT', background='light blue')

        pass

        pass

    def exporttoexcel():
        workbook = xlsxwriter.Workbook('stockupdate.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})

        alpa = ['TYPE', 'den_size', 'THKREMARK', 'BUNDLE', 'COVER', 'STM', 'R2', 'PCS', 'MM',
                'KG', 'PACKINGLIST', 'DATE', 'STATUS']

        d1 = d
        d1.insert(0, alpa)
        for i in range(len(d1)):
            d1[i] = list(d1[i])
        for i in range(len(d)):
            for j in range(len(d[0])):
                if (i == 0):
                    worksheet.write(i, j, f'''{d[i][j]}''', bold)
                else:
                    worksheet.write(i, j, f'''{d[i][j]}''')
        worksheet.set_column(0, 1, 25)
        worksheet.set_column(2, 2, 20)
        worksheet.set_column(4, 4, 15)
        worksheet.set_column(10, 12, 15)
        workbook.close()
        pass

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)

            f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
            f4.grid(row=1, column=2, sticky="nsew")
            b1 = Button(f4, text="  TYPE  ")
            b1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f4)
            e1.grid(row=0, column=1)
            l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f4)
            e2.grid(row=1, column=1)
            l3 = Label(f4, text="THK REMARK", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f4)
            e3.grid(row=2, column=1)
            l4 = Label(f4, text="BUNDLE", padx=5, width=8)
            l4.grid(row=3, column=0, padx=5, pady=5)
            e4 = Entry(f4)
            e4.grid(row=3, column=1)
            l5 = Label(f4, text="COVER", padx=5, width=8)
            l5.grid(row=4, column=0, padx=5, pady=5)
            e5 = Entry(f4)
            e5.grid(row=4, column=1)
            l6 = Label(f4, text="STM", padx=5, width=8)
            l6.grid(row=0, column=5, padx=5, pady=5)
            e6 = Entry(f4)
            e6.grid(row=0, column=6)
            l7 = Label(f4, text="R2", padx=5, width=8)
            l7.grid(row=0, column=3, padx=20, pady=5)
            e7 = Entry(f4)
            e7.grid(row=0, column=4)
            l8 = Label(f4, text="PCS", padx=5, width=8)
            l8.grid(row=1, column=3, padx=5, pady=5)
            e8 = Entry(f4)
            e8.grid(row=1, column=4)
            l9 = Label(f4, text="MM", padx=5, width=8)
            l9.grid(row=2, column=3, padx=5, pady=5)
            e9 = Entry(f4)
            e9.grid(row=2, column=4)
            l10 = Label(f4, text="KGS", padx=5, width=8)
            l10.grid(row=3, column=3, padx=5, pady=5)
            e10 = Entry(f4)
            e10.grid(row=3, column=4)
            l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
            l11.grid(row=4, column=3, padx=5, pady=5)
            e11 = Entry(f4)
            e11.grid(row=4, column=4)
            l12 = Label(f4, text="DATE", padx=5, width=8)
            l12.grid(row=3, column=5, padx=5, pady=5)
            e12 = Entry(f4)
            e12.grid(row=3, column=6)
            l13 = Label(f4, text="STATUS", padx=5, width=8)
            l13.grid(row=1, column=5, padx=20, pady=5)
            e13 = Entry(f4)
            e13.grid(row=1, column=6, padx=5, pady=5)

            e1.insert(0, a[0])
            e2.insert(0, a[1])
            e3.insert(0, a[2])
            e4.insert(0, a[3])
            e5.insert(0, a[4])
            e6.insert(0, a[5])
            e7.insert(0, a[6])
            e8.insert(0, a[7])
            e9.insert(0, a[8])
            e10.insert(0, a[9])
            e11.insert(0, a[10])
            e12.insert(0, a[11])
            e13.insert(0, a[12])

            def searchbundlenametype(event):
                f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")
                f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")

                def check():
                    connection = sqlite3.connect("mytables4.db")
                    crsr = connection.cursor()
                    crsr.execute(f"SELECT * FROM stockfinal634 WHERE Type ='{e112.get()}';")
                    w = crsr.fetchall()
                    print(w)
                    if (len(w) == 0):
                        Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
                        pass

                    else:
                        d = []
                        for i in w:
                            d.append(list(i))
                        connection.close()

                        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                        f3.grid(row=0, column=2, sticky="nsew")

                        treev = ttk.Treeview(f3, selectmode='browse', height=20)
                        treev.pack(fill=BOTH)
                        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
                        scrollbar.pack(side=BOTTOM, fill=X)
                        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
                        treev.configure(xscrollcommand=scrollbar.set)
                        # Defining heading
                        treev['show'] = 'headings'

                        # Assigning the width and anchor to  the
                        # respective columns
                        treev.column("1", width=250, anchor='c')
                        treev.column("2", width=300, anchor='c')
                        treev.column("3", width=150, anchor='c')
                        treev.column("4", width=80, anchor='c')
                        treev.column("5", width=100, anchor='c')
                        treev.column("6", width=100, anchor='c')
                        treev.column("7", width=60, anchor='c')
                        treev.column("8", width=60, anchor='c')
                        treev.column("9", width=60, anchor='c')
                        treev.column("10", width=60, anchor='c')
                        treev.column("11", width=80, anchor='c')
                        treev.column("12", width=100, anchor='c')
                        treev.column("13", width=100, anchor='c')

                        # Assigning the heading names to the
                        # respective columns
                        treev.heading("1", text="TYPE")
                        treev.heading("2", text="DENSIZE")
                        treev.heading("3", text="THK REMARK")
                        treev.heading("4", text="BUNDLENO")
                        treev.heading("5", text="COVER")
                        treev.heading("6", text="STM")
                        treev.heading("7", text="R2")
                        treev.heading("8", text="PCS")
                        treev.heading("9", text="MM")
                        treev.heading("10", text="KGS")
                        treev.heading("11", text="PACKINGLIST")
                        treev.heading("12", text="DATE")
                        treev.heading("13", text="STATUS")
                        # Inserting the items and their features to the
                        # columns built
                        for row in d:
                            s = tuple(row)
                            treev.insert("", 'end', values=s, tags=(s[12],))
                        treev.tag_configure('SOLD', background='light green')
                        treev.tag_configure('SPLIT', background='light blue')

                        Button(f4, text=" FOUND   ").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

                l = Label(f4, text=" TYPE  ", width=8)
                l.grid(row=0, column=0, padx=5, pady=5)
                e112 = Entry(f4)
                e112.insert(0, a[0])
                e112.grid(row=0, column=1)
                Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)
                pass

            b1.bind("<Button-1>", searchbundlenametype)

            def updateduringchecking():
                d12 = []
                d12.append(e1.get())
                d12.append(e2.get())
                d12.append(e3.get())
                d12.append(e4.get())
                d12.append(e5.get())
                d12.append(e6.get())
                d12.append(e7.get())
                d12.append(e8.get())
                d12.append(e9.get())
                d12.append(e10.get())
                d12.append(e11.get())
                d12.append(e12.get())
                d12.append(e13.get())

                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e4.get()}';")
                connection.commit()

                row = d12
                sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                try:
                    crsr.execute(sa)
                    tsmg.showinfo("Saved", "your entry has been saved")
                    connection.commit()
                    showstock(events)

                except Exception as e:
                    row = a
                    sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                    crsr.execute(sa)
                    connection.commit()
                    print(e)
                    showstock(events)

                connection.close()

            if(a[12]=="SOLD"):
                Button(f4, text="CANT SAVE").grid(row=4, column=5, columnspan=2, padx=25)
            else:
                Button(f4, text="SAVE DATA", command=updateduringchecking).grid(row=4, column=5, columnspan=2, padx=25)

    Button(f4, text="SOLD", command=showsoldstock).grid(row=0, column=0, sticky="nsew", pady=30, padx=100)
    Button(f4, text="IN STOCK", command=showinstock).grid(row=0, column=1, sticky="nsew", pady=30, padx=100)
    Button(f4, text="EXPORT TO EXCEL", command=exporttoexcel).grid(row=0, column=2, sticky="nsew", pady=30, padx=100)

    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack()
    treev.bind("<Double-Button-1>", clickedrow)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=110, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=60, anchor='c')
    treev.column("8", width=60, anchor='c')
    treev.column("9", width=60, anchor='c')
    treev.column("10", width=60, anchor='c')
    treev.column("11", width=60, anchor='c')
    treev.column("12", width=100, anchor='c')
    treev.column("13", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="TYPE")
    treev.heading("2", text="DENSIZE")
    treev.heading("3", text="THK REMARK")
    treev.heading("4", text="BUNDLENO")
    treev.heading("5", text="COVER")
    treev.heading("6", text="STM")
    treev.heading("7", text="R2")
    treev.heading("8", text="PCS")
    treev.heading("9", text="MM")
    treev.heading("10", text="KGS")
    treev.heading("11", text="PACKINGLIST")
    treev.heading("12", text="DATE")
    treev.heading("13", text="STATUS")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s, tags=(s[12],))
    treev.tag_configure('SOLD', background='light green')
    treev.tag_configure('SPLIT', background='light blue')

    pass


def showstocksbeforesaving(d):
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")

    treev = ttk.Treeview(f3, selectmode='browse', height=20)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
    treev.configure(xscrollcommand=scrollbar.set)
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=80, anchor='c')
    treev.column("5", width=100, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=60, anchor='c')
    treev.column("8", width=60, anchor='c')
    treev.column("9", width=60, anchor='c')
    treev.column("10", width=60, anchor='c')
    treev.column("11", width=80, anchor='c')
    treev.column("12", width=100, anchor='c')
    treev.column("13", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="TYPE")
    treev.heading("2", text="DENSIZE")
    treev.heading("3", text="THK REMARK")
    treev.heading("4", text="BUNDLENO")
    treev.heading("5", text="COVER")
    treev.heading("6", text="STM")
    treev.heading("7", text="R2")
    treev.heading("8", text="PCS")
    treev.heading("9", text="MM")
    treev.heading("10", text="KGS")
    treev.heading("11", text="PACKINGLIST")
    treev.heading("12", text="DATE")
    treev.heading("13", text="STATUS")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s)
    s = ("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    treev.insert("", 'end', values=s)
    s = ("", "TOTAL", "BUNDLE", len(treev.get_children()) - 1, "", "", "", "", "", "", "", "", "", "", "", "")
    treev.insert("", 'end', values=s)
    pass


def savebutton(d):
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    b1 = Button(f4, text="save data")

    def insertintotable(e):
        # tablename="stockfinal634"
        # createtable(tablename)
        # here d is the 2d array of excel
        connection = sqlite3.connect("mytables4.db")
        cursor = connection.cursor()
        for row in d:
            sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
            try:
                cursor.execute(sa)
                connection.commit()
            except Exception as e:
                print(e)
                tsmg.showinfo("Failed", "Packing list already exist")
                break
        connection.close()
        pass

    b1.bind('<Button-1>', insertintotable)
    b1.pack()
    pass


def addbundle(event):
    d = []

    def check():
        d.append(e1.get())
        d.append(e2.get())
        d.append(e3.get())
        d.append(e4.get())
        d.append(e5.get())
        d.append(e6.get())
        d.append(e7.get())
        d.append(e8.get())
        d.append(e9.get())
        d.append(e10.get())
        d.append(e11.get())
        d.append(e12.get())
        d.append(e13.get())

        d1 = tuple(d)
        connection = sqlite3.connect("mytables4.db")
        cursor = connection.cursor()
        row = d1
        sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
        try:
            cursor.execute(sa)
            connection.commit()
            tsmg.showinfo("Saved", "your entry has been saved")

            # errorcanoccur
            addbundle(event)

        except Exception as e:
            print(e)
            tsmg.showinfo("Failed", "Bundle no. exist")
            # errorcanoccur

            addbundle(event)

        connection.close()

        # now i need to store data in sql

    f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l1 = Label(f4, text="Bundle type", width=8)
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.grid(row=0, column=1)
    l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = Entry(f4)
    e2.grid(row=1, column=1)
    l3 = Label(f4, text="THK REMARK", padx=5, width=8)
    l3.grid(row=2, column=0, padx=5, pady=5)
    e3 = Entry(f4)
    e3.grid(row=2, column=1)
    l4 = Label(f4, text="BUNDLE", padx=5, width=8)
    l4.grid(row=3, column=0, padx=5, pady=5)
    e4 = Entry(f4)
    e4.grid(row=3, column=1)
    l5 = Label(f4, text="COVER", padx=5, width=8)
    l5.grid(row=4, column=0, padx=5, pady=5)
    e5 = Entry(f4)
    e5.grid(row=4, column=1)
    l6 = Label(f4, text="STM", padx=5, width=8)
    l6.grid(row=0, column=5, padx=5, pady=5)
    e6 = Entry(f4)
    e6.grid(row=0, column=6)
    l7 = Label(f4, text="R2", padx=5, width=8)
    l7.grid(row=0, column=3, padx=20, pady=5)
    e7 = Entry(f4)
    e7.grid(row=0, column=4)
    l8 = Label(f4, text="PCS", padx=5, width=8)
    l8.grid(row=1, column=3, padx=5, pady=5)
    e8 = Entry(f4)
    e8.grid(row=1, column=4)
    l9 = Label(f4, text="MM", padx=5, width=8)
    l9.grid(row=2, column=3, padx=5, pady=5)
    e9 = Entry(f4)
    e9.grid(row=2, column=4)
    l10 = Label(f4, text="KGS", padx=5, width=8)
    l10.grid(row=3, column=3, padx=5, pady=5)
    e10 = Entry(f4)
    e10.grid(row=3, column=4)
    l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
    l11.grid(row=4, column=3, padx=5, pady=5)
    e11 = Entry(f4)
    e11.grid(row=4, column=4)
    l12 = Label(f4, text="DATE", padx=5, width=8)
    l12.grid(row=3, column=5, padx=5, pady=5)
    e12 = Entry(f4)
    e12.grid(row=3, column=6)
    l13 = Label(f4, text="STATUS", padx=5, width=8)
    l13.grid(row=1, column=5, padx=20, pady=5)
    e13 = Entry(f4)
    e13.grid(row=1, column=6, padx=5, pady=5)



    #deleteifwanttodelete
    e1.bind("<KP_Enter>", lambda x: e2.focus())
    e1.bind("<Return>", lambda x: e2.focus())
    e2.bind("<KP_Enter>", lambda x: e3.focus())
    e2.bind("<Return>", lambda x: e3.focus())
    e3.bind("<KP_Enter>", lambda x: e4.focus())
    e3.bind("<Return>", lambda x: e4.focus())
    e4.bind("<KP_Enter>", lambda x: e5.focus())
    e4.bind("<Return>", lambda x: e5.focus())
    e5.bind("<KP_Enter>", lambda x: e7.focus())
    e5.bind("<Return>", lambda x: e7.focus())
    e7.bind("<KP_Enter>", lambda x: e8.focus())
    e7.bind("<Return>", lambda x: e8.focus())
    e8.bind("<KP_Enter>", lambda x: e9.focus())
    e8.bind("<Return>", lambda x: e9.focus())
    e9.bind("<KP_Enter>", lambda x: e10.focus())
    e9.bind("<Return>", lambda x: e10.focus())
    e10.bind("<KP_Enter>", lambda x: e11.focus())
    e10.bind("<Return>", lambda x: e11.focus())
    e11.bind("<KP_Enter>", lambda x: e6.focus())
    e11.bind("<Return>", lambda x: e6.focus())
    e6.bind("<KP_Enter>", lambda x: e13.focus())
    e6.bind("<Return>", lambda x: e13.focus())
    e13.bind("<KP_Enter>", lambda x: e12.focus())
    e13.bind("<Return>", lambda x: e12.focus())

    Button(f4, text="SAVE DATA", command=check).grid(row=4, column=5, columnspan=2, padx=25)

    pass


def addpacking(event):
    loc = filedialog.askopenfilename()
    po = open(loc, 'rb')
    pr = PyPDF2.PdfFileReader(po)
    pob = pr.getPage(0)
    f = pob.extractText()
    d = f.split('\n')
    w = []

    def removespaces(l):
        no = l.count('')
        while (no > 0):
            l.remove("")
            no = no - 1
        return (l)

    for i in d:
        l = i.split("  ")
        li = removespaces(l)
        w.append(li)
    # popping the last three lines
    w.pop()
    w.pop()
    w.pop()
    # now we will find packing list no and date
    g = ""
    for i in w:
        try:
            i.index('P.L.NO')
            g = i
        except Exception as eas:
            continue
    if (g == ""):
        for i in w:
            try:
                i.index('PL.No')
                g = i
            except:
                continue
    plno = g[2]
    plno = plno.strip()
    dateindex = w.index(g) - 1
    dat = str(w[dateindex][0])
    i1 = dat.find(':')
    pldate = dat[i1 + 1:]
    pldate = pldate.strip()

    for i in w:
        try:
            i.index('BUNDLE')
            p = i
        except:
            continue

    main = w.index(p)
    for i in range(main):
        w.pop(0)
    w.pop(0)
    new = []
    # now we will remove total column that contain total of type
    for i in w:
        if (i[0] == '1'):
            continue
        elif (i[0] == '2'):
            continue
        elif (i[0] == '3'):
            continue
        elif (i[0] == '4'):
            continue
        elif (i[0] == '5'):
            continue
        elif (i[0] == '6'):
            continue
        elif (i[0] == '7'):
            continue
        elif (i[0] == '8'):
            continue
        elif (i[0] == '9'):
            continue
        elif (i[0] == '10'):
            continue
        elif (i[0] == '11'):
            continue
        elif (i[0] == '12'):
            continue
        elif (i[0] == '13'):
            continue
        elif (i[0] == '14'):
            continue
        elif (i[0] == '15'):
            continue
        elif (i[0] == '16'):
            continue
        elif (i[0] == '17'):
            continue
        else:
            new.append(i)
    w = new
    new = []
    base = ""
    for i in w:
        if (len(i) == 1):
            base = i[0]
        else:
            e = []
            e.append(base)
            for j in i:
                e.append(j)
            new.append(e)
    w = new

    for i in range(len(w)):
        if (i % 2 == 0):
            if (len(w[i]) > 3):
                # i need to merge them
                if (len(w[i]) == 4):
                    w[i][1] = w[i][1] + w[i][2]
                    w[i].pop(2)
                elif (len(w[i]) == 5):
                    w[i][1] = w[i][1] + w[i][2] + w[i][3]
                    w[i].pop(2)
                    w[i].pop(2)
            elif (len(w[i]) < 3):
                w[i].append('')
            else:
                continue
        else:
            w[i].pop(0)
            if (w[i][0].count(" ") == 1):
                we = w[i][0].split(" ")
                w[i].pop(0)
                w[i].insert(0, we[1])
                w[i].insert(0, we[0])

            if (len(w[i]) == 7):
                continue
            elif (len(w[i]) < 7):
                while (len(w[i]) != 7):
                    w[i].insert(1, '')
            else:
                diff = len(w[i]) - 7
                for i2 in range(diff):
                    w[i].pop(2)

    l1 = []
    l2 = []
    for i in range(len(w)):
        if (i % 2 == 0):
            l1.append(w[i])
        else:
            l2.append(w[i])
    l3 = []
    for i in range(len(l1)):
        l4 = l1[i] + l2[i]
        l3.append(l4)
    d = l3
    for i in d:
        i.append(plno)
        i.append(pldate)
        status = "INSTOCK"
        i.append(status)
    showstocksbeforesaving(d)
    savebutton(d)

    pass

def importfromexcel(event):
    tsmg.showinfo("Warning","it will read only first 13 column")
    loc = filedialog.askopenfilename()
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    print(sheet.nrows)
    print(sheet.ncols)
    mainlist = []
    for i in range(sheet.nrows):
        listimport = []
        for j in range(sheet.ncols):
            listimport.append(sheet.cell_value(i, j))
        mainlist.append(listimport)
    ques=tsmg.askquestion("Chose","does first row contain heading ??")
    try:
        if(ques=='no'):
            showstocksbeforesaving(mainlist)
            savebutton(mainlist)
        else:
            mainlist.pop(0)
            showstocksbeforesaving(mainlist)
            savebutton(mainlist)
    except Exception as e:
        print(e)


def splitbundle(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l = Label(f4, text="BUNDLE NUMBER YOU WANT TO SPLIT")
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    def check():
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            tsmg.showinfo("Warning", "NOT IN STOCK")
            pass

        else:
            d = list(w[0])
            connection.close()
            if(d[12] =="SOLD"):
                tsmg.showinfo("Warning","ALREADY SOLD")
            else:
                f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                strdat = str(d)
                Label(f4, text=strdat).grid()

                print(d)
                Label(f3,text=f"{d[3]}A").grid(row=1, column=0,columnspan=2 ,padx=10)
                Label(f3,text=f"{d[3]}B").grid(row=1, column=2,columnspan=2 ,padx=10)
                Label(f3,text="PCS").grid(row=2, column=0,padx=10,pady=15)
                e1 = Entry(f3)
                e1.grid(row=2, column=1)
                Label(f3,text="PCS").grid(row=2, column=2 ,padx=10,pady=15)
                e2 = Entry(f3)
                e2.grid(row=2, column=3)
                Label(f3, text="KGS").grid(row=3, column=0, padx=10, pady=15)
                e3 = Entry(f3)
                e3.grid(row=3, column=1)
                Label(f3, text="KGS").grid(row=3, column=2, padx=10, pady=15)
                e4 = Entry(f3)
                e4.grid(row=3, column=3)
                def checkewd():


                    d1a=d.copy()
                    d1b=d.copy()
                    d1a[3] = f"{d[3]}A"
                    d1b[3] = f"{d[3]}B"
                    d1a[7]=e1.get()
                    d1b[7]=e2.get()
                    d1a[9] = e3.get()
                    d1b[9] = e4.get()
                    d1a[12] = "SPLIT"
                    d1b[12] = "SPLIT"
                    connection = sqlite3.connect("mytables4.db")
                    cursor = connection.cursor()
                    row=d1a
                    sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                    cursor.execute(sa)
                    connection.commit()
                    row = d1b
                    sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                    cursor.execute(sa)
                    connection.commit()
                    connection.close()
                    connection = sqlite3.connect("mytables4.db")
                    crsr = connection.cursor()
                    crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                    connection.commit()
                    connection.close()
                    tsmg.showinfo("completed","Bundle Splited")
                    splitbundle()


                    pass
                Button(f3, text="SLPIT", command=checkewd).grid(row=4, column=2, columnspan=2, padx=25)

        pass

    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass






def searchbundleno(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634")
    w = crsr.fetchall()
    connection.close()
    bunlis=[]
    for i in w:
        bunlis.append(i[3])
    def check():

        # we will retrive our data from here
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = list(w[0])
            connection.close()

            # now we will set the values
            l1 = Label(f3, text="Bundle type", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f3)
            e1.grid(row=0, column=1)
            l2 = Label(f3, text="DEN SIZE", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f3)
            e2.grid(row=1, column=1)
            l3 = Label(f3, text="THK REMARK", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f3)
            e3.grid(row=2, column=1)
            l4 = Label(f3, text="BUNDLE", padx=5, width=8)
            l4.grid(row=3, column=0, padx=5, pady=5)
            e4 = Entry(f3)
            e4.grid(row=3, column=1)
            l5 = Label(f3, text="COVER", padx=5, width=8)
            l5.grid(row=4, column=0, padx=5, pady=5)
            e5 = Entry(f3)
            e5.grid(row=4, column=1)
            l6 = Label(f3, text="STM", padx=5, width=8)
            l6.grid(row=0, column=5, padx=5, pady=5)
            e6 = Entry(f3)
            e6.grid(row=0, column=6)
            l7 = Label(f3, text="R2", padx=5, width=8)
            l7.grid(row=0, column=3, padx=20, pady=5)
            e7 = Entry(f3)
            e7.grid(row=0, column=4)
            l8 = Label(f3, text="PCS", padx=5, width=8)
            l8.grid(row=1, column=3, padx=5, pady=5)
            e8 = Entry(f3)
            e8.grid(row=1, column=4)
            l9 = Label(f3, text="MM", padx=5, width=8)
            l9.grid(row=2, column=3, padx=5, pady=5)
            e9 = Entry(f3)
            e9.grid(row=2, column=4)
            l10 = Label(f3, text="KGS", padx=5, width=8)
            l10.grid(row=3, column=3, padx=5, pady=5)
            e10 = Entry(f3)
            e10.grid(row=3, column=4)
            l11 = Label(f3, text="PACKINGNO", padx=5, width=8)
            l11.grid(row=4, column=3, padx=5, pady=5)
            e11 = Entry(f3)
            e11.grid(row=4, column=4)
            l12 = Label(f3, text="DATE", padx=5, width=8)
            l12.grid(row=3, column=5, padx=5, pady=5)
            e12 = Entry(f3)
            e12.grid(row=3, column=6)
            l13 = Label(f3, text="STATUS", padx=5, width=8)
            l13.grid(row=1, column=5, padx=20, pady=5)
            e13 = Entry(f3)
            e13.grid(row=1, column=6, padx=5, pady=5)

            e1.insert(0, d[0])
            e2.insert(0, d[1])
            e3.insert(0, d[2])
            e4.insert(0, d[3])
            e5.insert(0, d[4])
            e6.insert(0, d[5])
            e7.insert(0, d[6])
            e8.insert(0, d[7])
            e9.insert(0, d[8])
            e10.insert(0, d[9])
            e11.insert(0, d[10])
            e12.insert(0, d[11])
            e13.insert(0, d[12])

            def update():
                d1 = []
                d1.append(e1.get())
                d1.append(e2.get())
                d1.append(e3.get())
                d1.append(e4.get())
                d1.append(e5.get())
                d1.append(e6.get())
                d1.append(e7.get())
                d1.append(e8.get())
                d1.append(e9.get())
                d1.append(e10.get())
                d1.append(e11.get())
                d1.append(e12.get())
                d1.append(e13.get())
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                connection.commit()

                row = d1
                sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                try:
                    crsr.execute(sa)
                    tsmg.showinfo("Saved", "your entry has been saved")
                    connection.commit()
                    searchbundleno(event)

                except Exception as eas:
                    row = d
                    sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                    crsr.execute(sa)
                    connection.commit()
                    tsmg.showinfo("Failed", "Bundle no. exist")
                connection.close()

            def showbill():
                bno = e.get()
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM billstock5 WHERE BUNDLENO ='{bno}'")
                down = crsr.fetchall()
                connection.close()
                print(down)
                billno=down[0][0]
                bundlebuyer=down[0][1]
                print(bundlebuyer)
                print(billno)
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")
                treev1 = ttk.Treeview(f3, selectmode='browse', height=20)
                treev1.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev1["columns"] = ("1", "2", "3", "4", "5", "6", "7")
                treev1.configure(xscrollcommand=scrollbar.set)
                treev1['show'] = 'headings'

                treev1.column("1", anchor='c')
                treev1.column("2", width=200, anchor='c')
                treev1.column("3", width=80, anchor='c')
                treev1.column("4", width=80, anchor='c')
                treev1.column("5", width=80, anchor='c')
                treev1.column("6", width=80, anchor='c')
                treev1.column("7", width=80, anchor='c')
                na = bundlebuyer
                na = na.upper()
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                sel = crsr.fetchall()
                connection.close()
                sel = list(sel[0])
                r1 = ("NAME", sel[0], "", "BILLNO", billno, "", "")
                r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
                r3 = ("ADD2", sel[2], "", "DATE", down[0][7], "","")
                treev1.insert("", 'end', values=r1)
                treev1.insert("", 'end', values=r2)
                treev1.insert("", 'end', values=r3)
                r31 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r31)
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNo ='{billno}'")
                d = crsr.fetchall()
                connection.close()
                total = []
                for i in d:
                    listforinsert = []
                    listforinsert.append(i[2])
                    listforinsert.append(i[3])
                    listforinsert.append(i[4])
                    listforinsert.append(i[5])
                    listforinsert.append(i[6])
                    listforinsert.append(i[8])
                    listforinsert.append(i[9])
                    total.append(int(i[9]))
                    print(listforinsert)
                    treev1.insert("", 'end', values=listforinsert)
                r312 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r312)
                r32 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r32)
                r33 = ("", "", "", "", "TOTAL", "", sum(total))
                treev1.insert("", 'end', values=r33, tags=('tot',))
                treev1.tag_configure('tot', background='light blue')

            if(d[12] == "SOLD"):
                Button(f4, text=" SHOW BILL ", command=showbill).grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

            else:
                Button(f4, text="    UPDATE    ", command=update).grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

        pass

    l = Label(f4, text="BUNDLE NO", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = ttk.Combobox(f4, values=bunlis)
    e.grid(row=0, column=1)

    def keydown(event):
        ba = e.get()
        a = ba.upper()
        checklist = []
        for i in bunlis:
            if a in i:
                checklist.append(i)
        e["values"] = checklist

    e.bind("<KeyRelease>", keydown)

    def keyup(event):
        e.event_generate("<Down>")

    e.bind("<Return>", keyup)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def searchpl(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE PACKINGLIST ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = []
            for i in w:
                d.append(list(i))
            connection.close()

            f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
            f3.grid(row=0, column=2, sticky="nsew")

            treev = ttk.Treeview(f3, selectmode='browse', height=20)
            treev.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
            treev.configure(xscrollcommand=scrollbar.set)
            # Defining heading
            treev['show'] = 'headings'

            # Assigning the width and anchor to  the
            # respective columns
            treev.column("1", width=250, anchor='c')
            treev.column("2", width=300, anchor='c')
            treev.column("3", width=150, anchor='c')
            treev.column("4", width=80, anchor='c')
            treev.column("5", width=100, anchor='c')
            treev.column("6", width=100, anchor='c')
            treev.column("7", width=60, anchor='c')
            treev.column("8", width=60, anchor='c')
            treev.column("9", width=60, anchor='c')
            treev.column("10", width=60, anchor='c')
            treev.column("11", width=80, anchor='c')
            treev.column("12", width=100, anchor='c')
            treev.column("13", width=100, anchor='c')

            # Assigning the heading names to the
            # respective columns
            treev.heading("1", text="TYPE")
            treev.heading("2", text="DENSIZE")
            treev.heading("3", text="THK REMARK")
            treev.heading("4", text="BUNDLENO")
            treev.heading("5", text="COVER")
            treev.heading("6", text="STM")
            treev.heading("7", text="R2")
            treev.heading("8", text="PCS")
            treev.heading("9", text="MM")
            treev.heading("10", text="KGS")
            treev.heading("11", text="PACKINGLIST")
            treev.heading("12", text="DATE")
            treev.heading("13", text="STATUS")
            # Inserting the items and their features to the
            # columns built
            for row in d:
                s = tuple(row)
                treev.insert("", 'end', values=s, tags=(s[12],))
            treev.tag_configure('SOLD', background='light green')
            treev.tag_configure('SPLIT', background='light blue')

            Button(f4, text=" FOUND   ").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

    l = Label(f4, text=" PLNO  ", width=10)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def searchbundlename(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE Type ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = []
            for i in w:
                d.append(list(i))
            connection.close()

            f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
            f3.grid(row=0, column=2, sticky="nsew")

            treev = ttk.Treeview(f3, selectmode='browse', height=20)
            treev.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
            treev.configure(xscrollcommand=scrollbar.set)
            # Defining heading
            treev['show'] = 'headings'

            # Assigning the width and anchor to  the
            # respective columns
            treev.column("1", width=250, anchor='c')
            treev.column("2", width=300, anchor='c')
            treev.column("3", width=150, anchor='c')
            treev.column("4", width=80, anchor='c')
            treev.column("5", width=100, anchor='c')
            treev.column("6", width=100, anchor='c')
            treev.column("7", width=60, anchor='c')
            treev.column("8", width=60, anchor='c')
            treev.column("9", width=60, anchor='c')
            treev.column("10", width=60, anchor='c')
            treev.column("11", width=80, anchor='c')
            treev.column("12", width=100, anchor='c')
            treev.column("13", width=100, anchor='c')

            # Assigning the heading names to the
            # respective columns
            treev.heading("1", text="TYPE")
            treev.heading("2", text="DENSIZE")
            treev.heading("3", text="THK REMARK")
            treev.heading("4", text="BUNDLENO")
            treev.heading("5", text="COVER")
            treev.heading("6", text="STM")
            treev.heading("7", text="R2")
            treev.heading("8", text="PCS")
            treev.heading("9", text="MM")
            treev.heading("10", text="KGS")
            treev.heading("11", text="PACKINGLIST")
            treev.heading("12", text="DATE")
            treev.heading("13", text="STATUS")
            # Inserting the items and their features to the
            # columns built
            for row in d:
                s = tuple(row)
                treev.insert("", 'end', values=s, tags=(s[12],))
            treev.tag_configure('SOLD', background='light green')
            treev.tag_configure('SPLIT', background='light blue')

            Button(f4, text=" FOUND   ").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

    l = Label(f4, text=" TYPE  ", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)

    e.grid(row=0, column=1)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)
    pass


def deletepacking(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():

        def delete():
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            try:
                crsr.execute(f"DELETE FROM stockfinal634 WHERE PACKINGLIST ='{e.get()}';")
                connection.commit()
                connection.close()
                tsmg.showinfo("DELETED", f"Yor packing list - {e.get()} has been deleted");
                deletepacking(event)

            except Exception as eat:
                print(eat)

        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE PACKINGLIST ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = []
            for i in w:
                d.append(list(i))
            connection.close()

            f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
            f3.grid(row=0, column=2, sticky="nsew")

            treev = ttk.Treeview(f3, selectmode='browse', height=20)
            treev.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
            treev.configure(xscrollcommand=scrollbar.set)
            # Defining heading
            treev['show'] = 'headings'

            # Assigning the width and anchor to  the
            # respective columns
            treev.column("1", width=250, anchor='c')
            treev.column("2", width=300, anchor='c')
            treev.column("3", width=150, anchor='c')
            treev.column("4", width=80, anchor='c')
            treev.column("5", width=100, anchor='c')
            treev.column("6", width=100, anchor='c')
            treev.column("7", width=60, anchor='c')
            treev.column("8", width=60, anchor='c')
            treev.column("9", width=60, anchor='c')
            treev.column("10", width=60, anchor='c')
            treev.column("11", width=80, anchor='c')
            treev.column("12", width=100, anchor='c')
            treev.column("13", width=100, anchor='c')

            # Assigning the heading names to the
            # respective columns
            treev.heading("1", text="TYPE")
            treev.heading("2", text="DENSIZE")
            treev.heading("3", text="THK REMARK")
            treev.heading("4", text="BUNDLENO")
            treev.heading("5", text="COVER")
            treev.heading("6", text="STM")
            treev.heading("7", text="R2")
            treev.heading("8", text="PCS")
            treev.heading("9", text="MM")
            treev.heading("10", text="KGS")
            treev.heading("11", text="PACKINGLIST")
            treev.heading("12", text="DATE")
            treev.heading("13", text="STATUS")
            # Inserting the items and their features to the
            # columns built
            for row in d:
                s = tuple(row)
                treev.insert("", 'end', values=s, tags=(s[12],))
            treev.tag_configure('SOLD', background='light green')
            treev.tag_configure('SPLIT', background='light blue')

            Button(f4, text="   DELETE    ", command=delete).grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

    l = Label(f4, text=" PLNO  ", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)
    pass


def deletebundle(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():
        # we will retrive our data from here
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = list(w[0])
            connection.close()

            # now we will set the values

            l1 = Label(f3, text="Bundle type", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f3)
            e1.grid(row=0, column=1)
            l2 = Label(f3, text="DEN SIZE", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f3)
            e2.grid(row=1, column=1)
            l3 = Label(f3, text="THK REMARK", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f3)
            e3.grid(row=2, column=1)
            l4 = Label(f3, text="BUNDLE", padx=5, width=8)
            l4.grid(row=3, column=0, padx=5, pady=5)
            e4 = Entry(f3)
            e4.grid(row=3, column=1)
            l5 = Label(f3, text="COVER", padx=5, width=8)
            l5.grid(row=4, column=0, padx=5, pady=5)
            e5 = Entry(f3)
            e5.grid(row=4, column=1)
            l6 = Label(f3, text="STM", padx=5, width=8)
            l6.grid(row=0, column=5, padx=5, pady=5)
            e6 = Entry(f3)
            e6.grid(row=0, column=6)
            l7 = Label(f3, text="R2", padx=5, width=8)
            l7.grid(row=0, column=3, padx=20, pady=5)
            e7 = Entry(f3)
            e7.grid(row=0, column=4)
            l8 = Label(f3, text="PCS", padx=5, width=8)
            l8.grid(row=1, column=3, padx=5, pady=5)
            e8 = Entry(f3)
            e8.grid(row=1, column=4)
            l9 = Label(f3, text="MM", padx=5, width=8)
            l9.grid(row=2, column=3, padx=5, pady=5)
            e9 = Entry(f3)
            e9.grid(row=2, column=4)
            l10 = Label(f3, text="KGS", padx=5, width=8)
            l10.grid(row=3, column=3, padx=5, pady=5)
            e10 = Entry(f3)
            e10.grid(row=3, column=4)
            l11 = Label(f3, text="PACKINGNO", padx=5, width=8)
            l11.grid(row=4, column=3, padx=5, pady=5)
            e11 = Entry(f3)
            e11.grid(row=4, column=4)
            l12 = Label(f3, text="DATE", padx=5, width=8)
            l12.grid(row=3, column=5, padx=5, pady=5)
            e12 = Entry(f3)
            e12.grid(row=3, column=6)
            l13 = Label(f3, text="STATUS", padx=5, width=8)
            l13.grid(row=1, column=5, padx=20, pady=5)
            e13 = Entry(f3)
            e13.grid(row=1, column=6, padx=5, pady=5)

            e1.insert(0, d[0])
            e2.insert(0, d[1])
            e3.insert(0, d[2])
            e4.insert(0, d[3])
            e5.insert(0, d[4])
            e6.insert(0, d[5])
            e7.insert(0, d[6])
            e8.insert(0, d[7])
            e9.insert(0, d[8])
            e10.insert(0, d[9])
            e11.insert(0, d[10])
            e12.insert(0, d[11])
            e13.insert(0, d[12])

            def delete():

                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                connection.commit()
                connection.close()
                # recursivly calling the function againg so that it replace the screen
                deletebundle(event)

            Button(f4, text="    DELETE    ", command=delete).grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

        pass

    l = Label(f4, text="BUNDLE NO", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def updatebundleno(event):
    searchbundleno(event)
    pass


def createcustomertable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            NAME VARCHAR(40) PRIMARY KEY,
            ADD_LINE_1 VARCHAR(40),
            ADD_LINE_2 VARCHAR(30),
            CITY VARCHAR(30),
            PINCODE VARCHAR(30),
            MOBILE VARCHAR(30),
            LIMIT_ VARCHAR(30),
            TOTAL VARCHAR(30));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()
    pass


def addcustomer(event):
    # sat="custom9"
    # createcustomertable(sat)
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    print(d)
    connection.close()

    def check():
        newdata = []
        newdata.append(e1.get().upper())
        newdata.append(e2.get().upper())
        newdata.append(e3.get().upper())
        newdata.append(e4.get().upper())
        newdata.append(e5.get().upper())
        newdata.append(e6.get().upper())
        try:
            aerw1=float(e7.get())
            newdata.append(aerw1)
        except Exception as e:
            newdata.append('0')
        try:
            aerw=float(e8.get())
            newdata.append(aerw)
        except Exception as e:
            newdata.append('0')

        d1 = tuple(newdata)
        connection = sqlite3.connect("mytables4.db")
        cursor = connection.cursor()
        row = d1

        sa = f'''INSERT INTO custom9 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
        try:
            cursor.execute(sa)
            connection.commit()
            tsmg.showinfo("Saved", "your entry has been saved")

            # errorcanoccur
            addcustomer(event)

        except Exception as e:
            print(e)
            tsmg.showinfo("Failed", "Customer already exist")
            # errorcanoccur

            addcustomer(event)

        connection.close()
        # now i need to store data in sql
        print(d1)
        pass

    l1 = Label(f4, text="NAME", width=8)
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.grid(row=0, column=1)
    l2 = Label(f4, text="ADD_LINE_1", padx=5, width=8)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = Entry(f4)
    e2.grid(row=1, column=1)
    l3 = Label(f4, text="ADD_LINE_2", padx=5, width=8)
    l3.grid(row=2, column=0, padx=5, pady=5)
    e3 = Entry(f4)
    e3.grid(row=2, column=1)
    l4 = Label(f4, text="CITY", padx=5, width=8)
    l4.grid(row=0, column=2, padx=5, pady=5)
    e4 = Entry(f4)
    e4.grid(row=0, column=3)
    l5 = Label(f4, text="PINCODE", padx=5, width=8)
    l5.grid(row=1, column=2, padx=5, pady=5)
    e5 = Entry(f4)
    e5.grid(row=1, column=3)
    l6 = Label(f4, text="MOBILE NO", padx=5, width=8)
    l6.grid(row=2, column=2, padx=5, pady=5)
    e6 = Entry(f4)
    e6.grid(row=2, column=3)
    l7 = Label(f4, text="LIMIT_", padx=5, width=8)
    l7.grid(row=0, column=4, padx=20, pady=5)
    e7 = Entry(f4)
    e7.grid(row=0, column=5)
    l8 = Label(f4, text="TOTAL", padx=5, width=8)
    l8.grid(row=1, column=4, padx=5, pady=5)
    e8 = Entry(f4)
    e8.grid(row=1, column=5)
    e8.insert(0, '0')

    Button(f4, text="SAVE CUSTOMER", command=check).grid(row=2, column=4, columnspan=2, padx=25)

    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack(fill=BOTH)
    # treev.bind("<Double-Button-1>", clickedrow)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=110, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=100, anchor='c')
    treev.column("8", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="ADD_LINE_1")
    treev.heading("3", text="ADD_LINE_2")
    treev.heading("4", text="CITY")
    treev.heading("5", text="PINCODE")
    treev.heading("6", text="MOBILE")
    treev.heading("7", text="LIMIT_")
    treev.heading("8", text="TOTAL")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s)

    pass


def updatecustomer(event):
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()

    connection.close()

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)
            f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
            f4.grid(row=1, column=2, sticky="nsew")
            l1 = Label(f4, text="NAME", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f4)
            e1.grid(row=0, column=1)
            l2 = Label(f4, text="ADD_LINE_1", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f4)
            e2.grid(row=1, column=1)
            l3 = Label(f4, text="ADD_LINE_2", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f4)
            e3.grid(row=2, column=1)
            l4 = Label(f4, text="CITY", padx=5, width=8)
            l4.grid(row=0, column=2, padx=5, pady=5)
            e4 = Entry(f4)
            e4.grid(row=0, column=3)
            l5 = Label(f4, text="PINCODE", padx=5, width=8)
            l5.grid(row=1, column=2, padx=5, pady=5)
            e5 = Entry(f4)
            e5.grid(row=1, column=3)
            l6 = Label(f4, text="MOBILE NO", padx=5, width=8)
            l6.grid(row=2, column=2, padx=5, pady=5)
            e6 = Entry(f4)
            e6.grid(row=2, column=3)
            l7 = Label(f4, text="LIMIT_", padx=5, width=8)
            l7.grid(row=0, column=4, padx=20, pady=5)
            e7 = Entry(f4)
            e7.grid(row=0, column=5)
            l8 = Label(f4, text="TOTAL", padx=5, width=8)
            l8.grid(row=1, column=4, padx=5, pady=5)
            e8 = Entry(f4)
            e8.grid(row=1, column=5)
            e1.insert(0, a[0])
            e2.insert(0, a[1])
            e3.insert(0, a[2])
            e4.insert(0, a[3])
            e5.insert(0, a[4])
            e6.insert(0, a[5])
            e7.insert(0, a[6])
            e8.insert(0, a[7])

            def update():
                newdata = []
                newdata.append(e1.get().upper())
                newdata.append(e2.get().upper())
                newdata.append(e3.get().upper())
                newdata.append(e4.get().upper())
                newdata.append(e5.get().upper())
                newdata.append(e6.get().upper())
                try:
                    aerw1 = float(e7.get())
                    newdata.append(aerw1)
                except Exception as e:
                    newdata.append('0')
                try:
                    aerw = float(e8.get())
                    newdata.append(aerw)
                except Exception as e:
                    newdata.append('0')


                d1 = tuple(newdata)

                connection = sqlite3.connect("mytables4.db")
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM custom9 WHERE NAME ='{a[0]}';")
                connection.commit()
                row = d1
                sa = f'''INSERT INTO custom9 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
                try:
                    cursor.execute(sa)
                    connection.commit()
                    tsmg.showinfo("Saved", "your entry has been updated")
                    updatecustomer(event)
                    # errorcanoccur

                except Exception as e:
                    row = a

                    sa = f'''INSERT INTO custom9 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
                    cursor.execute(sa)
                    connection.commit()

                    print(e)
                    tsmg.showinfo("Failed", "Customer already exist")
                    updatecustomer(event)

                d1 = tuple(newdata)

            Button(f4, text="UPDATE CUSTOMER", command=update).grid(row=2, column=4, columnspan=2, padx=25)

        pass

    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack()
    treev.bind("<Double-Button-1>", clickedrow)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=110, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=100, anchor='c')
    treev.column("8", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="ADD_LINE_1")
    treev.heading("3", text="ADD_LINE_2")
    treev.heading("4", text="CITY")
    treev.heading("5", text="PINCODE")
    treev.heading("6", text="MOBILE")
    treev.heading("7", text="LIMIT_")
    treev.heading("8", text="TOTAL")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s)

    l1 = Label(f4, text="SEARCH BY NAME", width=18)
    l1.grid(row=0, column=0, padx=65, pady=15)
    e123 = Entry(f4)
    e123.grid(row=0, column=1)

    def searchbyname():
        namea = e123.get()
        nameaup = namea.upper()
        f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM custom9 WHERE NAME ='{nameaup}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            a = list(w[0])
            connection.close()
            l1 = Label(f4, text="NAME", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f4)
            e1.grid(row=0, column=1)
            l2 = Label(f4, text="ADD_LINE_1", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f4)
            e2.grid(row=1, column=1)
            l3 = Label(f4, text="ADD_LINE_2", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f4)
            e3.grid(row=2, column=1)
            l4 = Label(f4, text="CITY", padx=5, width=8)
            l4.grid(row=0, column=2, padx=5, pady=5)
            e4 = Entry(f4)
            e4.grid(row=0, column=3)
            l5 = Label(f4, text="PINCODE", padx=5, width=8)
            l5.grid(row=1, column=2, padx=5, pady=5)
            e5 = Entry(f4)
            e5.grid(row=1, column=3)
            l6 = Label(f4, text="MOBILE NO", padx=5, width=8)
            l6.grid(row=2, column=2, padx=5, pady=5)
            e6 = Entry(f4)
            e6.grid(row=2, column=3)
            l7 = Label(f4, text="LIMIT_", padx=5, width=8)
            l7.grid(row=0, column=4, padx=20, pady=5)
            e7 = Entry(f4)
            e7.grid(row=0, column=5)
            l8 = Label(f4, text="TOTAL", padx=5, width=8)
            l8.grid(row=1, column=4, padx=5, pady=5)
            e8 = Entry(f4)
            e8.grid(row=1, column=5)
            e1.insert(0, a[0])
            e2.insert(0, a[1])
            e3.insert(0, a[2])
            e4.insert(0, a[3])
            e5.insert(0, a[4])
            e6.insert(0, a[5])
            e7.insert(0, a[6])
            e8.insert(0, a[7])

            def update():
                newdata = []
                newdata.append(e1.get().upper())
                newdata.append(e2.get().upper())
                newdata.append(e3.get().upper())
                newdata.append(e4.get().upper())
                newdata.append(e5.get().upper())
                newdata.append(e6.get().upper())
                try:
                    aerw1 = float(e7.get())
                    newdata.append(aerw1)
                except Exception as e:
                    newdata.append('0')
                try:
                    aerw = float(e8.get())
                    newdata.append(aerw)
                except Exception as e:
                    newdata.append('0')
                d1 = tuple(newdata)

                connection = sqlite3.connect("mytables4.db")
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM custom9 WHERE NAME ='{a[0]}';")
                connection.commit()
                row = d1
                up = row[0]
                up = up.upper()
                sa = f'''INSERT INTO custom9 VALUES ("{up}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
                try:
                    cursor.execute(sa)
                    connection.commit()
                    tsmg.showinfo("Saved", "your entry has been updated")
                    updatecustomer(event)
                    # errorcanoccur

                except Exception as e:
                    row = a
                    sa = f'''INSERT INTO custom9 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
                    cursor.execute(sa)
                    connection.commit()

                    print(e)
                    tsmg.showinfo("Failed", "Customer already exist")
                    updatecustomer(event)

                d1 = tuple(newdata)

            Button(f4, text="UPDATE CUSTOMER", command=update).grid(row=2, column=4, columnspan=2, padx=25)

        pass

    Button(f4, text="SEARCH", command=searchbyname).grid(row=0, column=3, columnspan=2, padx=25)
    l2 = Label(f4, text="SEARCH BY CITY", width=18)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e234 = Entry(f4)
    e234.grid(row=1, column=1)

    def searchbycity():
        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        treev = ttk.Treeview(f3, selectmode='browse', height=19)
        treev.pack()
        treev.bind("<Double-Button-1>", clickedrow)
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev.configure(xscrollcommand=scrollbar.set)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=250, anchor='c')
        treev.column("2", width=300, anchor='c')
        treev.column("3", width=150, anchor='c')
        treev.column("4", width=100, anchor='c')
        treev.column("5", width=110, anchor='c')
        treev.column("6", width=100, anchor='c')
        treev.column("7", width=100, anchor='c')
        treev.column("8", width=100, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="NAME")
        treev.heading("2", text="ADD_LINE_1")
        treev.heading("3", text="ADD_LINE_2")
        treev.heading("4", text="CITY")
        treev.heading("5", text="PINCODE")
        treev.heading("6", text="MOBILE")
        treev.heading("7", text="LIMIT_")
        treev.heading("8", text="TOTAL")

        # Inserting the items and their features to the
        # columns built
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM custom9 WHERE CITY = '{e234.get()}'")
        d = crsr.fetchall()

        for row in d:
            s = tuple(row)
            treev.insert("", 'end', values=s)

        pass

    Button(f4, text="SEARCH", command=searchbycity).grid(row=1, column=3, columnspan=2, padx=25)

    pass


def showcustomer(event):
    # we will show customer now
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    print(d)
    connection.close()
    treev = ttk.Treeview(f3, selectmode='browse', height=34)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=150, anchor='c')
    treev.column("2", width=60, anchor='c')
    treev.column("3", width=60, anchor='c')
    treev.column("4", width=80, anchor='c')
    treev.column("5", width=80, anchor='c')
    treev.column("6", width=80, anchor='c')
    treev.column("7", width=80, anchor='c')
    treev.column("8", width=80, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="ADD_LINE_1")
    treev.heading("3", text="ADD_LINE_2")
    treev.heading("4", text="CITY")
    treev.heading("5", text="PINCODE")
    treev.heading("6", text="MOBILE")
    treev.heading("7", text="LIMIT_")
    treev.heading("8", text="TOTAL")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        if(float(s[7]) > float(s[6])):
            treev.insert("", 'end', values=s,tags=("outoflimit",))
        else:
            treev.insert("", 'end', values=s)
    treev.tag_configure('outoflimit', background='red',foreground="white")

    pass

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)
            f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
            f3.grid(row=0, column=2, rowspan=2, sticky="nsew")

            treev1 = ttk.Treeview(f3, selectmode='browse', height=34)
            treev1.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev1.configure(xscrollcommand=scrollbar.set)
            treev1.configure(xscrollcommand=scrollbar.set)
            treev1["columns"] = ("1", "2", "3","4")

            # Defining heading
            treev1['show'] = 'headings'

            # Assigning the width and anchor to  the
            # respective columns
            treev1.column("1", anchor='c')
            treev1.column("2", anchor='c')
            treev1.column("3", anchor='c')
            treev1.column("4", anchor='c')

            # Assigning the heading names to the
            # respective columns
            treev1.heading("1", text="BILLNO")
            treev1.heading("2", text="BUYER")
            treev1.heading("3", text="DATE")
            treev1.heading("4", text="TOTAL")
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            print(a[0])
            crsr.execute(f"SELECT * FROM billstock5 WHERE BUYER = '{a[0]}'")
            d = crsr.fetchall()
            connection.close()
            print(d)


            dict = {}
            for row in d:
                if row[0] not in dict:
                    dict[row[0]] = [row[1], row[7], row[9]]
                else:
                    tot = dict[row[0]][2]
                    dict[row[0]][2] = float(tot) + float(row[9])
            tes = dict.items()
            tes = list(tes)
            newres = []
            for i in tes:
                k = []
                j = list(i)
                k.append(j[0])
                for h in j[1]:
                    k.append(h)
                newres.append(k)

            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            print(a[0])
            crsr.execute(f"SELECT * FROM credittable WHERE NAME = '{a[0]}'")
            dome = crsr.fetchall()
            connection.close()
            print(dome)
            for erw in dome:
                s=[]
                if(erw[2] == 'CANCEL BILLED'):
                    s.append(f"CANCEL BILL {erw[1]}")
                else:
                    s.append('CREDIT')
                s.append(erw[0])
                s.append(erw[4])
                s.append(erw[3])
                newres.append(s)
            reswer=[]
            for s in newres:
                qwq = s[2].split('-')
                if (len(qwq[0]) == 1):
                    qwq[0] = '0' + qwq[0]
                if (len(qwq[1]) == 1):
                    qwq[1] = '0' + qwq[1]
                qwq.reverse()
                re = ''.join(qwq)
                s.append(re)
            reswer=sorted(newres,key=lambda x:x[4])
            print(reswer)
            for s in reswer:
                s.pop()
                treev1.insert("", 'end', values=s,tags=(s[0],))
            treev1.tag_configure('CREDIT',background='light green')


            def opencustbill(event):
                print("now show the new one")
                item = treev1.identify_row(event.y)
                if item:
                    a = treev1.item(item, 'values')
                    a = list(a)
                    if a[0]!="CREDIT":
                        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                        f3.grid(row=0, column=2, sticky="nsew")

                        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                        f4.grid(row=1, column=2, sticky="nsew")
                        treev2 = ttk.Treeview(f3, selectmode='browse', height=20)
                        treev2.pack(fill=BOTH)
                        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev2.xview)
                        scrollbar.pack(side=BOTTOM, fill=X)
                        treev2["columns"] = ("1", "2", "3", "4", "5", "6", "7")
                        treev2.configure(xscrollcommand=scrollbar.set)
                        treev2['show'] = 'headings'

                        treev2.column("1", anchor='c')
                        treev2.column("2", width=200, anchor='c')
                        treev2.column("3", width=80, anchor='c')
                        treev2.column("4", width=80, anchor='c')
                        treev2.column("5", width=80, anchor='c')
                        treev2.column("6", width=80, anchor='c')
                        treev2.column("7", width=80, anchor='c')
                        na = a[1]
                        na = na.upper()
                        connection = sqlite3.connect("mytables4.db")
                        crsr = connection.cursor()
                        crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                        sel = crsr.fetchall()
                        connection.close()
                        sel = list(sel[0])
                        r1 = ("NAME", sel[0], "", "BILLNO", a[0], "", "")
                        r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
                        r3 = ("ADD2", sel[2], "", "DATE", a[2], "", "")
                        treev2.insert("", 'end', values=r1)
                        treev2.insert("", 'end', values=r2)
                        treev2.insert("", 'end', values=r3)
                        r31 = ("", "", "", "", "", "", "")
                        treev2.insert("", 'end', values=r31)

                        connection = sqlite3.connect("mytables4.db")
                        crsr = connection.cursor()
                        crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNo ='{a[0]}'")
                        d = crsr.fetchall()
                        connection.close()
                        total = []
                        for i in d:
                            listforinsert = []
                            listforinsert.append(i[2])
                            listforinsert.append(i[3])
                            listforinsert.append(i[4])
                            listforinsert.append(i[5])
                            listforinsert.append(i[6])
                            listforinsert.append(i[8])
                            listforinsert.append(i[9])
                            total.append(int(i[9]))
                            print(listforinsert)
                            treev2.insert("", 'end', values=listforinsert)
                        r312 = ("", "", "", "", "", "", "")
                        treev2.insert("", 'end', values=r312)
                        r32 = ("", "", "", "", "", "", "")
                        treev2.insert("", 'end', values=r32)
                        r33 = ("", "", "", "", "TOTAL", "", sum(total))
                        treev2.insert("", 'end', values=r33, tags=('tot',))
                        treev2.tag_configure('tot', background='light blue')
                    else:
                        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                        f4.grid(row=1, column=2, sticky="nsew")
                        connection = sqlite3.connect("mytables4.db")
                        crsr = connection.cursor()
                        crsr.execute(f"SELECT * FROM credittable WHERE NAME = '{a[1]}' AND AMOUNT = '{a[3]}' AND DATE ='{a[2]}'")
                        damw = crsr.fetchall()
                        connection.close()
                        print(damw)
                        dawn=list(damw[0])
                        l1 = Label(f4, text=f"NAME", width=8)
                        l1.grid(row=0, column=0, padx=5, pady=5)
                        e1 = Entry(f4)
                        e1.grid(row=0, column=1)
                        l2 = Label(f4, text="TYPE", padx=5, width=8)
                        l2.grid(row=1, column=0, padx=5, pady=5)
                        e2 = Entry(f4)
                        e2.grid(row=1, column=1)
                        l3 = Label(f4, text="TRANSAC. NO", padx=5, width=8)
                        l3.grid(row=2, column=0, padx=5, pady=5)
                        e3 = Entry(f4)
                        e3.grid(row=2, column=1)
                        l4 = Label(f4, text="AMOUNT", padx=5, width=8)
                        l4.grid(row=0, column=2, padx=5, pady=5)
                        e4 = Entry(f4)
                        e4.grid(row=0, column=3)
                        l5 = Label(f4, text="DATE", padx=5, width=8)
                        l5.grid(row=1, column=2, padx=5, pady=5)
                        e5 = Entry(f4)
                        e5.grid(row=1, column=3)
                        e1.insert(0,dawn[0])
                        e2.insert(0,dawn[1])
                        e3.insert(0,dawn[2])
                        e4.insert(0,dawn[3])
                        e5.insert(0,dawn[4])


                        pass

                pass

            treev1.bind("<Double-Button-1>", opencustbill)
        else:
            print("Nothing it have")

        pass

    treev.bind("<Double-Button-1>", clickedrow)


def showbill(event):
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM billstock5")
    d = crsr.fetchall()
    connection.close()
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack(fill=X)

    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3","4")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", anchor='c')
    treev.column("2", anchor='c')
    treev.column("3", anchor='c')
    treev.column("4", anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="BILLNO")
    treev.heading("2", text="BUYER")
    treev.heading("3", text="DATE")
    treev.heading("4", text="TOTAL")

    # # showing bill only one time
    # res = []
    # for row in d:
    #     s = []
    #     s.append(row[0])
    #     s.append(row[1])
    #     s.append(row[7])
    #     s.append(row[9])
    #     res.append(s)
    # newres = []
    # #we need to comment this out
    # for row in res:
    #     if row not in newres:
    #         newres.append(row)
    # #till here
    # for s in newres:
    #     treev.insert("", 'end', values=s)

    dict={}
    for row in d:
        if row[0] not in dict:
            dict[row[0]] = [row[1],row[7],row[9]]
        else:
            tot=dict[row[0]][2]
            dict[row[0]][2]=float(tot) + float(row[9])
    tes=dict.items()
    tes=list(tes)
    newres=[]
    for i in tes:
        k=[]
        j=list(i)
        k.append(j[0])
        for h in j[1]:
            k.append(h)
        newres.append(k)

    for s in newres:
        if '-' in s[0]:
            treev.insert("", 'end', values=s,tags=('cancelbill',))
        else:
            treev.insert("", 'end', values=s)
    treev.tag_configure('cancelbill', background='red',foreground='white')

    def clickedrow(event):
        print("now show the new one")
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)
            f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
            f3.grid(row=0, column=2, sticky="nsew")
            treev1 = ttk.Treeview(f3, selectmode='browse', height=20)
            treev1.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev1["columns"] = ("1", "2", "3", "4", "5", "6", "7")
            treev1.configure(xscrollcommand=scrollbar.set)
            treev1['show'] = 'headings'

            treev1.column("1", anchor='c')
            treev1.column("2", width=200, anchor='c')
            treev1.column("3", width=80, anchor='c')
            treev1.column("4", width=80, anchor='c')
            treev1.column("5", width=80, anchor='c')
            treev1.column("6", width=80, anchor='c')
            treev1.column("7", width=80, anchor='c')
            na = a[1]
            na = na.upper()
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
            r1 = ("NAME", sel[0], "", "BILLNO", a[0], "", "")
            r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
            r3 = ("ADD2", sel[2], "", "DATE", a[2], "", "")
            treev1.insert("", 'end', values=r1)
            treev1.insert("", 'end', values=r2)
            treev1.insert("", 'end', values=r3)
            r31 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r31)

            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNo ='{a[0]}'")
            d = crsr.fetchall()
            connection.close()
            total = []
            for i in d:
                listforinsert = []
                listforinsert.append(i[2])
                listforinsert.append(i[3])
                listforinsert.append(i[4])
                listforinsert.append(i[5])
                listforinsert.append(i[6])
                listforinsert.append(i[8])
                listforinsert.append(i[9])
                try:
                    total.append(int(i[9]))
                except Exception as e:
                    print(e)
                print(listforinsert)
                treev1.insert("", 'end', values=listforinsert)
            r312 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r312)
            r32 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r32)
            r33 = ("", "", "", "", "TOTAL", "", sum(total))
            treev1.insert("", 'end', values=r33, tags=('tot',))
            treev1.tag_configure('tot', background='light blue')

        pass

    treev.bind("<Double-Button-1>", clickedrow)
    pass


def createbilltable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            BILLNO VARCHAR(40),
            BUYER VARCHAR(40),
            BUNDLENO VARCHAR(40),
            PRODUCT VARCHAR(40),
            SIZE VARCHAR(40),
            PCS VARCHAR(30),
            KG VARCHAR(30),
            DATE VARCHAR(40),
            RATE VARCHAR(30),
            TOTAL VARCHAR(30));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()


def createbillnotable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            NAME VARCHAR(30),
            BILLNO VARCHAR(30));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()


def createcredittable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            NAME VARCHAR(30),
            TYPE VARCHAR(30),
            TRANSACTION_NO VARCHAR(30),
            AMOUNT VARCHAR(30),
            DATE VARCHAR(30));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()

def addpayment(event):
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    connection.close()


    namelist = []
    for i in d:
        namelist.append(i[0])
    namelist = sorted(namelist)
    drop = ttk.Combobox(f4, values=namelist)
    drop.pack()


    def keydown(e):
        ba = drop.get()
        a = ba.upper()
        checklist = []
        for i in namelist:
            if a in i:
                checklist.append(i)
        drop["values"] = checklist


    def keyup(e):
        drop.event_generate("<Down>")

    def contin():
        f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
        f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
        # here we will create the bill

        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        name=drop.get()
        l1 = Label(f4, text=f"{name}", width=8)
        l1.grid(row=0, column=0,columnspan=2, padx=5, pady=5)

        l2 = Label(f4, text="TYPE", padx=5, width=8)
        l2.grid(row=1, column=0, padx=5, pady=5)
        e2 = Entry(f4)
        e2.grid(row=1, column=1)
        l3 = Label(f4, text="TRANSAC. NO", padx=5, width=8)
        l3.grid(row=2, column=0, padx=5, pady=5)
        e3 = Entry(f4)
        e3.grid(row=2, column=1)
        l4 = Label(f4, text="AMOUNT", padx=5, width=8)
        l4.grid(row=0, column=2, padx=5, pady=5)
        e4 = Entry(f4)
        e4.grid(row=0, column=3)
        l5 = Label(f4, text="DATE", padx=5, width=8)
        l5.grid(row=1, column=2, padx=5, pady=5)
        e5 = Entry(f4)
        e5.grid(row=1, column=3)
        def savecredit():
            connection = sqlite3.connect("mytables4.db")
            cursor = connection.cursor()
            asd=[]
            asd.append(name)
            asd.append(e2.get())
            asd.append(e3.get())
            try:
                we=float(e4.get())
                asd.append(we)
            except Exception as e:
                asd.append('0')
            try:
                we=e5.get()
                qw=we.split('-')
                if(len(qw)==3):
                    asd.append(e5.get())
                else:
                    tsmg.showinfo("wrong","wrong date format")
                    addpayment(event)
            except Exception as e:
                print(e)

            sa = f'''INSERT INTO credittable VALUES ("{asd[0]}","{asd[1]}","{asd[2]}","{asd[3]}","{asd[4]}")'''
            try:
                cursor.execute(sa)
                connection.commit()
                connection.close()
                connection = sqlite3.connect('mytables4.db')
                conn = connection.cursor()
                conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{name}'")
                sele = conn.fetchall()
                selecate = list(sele[0])
                total = float(selecate[7])
                newtotal = total - float(asd[3])
                conn.execute(f"UPDATE custom9 SET TOTAL = '{newtotal}' where NAME='{name}'")

                connection.commit()
                connection.close()
                tsmg.showinfo("successful","your credis has been saved")
                addpayment(event)

            except Exception as e:
                tsmg.showinfo("warning !","something went wrong")
                print(e)
                addpayment(event)


            pass



        Button(f4, text="SAVE CREDIT", command=savecredit).grid(row=2, column=2,columnspan=2, padx=25)
        pass


    drop.bind("<KeyRelease>", keydown)
    drop.bind("<Return>", keyup)
    Button(f4, text="UPDATE CUSTOMER", command=contin).pack(pady=30)




    pass



def showpayments(events):
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM credittable")
    d = crsr.fetchall()
    connection.close()
    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack()
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", anchor='c')
    treev.column("2", anchor='c')
    treev.column("3", anchor='c')
    treev.column("4", anchor='c')
    treev.column("5", anchor='c')


    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="TYPE")
    treev.heading("3", text="TRANSACTION NO")
    treev.heading("4", text="AMOUNT")
    treev.heading("5", text="DATE")
    for r in d:
        treev.insert("",'end',values=r)

    pass



def createbill(event):
    # tablename="billstock5"
    # createbilltable(tablename)
    # billtablename="billno9"
    # createbillnotable(billtablename)
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
    f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    connection.close()

    namelist = []
    for i in d:
        namelist.append(i[0])
    namelist = sorted(namelist)
    drop = ttk.Combobox(f4, values=namelist)
    drop.pack()

    def keydown(e):
        ba = drop.get()
        a = ba.upper()
        checklist = []
        for i in namelist:
            if a in i:
                checklist.append(i)
        drop["values"] = checklist

    def keyup(e):
        drop.event_generate("<Down>")

    def contin():
        billbundlelist = []
        bnolist = []
        poplino=0
        f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
        f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
        # here we will create the bill

        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")

        treev = ttk.Treeview(f3, selectmode='browse', height=20)
        treev.pack(fill=BOTH)
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        treev.configure(xscrollcommand=scrollbar.set)
        treev['show'] = 'headings'

        treev.column("1", anchor='c')
        treev.column("2", width=200, anchor='c')
        treev.column("3", width=80, anchor='c')
        treev.column("4", width=80, anchor='c')
        treev.column("5", width=80, anchor='c')
        treev.column("6", width=80, anchor='c')
        treev.column("7", width=80, anchor='c')

        try:
            na = drop.get()
            na = na.upper()
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
        except Exception as eas:
            tsmg.showinfo("Error !", "Wrong name entered")
            createbill(event)

        # we will fatch bundle no now
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM billno9")
        w = crsr.fetchall()
        connection.close()
        wai = list(w[0])
        billno = wai[1]
        # remember to upgrade bill no
        r1 = ("NAME", sel[0], "", "BILLNO", billno, "", "")
        r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
        r3 = ("ADD2", sel[2], "", "", "", "", "")
        treev.insert("", 'end', values=r1)
        treev.insert("", 'end', values=r2)
        treev.insert("", 'end', values=r3)
        r31 = ("", "", "", "", "", "", "")
        treev.insert("", 'end', values=r31)

        def check():

            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{ese.get()}';")
            w = crsr.fetchall()
            if (len(w) == 0):

                f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
                pass

            else:
                d = list(w[0])
                connection.close()
                if (d[12] != "SOLD"):
                    f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                    f4.grid(row=1, column=2, sticky="nsew")
                    l1 = Label(f4, text="Bundle type", width=8)
                    l1.grid(row=0, column=0, padx=5, pady=5)
                    e1 = Entry(f4)
                    e1.grid(row=0, column=1)
                    l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
                    l2.grid(row=1, column=0, padx=5, pady=5)
                    e2 = Entry(f4)
                    e2.grid(row=1, column=1)
                    l3 = Label(f4, text="THK REMARK", padx=5, width=8)
                    l3.grid(row=2, column=0, padx=5, pady=5)
                    e3 = Entry(f4)
                    e3.grid(row=2, column=1)
                    l4 = Label(f4, text="BUNDLE", padx=5, width=8)
                    l4.grid(row=3, column=0, padx=5, pady=5)
                    e4 = Entry(f4)
                    e4.grid(row=3, column=1)
                    l5 = Label(f4, text="COVER", padx=5, width=8)
                    l5.grid(row=4, column=0, padx=5, pady=5)
                    e5 = Entry(f4)
                    e5.grid(row=4, column=1)
                    l6 = Label(f4, text="STM", padx=5, width=8)
                    l6.grid(row=0, column=5, padx=5, pady=5)
                    e6 = Entry(f4)
                    e6.grid(row=0, column=6)
                    l7 = Label(f4, text="R2", padx=5, width=8)
                    l7.grid(row=0, column=3, padx=20, pady=5)
                    e7 = Entry(f4)
                    e7.grid(row=0, column=4)
                    l8 = Label(f4, text="PCS", padx=5, width=8)
                    l8.grid(row=1, column=3, padx=5, pady=5)
                    e8 = Entry(f4)
                    e8.grid(row=1, column=4)
                    l9 = Label(f4, text="MM", padx=5, width=8)
                    l9.grid(row=2, column=3, padx=5, pady=5)
                    e9 = Entry(f4)
                    e9.grid(row=2, column=4)
                    l10 = Label(f4, text="KGS", padx=5, width=8)
                    l10.grid(row=3, column=3, padx=5, pady=5)
                    e10 = Entry(f4)
                    e10.grid(row=3, column=4)
                    l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
                    l11.grid(row=4, column=3, padx=5, pady=5)
                    e11 = Entry(f4)
                    e11.grid(row=4, column=4)
                    l14 = Label(f4, text="TOTAL", padx=5, width=8)
                    l14.grid(row=3, column=5, padx=5, pady=5)
                    e14 = Entry(f4)
                    e14.grid(row=3, column=6)
                    l12 = Label(f4, text="RATE", padx=5, width=8)
                    l12.grid(row=2, column=5, padx=5, pady=5)
                    e12 = Entry(f4)
                    e12.grid(row=2, column=6)
                    l13 = Label(f4, text="STATUS", padx=5, width=8)
                    l13.grid(row=1, column=5, padx=20, pady=5)
                    e13 = Entry(f4)
                    e13.grid(row=1, column=6, padx=5, pady=5)
                    e1.insert(0, d[0])
                    e2.insert(0, d[1])
                    e3.insert(0, d[2])
                    e4.insert(0, d[3])
                    e5.insert(0, d[4])
                    e6.insert(0, d[5])
                    e7.insert(0, d[6])
                    e8.insert(0, d[7])
                    e9.insert(0, d[8])
                    e10.insert(0, d[9])
                    e11.insert(0, d[10])
                    e13.insert(0, d[12])

                    def addtobill():
                        nonlocal poplino
                        poplino=1
                        r4 = []
                        r4.append(d[3])
                        r4.append(d[0])
                        r4.append(d[1])
                        r4.append(d[7])
                        r4.append(d[9])
                        if e12.get() == '':
                            r4.append('0')
                        else:
                            try:
                                ew=e12.get()
                                eew = float(ew)
                                r4.append(int(eew))
                            except Exception as e:
                                print(e)
                                r4.append('0')
                                tsmg.showinfo("info","sorry wrong input price")

                        if e14.get() == '':
                            r4.append('0')
                        else:
                            try:
                                ew1=e14.get()
                                eew1= float(ew1)
                                r4.append(int(eew1))
                            except Exception as e:
                                r4.append('0')
                                tsmg.showinfo("info", "sorry wrong input price")
                        r5 = []

                        r5 = r4.copy()
                        r5.insert(0, billno)
                        if r5 not in billbundlelist:
                            treev.insert("", 'end', values=r4)
                            billbundlelist.append(r5)
                            bnolist.append(d[3])
                        else:
                            tsmg.showinfo("info","bundle no already in the bill")

                    b4 = Button(f2, text="SAVE BILL")
                    b4.pack(pady=150)

                    def savebill(event):
                        nonlocal poplino
                        if poplino == 0 :
                            print("nothing entered")
                            tsmg.showinfo("alert","no entry")
                            createbill(event)

                        else:
                            f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
                            f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

                            today = date.today()
                            datetoday = today.strftime("%d-%m-%Y")
                            bnolist1 = list(set(bnolist))
                            conn = sqlite3.connect('mytables4.db')
                            for i in bnolist1:
                                conn.execute(f"UPDATE stockfinal634 SET STATUS = 'SOLD' where BUNDLE='{i}'")
                                conn.commit()
                            conn.close()
                            # now will update bill no
                            connection = sqlite3.connect('mytables4.db')
                            conn = connection.cursor()
                            conn.execute("SELECT * FROM billno9 WHERE NAME = '1'")
                            temp = conn.fetchall()
                            tempno = int(temp[0][1])
                            tempno = tempno + 1
                            conn.execute(f"UPDATE billno9 SET BILLNO = '{tempno}' where NAME='1'")
                            connection.commit()
                            connection = sqlite3.connect("mytables4.db")
                            cursor = connection.cursor()
                            print(billbundlelist)
                            print("check")
                            for i in billbundlelist:
                                i.insert(6, datetoday)
                                i.append(sel[0])
                                print(i)
                                sa = f'''INSERT INTO billstock5 VALUES ("{i[0]}","{i[9]}","{i[1]}","{i[2]}","{i[3]}","{i[4]}","{i[5]}","{i[6]}","{i[7]}","{i[8]}")'''
                                cursor.execute(sa)
                                connection.commit()
                            connection.close()

                            file = open('bill_location.txt', 'r')
                            for e in file:
                                mainloc = e
                            workbook = xlsxwriter.Workbook(f'{mainloc}{billbundlelist[0][0]}.xlsx')
                            worksheet = workbook.add_worksheet()
                            bold = workbook.add_format({'bold': True})

                            connection = sqlite3.connect("mytables4.db")
                            crsr = connection.cursor()
                            crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO = '{billbundlelist[0][0]}'")
                            w = crsr.fetchall()
                            connection.close()
                            d = list(w[0])
                            print(d[1])
                            na = d[1]
                            connection = sqlite3.connect("mytables4.db")
                            crsr = connection.cursor()
                            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                            selec = crsr.fetchall()
                            connection.close()
                            selec = list(selec[0])
                            worksheet.set_column('A:A', 10)
                            worksheet.set_column('B:B', 30)
                            worksheet.set_column('C:C', 30)

                            worksheet.write(0, 0, "NAME")
                            worksheet.write(0, 1, selec[0])
                            worksheet.write(1, 0, "ADD1")
                            worksheet.write(1, 1, selec[1])
                            worksheet.write(2, 0, "ADD2")
                            worksheet.write(2, 1, selec[2])
                            worksheet.write(0, 2, "BILLNO")
                            worksheet.write(0, 3, temp[0][1])
                            worksheet.write(1, 2, "MOBILENO")
                            worksheet.write(1, 3, selec[5])
                            worksheet.write(2, 2, "DATE")
                            worksheet.write(2, 3, d[7])
                            num = 3
                            worksheet.write(num, 0, "BUNDLENO", bold)
                            worksheet.write(num, 1, "PRODUCT", bold)
                            worksheet.write(num, 2, "SIZE", bold)
                            worksheet.write(num, 3, "PCS", bold)
                            worksheet.write(num, 4, "KG", bold)
                            worksheet.write(num, 5, "RATE", bold)
                            worksheet.write(num, 6, "TOTAL", bold)
                            num = 4
                            total = []
                            for i in w:
                                num += 1
                                worksheet.write(num, 0, i[2])
                                worksheet.write(num, 1, i[3])
                                worksheet.write(num, 2, i[4])
                                worksheet.write(num, 3, i[5])
                                worksheet.write(num, 4, i[6])
                                worksheet.write(num, 5, i[8])
                                worksheet.write(num, 6, i[9])
                                total.append(int(i[9]))
                            worksheet.write(num + 2, 5, "TOTAL", bold)
                            worksheet.write(num + 2, 6, str(sum(total)), bold)
                            totka=sum(total)

                            workbook.close()



                            connection = sqlite3.connect('mytables4.db')
                            conn = connection.cursor()
                            conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                            sele = conn.fetchall()
                            selecate = list(sele[0])
                            total=float(selecate[7])
                            newtotal=total +totka
                            conn.execute(f"UPDATE custom9 SET TOTAL = '{newtotal}' where NAME='{na}'")

                            connection.commit()
                            connection.close()

                            tsmg.showinfo("Saved", "Your bill has been saved successfully")




                            createbill(event)
                            pass

                    b4.bind('<Button-1>', savebill)
                    var1 = IntVar()

                    def mixcheck():
                        print(var1.get())
                        if (var1.get() == 1):
                            # errorcanoccur
                            e14.delete(0, END)
                            tot = float(e12.get()) * float(e10.get())
                            e14.insert(0, int(tot))
                        else:
                            # errorcanoccur
                            e14.delete(0, END)
                            tot = float(e12.get()) * float(e8.get())
                            e14.insert(0, int(tot))

                    Checkbutton(f4, text="BY KG", variable=var1, command=mixcheck).grid(row=4, column=5, padx=25)
                    Button(f4, text="ADD TO BILL", command=addtobill).grid(row=4, column=6, padx=25)
                else:
                    f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                    f4.grid(row=1, column=2, sticky="nsew")
                    Button(f4, text="ALREADY SOLD").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

            pass

        #new edit
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634")
        w = crsr.fetchall()
        connection.close()
        bunlis = []
        for i in w:
            bunlis.append(i[3])


        l = Label(f2, text="BUNDLE NO", width=8)
        l.pack(pady=5)
        ese = ttk.Combobox(f2, values=bunlis,width=10)
        ese.pack(pady=5)

        def keydown(event):
            ba = ese.get()
            a = ba.upper()
            checklist = []
            for i in bunlis:
                if a in i:
                    checklist.append(i)
            ese["values"] = checklist

        ese.bind("<KeyRelease>", keydown)

        def keyup(event):
            ese.event_generate("<Down>")

        ese.bind("<Return>", keyup)

        Button(f2, text="SEARCH", command=check).pack(pady=10)

    pass
    drop.bind("<KeyRelease>", keydown)
    drop.bind("<Return>", keyup)
    Button(f4, text="UPDATE CUSTOMER", command=contin).pack(pady=30)

    pass


def billallexcel(event):
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM billstock5 ")
    d = crsr.fetchall()
    connection.close()
    print(d)
    # ['CREDIT', 'EWRS', '10-11-2019', '30000.0']
    workbook = xlsxwriter.Workbook('BILLLIST.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    alpa = ['BILLNO', 'BUYER', 'BUNDLE', 'TYPE', 'DIMENSION', 'PCS', 'KG', 'DATE', 'RATE', 'TOTAL']

    d1 = d
    d1.insert(0, alpa)
    for i in range(len(d1)):
        d1[i] = list(d1[i])
    for i in range(len(d1)):
        for j in range(len(d1[0])):
            if (i == 0):
                worksheet.write(i, j, f'''{d1[i][j]}''', bold)
            else:
                worksheet.write(i, j, f'''{d1[i][j]}''')
    worksheet.set_column(2, 3, 25)
    worksheet.set_column(4, 4, 20)
    worksheet.set_column(7, 7, 15)
    worksheet.set_column(10, 12, 15)
    workbook.close()
    tsmg.showinfo("converted","created a file name BILLLIST")


def exportbill(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l = Label(f4, text="BILL NUMBER", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.grid(row=0, column=1)

    def check():
        try:
            #we will create a folder to store bill
            file = open('bill_location.txt', 'r')
            for e in file:
                mainloc = e
            workbook = xlsxwriter.Workbook(f'{mainloc}{e1.get()}.xlsx')
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})

            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO = '{e1.get()}'")
            w = crsr.fetchall()
            connection.close()
            d = list(w[0])
            print(d[1])
            na = d[1]
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
            worksheet.set_column('A:A', 10)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 30)

            worksheet.write(0, 0, "NAME")
            worksheet.write(0, 1, sel[0])
            worksheet.write(1, 0, "ADD1")
            worksheet.write(1, 1, sel[1])
            worksheet.write(2, 0, "ADD2")
            worksheet.write(2, 1, sel[2])
            worksheet.write(0, 2, "BILLNO")
            worksheet.write(0, 3, e1.get())
            worksheet.write(1, 2, "MOBILENO")
            worksheet.write(1, 3, sel[5])
            worksheet.write(2, 2, "DATE")
            worksheet.write(2, 3, d[7])
            num = 3
            worksheet.write(num, 0, "BUNDLENO", bold)
            worksheet.write(num, 1, "PRODUCT", bold)
            worksheet.write(num, 2, "SIZE", bold)
            worksheet.write(num, 3, "PCS", bold)
            worksheet.write(num, 4, "KG", bold)
            worksheet.write(num, 5, "RATE", bold)
            worksheet.write(num, 6, "TOTAL", bold)
            num = 4
            total = []
            for i in w:
                num += 1
                worksheet.write(num, 0, i[2])
                worksheet.write(num, 1, i[3])
                worksheet.write(num, 2, i[4])
                worksheet.write(num, 3, i[5])
                worksheet.write(num, 4, i[6])
                worksheet.write(num, 5, i[8])
                worksheet.write(num, 6, i[9])
                total.append(int(i[9]))
            worksheet.write(num + 2, 5, "TOTAL", bold)
            worksheet.write(num + 2, 6, str(sum(total)), bold)

            workbook.close()
            tsmg.showinfo("CREATED", "File has been created")
            exportbill(event)
        except Exception as e:
            tsmg.showinfo("Oops!", "Something went wrong ")
            exportbill(event)
            print(e)

    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def updatebill(event):
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l = Label(f4, text="BILL NUMBER", width=10)
    l.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.grid(row=0, column=1)
    def upbill():
        f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        qwwq=e1.get()
        qwerewq=qwwq.split('-')
        print(qwerewq)
        if(len(qwerewq)==1):
            crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO= '{e1.get()}'")
            d = crsr.fetchall()
            connection.close()
            print(d)

            treev1 = ttk.Treeview(f3, selectmode='browse', height=20)
            treev1.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev1["columns"] = ("1", "2", "3", "4", "5", "6", "7")
            treev1.configure(xscrollcommand=scrollbar.set)
            treev1['show'] = 'headings'

            treev1.column("1", anchor='c')
            treev1.column("2", width=200, anchor='c')
            treev1.column("3", width=80, anchor='c')
            treev1.column("4", width=80, anchor='c')
            treev1.column("5", width=80, anchor='c')
            treev1.column("6", width=80, anchor='c')
            treev1.column("7", width=80, anchor='c')
            na = d[0][1]
            na = na.upper()
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
            r1 = ("NAME", sel[0], "", "BILLNO", d[0][0], "", "")
            r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
            r3 = ("ADD2", sel[2], "", "DATE", d[0][7], "", "")
            treev1.insert("", 'end', values=r1)
            treev1.insert("", 'end', values=r2)
            treev1.insert("", 'end', values=r3)
            r31 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r31)

            de=d.copy()
            total = []
            for i in de:
                listforinsert = []
                listforinsert.append(i[2])
                listforinsert.append(i[3])
                listforinsert.append(i[4])
                listforinsert.append(i[5])
                listforinsert.append(i[6])
                listforinsert.append(i[8])
                listforinsert.append(i[9])
                try:
                    total.append(int(i[9]))
                except Exception as e:
                    print(e)
                print(listforinsert)
                treev1.insert("", 'end', values=listforinsert)
            r312 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r312)
            r32 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r32)
            r33 = ("", "", "", "", "TOTAL", "", sum(total))
            treev1.insert("", 'end', values=r33, tags=('tot',))
            treev1.tag_configure('tot', background='light blue')

            def changedate():
                f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                l = Label(f4, text="ENTER NEW DATE", width=15)
                l.grid(row=0, column=0, padx=5, pady=5)
                e12 = Entry(f4)
                e12.grid(row=0, column=1)
                def face():
                    dat = e12.get()
                    qwq = dat.split('-')
                    if (len(qwq) == 3):
                        # UPDATE DATE
                        connection = sqlite3.connect('mytables4.db')
                        connection.execute(f"UPDATE billstock5 SET DATE = '{dat}' where BILLNO='{d[0][0]}'")
                        connection.commit()
                        connection.close()
                        tsmg.showinfo("completed", "DATE CHANGED")
                        showbill(event)

                    else:
                        tsmg.showinfo("Wrong", "Wrong date entered")


                Button(f4, text="CHANGE DATE", command=face).grid(row=1, column=0, columnspan=2)


                pass
            Button(f4, text="CHANGE DATE", command=changedate).grid(row=1, column=0, columnspan=2,padx=150)


            def cancelbill():
                chos = tsmg.askquestion("sure!", "Are you sure you want to cancel bill")
                if chos == "yes":
                    try:
                        kite=[]
                        totka=total
                        for i in de:
                            kite.append(i[2])
                        conn = sqlite3.connect('mytables4.db')
                        for i in kite:
                            conn.execute(f"UPDATE stockfinal634 SET STATUS = 'INSTOCK' where BUNDLE='{i}'")
                            conn.commit()
                        conn.close()
                        connection = sqlite3.connect('mytables4.db')
                        conn = connection.cursor()
                        conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                        sele = conn.fetchall()
                        selecate = list(sele[0])
                        totale = float(selecate[7])
                        new_tot = totale - float(sum(totka))
                        conn.execute(f"UPDATE custom9 SET TOTAL = '{new_tot}' where NAME='{na}'")
                        connection.commit()
                        connection.close()
                        connection = sqlite3.connect("mytables4.db")
                        cursor = connection.cursor()
                        sa = f'''INSERT INTO credittable VALUES ("{na}","C-{de[0][0]}","CANCEL BILLED","{sum(totka)}","{de[0][7]}")'''
                        cursor.execute(sa)
                        connection.commit()
                        connection.close()

                        connection = sqlite3.connect('mytables4.db')
                        connection.execute(f"UPDATE billstock5 SET BILLNO = 'C-{d[0][0]}' where BILLNO='{d[0][0]}'")
                        connection.commit()
                        connection.close()
                        tsmg.showinfo("Completed","your bill has been canceled")
                        updatebill(event)
                    except Exception as e:
                        print(e)
                        tsmg.showinfo("error",f"{e}")
                        updatebill(event)

                pass
            Button(f4, text="CANCEL BILL", command=cancelbill).grid(row=1, column=5, columnspan=2,padx=150)
        else:
            tsmg.showinfo("Sorry","Can't update cancelled bill ! ")
            updatebill(event)
    Button(f4, text="UPDATE BILL", command=upbill).grid(row=1,column=0,columnspan=2)


    pass


def f2f4destroy(event):
    t = event.widget.cget("text")
    f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
    f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

    if (t == "ADDED"):
        b1 = Button(f2, text="  BUNDLE ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", addbundle)
        b2 = Button(f2, text="PACKING LIST", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", addpacking)
        b3 = Button(f2, text="IMPORT EXCEL", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", importfromexcel)
        b4 = Button(f2, text="SPLIT BUN.", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", splitbundle)

    elif (t == "SEARCH"):
        b1 = Button(f2, text="  BY PL ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", searchpl)

        b2 = Button(f2, text="BY BUNDLE NO.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", searchbundleno)

        b3 = Button(f2, text="  BY NAME ", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", searchbundlename)

    elif (t == "DELETE"):
        b1 = Button(f2, text="PACKING LIST", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", deletepacking)

        b2 = Button(f2, text="BUNDLE", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", deletebundle)

    elif (t == "UPDATE"):
        b1 = Button(f2, text="BUNDLE NO. ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", updatebundleno)
        b2 = Button(f2, text="SHOW STOCK", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", showstock)

    elif (t == "SELL"):
        # even function name not created
        b1 = Button(f2, text="SHOW BILL", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", showbill)
        b2 = Button(f2, text="CREAT BILL", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", createbill)
        b3 = Button(f2, text="EXPORT BILL", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", exportbill)
        b4 = Button(f2, text="UPDATE BILL", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", updatebill)
        b5 = Button(f2, text="ALL EXCEL", bg="white")
        b5.pack(pady=50)
        b5.bind("<Button-1>", billallexcel)



    elif (t == "CUSTOMER"):
        b1 = Button(f2, text="ADD CUSTO.", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", addcustomer)

        b2 = Button(f2, text="UPDATE CUST.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", updatecustomer)

        b3 = Button(f2, text="SHOW CUSTO.", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", showcustomer)

        b4 = Button(f2, text="ADD PAY.", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", addpayment)

        b4 = Button(f2, text="PAYMENTS", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", showpayments)
    else:
        pass

try:
    qwe = "credittable"
    createcredittable(qwe)
    tablename = "stockfinal634"
    createtable(tablename)
    sat = "custom9"
    createcustomertable(sat)


    tablename = "billstock5"
    createbilltable(tablename)
    billtablename = "billno9"
    createbillnotable(billtablename)
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sa = f'''INSERT INTO billno9 VALUES ('1','1')'''
    cursor.execute(sa)
    connection.commit()
    tsmg.showinfo("Setup","Create a folder where you want to save bill")
    chos=tsmg.askquestion("Created","if created click yes and select it from file")
    if chos=="yes":
        mainloc = filedialog.askdirectory()
        file = open('bill_location.txt', 'w')
        file.write(f"{mainloc}/")
        file.close()

except Exception as e:
    file = open('bill_location.txt', 'r')
    for each in file:
        mainloc = each
    print(e)
    b1 = Button(f1, text="ADDED", bg="white")
    b1.pack(pady=25, padx=10, anchor="w")
    b1.bind("<Button-1>", f2f4destroy)

    b2 = Button(f1, text="SEARCH")
    b2.pack(pady=25, padx=10, anchor="w")
    b2.bind("<Button-1>", f2f4destroy)

    b3 = Button(f1, text="DELETE", bg="white")
    b3.pack(pady=25, padx=10, anchor="w")
    b3.bind("<Button-1>", f2f4destroy)

    b4 = Button(f1, text="UPDATE", bg="white")
    b4.pack(pady=25, padx=10, anchor="w")
    b4.bind("<Button-1>", f2f4destroy)

    b4 = Button(f1, text="SELL", bg="white")
    b4.pack(pady=25, padx=15, anchor="w")
    b4.bind("<Button-1>", f2f4destroy)

    b5 = Button(f1, text="CUSTOMER", bg="white")
    b5.pack(pady=25, anchor="w")
    b5.bind("<Button-1>", f2f4destroy)

root.mainloop()