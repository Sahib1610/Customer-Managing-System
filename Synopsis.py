import tkinter as tk
import sys
import tkcalendar as tkc
import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import messagebox as mb
from tkinter import ttk

def NewWin():
    def open_calendar():
        def select_date():
            global selected_date
            selected_date = cal.get_date()
            date_enter.config(text=selected_date+u"\u25BC")
            top.destroy()

        global top
        top = tk.Toplevel(window1)
        cal = tkc.Calendar(top, selectmode="day")
        cal.pack()
        button = tk.Button(top, text="Select Date", command=select_date)
        button.pack()
    def SAVE():
        folder_path = 'Data/'
        file_name = name_enter.get() + ".csv"
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            mb.showerror("Error","Name Already Exists!" )
        else:
            if CASH.get() == 1:
                a = "Cash"
            if UPI.get() == 1:
                a = "UPI"
            if CARD.get() == 1:
                a = "Card"
            if WALLET.get() == 1:
                a = "Wallet"
            if OTHER.get() == 1:
                a = "Other"
            DATE = selected_date
            a = pd.read_csv("Items.csv")
            b = a.set_index("Item").T.to_dict("list")
            c = b.get(item_enter.get())
            d = int(price_enter.get()) - c[0]
            e,f,g = DATE.split(sep="/")
            Name = "Data/" + name_enter.get() + ".csv"
            Name1 = "Default_Ph_No/"+name_enter.get()+"No.csv"
            Date_Sort = "Profit/Date/"+e+"_"+f+"_"+g+".csv"
            Month_Sort= "Profit/Month/"+e+"_"+g+".csv"
            Year_Sort = "Profit/Year/"+g+".csv"
            df = pd.DataFrame({"Item": [item_enter.get()], "ItemNo.": [item_no_enter.get()], "Price": [price_enter.get()], "PhoneNo.":[p_no_enter.get()],"MOP": [a],"Date": [DATE],"Tax":tax_enter.get()})
            df.to_csv(Name, index=False)
            df1= pd.DataFrame({"Name":[name_enter.get()],"PhNo.":[p_no_enter.get()]})
            df1.to_csv(Name1,index=False)
            df2_1 = pd.DataFrame({"Name": [name_enter.get()],"Item":[item_enter.get()],"ItemNo.":[item_no_enter.get()],"BuyPrice":[c[0]],"Profit":[d],"Tax":tax_enter.get()})
            if os.path.exists(Date_Sort):
                df2_1.to_csv(Date_Sort,mode="a",header=False,index=False)
            elif os.path.exists(Date_Sort)==False:
                df2_1.to_csv(Date_Sort, index=False)
            if os.path.exists(Month_Sort):
                df2_1.to_csv(Month_Sort,mode="a",header=False,index=False)
            elif os.path.exists(Month_Sort)==False:
                df2_1.to_csv(Month_Sort, index=False)
            if os.path.exists(Year_Sort):
                df2_1.to_csv(Year_Sort,mode="a",header=False,index=False)
            elif os.path.exists(Year_Sort) == False:
                df2_1.to_csv(Year_Sort,index=False)
            mb.showinfo("Saved", "Data has been saved")
    def Exit():
        window.deiconify()
        window1.destroy()
    window1 = tk.Toplevel()
    window1.title("Add New Customer")
    window1.config(bg="Grey")
    window1.minsize(800,600)
    window1.maxsize(800,600)
    window1.iconbitmap("target.ico")
    window.withdraw()
    canvas2 = tk.Canvas(window1, width=800, height=600)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg1, anchor="nw")
    title1 = canvas2.create_text(400, 50, text="Add New Customer", font=("Ariel", 60), fill="White")
    name = canvas2.create_text(100,150,text="Name :", font=("Ariel",16),fill="White")
    item = canvas2.create_text(100,200,text="Item   :",font=("Ariel",16),fill="White")
    item_no = canvas2.create_text(90,250,text="ItemNo. :",font=("Ariel",16),fill="White")
    price = canvas2.create_text(100,300,text="Price  :",font=("Ariel",16),fill="White")
    p_no = canvas2.create_text(85,350,text="PhoneNo.:",font=("Ariel",16),fill="White")
    mop = canvas2.create_text(100,400,text="Mode Of Payment:",font=("Ariel",16),fill="White")
    date = canvas2.create_text(600,150,text="Date:",font=("Ariel",16),fill="White")
    tax = canvas2.create_text(605, 200, text="Tax:", font=("Ariel", 16), fill="White")
    CASH = tk.IntVar()
    UPI = tk.IntVar()
    CARD = tk.IntVar()
    WALLET = tk.IntVar()
    OTHER = tk.IntVar()
    name_enter = tk.Entry(window1,width=30,font=("Ariel",13))
    a = pd.read_csv("Items.csv")
    b = a['Item'].tolist()
    item_enter = ttk.Combobox(window1, width=28, font=("Ariel", 13), state="readonly", values=b)
    item_no_enter = tk.Entry(window1,width=30, font=("Ariel",13))
    price_enter = tk.Entry(window1,width=30,font=("Ariel",13))
    p_no_enter = tk.Entry(window1, width=30, font=("Ariel", 13))
    cash_enter = tk.Checkbutton(window1,text="Cash",font=("Ariel",13), variable=CASH, background="salmon1",selectcolor="salmon1",foreground="White",activeforeground="White",activebackground="Orange",cursor="Hand1")
    upi_enter = tk.Checkbutton(window1, text="UPI", font=("Ariel", 13), variable=UPI, background="salmon1", selectcolor="salmon1",foreground="White", activeforeground="White", activebackground="Orange", cursor="Hand1")
    card_enter = tk.Checkbutton(window1, text="Credit/Debit Card", font=("Ariel", 13), variable=CARD, background="salmon1", selectcolor="salmon1",foreground="White", activeforeground="White", activebackground="Orange", cursor="Hand1")
    wallet_enter = tk.Checkbutton(window1, text="Online Wallet", font=("Ariel", 13), variable=WALLET, background="salmon1", selectcolor="salmon1",foreground="White", activeforeground="White", activebackground="Orange", cursor="Hand1")
    other_enter = tk.Checkbutton(window1, text="Other", font=("Ariel", 13), variable=OTHER, background="salmon1",selectcolor="salmon1", foreground="White", activeforeground="White",activebackground="Orange", cursor="Hand1")
    date_enter = tk.Button(window1,text= "12/1/23 "+u"\u25BC",font=("Ariel",13),background="salmon1", foreground="White",cursor="Hand1",command= open_calendar)
    tax_enter=ttk.Combobox(window1,width=7,font=("Ariel",13),state="readonly",values=["6%","12%"])
    name_enter.place(x=140,y=135)
    item_enter.place(x=140,y=185)
    item_no_enter.place(x=140,y=235)
    price_enter.place(x=140,y=285)
    p_no_enter.place(x=140,y=335)
    cash_enter.place(x=80,y=435)
    upi_enter.place(x=170,y=435)
    card_enter.place(x=260,y=435)
    wallet_enter.place(x=440,y=435)
    other_enter.place(x=600,y=435)
    date_enter.place(x=630,y=130)
    tax_enter.place(x=630,y=185)
    Save = tk.Button(window1, text="Save",font=("Blacklight", 13), fg="White",image=save,compound=tk.LEFT, width=100, bg="salmon1", activebackground="Green",activeforeground="White", cursor="Hand1",command=SAVE)
    Save.place(x=353, y=480)
    Back = tk.Button(window1,text="Back",font=("Blacklight",13),fg="White",image=back,compound=tk.LEFT,width=100,bg="salmon1",command=Exit,activebackground="Red",activeforeground="White",cursor="Hand1")
    Back.place(x=353,y=530)
def Old():
    def SEARCH():
        name_entry = entery.get() + ".csv"
        folder_path = 'Data/'
        file_name = name_entry
        Name1 = "Default_Ph_No/" + entery.get() + "No.csv"
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            def delete():
                os.remove(file_path)
                os.remove(Name1)
                mb.showinfo("Removed", "Record Removed!")
                window2.destroy()
                window1.deiconify()
            def Enter():
                def Phno():
                    def Submit():
                        Name = "Default_Ph_No/" + entery.get() + "No.csv"
                        df1 = pd.DataFrame({"Name": [entery.get()], "PhNo.": [number_enter.get()]})
                        df1.to_csv(Name, index=False)
                    window4 = tk.Toplevel()
                    window4.title("Update Phone No.!")
                    window4.minsize(300, 100)
                    Title = tk.Label(window4,text="Edit Phone No.",font=("Ariel",13))
                    Title.pack()
                    number_enter = tk.Entry(window4,width=30,justify="center")
                    number_enter.pack()
                    submit = tk.Button(window4,text="Submit",cursor="Hand1",command=Submit)
                    submit.pack()
                def Update():
                    if CASH.get() == 1:
                        a = "Cash"
                    if UPI.get() == 1:
                        a = "UPI"
                    if CARD.get() == 1:
                        a = "Card"
                    if WALLET.get() == 1:
                        a = "Wallet"
                    if OTHER.get() == 1:
                        a = "Other"
                    Nom = pd.read_csv("Default_Ph_No/SahibNo.csv")
                    Numb  = Nom.loc[0, "PhNo."]
                    DATE = selected_date
                    a = pd.read_csv("Items.csv")
                    b = a.set_index("Item").T.to_dict("list")
                    c = b.get(item_enter.get())
                    d = int(price_enter.get()) - c[0]
                    e, f, g = DATE.split(sep="/")
                    Date_Sort = "Profit/Date/" + e + "_" + f + "_" + g + ".csv"
                    Month_Sort = "Profit/Month/" + e + "_" + g + ".csv"
                    Year_Sort = "Profit/Year/" + g + ".csv"
                    df = pd.DataFrame({"Item": [item_enter.get()], "ItemNo.": [item_no_enter.get()], "Price": [price_enter.get()],"PhoneNo.": [Numb], "MOP": [a], "Date": [DATE],"tax":tax_enter.get()})
                    df.to_csv(file_path,index=False,header=False,mode="a")
                    df2_1 = pd.DataFrame({"Name": [entery.get()],"Item":[item_enter.get()],"ItemNo.":[item_no_enter.get()],"BuyPrice":[c[0]],"Profit":[d],"Tax":tax_enter.get()})
                    if os.path.exists(Date_Sort):
                        df2_1.to_csv(Date_Sort, mode="a", header=False, index=False)
                    elif os.path.exists(Date_Sort) == False:
                        df2_1.to_csv(Date_Sort, index=False)
                    if os.path.exists(Month_Sort):
                        df2_1.to_csv(Month_Sort, mode="a", header=False, index=False)
                    elif os.path.exists(Month_Sort) == False:
                        df2_1.to_csv(Month_Sort, index=False)
                    if os.path.exists(Year_Sort):
                        df2_1.to_csv(Year_Sort, mode="a", header=False, index=False)
                    elif os.path.exists(Year_Sort) == False:
                        df2_1.to_csv(Year_Sort, index=False)
                    mb.showinfo("Saved", "Data has been updated !")
                def open_calendar():
                    def select_date():
                        global selected_date
                        selected_date = cal.get_date()
                        date_enter.config(text=selected_date + u"\u25BC")
                        top.destroy()
                    global top
                    top = tk.Toplevel(window1)
                    cal = tkc.Calendar(top, selectmode="day")
                    cal.pack()
                    button = tk.Button(top, text="Select Date", command=select_date)
                    button.pack()
                def Exit():
                    window3.destroy()
                    window2.deiconify()
                window3 = tk.Toplevel()
                window3.title("Update Record")
                window3.config(bg="Grey")
                window3.minsize(800, 600)
                window3.maxsize(800, 600)
                window3.iconbitmap("target.ico")
                window2.withdraw()
                canvas2 = tk.Canvas(window3, width=800, height=600)
                canvas2.pack(fill="both", expand=True)
                canvas2.create_image(0, 0, image=bg1, anchor="nw")
                title1 = canvas2.create_text(400, 100, text="Update Record", font=("Ariel", 60), fill="White")
                item = canvas2.create_text(100, 200, text="Item  :", font=("Ariel", 16), fill="White")
                item_no = canvas2.create_text(90, 250, text="ItemNo.:", font=("Ariel", 16), fill="White")
                price = canvas2.create_text(100, 300, text="Price :", font=("Ariel", 16), fill="White")
                mop = canvas2.create_text(100, 400, text="Mode Of Payment:", font=("Ariel", 16), fill="White")
                date = canvas2.create_text(600, 200, text="Date:", font=("Ariel", 16), fill="White")
                tax = canvas2.create_text(605, 250, text="Tax:", font=("Ariel", 16), fill="White")
                a = pd.read_csv("Items.csv")
                b = a['Item'].tolist()
                item_enter = ttk.Combobox(window3, width=28, font=("Ariel", 13), state="readonly", values=b)
                item_no_enter = tk.Entry(window3, width=30, font=("Ariel", 13))
                price_enter = tk.Entry(window3, width=30, font=("Ariel", 13))
                CASH = tk.IntVar()
                UPI = tk.IntVar()
                CARD = tk.IntVar()
                WALLET = tk.IntVar()
                OTHER = tk.IntVar()
                cash_enter = tk.Checkbutton(window3, text="Cash", font=("Ariel", 13), variable=CASH, background="salmon1",selectcolor="salmon1", foreground="White", activeforeground="White",activebackground="Orange", cursor="Hand1")
                upi_enter = tk.Checkbutton(window3, text="UPI", font=("Ariel", 13), variable=UPI, background="salmon1", selectcolor="salmon1",foreground="White", activeforeground="White", activebackground="Orange",cursor="Hand1")
                card_enter = tk.Checkbutton(window3, text="Credit/Debit Card",font=("Ariel", 13), variable=CARD, background="salmon1",selectcolor="salmon1", foreground="White", activeforeground="White",activebackground="Orange", cursor="Hand1")
                wallet_enter = tk.Checkbutton(window3, text="Online Wallet", font=("Ariel", 13), variable=WALLET, background="salmon1",selectcolor="salmon1", foreground="White", activeforeground="White",activebackground="Orange", cursor="Hand1")
                other_enter = tk.Checkbutton(window3, text="Other", font=("Ariel", 13),  variable=OTHER, background="salmon1",selectcolor="salmon1", foreground="White", activeforeground="White",activebackground="Orange", cursor="Hand1")
                date_enter = tk.Button(window3, text="12/1/23" + u"\u25BC", font=("Ariel", 13), background="salmon1",foreground="White", command=open_calendar,cursor="Hand1")
                p_no = tk.Button(window3, image=Edit,compound=tk.LEFT,text="Edit Phone Number", font=("Ariel", 13),width=180, background="salmon1",foreground="White",activebackground="Orange",activeforeground="White",cursor="Hand1",command=Phno)
                tax_enter = ttk.Combobox(window3, width=7, font=("Ariel", 13), state="readonly", values=["6%", "12%"])
                item_enter.place(x=140, y=185)
                item_no_enter.place(x=140, y=235)
                price_enter.place(x=140, y=285)
                cash_enter.place(x=80, y=435)
                upi_enter.place(x=170, y=435)
                card_enter.place(x=260, y=435)
                wallet_enter.place(x=440, y=435)
                other_enter.place(x=600, y=435)
                date_enter.place(x=630, y=180)
                p_no.place(x=140,y=335)
                tax_enter.place(x=630, y=235)
                Save = tk.Button(window3, text="Update",font=("Blacklight", 13), fg="White", image=save, compound=tk.LEFT, width=100, bg="salmon1",activebackground="Green", activeforeground="White", cursor="Hand1",command=Update)
                Save.place(x=353, y=480)
                Back = tk.Button(window3, text="Back",font=("Blacklight", 13), fg="White", image=back, compound=tk.LEFT, width=100, bg="salmon1", command=Exit,activebackground="Red", activeforeground="White", cursor="Hand1")
                Back.place(x=353, y=530)
            def Exit():
                window2.destroy()
                window1.deiconify()

            window2 = tk.Toplevel()
            window2.title("Update Old Customer")
            window2.minsize(800, 600)
            window2.maxsize(800, 600)
            window2.iconbitmap("target.ico")
            window1.withdraw()
            canvas2 = tk.Canvas(window2, width=800, height=600)
            canvas2.pack(fill="both", expand=True)
            canvas2.create_image(0, 0, image=bg1, anchor="nw")

            title1 = canvas2.create_text(400, 100, text="Update Old Customer", font=("Ariel", 60), fill="White")

            record = tk.Button(window2, text="Update Record", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=300, padx=10,bg="Salmon1", activebackground="Orange", activeforeground="White",cursor="Hand1",command=Enter)
            record.place(x=230, y=200)
            rem_record = tk.Button(window2, text="Delete Record", font=("Ariel", 12), fg="White", image=graph,compound=tk.LEFT, width=300, padx=10, bg="Salmon1", activebackground="Orange",activeforeground="White", cursor="Hand1",command=delete)
            rem_record.place(x=230, y=300)
            Back = tk.Button(window2, text="Back", font=("Blacklight", 12), fg="White", image=back1, compound=tk.LEFT,width=300,padx=10, bg="salmon1", activebackground="Red", activeforeground="White",cursor="Hand1",command=Exit)
            Back.place(x=230, y=400)
        else:
            mb.showerror("Error","Name Is Not Registered!")
    def Exit():
        window.deiconify()
        window1.destroy()
    window1 = tk.Toplevel()
    window1.title("Update Old Customer")
    window1.config(bg="Grey")
    window1.minsize(800,600)
    window1.maxsize(800,600)
    window1.iconbitmap("target.ico")
    window.withdraw()
    canvas2 = tk.Canvas(window1, width=800, height=600)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg1, anchor="nw")
    title1 = canvas2.create_text(400,100,text="Update Old Customer", font=("Ariel",60),fill="White")
    name = canvas2.create_text(400,200,text="Enter Name Of Customer",font=("Ariel",30),fill="White")
    Search = tk.Button(window1,text="Search",font=("Blacklight",12),fg="White",image=search,compound=tk.LEFT,bg="Salmon1",width=90,activebackground="Green",activeforeground="White",command=SEARCH,cursor="Hand1")
    Search.place(x=353,y=270)
    Back = tk.Button(window1,text="Back",font=("Blacklight",12),fg="White",image=back,compound=tk.LEFT,bg="Salmon1",width=90,command=Exit,activebackground="Red",activeforeground="White",cursor="Hand1")
    Back.place(x=353,y=530)
    entery = tk.Entry(window1,width=60,font=("Ariel",15),justify="center")
    entery.place(x=70,y=230)
def status():
    def tax():
        def Update():
            os.startfile("Tax.csv")
        def Show():
            window3=tk.Toplevel()
            window3.geometry("250x80")
            window3.minsize(250,50)
            window3.maxsize(250, 950)
            window3.title("Tax List")
            Tax_Title=tk.Label(window3,text="Task List",font=("Bold",20))
            Tax_Title.pack()
            a = pd.read_csv("Tax.csv")
            b=a["Tax"].tolist()
            for i in b:
                Tax_list=tk.Label(window3,text=i)
                Tax_list.pack()
        def Exit():
            window1.deiconify()
            window2.destroy()
        window2 = tk.Toplevel()
        window2.title("Tax")
        window2.minsize(800, 600)
        window2.maxsize(800, 600)
        window2.iconbitmap("target.ico")
        window1.withdraw()
        canvas2 = tk.Canvas(window2, width=800, height=600)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg1, anchor="nw")
        title1 = canvas2.create_text(405, 100, text="Tax %", font=("Ariel", 60), fill="White")
        See_Tax = tk.Button(window2, text="Open Tax List", image=Tax, compound="left", width=300, bg="Salmon1",activebackground="Orange", activeforeground="White", font=("Blacklight", 15), fg="White",cursor="Hand1",command=Show)
        See_Tax.place(x=250, y=190)
        Update_Tax = tk.Button(window2, text="Update Tax List", image=Tax, compound="left", width=300,bg="Salmon1", activebackground="Orange", activeforeground="White",font=("Blacklight", 15), fg="White", cursor="Hand1", command=Update)
        Update_Tax.place(x=250, y=300)
        Back = tk.Button(window2, text="Back", font=("Blacklight", 15), fg="White", image=back1, compound=tk.LEFT,width=300, bg="Salmon1", activebackground="Red", activeforeground="White", command=Exit,cursor="Hand1")
        Back.place(x=250, y=410)

    def Buy_Price():
        def New():
            def Submit():
                Items = pd.read_csv("Items.csv")
                Item_Dict = Items.set_index("Item").T.to_dict("records")
                a = Item_Dict[0]
                dict1 = {item_enter.get(): int(price.get())}
                a.update(dict1)
                b = pd.DataFrame({"Item": a.keys(), "Buying Price": a.values()})
                b.to_csv("Items.csv", index=False)
                mb.showinfo("Successful", "Updated Successfully!")

            window3 = tk.Toplevel()
            window3.title("Update Old Items And Its Price")
            window3.geometry("500x300")
            a = pd.read_csv("Items.csv")
            b = a['Item'].tolist()
            title = tk.Label(window3, text="Enter Item Name", font=("Bold", 20), pady=5)
            title.pack()
            item_enter = tk.Entry(window3, width=30, font=("Ariel", 13))
            item_enter.pack()
            price_txt = tk.Label(window3, text="Enter Buy Price", font=("Bold", 20), pady=5)
            price_txt.pack()
            price = tk.Entry(window3, width=30, font=("Ariel", 13))
            price.pack()
            submit = tk.Button(window3, text="Submit", font=("Ariel", 13), command=Submit)
            submit.place(x=220, y=250)
        def Update():
            def Submit():
                Items = pd.read_csv("Items.csv")
                Item_Dict = Items.set_index("Item").T.to_dict("records")
                a=Item_Dict[0]
                a[item_enter.get()]=int(new_price.get())
                b=pd.DataFrame({"Item":a.keys(),"Buying Price":a.values()})
                b.to_csv("Items.csv",index=False)
                mb.showinfo("Successful","Updated Successfully!")
            window3=tk.Toplevel()
            window3.title("Update Old Items And Its Price")
            window3.geometry("500x300")
            a = pd.read_csv("Items.csv")
            b = a['Item'].tolist()
            title=tk.Label(window3,text="Select Item",font=("Bold",20),pady=5)
            title.pack()
            item_enter = ttk.Combobox(window3, width=28, font=("Ariel", 13), state="readonly", values=b)
            item_enter.pack()
            new_price_txt= tk.Label(window3,text="Enter New Buy Price",font=("Bold",20),pady=5)
            new_price_txt.pack()
            new_price = tk.Entry(window3,width=30, font=("Ariel",13))
            new_price.pack()
            submit=tk.Button(window3,text="Submit",font=("Ariel",13),command=Submit)
            submit.place(x=220,y=250)
        def Delete():
            def Submit():
                Items = pd.read_csv("Items.csv")
                Item_Dict = Items.set_index("Item").T.to_dict("records")
                a=Item_Dict[0]
                del a[item_enter.get()]
                b=pd.DataFrame({"Item":a.keys(),"Buying Price":a.values()})
                b.to_csv("Items.csv",index=False)
                mb.showinfo("Successful","Updated Successfully!")
                window3.destroy()
            window3=tk.Toplevel()
            window3.title("Update Old Items And Its Price")
            window3.geometry("500x300")
            a = pd.read_csv("Items.csv")
            b = a['Item'].tolist()
            title=tk.Label(window3,text="Select Item",font=("Bold",20),pady=5)
            title.pack()
            item_enter = ttk.Combobox(window3, width=28, font=("Ariel", 13), state="readonly", values=b)
            item_enter.pack()
            submit=tk.Button(window3,text="Delete",font=("Ariel",13),command=Submit)
            submit.place(x=220,y=250)
        def Exit():
            window1.deiconify()
            window2.destroy()
        window2 = tk.Toplevel()
        window2.title("Buying Price")
        window2.minsize(800, 600)
        window2.maxsize(800, 600)
        window2.iconbitmap("target.ico")
        window1.withdraw()
        canvas2 = tk.Canvas(window2, width=800, height=600)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg1, anchor="nw")
        title1 = canvas2.create_text(405, 100, text="Buying Price", font=("Ariel", 60), fill="White")
        New_Price = tk.Button(window2, text="New Item And Price", image=Price, compound="left", width=300,bg="Salmon1", activebackground="Orange", activeforeground="White",font=("Blacklight", 15), fg="White", cursor="Hand1",command=New)
        New_Price.place(x=250, y=170)
        Update_Price = tk.Button(window2, text="Update Old Item And Price", image=Price, compound="left", width=300, bg="Salmon1",activebackground="Orange", activeforeground="White", font=("Blacklight", 15), fg="White", cursor="Hand1",command=Update)
        Update_Price.place(x=250, y=280)
        Delete_Price = tk.Button(window2, text="Delete An Item", image=Price, compound="left", width=300,bg="Salmon1", activebackground="Orange", activeforeground="White",font=("Blacklight", 15), fg="White", cursor="Hand1", command=Delete)
        Delete_Price.place(x=250, y=390)
        Back = tk.Button(window2, text="Back", font=("Blacklight", 15), fg="White", image=back1, compound=tk.LEFT,width=300, bg="Salmon1", activebackground="Red", activeforeground="White", command=Exit,cursor="Hand1")
        Back.place(x=250, y=500)
    def PROFIT():
        def Date_Sort():
            def open_calendar():
                def select_date():
                    global selected_date
                    selected_date = cal.get_date()
                    date_enter.config(text=selected_date + u"\u25BC")
                    top.destroy()

                global top
                top = tk.Toplevel(window1)
                cal = tkc.Calendar(top, selectmode="day")
                cal.pack()
                button = tk.Button(top, text="Select Date", command=select_date)
                button.pack()
            def Submit():
                folder_path = 'Profit/Date/'
                a,b,c= selected_date.split(sep="/")
                file=folder_path+a+"_"+b+"_"+c+".csv"
                if os.path.exists(file):
                    d = pd.read_csv(file)
                    e = d["Profit"].tolist()
                    f = sum(e)
                    Profit_txt = "Profit Made On This Date Is :"+str(f)
                    mb.showinfo("Profit Made!", Profit_txt)
                    conf=mb.askyesno("Confirmation","Do You want to open this date's data?")
                    if conf:
                        files="Profit\\Date\\"+a+"_"+b+"_"+c+".csv"
                        os.startfile(files)
                else:
                    mb.showerror("Error","Data Is Not Available For This Date")

            window3=tk.Toplevel()
            window3.title("Sort(Date)")
            window3.minsize(300, 100)
            Title = tk.Label(window3, text="Enter Date", font=("Ariel", 13))
            Title.pack()
            date_enter=tk.Button(window3,text= "12/1/23"+u"\u25BC",font=("Ariel",13),cursor="Hand1",command= open_calendar)
            date_enter.pack()
            submit = tk.Button(window3, text="Submit", cursor="Hand1", command=Submit)
            submit.place(x=125,y=70)
        def Month_Sort():
            def Submit():
                folder_path = 'Profit/Month/'
                a=Month_enter.get()
                b=int(year_enter.get())-2000
                file = folder_path +a + "_" +str(b) + ".csv"
                if os.path.exists(file):
                    d = pd.read_csv(file)
                    e = d["Profit"].tolist()
                    f = sum(e)
                    Profit_txt = "Profit Made On This Month Is :" + str(f)
                    mb.showinfo("Profit Made!", Profit_txt)
                    conf = mb.askyesno("Confirmation", "Do You want to open this date's data?")
                    if conf:
                        files = ("Profit\\Month\\"+ a + "_" +
                                 str(b) + ".csv")
                        os.startfile(files)
                else:
                    mb.showerror("Error","Data Is Not Available For This Month")

            window3 = tk.Toplevel()
            window3.title("Sort(Month)")
            window3.minsize(300,160)
            Title = tk.Label(window3, text="Select Month No.", font=("Ariel", 13))
            Title.pack()
            Month_enter = ttk.Combobox(window3,width=7,font=("Ariel",13),state="readonly",values=list(range(1,13)))
            Month_enter.pack()
            Title1 = tk.Label(window3, text="Select Year", font=("Ariel", 13))
            Title1.pack()
            year_enter = ttk.Combobox(window3,width=7,font=("Ariel",13),state="readonly",values=list(range(2022,2060)))
            year_enter.pack()
            submit = tk.Button(window3, text="Submit", cursor="Hand1", command=Submit)
            submit.place(x=125, y=130)
        def Year_Sort():
            def Submit():
                folder_path = 'Profit/Year/'
                b=int(year_enter.get())-2000
                file = folder_path + str(b) + ".csv"
                if os.path.exists(file):
                    d = pd.read_csv(file)
                    e = d["Profit"].tolist()
                    f = sum(e)
                    Profit_txt = "Profit Made!, This Year Is :" + str(f)
                    mb.showinfo("Profit Made!", Profit_txt)
                    conf = mb.askyesno("Confirmation", "Do You want to open this year's data?")
                    if conf:
                        files = "Profit\\Year\\" + str(b) + ".csv"
                        os.startfile(files)
                else:
                    mb.showerror("Error!","Data Not available for this year")

            window3 = tk.Toplevel()
            window3.title("Sort(Month)")
            window3.minsize(300,140)
            Title1 = tk.Label(window3, text="Select Year", font=("Ariel", 13))
            Title1.pack()
            year_enter = ttk.Combobox(window3,width=7,font=("Ariel",13),state="readonly",values=list(range(2022,2060)))
            year_enter.pack()
            submit = tk.Button(window3, text="Submit", cursor="Hand1", command=Submit)
            submit.place(x=125, y=110)
        def Exit():
            window1.deiconify()
            window2.destroy()
        window2 = tk.Toplevel()
        window2.title("Buying Price")
        window2.minsize(800, 600)
        window2.maxsize(800, 600)
        window2.iconbitmap("target.ico")
        window1.withdraw()
        canvas2 = tk.Canvas(window2, width=800, height=600)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg1, anchor="nw")
        title1 = canvas2.create_text(405, 100, text="Sort Profit Made By", font=("Ariel", 60), fill="White")
        date = tk.Button(window2, text="Date", image=profit, compound="left", width=200, bg="Salmon1",activebackground="Orange", activeforeground="White", font=("Blacklight", 15), fg="White",cursor="Hand1",command=Date_Sort)
        date.place(x=280, y=170)
        Month = tk.Button(window2, text="Month", image=profit, compound="left", width=200,bg="Salmon1", activebackground="Orange", activeforeground="White",font=("Blacklight", 15), fg="White", cursor="Hand1",command=Month_Sort)
        Month.place(x=280, y=280)
        year = tk.Button(window2, text="Year", image=profit, compound="left", width=200, bg="Salmon1",activebackground="Orange", activeforeground="White", font=("Blacklight", 15), fg="White", cursor="Hand1",command=Year_Sort)
        year.place(x=280, y=390)
        Back = tk.Button(window2, text="Back", font=("Blacklight", 15), fg="White", image=back1, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Red", activeforeground="White", command=Exit,cursor="Hand1")
        Back.place(x=280, y=500)
    def Exit():
        window.deiconify()
        window1.destroy()
    window1 = tk.Toplevel()
    window1.title("Shop Statistics")
    window1.config(bg="Grey")
    window1.minsize(800,600)
    window1.maxsize(800,600)
    window1.iconbitmap("target.ico")
    window.withdraw()
    canvas2 = tk.Canvas(window1, width=800, height=600)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg1, anchor="nw")
    title1 = canvas2.create_text(405, 100, text="Shop Statistics", font=("Ariel", 60), fill="White")
    tax = tk.Button(window1,text="Tax",image=Tax,compound="left",width=250,bg="Salmon1",activebackground="Orange",activeforeground="White",font=("Blacklight",15),fg="White",cursor="Hand1",command=tax)
    tax.place(x=280,y=170)
    Buying_Price = tk.Button(window1, text="Buying Price Of Items", image=Price, compound="left", width=250, bg="Salmon1", activebackground="Orange",activeforeground="White", font=("Blacklight", 15), fg="White",command=Buy_Price, cursor="Hand1")
    Buying_Price.place(x=280, y=280)
    Profit = tk.Button(window1, text="Profit Made", image=profit, compound="left", width=250, bg="Salmon1", activebackground="Orange",activeforeground="White", font=("Blacklight", 15), fg="White",command=PROFIT, cursor="Hand1")
    Profit.place(x=280, y=390)
    Back = tk.Button(window1,text="Back",font=("Blacklight",15),fg="White",image=back1,compound=tk.LEFT,width=250,bg="Salmon1",activebackground="Red",activeforeground="White",command=Exit,cursor="Hand1")
    Back.place(x=280,y=500)
def Graphs():
    def items():
        df=pd.read_csv("Items.csv",index_col=0)
        df.plot(kind="barh")
        plt.title("Buying Price Of Items")
        plt.ylabel("Items")
        plt.xlabel("Price")
        plt.show()
    def items_pie():
        df=pd.read_csv("Items.csv",index_col=0)
        df.plot(kind="pie",y="Buying Price")
        plt.title("Buying Price Of Items")
        plt.ylabel("Price")
        plt.show()
    def profit_year():
        df0=pd.read_csv("Profit/Year/23.csv")
        df=df0[["Name","Profit"]]
        df.set_index("Name",inplace=True)
        df.plot(kind="bar")
        plt.xlabel("Names")
        plt.ylabel("Profit")
        plt.show()
    def profit_year_hist():
        df0=pd.read_csv("Profit/Year/23.csv")
        df=df0[["Name","Profit"]]
        df.plot(kind="hist")
        plt.xlabel("Profit")
        plt.show()
    def earnings():
        df = pd.read_csv("Earnings.csv")
        df.plot(kind='bar',color = 'b')
        plt.xlabel("Days")
        plt.ylabel("Profit Made")
        plt.grid(True)
        plt.title("Earnings")
        tick=df.index.tolist()
        plt.xticks(tick,df.Days)
        plt.show()
    def earnings_line():
        df = pd.read_csv("Earnings.csv")
        df.plot(kind='line',color = 'b',linestyle="-.",marker="*")
        plt.xlabel("Days")
        plt.ylabel("Profit Made")
        plt.grid(True)
        plt.title("Earnings")
        tick=df.index.tolist()
        plt.xticks(tick,df.Days)
        plt.show()
    def earnings_pie():
        df = pd.read_csv("Earnings.csv",index_col=0)
        df.plot(kind='pie',y="Earnings")
        plt.ylabel("Profit Made")
        plt.grid(True)
        plt.title("Earnings")
        plt.show()
    def seasons():
        df=pd.read_csv("Seasons.csv")
        df.set_index("Seasons",inplace=True)
        df.plot(kind = "pie",y='Count',)
        plt.ylabel("Seasons")
        plt.show()

    def seasons_bar():
        df=pd.read_csv("Seasons.csv")
        df.set_index("Seasons",inplace=True)
        df.plot(kind = "bar")
        plt.ylabel("Sales")
        plt.xlabel("Seasons")
        plt.show()

    def seasons_barh():
        df=pd.read_csv("Seasons.csv")
        df.set_index("Seasons",inplace=True)
        df.plot(kind = "barh")
        plt.xlabel("Sales")
        plt.ylabel("Seasons")
        plt.show()

    def percent_of_diff_shops():
        df = pd.read_csv("% of shops.csv")
        df.set_index('Type',inplace=True)
        df.plot(kind='barh')
        plt.xlabel("Percentage")
        plt.ylabel("Type")
        plt.grid(True)
        plt.title("Earnings")
        plt.show()
    def percent_of_diff_shops_bar():
        df = pd.read_csv("% of shops.csv")
        df.set_index('Type',inplace=True)
        df.plot(kind='bar',color='m')
        plt.xlabel("Percentage")
        plt.ylabel("Type")
        plt.grid(True)
        plt.title("Earnings")
        plt.show()
    def comparison():
        df = pd.read_csv("Comparision.csv",index_col=0)
        df.plot(kind = 'barh')
        plt.ylabel("Comparison")
        plt.xlabel("Pecentage%")
        plt.grid(True)
        plt.show()
    def comparison_line():
        df=pd.read_csv("Comparision.csv",index_col=0)
        df.plot(kind="line")
        plt.ylabel("Percentage%")
        plt.xlabel("Comparison")
        plt.grid(True)
        plt.show()
    def comparison_bar():
        df=pd.read_csv("Comparision.csv",index_col=0)
        df.plot(kind="bar")
        plt.xlabel("Percentage%")
        plt.ylabel("Comparison")
        plt.grid(True)
        plt.show()
    def Exit():
        window.deiconify()
        window1.destroy()
    window1 = tk.Toplevel()
    window1.title("Graphs")
    window1.config(bg="Grey")
    window1.minsize(800,600)
    window1.maxsize(800,600)
    window1.iconbitmap("target.ico")
    window.withdraw()
    canvas2 = tk.Canvas(window1, width=800, height=600)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg1, anchor="nw")
    title1 = canvas2.create_text(400, 100, text="Graphs", font=("Ariel", 60), fill="White")
    Earning = tk.Button(window1, text="Earnings Graph", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT, width=200,bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=earnings)
    Earning.place(x=80, y=200)
    Season = tk.Button(window1, text="Seasons", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=seasons)
    Season.place(x=300, y=200)
    diff = tk.Button(window1, text="Different Shops", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=percent_of_diff_shops)
    diff.place(x=520, y=200)
    Comparision = tk.Button(window1, text="Comparison", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=comparison)
    Comparision.place(x=80, y=250)
    Comparision_line = tk.Button(window1, text="Comparison (line)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=comparison_line)
    Comparision_line.place(x=300, y=250)
    Year_Profit = tk.Button(window1, text="Profit (Year)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=profit_year)
    Year_Profit.place(x=520, y=250)
    Year_Profit_Hist = tk.Button(window1, text="Profit (Year_Hist)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=profit_year_hist)
    Year_Profit_Hist.place(x=80, y=300)
    Earning_line = tk.Button(window1, text="Earnings(line) Graph", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=earnings_line)
    Earning_line.place(x=300, y=300)
    diff_bar = tk.Button(window1, text="Different Shops (Bar)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=percent_of_diff_shops_bar)
    diff_bar.place(x=520, y=300)
    Earning_pie = tk.Button(window1, text="Earnings (Pie)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=earnings_pie)
    Earning_pie.place(x=80, y=350)
    Buy_Price = tk.Button(window1, text="Buy Price Of Items", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=items)
    Buy_Price.place(x=300, y=350)
    Season_bar = tk.Button(window1, text="Seasons (Bar)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=seasons_bar)
    Season_bar.place(x=520, y=350)
    Buy_Price_Pie = tk.Button(window1, text="Buying Price (Pie)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=items_pie)
    Buy_Price_Pie.place(x=80, y=400)
    Comparision_Bar = tk.Button(window1, text="Comparison (Bar)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=comparison_bar)
    Comparision_Bar.place(x=300, y=400)
    Season_Barh = tk.Button(window1, text="Season (BarH)", font=("Ariel", 12), fg="White", image=graph, compound=tk.LEFT,width=200, bg="Salmon1", activebackground="Orange", activeforeground="White", cursor="Hand1",command=seasons_barh)
    Season_Barh.place(x=520, y=400)
    Back = tk.Button(window1,text="Back",font=("Ariel",12),fg="White",image=back1,compound=tk.LEFT,width=200,bg="Salmon1",activebackground="Red",activeforeground="White",command=Exit,cursor="Hand1")
    Back.place(x=300,y=530)
def EXIT():
    sys.exit()

window= tk.Tk()
window.title("Customer Management System")
window.geometry("1920x1080")
window.iconbitmap('target.ico')

bg = tk.PhotoImage(file="Background/bg2.png")
bg1 = tk.PhotoImage(file="Background/bg1.png")
newimg = tk.PhotoImage(file="Icons/customer.png")
oldimg= tk.PhotoImage(file="Icons/customer1.png")
shop = tk.PhotoImage(file="Icons/shop.png")
graph = tk.PhotoImage(file="Icons/bar-graph.png")
QUIT = tk.PhotoImage(file="Icons/logout.png")
search = tk.PhotoImage(file="Icons/search.png")
back = tk.PhotoImage(file="Icons/back.png")
back1 = tk.PhotoImage(file="Icons/back1.png")
save = tk.PhotoImage(file="Icons/save.png")
Tax = tk.PhotoImage(file="Icons/tax.png")
Price = tk.PhotoImage(file="Icons/price.png")
profit = tk.PhotoImage(file="Icons/Profit.png")
Edit = tk.PhotoImage(file="Icons/pencil.png")

canvas1 = tk.Canvas( window,width=1920,height=1080)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

title = canvas1.create_text(960,120,text="Customer Management System", font=("Ariel",100),fill="DeepSkyBlue")

NewCustomer = tk.Button(window,text="Add New Customer",font=("Blacklight",23), fg="SkyBlue",image=newimg,padx=20,compound=tk.LEFT,height=50,width=500,bg="RoyalBlue2",command=NewWin,activebackground="Blue",activeforeground="White",cursor="Hand1")
NewCustomer_canvas = canvas1.create_window(960,300,anchor= "center",window=NewCustomer)

OldCustomer = tk.Button(window,text="Update Old Customer",font=("Blacklight",23),fg="SkyBlue",image=oldimg,padx=20,compound=tk.LEFT,height=50,width=500,bg="RoyalBlue2",command=Old,activebackground="Blue",activeforeground="White",cursor="Hand1")
OldCustomer_canvas = canvas1.create_window(960,450,anchor= "center",window=OldCustomer)

Status = tk.Button(window,text="Shop Statistics",font=("Blacklight",23),fg="SkyBlue",image=shop,padx=20,compound=tk.LEFT,height=50,width=500,bg="RoyalBlue2",command=status,activebackground="Blue",activeforeground="White",cursor="Hand1")
Status_canvas = canvas1.create_window(960,600,anchor= "center",window=Status)

graphs = tk.Button(window,text="Graphs",font=("Blacklight",23),fg="SkyBlue",image=graph,padx=20,compound=tk.LEFT,height=50,width=500,bg="RoyalBlue2",command=Graphs,activebackground="Blue",activeforeground="White",cursor="Hand1")
graphs_canvas = canvas1.create_window(960,750,anchor= "center",window=graphs)

Quit = tk.Button(window,text="Exit",font=("Blacklight",23),fg="SkyBlue",image=QUIT,padx=20,compound=tk.LEFT,height=50,width=500,bg="RoyalBlue2",command=EXIT, activebackground="Red",activeforeground="White",cursor="Hand1")
Quit_canvas = canvas1.create_window(960,900,anchor= "center",window=Quit)

tk.mainloop()