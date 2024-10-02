import smtplib, ssl


def send_email(messages):
    host = "smtp.gmail.com"
    port = 465

    username = "tahmidkabirp01814@gmail.com"
    password = "vkyk hjrz pncq wmjj"
    receiver = "tahmidkabirp01814@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, messages)

