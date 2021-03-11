# import smtplib
# from email.message import EmailMessage

# email = EmailMessage()
# email['from'] = 'Thamaraikkannan MV'
# email['to'] = 'thamaraik14996kannan@gmail.com'
# email['subject'] = 'You won 1,000,000 dollers!!'

# email.set_content('I am a Python Master!!!!')

# with smtplib.SMTP(host='smtp.gmail.com', port=465) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('industriousthams@gmail.com', 'Thams@14996')
#     smtp.send_message(email)
#     print('all good boss!!')


import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "industriousthams@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 