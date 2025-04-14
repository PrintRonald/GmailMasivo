import smtplib
from email.mime.text import MIMEText

# Configuración del correo
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_sender = "ronald.madariaga@colegionacional.cl"
email_password = "lkyc rhar hzyz xwiq"

# Lista de destinatarios
recipients = ["madariaga492@gmail.com", "criptonitadick@gmail.com"]

# Conectar al servidor SMTP y enviar correos
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_sender, email_password)

    for recipient in recipients:
        # Crear un mensaje NUEVO para cada destinatario
        subject = "Correo 2 de prueba de envio masivo con Python"
        body = "Hola 2, este es un correo de prueba enviado con Python."
        msg = MIMEText(body, "plain")
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = recipient

        server.sendmail(email_sender, recipient, msg.as_string())
        print(f"Correo enviado a {recipient}")

print("Todos los correos fueron enviados exitosamente.")
