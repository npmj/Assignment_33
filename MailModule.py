import os
import smtplib
from email.message import EmailMessage

def SendMail(FileName,ReceiverEmail,Subject,Body):
    try:
        # Sender Gmail address
        sender_email = "kadamnehaj1999@gmail.com" 
        
        # Google App Password (16 characters)
        app_password = "wckg vicj bxes lfoe"

        # Receiver Gmail address
        receiver_email = ReceiverEmail 
        
        subject = Subject
        
        body = Body


        fobj = open(FileName,"rb")
        file_content = fobj.read()
    

        # Step 1: Create Email object
        msg = EmailMessage()

        # Step 2: Set mail headers
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Step 3: Add mail body
        msg.set_content(body)

        msg.add_attachment(
            file_content,
            maintype="text",
            subtype="plain",
            filename=os.path.basename(FileName)
        )

        # Step 4: Create SMTP SSL connection
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        # Step 5: Login using Gmail + App Password
        smtp.login(sender_email, app_password)

        # Step 6: Send the email
        smtp.send_message(msg)

        # Step 7: Close the connection
        smtp.quit()

        return True
    
    except Exception as e:
            return False

   