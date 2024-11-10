import smtplib as mail

obj = mail.SMTP('smtp.gmail.com', 587)

obj.ehlo()

obj.starttls()

obj.login('sender_email', 'gmail_app_password') # you can generate app password from google account settings

subject = "Test Mail"
body = "Hey, my name is yash i love python "


message = f"Subject: {subject}\n\n{body}"

email_list = ['reciever_email_1','reciever_email_2','reciever_email_n']

obj.sendmail('sender_email', email_list, message)

print("Mail has been sent")

obj.quit()
