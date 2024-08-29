#Python Email send App by.Reha Demircan

#The Sender Email Address field is where you enter the email address of the sender.
#The Sender Email Password field is where you enter the password for the sender's email account.
#The Recipient Email Address field is where you enter the email address of the recipient.
#The Email Body field is where you type the main content of the email you want to send.


import smtplib
from tkinter import *
from tkinter import messagebox

def send_message():
    sender_email = sender_address_entry.get()
    sender_password = sender_password_entry.get()
    recipient_address = recipient_address_entry.get()
    email_body = email_body_entry.get()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        print("Login successful")
        server.sendmail(sender_email, recipient_address, email_body)
        print("Message sent")
        server.quit()
        messagebox.showinfo("Success", "Message sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        messagebox.showerror("Authentication Error", f"Failed to authenticate: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    sender_address_entry.delete(0, END)
    sender_password_entry.delete(0, END)
    recipient_address_entry.delete(0, END)
    email_body_entry.delete(0, END)

app = Tk()
app.geometry("500x500")
app.title("Python Mail Send App")

headline = Label(app, text="Python Mail Send App", bg="Yellow", fg="black", font="10", width="500", height="3")
headline.pack()

sender_address_label = Label(app, text="Sender Email Address:")
sender_address_label.place(x=15, y=70)
sender_address = StringVar()
sender_address_entry = Entry(app, textvariable=sender_address, width="30")
sender_address_entry.place(x=15, y=100)

sender_password_label = Label(app, text="Sender Email Password:")
sender_password_label.place(x=15, y=140)
sender_password = StringVar()
sender_password_entry = Entry(app, textvariable=sender_password, width="30", show="*")
sender_password_entry.place(x=15, y=170)

recipient_address_label = Label(app, text="Recipient Email Address:")
recipient_address_label.place(x=15, y=210)
recipient_address = StringVar()
recipient_address_entry = Entry(app, textvariable=recipient_address, width="30")
recipient_address_entry.place(x=15, y=240)

email_body_label = Label(app, text="Email Body:")
email_body_label.place(x=15, y=280)
email_body = StringVar()
email_body_entry = Entry(app, textvariable=email_body, width="30")
email_body_entry.place(x=15, y=310)

send_button = Button(app, text="Send Message", command=send_message, width="30", height="2", bg="grey")
send_button.place(x=15, y=350)

mainloop()
