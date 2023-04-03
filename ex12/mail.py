import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email information
from_email = 'penis_inspector420@outlook.com'
from_password = ''
to_email = ''
subject = 'Subject: Email with attachment'
body = 'Hello, this is an email with an attachment.'
file_path = './attachment.txt'

# Create the email
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach the file
with open(file_path, 'rb') as attachment:
    attachment_name = file_path.split('/')[-1]
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={attachment_name}')
    msg.attach(part)

# Send the email
try:
    server = smtplib.SMTP('smtp-mail.outlook.com', 25)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Error: {e}")
