import tkinter as tk

from connectSQL import executeScriptsFromFile

data = executeScriptsFromFile("sqlCommand.sql")
patientData = executeScriptsFromFile("patient.sql")

OPTIONS = ["None",
           "Refill",
           "RxChange - Type D (Drug Utilization Review)",
           "RxChange - Type G (Generic Substitution)",
           "RxChange - Type OS (Out of Stock)",
           "RxChange - Type P (Prior Authorization)",
           "RxChange - Type S (Script Clarification)",
           "RxChange - Type T (Therapeutic Interchange)",
           "RxChange - Type U (Prescriber Authorization)"]

PATIENTNAME = []
PATIENTFIRST = []
PATIENTLAST = []
for i in patientData:
    if i[0] not in PATIENTNAME:
        PATIENTNAME.append(i[0])

PRESCRNUMS = []

MEDICATIONS = []


def getMedications(prescnum):
    MEDICATIONS = []
    for k in data:
        if str(prescnum) in k[0]:
            meddescription.set(k[13])
            ndcvalue.set(k[14])
            medqty.set(k[15])
            medInstructions.set(k[16])
            return meddescription.get(), ndcvalue.get(), medqty.get(), medInstructions.get()


def updatePresc(patid):
    PRESCRNUMS = []
    for j in data:
        if str(patid) in j[5]:
            if j[0] not in PRESCRNUMS:
                PRESCRNUMS.append(j[0])
    prescnum.set(PRESCRNUMS[0])
    prescnum_entry = tk.OptionMenu(content2, prescnum, *PRESCRNUMS).grid(row=0, column=1)
    return PRESCRNUMS, prescnum, prescnum_entry


def update_patient():
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
            patfname1.set(i[9])
            patlname1.set(i[10])
            updatePresc(patid1.get())
            return patid1.get(), patgender1.get(), patdob1.get(), pataddress1.get(), patcity1.get(), patstate1.get(), \
                   patzip1.get(), patphone1.get(), patfname1.get(), patlname1.get()


def closeapp():
    window.destroy()


def submit_data():
    pName = patname1.get()
    pGender = patgender1.get()
    pDOB = patdob1.get()
    pAddress = pataddress1.get()
    pCity = patcity1.get()
    pState = patstate1.get()
    pZip = patzip1.get()
    pPhone = patphone1.get()
    pPreNum = prescnum.get()
    pMed = meddescription.get()
    pNDC = ndcvalue.get()
    pQty = medqty.get()
    pInstr = medInstructions.get()
    pfname = patfname1.get()
    plname = patlname1.get()
    return pName, pGender, pDOB, pAddress, pCity, pState, pZip, pPhone, pPreNum, pMed, pNDC, pQty, pInstr, pfname, plname


# window
window = tk.Tk()
window.title("Enter Data")
window.resizable(height="true", width="true")
# window.minsize(height=400, width=800)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# topFrame
# get data for Message Type
top_Frame = tk.Frame(window, highlightthickness=1)
top_Frame.grid(row=0, column=0, sticky="NESW", pady=10)
# top_Frame.grid_rowconfigure(0, weight=1)
# top_Frame.grid_columnconfigure(0, weight=1)
heading = tk.Label(top_Frame, text="Create Pharmacy Messages", font=("Calibri", "12"), fg="red")
# heading.grid(row=0, column=0)
heading.pack(side="top")

# midFrame
mid_Frame = tk.Frame(window, highlightthickness=1)
mid_Frame.grid(row=1, column=0, sticky="nesw", pady=10)

content0 = tk.Frame(mid_Frame, highlightthickness=1)
content0.grid(row=0, column=0, pady=5, columnspan=2, sticky="nesw")  # MessageType
# content0.pack(side="top")

# Message Type field to start with
messageType = tk.Label(content0, text="Message Type:", font=("calibri", "11"), width=15, anchor="w")
messageType.grid(row=0, column=0, padx=5, pady=2)
mTEntry = tk.StringVar(content0)
mTEntry.set(OPTIONS[1])
messageTypeEntry = tk.OptionMenu(content0, mTEntry, *OPTIONS)
messageTypeEntry.grid(row=0, column=1, padx=2, pady=2)

patname = tk.Label(content0, text="Patient Name:", font=("calibri", "11"), width=15, anchor="w")
patname.grid(row=0, column=2, padx=5, pady=2)
patname1 = tk.StringVar(content0)
patname1.set(PATIENTNAME[0])
patname_entry = tk.OptionMenu(content0, patname1, *PATIENTNAME)
patname_entry.grid(row=0, column=3, padx=2, pady=2)

patfname1 = tk.StringVar(content0)

patlname1 = tk.StringVar(content0)

update = tk.Button(content0, text="Update Patient Details", font=("calibri", "11"), command=lambda: update_patient(),
                   bg="#fff", fg="#4b4f56")
update.grid(row=0, column=4, padx=10, pady=2)

content1 = tk.Frame(mid_Frame, highlightthickness=1)
content1.grid(row=1, column=0, columnspan=2, pady=5, sticky="nesw")  # Patient

patid = tk.Label(content1, text="PatientId:", font=("calibri", "11"), width=15, anchor="w")
patid.grid(row=0, column=0, padx=5, pady=2)
patid1 = tk.StringVar()
patid_entry = tk.Label(content1, textvariable=patid1, font=("calibri", "11"), width=15, anchor="w")
patid_entry.grid(row=0, column=1)

patgender = tk.Label(content1, text="Gender:", font=("calibri", "11"), width=15, anchor="w")
patgender.grid(row=1, column=0, padx=5, pady=2)
patgender1 = tk.StringVar()
patgender_entry = tk.Label(content1, textvariable=patgender1, font=("calibri", "11"), width=15, anchor="w")
patgender_entry.grid(row=1, column=1)

patdob = tk.Label(content1, text="Date Of Birth:", font=("calibri", "11"), width=15, anchor="w")
patdob.grid(row=2, column=0, padx=5, pady=2)
patdob1 = tk.StringVar()
patdob_entry = tk.Label(content1, textvariable=patdob1, font=("calibri", "11"), width=15, anchor="w")
patdob_entry.grid(row=2, column=1)

pataddress = tk.Label(content1, text="Address Line 1:", font=("calibri", "11"), width=15, anchor="w")
pataddress.grid(row=3, column=0, padx=5, pady=2)
pataddress1 = tk.StringVar()
pataddress_entry = tk.Label(content1, textvariable=pataddress1, font=("calibri", "11"), width=15, anchor="w")
pataddress_entry.grid(row=3, column=1)

patcity = tk.Label(content1, text="City:", font=("calibri", "11"), width=15, anchor="w")
patcity.grid(row=4, column=0, padx=5, pady=2)
patcity1 = tk.StringVar()
patcity_entry = tk.Label(content1, textvariable=patcity1, font=("calibri", "11"), width=15, anchor="w")
patcity_entry.grid(row=4, column=1)

patstate = tk.Label(content1, text="State:", font=("calibri", "11"), width=15, anchor="w")
patstate.grid(row=5, column=0, padx=5, pady=2)
patstate1 = tk.StringVar()
patstate_entry = tk.Label(content1, textvariable=patstate1, font=("calibri", "11"), width=15, anchor="w")
patstate_entry.grid(row=5, column=1)

patzip = tk.Label(content1, text="Zip:", font=("calibri", "11"), width=15, anchor="w")
patzip.grid(row=6, column=0, padx=5, pady=2)
patzip1 = tk.StringVar()
patzip_entry = tk.Label(content1, textvariable=patzip1, font=("calibri", "11"), width=15, anchor="w")
patzip_entry.grid(row=6, column=1)

patphone = tk.Label(content1, text="Phone:", font=("calibri", "11"), width=15, anchor="w")
patphone.grid(row=7, column=0, padx=5, pady=2)
patphone1 = tk.StringVar()
patphone_entry = tk.Label(content1, textvariable=patphone1, font=("calibri", "11"), width=15, anchor="w")
patphone_entry.grid(row=7, column=1)

content2 = tk.Frame(mid_Frame, highlightthickness=1)
content2.grid(row=1, column=1, columnspan=2, pady=5, sticky="nesw")  # Drug

prescnumLabel = tk.Label(content2, text="Prescription Number:", font=("calibri", "11"), width=20,
                         anchor="w").grid(row=0, column=0, padx=5, pady=2)
prescnum = tk.StringVar(content2)
prescnum_entry = tk.OptionMenu(content2, prescnum, value="").grid(row=0, column=1, padx=5, pady=2)

update = tk.Button(content2, text="Update Medication", font=("calibri", "11"),
                   command=lambda: getMedications(prescnum.get()),
                   bg="#fff", fg="#4b4f56")
update.grid(row=1, column=0, padx=5, pady=2)

medlabel = tk.Label(content2, text="Medication:", font=("calibri", "11"), width=20, pady=2, anchor="w").grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=5,
                                                                                                             pady=2)
meddescription = tk.StringVar(content2)
meddescription_entry = tk.Label(content2, textvariable=meddescription, font=("calibri", "11"), width=30).grid(row=2,
                                                                                                              column=1)

ndclabel = tk.Label(content2, text="NDCID:", font=("calibri", "11"), width=20, pady=2, anchor="w").grid(row=3, column=0,
                                                                                                        padx=5, pady=2)
ndcvalue = tk.StringVar(content2)
ndcvalue_entry = tk.Label(content2, textvariable=ndcvalue, font=("calibri", "11"), width=30).grid(row=3, column=1)

qtylabel = tk.Label(content2, text="Quantity:", font=("calibri", "11"), width=20, pady=2, anchor="w").grid(row=4,
                                                                                                           column=0,
                                                                                                           padx=5,
                                                                                                           pady=2)
medqty = tk.StringVar(content2)
medqty_entry = tk.Label(content2, textvariable=medqty, font=("calibri", "11"), width=30).grid(row=4, column=1)

instrlabel = tk.Label(content2, text="Instructions:", font=("calibri", "11"), width=20, pady=2, anchor="w").grid(row=5,
                                                                                                                 column=0,
                                                                                                                 padx=5,
                                                                                                                 pady=2)
medInstructions = tk.StringVar(content2)
medInstructions_entry = tk.Label(content2, textvariable=medInstructions, font=("calibri", "11"), width=30).grid(row=5,
                                                                                                                column=1)

bottom_Frame = tk.Frame(window, highlightthickness=1)
bottom_Frame.grid(row=4, column=0, sticky="nesw", pady=10)

submit = tk.Button(bottom_Frame, text="Submit", font=("calibri", "12"), bg="#fff", fg="#4b4f56", width=15,
                   command=submit_data)
submit.grid(pady=5, padx=10, row=0, column=1)
close = tk.Button(bottom_Frame, text="Close", font=("calibri", "12"), bg="#fff", fg="#4b4f56", command=closeapp,
                  width=15)
close.grid(pady=5, padx=10, row=0, column=2)

window.mainloop()
