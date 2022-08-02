import smtplib
import ssl


def send_email(smtp, smtp_port, user, password, destination, subject, msg):
    """
    Email the specified destination using provided credentials
    @param smtp: smtp server, for example smtp.gmail.com
    @param smtp_port: smtp server port, for example 587
    @param user: user credential to send through smtp
    @param password: user credential to send through smtp
    @param destination: where to send the report\
    @param subject: subject of the message
    @param msg: message to send
    """
    # we use a secure SSL context
    context = ssl.create_default_context()

    # Now we try to log in to the server and send email
    try:
        server = smtplib.SMTP(smtp, smtp_port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection using the tls protocol
        server.login(user, password)

        message = 'Subject: {}\n\n{}'.format(subject, msg)
        print("Sending email to: " + destination)
        server.sendmail(from_addr=user, to_addrs=destination, msg=message)
    except Exception as e:
        print(e)
    finally:
        server.quit()
