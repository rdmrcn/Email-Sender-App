# Email-Sender-App
A simple Python application to send emails using the smtplib library and a graphical user interface built with Tkinter. This app allows users to send emails by entering the sender's email credentials, recipient's email address, and the email content.
made by Reha Demircan 


Features
Sender Email Address: Enter the email address of the sender.
Sender Email Password: Enter the password for the sender's email account. (Note: Ensure to use app-specific passwords for enhanced security.)
Recipient Email Address: Enter the email address of the recipient.
Email Body: Enter the main content of the email to be sent.
Send Button: Click to send the email.
How It Works
The app uses Python's smtplib to connect to the Gmail SMTP server (smtp.gmail.com) on port 587.
The sender's email and password are used to log in to the SMTP server.
The email is sent from the sender's address to the recipient's address with the content provided in the "Email Body" field.
The app provides a success message upon successful delivery or an error message if any issue occurs.
Requirements
Python 3.x
tkinter (comes pre-installed with Python)
Internet connection for SMTP server access

Important Notes
Security: It is highly recommended to use App Passwords instead of your regular email password when logging in.
Enable Less Secure Apps: Make sure to allow access to less secure apps in your Gmail account settings if using a standard Gmail login.
Screenshots

Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Built using the Python smtplib library for email handling.
User interface created using tkinter.
