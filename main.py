# * means import everything from tkinter
from tkinter import *
root = Tk()

root.geometry("500x500")
root.title("  Registration ") 
root.configure(background="light blue")

firstname= Label(root,text="First name:")
lastname= Label(root,text="Last name:")
Address= Label(root,text="Address:")
Email= Label(root,text="Email:")
Phone= Label(root,text="Phone:")
Paymentmood= Label(root,text="Payment Mode:")

firstname.grid(row=1, column=0 , padx=10, pady=10, sticky=W)
lastname.grid(row=2, column=0 , padx=10, pady=10, sticky=W)
Address.grid(row=3, column= 0, padx=10, pady=10, sticky=W)
Email.grid(row=4, column= 0, padx=10, pady=10, sticky=W)
Phone.grid(row=5, column= 0, padx=10, pady=10, sticky=W)
Paymentmood.grid(row=6, column= 0, padx=10, pady=10, sticky=W)

firstnamevalue= StringVar
phonevalue=StringVar
lastnamevalue= StringVar
emailvalue=StringVar
paymentvalue=StringVar
address= StringVar
checkvalue= IntVar

firstnameentry= Entry(root, textvariable=firstnamevalue)
lastnameentry= Entry(root,textvariable=lastname)
address= Entry(root,textvariable=address)
emailentry= Entry(root, textvariable=emailvalue)
phoneentry= Entry(root, textvariable=phonevalue)


firstnameentry.grid(row=1, column=1)
lastnameentry.grid(row=2, column=1)
address.grid(row=3, column=1)
emailentry.grid(row=4, column=1)
phoneentry.grid(row=5, column=1)



#drop down box maybe**
payment = StringVar()
payment.set("Credit Card")
drop = OptionMenu(root, payment, "Credit card","Paypal","Cash")
drop.config(bg="light green")
drop.grid(row=6, column=1 , padx=10, pady=10, sticky=W)





root.mainloop()                                                  