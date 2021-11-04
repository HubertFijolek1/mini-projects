import smtplib
 
mailFrom = 'Your automation system'
mailTo = ['your@email.here0','your_another@email.here']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello
 
This mail confirms that processing has finished without problems,
 
Have a nice day!'''
 
message = '''From: {}
Subject: {}
 
{}
'''.format(mailFrom, mailSubject, mailBody)
 
user = 'your_username@gmail.com'
password = 'your_password_here'
 
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
