import smtplib
# import the smtplib module.

# from user details
from_user_email_id = '<sample-email>@gmail.com'
from_user_email_pwd = 'xxxxx'

# provide subject for email
email_subject = 'Sample Subject'

# provide here user email id's. As a List
to_user_email_id = ['<sample-email>@gmail.com','<sample-email>@outlook.com']

# smtplib = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
# see below example of gmail
smtplib = smtplib.SMTP("smtp.gmail.com",587)
smtplib.ehlo()
smtplib.starttls()
smtplib.ehlo

# login the SMTP server
smtplib.login(from_user_email_id, from_user_email_pwd)

# preparing email message
email_header = 'To:' + ", ".join(to_user_email_id)  + '\n' + 'From: ' + from_user_email_id + '\n' + 'Subject: ' +  email_subject + '  \n'
email_message = email_header + 'Hi User,\n Hope you are doing great!\n\n Warm Regards.'

# sending email
smtplib.sendmail(from_user_email_id, to_user_email_id, email_message)

smtplib.close()
