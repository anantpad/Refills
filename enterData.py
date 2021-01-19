import tkinter as tk

from connectSQL import executeScriptsFromFile

data = executeScriptsFromFile('sqlCommand.sql')
PATIENTFIRSTNAME = []
PATIENTLASTNAME = []
PATIENTGENDER = []
PATIENTDOB = []
PATIENTADDRESSLINE1 = []
PATIENTCITY = []
PATIENTSTATECODE = []
PATIENTZIP = []
PATIENTPHONE = []

for i in data:
    if i[12] not in PATIENTFIRSTNAME:
        PATIENTFIRSTNAME.append(i[12])

for i in data:
    if i[13] not in PATIENTLASTNAME:
        PATIENTLASTNAME.append(i[13])

PRESCRNUMS = []
for i in data:
    PRESCRNUMS.append(i[0])

OPTIONS = ["None",
           "Refill",
           "RxChange - Type D (Drug Utilization Review)",
           "RxChange - Type G (Generic Substitution)",
           "RxChange - Type OS (Out of Stock)",
           "RxChange - Type P (Prior Authorization)",
           "RxChange - Type S (Script Clarification)",
           "RxChange - Type T (Therapeutic Interchange)",
           "RxChange - Type U (Prescriber Authorization)"]


def closeapp():
    window.destroy()


# window
window = tk.Tk()
window.title("Enter Data")
window.resizable(height="true", width="true")
# window.minsize(height=500, width=500)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# topFrame
# get data for Message Type
top_Frame = tk.Frame(window, highlightbackground="black", highlightthickness=1, height=2)
top_Frame.grid(row=0, column=0, sticky="NESW")
top_Frame.grid_rowconfigure(0, weight=1)
top_Frame.grid_columnconfigure(0, weight=1)
heading = tk.Label(top_Frame, text="Create Pharmacy Messages", font=("Calibri", "12"), fg="red")
heading.grid(row=0, column=0, sticky="")

# midFrame
mid_Frame = tk.Frame(window, borderwidth=2, highlightbackground="black", highlightthickness=1)
mid_Frame.grid(row=1, column=0, rowspan=3, columnspan=2, padx=20, pady=10)

content0 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content0.grid(row=0, column=1)  # MessageType
content1 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content1.grid(row=1, column=0, rowspan=8, columnspan=2)  # Patient
content2 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content2.grid(row=2, column=0, rowspan=8, columnspan=2)  # Provider
content3 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content3.grid(row=1, column=1, rowspan=8, columnspan=2)  # Pharmacy
content4 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content4.grid(row=0, column=1, rowspan=8, columnspan=2)  # Drug

# Message Type field to start with
messageType = tk.Label(content0, text="Message Type", anchor="w")
mTEntry = tk.StringVar(content0)
mTEntry.set(OPTIONS[0])
messageTypeEntry = tk.OptionMenu(content0, mTEntry, *OPTIONS)

patfname = tk.Label(content1, text="First Name:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patfname.grid(row=0, column=0)
patfname1 = tk.StringVar(content1)
patfname1.set(PATIENTFIRSTNAME[0])
patfname_entry = tk.OptionMenu(content1, patfname1, *PATIENTFIRSTNAME)
patfname_entry.grid(row=0, column=1)

patlname = tk.Label(content1, text="Last Name:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patlname.grid(row=1, column=0)
patlname1 = tk.StringVar(content1)
patlname1.set(PATIENTLASTNAME[0])
patlname_entry = tk.OptionMenu(content1, patlname1, *PATIENTLASTNAME)
patlname_entry.grid(row=1, column=1)

patgender = tk.Label(content1, text="Gender:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patgender.grid(row=2, column=0)
patgender1 = tk.StringVar()
patfname_entry = tk.Entry(content1, textvariable=patgender1, width=12)
patfname_entry.grid(row=2, column=1)

pataddress = tk.Label(content1, text="Address Line 1:", font=("calibri", "11"), width=12, pady=2, anchor="w")
pataddress.grid(row=4, column=0)
pataddress = tk.StringVar()
pataddress_entry = tk.Entry(content1, textvariable=pataddress, width=12)
pataddress_entry.grid(row=4, column=1)

# Patient Info

# PatientName


# Gender
# DOB
# AddressLine1
# City
# StateCode
# Zip
# PhoneNumber

# prescriptionNumber = tk.Label(content3, text="Prescription Number")
# prescNum = tk.StringVar(content3)
# prescNum.set(PRESCRNUMS[0])
# pNum = tk.OptionMenu(content3, prescNum, *PRESCRNUMS)

bottom_Frame = tk.Frame(window, highlightbackground="black", highlightthickness=1)
bottom_Frame.grid(row=4, column=0, pady=10, sticky="e")
close = tk.Button(bottom_Frame, text="Close", font=("calibri", "12"), bg="#fff", fg="#4b4f56", command=closeapp,
                  width=12)
close.grid(pady=5, padx=10, row=0, column=1)

heading.pack(side="top")
messageType.pack(side="left", padx=2, pady=2)
messageTypeEntry.pack(side="right", padx=2, pady=2)
# prescriptionNumber.pack(side="left", padx=2, pady=2)
# pNum.pack(side="left", padx=2, pady=2)

window.mainloop()
