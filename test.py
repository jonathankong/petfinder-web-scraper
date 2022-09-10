
#region Test Email through debug SMTP server
# import smtplib, ssl, os

# port = 1025  # For SSL
# smtp_server = "localhost"
# sender_email = "my@gmail.com"  # Enter your address
# receiver_email = "your@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as smtp:
#     # smtp.ehlo()
#     # smtp.starttls()
#     # smtp.ehlo()

#     # smtp.login(sender_email, password)
#     smtp.sendmail(sender_email, receiver_email, message)
#endregion

import win32com.client as win32
from pathlib import Path
import os 

PATH = Path.cwd() / "images" / "Ben.png"
print(os.path.join(os.getcwd(), "images\Ben.png"))

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.Subject = 'Dummy Email'
mail.BodyFormat = 1
mail.Body = 'Hello World'
mail.To = 'icesnowwaterme@gmail.com'
mail.Attachments.Add(os.path.join(os.getcwd(), "Ben.png"))
mail.Display()

mail.Send()