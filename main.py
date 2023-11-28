# * means import everything from tkinter
from tkinter import *
root = Tk()

root.geometry("500x500")
root.title("  Registration ") 
root.configure(background="white")

# Label widgets

firstname= Label(root,text="First name:",bg="light yellow")
lastname= Label(root,text="Last name:",bg="light yellow")
Address= Label(root,text="Address:",bg= "light yellow")
Email= Label(root,text="Email:",bg= "light yellow")
Phone= Label(root,text="Phone:", bg= "light yellow")
Paymentmood= Label(root,text="Payment Mode:", bg = "light yellow")


# size of widgets
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

# Entry Widgets
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
drop.grid(row=6, column=1 , padx=10, pady=10, sticky=W)



# pop up box
import tkinter.messagebox 

def onClick(): 
  tkinter.messagebox.showinfo("" , "Verification Successful")


# Create a Button 
button = Button(root, text="Register", command=onClick, height=1, width=5, padx=10, pady=10, bg='grey')


# Set the position of button on the top of window. 
 # button.pack(side='bottom')
button.grid(row=7, column=1)




root.mainloop()                                                  