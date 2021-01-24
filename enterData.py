import tkinter as tk

from connectSQL import executeScriptsFromFile

data = executeScriptsFromFile("sqlCommand.sql")
patientData = executeScriptsFromFile("patient.sql")

PATIENTNAME = []
for i in patientData:
    if i[0] not in PATIENTNAME:
        PATIENTNAME.append(i[0])
print(PATIENTNAME)

OPTIONS = ["None",
           "Refill",
           "RxChange - Type D (Drug Utilization Review)",
           "RxChange - Type G (Generic Substitution)",
           "RxChange - Type OS (Out of Stock)",
           "RxChange - Type P (Prior Authorization)",
           "RxChange - Type S (Script Clarification)",
           "RxChange - Type T (Therapeutic Interchange)",
           "RxChange - Type U (Prescriber Authorization)"]

PRESCRNUMS = []


def updatePresc(patid):
    PRESCRNUMS = []
    for j in data:
        if str(patid) in j[5]:
            if j[0] not in PRESCRNUMS:
                PRESCRNUMS.append(j[0])
    prescnum.set(PRESCRNUMS[0])
    prescnum_entry = tk.OptionMenu(content2, prescnum, *PRESCRNUMS).grid(row=0, column=1)
    return PRESCRNUMS, prescnum, prescnum_entry


def updatePatient():
    pName = patname1.get()
    for i in patientData:
        if pName in i[0]:
            patid1.set(i[1])
            patgender1.set(i[2])
            patdob1.set(i[3])
            pataddress1.set(i[4])
            patcity1.set(i[5])
            patstate1.set(i[6])
            patzip1.set(i[7])
            patphone1.set(i[8])
            updatePresc(patid1.get())
            return patid1.get(), patgender1.get(), patdob1.get(), pataddress1.get(), patcity1.get(), patstate1.get(), patzip1.get(), patphone1.get()


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
top_Frame = tk.Frame(window, highlightthickness=1)
top_Frame.grid(row=0, column=0, sticky="NESW")
# top_Frame.grid_rowconfigure(0, weight=1)
# top_Frame.grid_columnconfigure(0, weight=1)
heading = tk.Label(top_Frame, text="Create Pharmacy Messages", font=("Calibri", "12"), fg="red")
heading.grid(row=0, column=0)

# midFrame
mid_Frame = tk.Frame(window, borderwidth=2, highlightthickness=1)
mid_Frame.grid(row=1, column=0, sticky="nesw")

content0 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content0.grid(row=0, column=0)  # MessageType

# Message Type field to start with
messageType = tk.Label(content0, text="Message Type", anchor="n")
mTEntry = tk.StringVar(content0)
mTEntry.set(OPTIONS[1])
messageTypeEntry = tk.OptionMenu(content0, mTEntry, *OPTIONS)

content1 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content1.grid(row=1, column=0)  # Patient

patname = tk.Label(content1, text="Patient Name:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patname.grid(row=0, column=0)
patname1 = tk.StringVar(content1)
patname1.set(PATIENTNAME[0])
patname_entry = tk.OptionMenu(content1, patname1, *PATIENTNAME)
patname_entry.grid(row=0, column=1)

patid = tk.Label(content1, text="PatientId:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patid.grid(row=1, column=0)
patid1 = tk.StringVar()
patid_entry = tk.Entry(content1, textvariable=patid1, width=12)
patid_entry.grid(row=1, column=1)

patgender = tk.Label(content1, text="Gender:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patgender.grid(row=2, column=0)
patgender1 = tk.StringVar()
patgender_entry = tk.Entry(content1, textvariable=patgender1, width=12)
patgender_entry.grid(row=2, column=1)

patdob = tk.Label(content1, text="Date Of Birth:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patdob.grid(row=3, column=0)
patdob1 = tk.StringVar()
patdob_entry = tk.Entry(content1, textvariable=patdob1, width=12)
patdob_entry.grid(row=3, column=1)

pataddress = tk.Label(content1, text="Address Line 1:", font=("calibri", "11"), width=12, pady=2, anchor="w")
pataddress.grid(row=4, column=0)
pataddress1 = tk.StringVar()
pataddress_entry = tk.Entry(content1, textvariable=pataddress1, width=12)
pataddress_entry.grid(row=4, column=1)

patcity = tk.Label(content1, text="City:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patcity.grid(row=5, column=0)
patcity1 = tk.StringVar()
patcity_entry = tk.Entry(content1, textvariable=patcity1, width=12)
patcity_entry.grid(row=5, column=1)

patstate = tk.Label(content1, text="State:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patstate.grid(row=6, column=0)
patstate1 = tk.StringVar()
patstate_entry = tk.Entry(content1, textvariable=patstate1, width=12)
patstate_entry.grid(row=6, column=1)

patzip = tk.Label(content1, text="Zip:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patzip.grid(row=7, column=0)
patzip1 = tk.StringVar()
patzip_entry = tk.Entry(content1, textvariable=patzip1, width=12)
patzip_entry.grid(row=7, column=1)

patphone = tk.Label(content1, text="Phone:", font=("calibri", "11"), width=12, pady=2, anchor="w")
patphone.grid(row=8, column=0)
patphone1 = tk.StringVar()
patphone_entry = tk.Entry(content1, textvariable=patphone1, width=12)
patphone_entry.grid(row=8, column=1)

content2 = tk.Frame(mid_Frame, bd=2, highlightbackground="black")
content2.grid(row=1, column=1)  # Drug

prescnumLabel = tk.Label(content2, text="Prescription Number:", font=("calibri", "11"), width=20, pady=2, anchor="w")
prescnumLabel.grid(row=0, column=0)
prescnum = tk.StringVar(content2)
# prescnum_entry = tk.OptionMenu(content2, prescnum, *PRESCRNUMS)


bottom_Frame = tk.Frame(window, highlightthickness=1)
bottom_Frame.grid(row=4, column=0, pady=10, sticky="e")
update = tk.Button(bottom_Frame, text="Update", font=("calibri", "12"), command=lambda: updatePatient(), bg="#fff",
                   fg="#4b4f56", width=12)
update.grid(pady=5, padx=10, row=0, column=0)
submit = tk.Button(bottom_Frame, text="Submit", font=("calibri", "12"), bg="#fff", fg="#4b4f56", width=12)
submit.grid(pady=5, padx=10, row=0, column=1)
close = tk.Button(bottom_Frame, text="Close", font=("calibri", "12"), bg="#fff", fg="#4b4f56", command=closeapp,
                  width=12)
close.grid(pady=5, padx=10, row=0, column=2)

heading.pack(side="top")
messageType.pack(side="left", padx=2, pady=2)
messageTypeEntry.pack(side="left", padx=2, pady=2)

window.mainloop()
