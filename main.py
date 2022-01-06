# importing modules
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
from tkcalendar import DateEntry
from tkinter.filedialog import asksaveasfile
from csv import DictWriter
import json

# main callabele function
def main():
    # user function
    def user_login():
        # user class
        class User(tk.Frame):
            def __init__(self, window, *args, **kwargs):
                super().__init__(window, *args, **kwargs)
                self.windows = window

                # notebook frame
                tab_control = ttk.Notebook(window)
                self.tab1 = ttk.Frame(tab_control, width=1000, height=100)
                tab_control.add(self.tab1)
                tab_control.pack(expand=500, fill="both")

                #  opening camping vans database
                with open("camper_vans.json", "r") as openfile:
                    json_object = json.load(openfile)

                # saving camper vans data in camper_vans list
                self.camper_vans = []
                for each in json_object["camper_vans"]:
                    self.camper_vans.append(
                        [
                            each["name"],
                            each["type"],
                            each["capacity"],
                            each["price"],
                            each["availability"],
                        ]
                    )

                # creating label for booking camping vans  title
                self.lb17_add = tk.Label(
                    self.tab1,
                    text="Camping Van Details:",
                    font=("Helvetica", 12, "bold"),
                    bg="#EFEFEF",
                    underline=True,
                    borderwidth=5,
                )
                self.lb17_add.place(x=60, y=15)

                # creating labels, fields and buttons for bookings
                self.lb1_add = tk.Label(
                    self.tab1, text="Model:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb1_add.place(x=60, y=50)

                self.textfield1_add = ttk.Combobox(
                    self.tab1,
                    font=("Helvetica", 10),
                    state="readonly",
                    values=["Van-1", "Van-2", "Van-3"],
                )
                self.textfield1_add.place(x=180, y=50, width=280)

                self.lb2_add = tk.Label(
                    self.tab1, text="Type:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb2_add.place(x=530, y=50)

                self.textfield2_add = ttk.Combobox(
                    self.tab1,
                    font=("Helvetica", 10),
                    state="readonly",
                    values=["Small", "Medium", "Large"],
                )
                self.textfield2_add.place(x=620, y=50, width=280)

                self.lb3_add = tk.Label(
                    self.tab1, text="Capacity:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb3_add.place(x=60, y=80)

                self.textfield3_add = ttk.Combobox(
                    self.tab1,
                    font=("Helvetica", 10),
                    state="readonly",
                    values=["1-4", "1-6", "8+"],
                )
                self.textfield3_add.place(x=180, y=80, width=280)

                self.lb4_add = tk.Label(
                    self.tab1, text="Price:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb4_add.place(x=530, y=80)

                self.textfield4_add = ttk.Combobox(
                    self.tab1,
                    font=("Helvetica", 10),
                    state="readonly",
                    values=["20", "40", "60"],
                )
                self.textfield4_add.place(x=620, y=80, width=280)

                # function to automatically add vans to the listbox
                def selectItem(a):
                    cur_item = self.tree.focus()
                    print(self.tree.item(cur_item)["values"][0], a)
                    self.textfield1_add.set(self.tree.item(cur_item)["values"][0])
                    self.textfield2_add.set(self.tree.item(cur_item)["values"][1])
                    self.textfield3_add.set(self.tree.item(cur_item)["values"][2])
                    self.textfield4_add.set(self.tree.item(cur_item)["values"][3])

                # creating label for camper vans frame
                self.lb1_add = tk.Label(
                    self.tab1,
                    text="Select Suitable Camping Van:",
                    font=("Helvetica", 12, "bold"),
                    bg="#EFEFEF",
                    underline=True,
                    borderwidth=5,
                )
                self.lb1_add.place(x=60, y=120)

                # creating frame for camper vans list
                self.frame = Frame(self.tab1)
                self.frame.place(x=60, y=150)

                self.tree = ttk.Treeview(
                    self.frame, columns=(1, 2, 3, 4, 5), height=7, show="headings"
                )
                self.tree.pack(side="left")
                self.tree.bind("<ButtonRelease-1>", selectItem)

                self.val = ["Name", "Type", "Capacity", "Price", "Availability"]

                # creating headings for camper vans list
                for i in range(1, len(self.val) + 1):
                    self.tree.heading(i, text=self.val[i - 1])

                # creating columns for camper vans list
                for i in range(1, len(self.val) + 1):
                    self.tree.column(i, width=165, anchor="center")

                # creating scrollbar for camper vans list
                self.scroll1 = ttk.Scrollbar(
                    self.frame, orient="vertical", command=self.tree.yview
                )
                self.scroll1.pack(side="right", fill="y")

                # creating listbox for camper vans list
                for i in range(len(self.camper_vans)):
                    if int(self.camper_vans[i][4]) > 0:
                        self.tree.insert(
                            "",
                            "end",
                            values=(
                                str(self.camper_vans[i][0]),
                                str(self.camper_vans[i][1]),
                                str(self.camper_vans[i][2]),
                                str(self.camper_vans[i][3]),
                                str(self.camper_vans[i][4]),
                            ),
                            tags=("odd",),
                        )

                # creating label for customer details title
                self.lb18_add = tk.Label(
                    self.tab1,
                    text="Customer Details:",
                    font=("Helvetica", 12, "bold"),
                    bg="#EFEFEF",
                    underline=True,
                    borderwidth=5,
                )
                self.lb18_add.place(x=60, y=320)

                # creating labels, fields and buttons for customer details
                self.lb7 = tk.Label(
                    self.tab1, text="Full name:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb7.place(x=60, y=350)

                self.textfield7_add = ttk.Entry(self.tab1, font=("Helvetica", 10))
                self.textfield7_add.place(x=180, y=350, width=720)

                self.lb8 = tk.Label(
                    self.tab1, text="ID card #:", font=("Helvetica", 10), bg="#EFEFEF",
                )
                self.lb8.place(x=60, y=380)

                self.textfield8_add = ttk.Entry(self.tab1, font=("Helvetica", 10))
                self.textfield8_add.place(x=180, y=380, width=300)

                self.lb9 = tk.Label(
                    self.tab1,
                    text="# of Travellers:",
                    font=("Helvetica", 10),
                    bg="#EFEFEF",
                )
                self.lb9.place(x=500, y=380)

                self.textfield9_add = ttk.Entry(self.tab1, font=("Helvetica", 10))
                self.textfield9_add.place(x=600, y=380, width=300)

                self.lb10 = tk.Label(
                    self.tab1,
                    text="Journey Date:",
                    font=("Helvetica", 10),
                    bg="#EFEFEF",
                )
                self.lb10.place(x=60, y=410)

                self.textfield10_add = DateEntry(
                    self.tab1,
                    font=("Helvetica", 10),
                    state="readonly",
                    date_pattern="mm/dd/yyyy",
                    anchor="center",
                )
                self.textfield10_add.place(x=180, y=410, width=300)

                self.lb11 = tk.Label(
                    self.tab1, text="Return Date:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb11.place(x=500, y=410)

                self.textfield11_add = DateEntry(
                    self.tab1,
                    font=("Helvetica", 10),
                    state="readonly",
                    date_pattern="mm/dd/yyyy",
                    anchor="center",
                )
                self.textfield11_add.place(x=600, y=410, width=300)

                #  opening regions database
                with open("region.json", "r") as openfile:
                    json_object = json.load(openfile)

                self.region = json_object["Region"]
                self.main_region = {}

                # creating list of regions
                for each in self.region:
                    for key, value in each.items():
                        self.main_region[key] = value

                # region combobox values
                def callbackFunc(event):
                    print(event)
                    self.textfield13_add.destroy()
                    self.textfield13_add = ttk.Combobox(
                        self.tab1,
                        font=("Helvetica", 10),
                        values=self.main_region[str(self.textfield12_add.get())],
                        state="readonly",
                    )
                    self.textfield13_add.place(x=600, y=490, width=300)

                # creating region label
                self.lb14_add = tk.Label(
                    self.tab1,
                    text="Available Regions:",
                    font=("Helvetica", 12, "bold"),
                    bg="#EFEFEF",
                    underline=True,
                    borderwidth=5,
                )
                self.lb14_add.place(x=60, y=450)

                # creating region and sub region combobox
                self.lb12 = tk.Label(
                    self.tab1, text="Region:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb12.place(x=60, y=480)

                self.textfield12_add = ttk.Combobox(
                    self.tab1,
                    font=("Helvetica", 10),
                    values=list(self.main_region.keys()),
                    state="readonly",
                )
                self.textfield12_add.place(x=180, y=480, width=300)
                self.textfield12_add.bind("<<ComboboxSelected>>", callbackFunc)

                self.lb13 = tk.Label(
                    self.tab1, text="Sub Region:", font=("Helvetica", 10), bg="#EFEFEF"
                )
                self.lb13.place(x=500, y=480)

                self.textfield13_add = ttk.Combobox(
                    self.tab1, font=("Helvetica", 10), state="readonly"
                )
                self.textfield13_add.place(x=600, y=480, width=300)

                self.btn_add_ok1 = ttk.Button(
                    self.tab1, text="Save Booking", command=self.validate
                )
                self.btn_add_ok1.place(x=400, y=520, width=200, height=35)

            # function to validate the booking input values
            def validate(self):
                messagebox.showinfo(
                    "Warning", "Confirm Booking? Re-ensure fileds have been filled!"
                )
                if (
                    (str(self.textfield1_add.get()) != "")
                    and (str(self.textfield2_add.get()) != "")
                    and (str(self.textfield3_add.get()) != "")
                    and (str(self.textfield4_add.get()) != "")
                    and (str(self.textfield7_add.get()) != "")
                    and (str(self.textfield8_add.get()) != "")
                    and (str(self.textfield9_add.get()) != "")
                    and (str(self.textfield10_add.get()) != "")
                    and (str(self.textfield11_add.get()) != "")
                    and (str(self.textfield12_add.get()) != "")
                    and (str(self.textfield13_add.get()) != "")
                ):

                    # saving customer summary details
                    f = asksaveasfile(
                        initialfile="Summary.txt",
                        defaultextension=".txt",
                        filetypes=[("txt", "*.*")],
                    )
                    a = (
                        "Customer Camping Trip Summary\n\n"
                        + "Customer Name: "
                        + str(self.textfield7_add.get())
                        + "\nID Card Number: "
                        + str(self.textfield8_add.get())
                        + "\nJourney timeline: "
                        + str(self.textfield10_add.get())
                        + " - "
                        + str(self.textfield11_add.get())
                        + "\nCamping Van: "
                        + str(self.textfield1_add.get())
                        + "\nRegion: "
                        + str(self.textfield12_add.get())
                        + " Sub Region: "
                        + str(self.textfield13_add.get())
                        + "\n\nTotal Price: "
                        + str(self.textfield4_add.get() + "$")
                    )
                    f.write(a)
                    f.close()

                    # adding booked trip details into csv databse
                    field_names = [
                        "Van Name",
                        "Van type",
                        "Van capacity",
                        "Van Price",
                        "Customer Name",
                        "ID Number",
                        "No of Travellers",
                        "Journey Date",
                        "Return Date",
                        "Region",
                        "Sub Region",
                    ]

                    booking = {
                        "Van Name": str(self.textfield1_add.get()),
                        "Van type": str(self.textfield2_add.get()),
                        "Van capacity": str(self.textfield3_add.get()),
                        "Van Price": str(self.textfield4_add.get()),
                        "Customer Name": str(self.textfield7_add.get()),
                        "ID Number": str(self.textfield8_add.get()),
                        "No of Travellers": str(self.textfield9_add.get()),
                        "Journey Date": str(self.textfield10_add.get()),
                        "Return Date": str(self.textfield11_add.get()),
                        "Region": str(self.textfield12_add.get()),
                        "Sub Region": str(self.textfield13_add.get()),
                    }

                    # opening csv database
                    with open("bookings.csv", "a") as f_object:
                        # creating csv writer and adding column names
                        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                        # writing data to csv file
                        dictwriter_object.writerow(booking)
                        # close the file object
                        f_object.close()

                    # messagebox
                    messagebox.showinfo(
                        "Successfully",
                        "Summary created, Details added to database. Successfully!",
                    )
                    window_user_login.destroy()
                    user_login()
                else:
                    messagebox.showerror(
                        "Operation failed",
                        "The details cannot be saved, Enter valid data!",
                    )

        # function to exit the program
        def exits():
            msgobj_close = messagebox.askquestion(
                "Warning",
                "Your changes have not been saved. " "Confirm Exit?",
                icon="warning",
            )
            if msgobj_close == "yes":
                exit(0)
            else:
                pass

        # creating tkinters window
        window_user_login = tk.Tk()
        window_user_login.config(background="#EFEFEF")
        # creating window title
        label_title = tk.Label(
            window_user_login,
            text="Solent Campers - Advisor Panel",
            font=("times new roman", 40, "bold"),
            bd=15,
            relief="ridge",
            bg="black",
            fg="white",
        )
        label_title.pack(side=tk.TOP, fill=tk.X)
        # creating object of User class
        User(window_user_login)
        # creating title
        window_user_login.title("Solent Campers")
        window_user_login.geometry("1000x680")
        window_user_login.resizable(False, False)
        window_user_login.protocol("WM_DELETE_WINDOW", exits)
        window_user_login.mainloop()

    # function to show user login window
    user_login()


if __name__ == "__main__":
    # calling the main function
    main()
