# import modules
from tkinter import *
from tkinter import messagebox
import requests


def Getifsc(query):
	"""

	:param query:
	"""
	try:
		IFSC_Code = query
		URL = "https://ifsc.razorpay.com/"
		result = requests.get(URL + IFSC_Code).json()
		Centre.set(result['CENTRE'])
		contact.set(result['CONTACT'])
		UPI.set(result['UPI'])
		CITY.set(result['CITY'])
		STATE.set(result['STATE'])
		DISTRICT.set(result['DISTRICT'])
		IMPS.set(result['IMPS'])
		ADDRESS.set(result['ADDRESS'])
		BRANCH.set(result['BRANCH'])
		STD.set(result['STD CODE'])
		MICR.set(result['MICR CODE'])
		BANK.set(result['BANK'])
		BANKCODE.set(result['BANKCODE'])
		IFSC.set(result['IFSC'])
	except:
		messagebox.showerror("showerror", "Something wrong")


# object of tkinter
# and background set for light grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
Centre = StringVar()
contact = StringVar()
UPI = StringVar()
CITY = StringVar()
STATE = StringVar()
DISTRICT = StringVar()
IMPS = StringVar()
ADDRESS = StringVar()
BRANCH = StringVar()
STD = StringVar()
MICR = StringVar()
BANK = StringVar()
BANKCODE = StringVar()
IFSC = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter IFSC Code :", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Bank Name :", bg="light grey").grid(row=1, sticky=W)
Label(master, text="Centre :", bg="light grey").grid(row=2, sticky=W)
Label(master, text="contact :", bg="light grey").grid(row=3, sticky=W)
Label(master, text="UPI :", bg="light grey").grid(row=4, sticky=W)
Label(master, text="CITY :", bg="light grey").grid(row=5, sticky=W)
Label(master, text="STATE :", bg="light grey").grid(row=6, sticky=W)
Label(master, text="DISTRICT :", bg="light grey").grid(row=7, sticky=W)
Label(master, text="ADDRESS :", bg="light grey").grid(row=8, sticky=W)
Label(master, text="BRANCH :", bg="light grey").grid(row=9, sticky=W)
Label(master, text="STD :", bg="light grey").grid(row=10, sticky=W)
Label(master, text="MICR :", bg="light grey").grid(row=11, sticky=W)
Label(master, text="IFSC :", bg="light grey").grid(row=12, sticky=W)

# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=BANK,
	  bg="light grey").grid(row=1, column=1, sticky=W)
Label(master, text="", textvariable=Centre,
	  bg="light grey").grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=contact,
	  bg="light grey").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=UPI, bg="light grey").grid(
	row=4, column=1, sticky=W)
Label(master, text="", textvariable=CITY,
	  bg="light grey").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=STATE,
	  bg="light grey").grid(row=6, column=1, sticky=W)
Label(master, text="", textvariable=DISTRICT,
	  bg="light grey").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=ADDRESS,
	  bg="light grey").grid(row=8, column=1, sticky=W)
Label(master, text="", textvariable=BRANCH,
	  bg="light grey").grid(row=9, column=1, sticky=W)
Label(master, text="", textvariable=STD, bg="light grey").grid(
	row=10, column=1, sticky=W)
Label(master, text="", textvariable=MICR, bg="light grey").grid(
	row=11, column=1, sticky=W)
Label(master, text="", textvariable=IFSC, bg="light grey").grid(
	row=12, column=1, sticky=W)

e = Entry(master)
e.grid(row=0, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=getifsc)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()