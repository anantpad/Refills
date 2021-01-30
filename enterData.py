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

PRESCRNUMS = ["NONE"]

def getMedications(prescnum):
    for k in data:
        if str(prescnum) in k[13]:
            meddescription.set(k[0])
            ndcvalue.set(k[14])
            medqty.set(k[15])
            medInstructions.set(k[16])
            return meddescription.get(), ndcvalue.get(), medqty.get(), medInstructions.get()

def updatePresc(patid):
    PRESCRNUMS = []
    for j in data:
        if str(patid) in j[5]:
            if j[13] not in PRESCRNUMS:
                PRESCRNUMS.append(j[13])
    prescnum.set(PRESCRNUMS[0])
    prescnum_entry = tk.OptionMenu(mid_Frame, prescnum, *PRESCRNUMS).grid(row = 1, column = 2, columnspan = 2,
                                                                          padx = (5, 5),
                                                                          pady = (2, 6))
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
    pMed = prescnum.get()
    pPreNum = meddescription.get()
    pNDC = ndcvalue.get()
    pQty = medqty.get()
    pInstr = medInstructions.get()
    pfname = patfname1.get()
    plname = patlname1.get()
    return pName, pGender, pDOB, pAddress, pCity, pState, pZip, pPhone, pPreNum, pMed, pNDC, pQty, pInstr, pfname, plname


# window
window = tk.Tk()
window.title("Enter Data")
window.resizable(height = "true", width = "true")
# window.minsize(height=400, width=800)
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)

# topFrame
top_Frame = tk.Frame(window, bd = 2, bg = "#15396a")
# midFrame
mid_Frame = tk.Frame(window, bd = 2, bg = "#D8BBAA")
mid_Frame2 = tk.Frame(window, bd = 2, bg = "#D8BBAA")
# bottomFrame
bottom_Frame = tk.Frame(window, bd = 2, bg = "#15396a")

# grids
top_Frame.grid(columnspan = 4, padx = 10, pady = 10)
mid_Frame.grid(columnspan = 4, padx = 10, pady = 10)
mid_Frame2.grid(columnspan = 5, padx = 10, pady = 10)
bottom_Frame.grid(columnspan = 4, padx = 10, pady = 10)

# declare variables
mTEntry = tk.StringVar(mid_Frame)
patname1 = tk.StringVar(mid_Frame)
patfname1 = tk.StringVar(mid_Frame)
patlname1 = tk.StringVar(mid_Frame)
patid1 = tk.StringVar()
patgender1 = tk.StringVar()
patdob1 = tk.StringVar()
pataddress1 = tk.StringVar()
patcity1 = tk.StringVar()
patstate1 = tk.StringVar()
patzip1 = tk.StringVar()
patphone1 = tk.StringVar()
prescnum = tk.StringVar(mid_Frame)
meddescription = tk.StringVar(mid_Frame2)
ndcvalue = tk.StringVar(mid_Frame2)
medqty = tk.StringVar(mid_Frame2)
medInstructions = tk.StringVar(mid_Frame2)

heading = tk.Label(top_Frame, text = "Create Pharmacy Messages", font = ("Calibri", "12", "bold"), width = 70,
                   bg = "#15396A", fg = "white")
heading.grid(row = 0, column = 0, rowspan = 1, columnspan = 5)

patname = tk.Label(mid_Frame, text = "Patient Name:", font = ("calibri", "11"), width = 15, anchor = "w", bd = 2)
patname1.set(PATIENTNAME[0])
patname_entry = tk.OptionMenu(mid_Frame, patname1, *PATIENTNAME)
patname_entry.config(width = 15)
UpdatePatient = tk.Button(mid_Frame, text = "Update Patient", font = ("calibri", "12", "bold"), bg = "#A4606C",
                          fg = "#ffffff",
                          activebackground = "#b6afaf", activeforeground = "#0d0c0c", width = 15,
                          command = lambda: update_patient(),
                          anchor = "center")
messageType = tk.Label(mid_Frame, text = "Message Type:", bd = 2, font = ("calibri", "11"), width = 15, anchor = "w")
mTEntry.set(OPTIONS[1])
messageTypeEntry = tk.OptionMenu(mid_Frame, mTEntry, *OPTIONS)
messageTypeEntry.config(width = 15)

UpdatePrescription = tk.Button(mid_Frame, text = "Update Script #", font = ("calibri", "12", "bold"), bg = "#A4606C",
                               fg = "#ffffff",
                               activebackground = "#b6afaf", activeforeground = "#0d0c0c", width = 15,
                               command = lambda: getMedications(prescnum.get()),
                               anchor = "center")

# grid
patname.grid(row = 0, column = 0, padx = (15, 0), pady = (6, 2))
patname_entry.grid(row = 0, column = 1, padx = (5, 0), pady = (6, 2))
UpdatePatient.grid(row = 0, column = 2, padx = (5, 0), pady = (6, 2))
UpdatePrescription.grid(row = 0, column = 4, padx = (5, 15), pady = (6, 2))
messageType.grid(row = 1, column = 0, padx = (15, 0), pady = (2, 6))
messageTypeEntry.grid(row = 1, column = 1, padx = (5, 5), pady = (2, 6))

patid = tk.Label(mid_Frame2, text = "PatientId:", font = ("calibri", "11"), width = 15, anchor = "w")
patid_entry = tk.Label(mid_Frame2, textvariable = patid1, font = ("calibri", "11"), width = 15, anchor = "w")

patgender = tk.Label(mid_Frame2, text = "Gender:", font = ("calibri", "11"), width = 15, anchor = "w")
patgender_entry = tk.Label(mid_Frame2, textvariable = patgender1, font = ("calibri", "11"), width = 15)

patdob = tk.Label(mid_Frame2, text = "Date Of Birth:", font = ("calibri", "11"), width = 15, anchor = "w")
patdob_entry = tk.Label(mid_Frame2, textvariable = patdob1, font = ("calibri", "11"), width = 15, anchor = "w")

pataddress = tk.Label(mid_Frame2, text = "Address Line 1:", font = ("calibri", "11"), width = 15, anchor = "w")
pataddress_entry = tk.Label(mid_Frame2, textvariable = pataddress1, font = ("calibri", "11"), width = 15, anchor = "w",
                            wraplength = 100)

patcity = tk.Label(mid_Frame2, text = "City:", font = ("calibri", "11"), width = 15, anchor = "w")
patcity_entry = tk.Label(mid_Frame2, textvariable = patcity1, font = ("calibri", "11"), width = 15, anchor = "w")

patstate = tk.Label(mid_Frame2, text = "State:", font = ("calibri", "11"), width = 15, anchor = "w")
patstate_entry = tk.Label(mid_Frame2, textvariable = patstate1, font = ("calibri", "11"), width = 15, anchor = "w")

patzip = tk.Label(mid_Frame2, text = "Zip:", font = ("calibri", "11"), width = 15, anchor = "w")
patzip_entry = tk.Label(mid_Frame2, textvariable = patzip1, font = ("calibri", "11"), width = 15, anchor = "w")

patphone = tk.Label(mid_Frame2, text = "Phone:", font = ("calibri", "11"), width = 15, anchor = "w")
patphone_entry = tk.Label(mid_Frame2, textvariable = patphone1, font = ("calibri", "11"), width = 15, anchor = "w")

# grid
patid.grid(row = 2, column = 0, padx = (5, 2), pady = (6, 2))
patid_entry.grid(row = 2, column = 1, padx = (5, 2), pady = (6, 2))
patgender.grid(row = 3, column = 0, padx = (5, 2), pady = 2)
patgender_entry.grid(row = 3, column = 1, padx = (5, 2), pady = 2)
patdob.grid(row = 4, column = 0, padx = (5, 2), pady = 2)
patdob_entry.grid(row = 4, column = 1, padx = (5, 2), pady = 2)
pataddress.grid(row = 5, column = 0, padx = (5, 2), pady = 2)
pataddress_entry.grid(row = 5, column = 1, padx = (5, 2), pady = 2)
patcity.grid(row = 6, column = 0, padx = (5, 2), pady = 2)
patcity_entry.grid(row = 6, column = 1, padx = (5, 2), pady = 2)
patstate.grid(row = 7, column = 0, padx = (5, 2), pady = 2)
patstate_entry.grid(row = 7, column = 1, padx = (5, 2), pady = 2)
patzip.grid(row = 8, column = 0, padx = (5, 2), pady = 2)
patzip_entry.grid(row = 8, column = 1, padx = (5, 2), pady = 2)
patphone.grid(row = 9, column = 0, padx = (5, 2), pady = 2)
patphone_entry.grid(row = 9, column = 1, padx = (5, 2), pady = 2)

blank1 = tk.Label(mid_Frame2, text = "", bg = "#D8BBAA", width = 5)

medlabel = tk.Label(mid_Frame2, text = "Script#:", font = ("calibri", "11"), width = 15, anchor = "w")
meddescription_entry = tk.Label(mid_Frame2, textvariable = meddescription, font = ("calibri", "11"), width = 15,
                                wraplength = 100)
#
ndclabel = tk.Label(mid_Frame2, text = "NDCID:", font = ("calibri", "11"), width = 15, anchor = "w")
ndcvalue_entry = tk.Label(mid_Frame2, textvariable = ndcvalue, font = ("calibri", "11"), width = 15)
#
qtylabel = tk.Label(mid_Frame2, text = "Quantity:", font = ("calibri", "11"), width = 15, anchor = "w")
medqty_entry = tk.Label(mid_Frame2, textvariable = medqty, font = ("calibri", "11"), width = 15)
#
instrlabel = tk.Label(mid_Frame2, text = "Instructions:", font = ("calibri", "11"), width = 15, anchor = "w")
medInstructions_entry = tk.Label(mid_Frame2, textvariable = medInstructions, font = ("calibri", "11"), width = 15,
                                 wraplength = 100)

# grid
blank1.grid(row = 2, column = 2)

medlabel.grid(row = 2, column = 3, padx = (5, 2), pady = (6, 2))
meddescription_entry.grid(row = 2, column = 4, padx = (5, 2), pady = (6, 2))
ndclabel.grid(row = 3, column = 3, padx = (5, 2), pady = 2)
ndcvalue_entry.grid(row = 3, column = 4, padx = (5, 2), pady = 2)
qtylabel.grid(row = 4, column = 3, padx = (5, 2), pady = 2)
medqty_entry.grid(row = 4, column = 4, padx = (5, 2), pady = 2)
instrlabel.grid(row = 5, column = 3, padx = (5, 2), pady = 2)
medInstructions_entry.grid(row = 5, column = 4, padx = (5, 2), pady = 2)

submit = tk.Button(bottom_Frame, text = "Submit", font = ("calibri", "12", "bold"), bg = "#A4606C", fg = "#ffffff",
                   activebackground = "#b6afaf", activeforeground = "#0d0c0c", width = 10, command = submit_data,
                   anchor = "center")
close = tk.Button(bottom_Frame, text = "Close", font = ("calibri", "12", "bold"), bg = "#A4606C", fg = "#ffffff",
                  activebackground = "#b6afaf", activeforeground = "#0d0c0c", width = 10, command = closeapp,
                  anchor = "center")

submit.grid(row = 0, column = 1, padx = 95, pady = 2, ipadx = 1, ipady = 1)
close.grid(row = 0, column = 2, padx = 95, pady = 2, ipadx = 1, ipady = 1)

window.mainloop()
