import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ListaCorreos import email_list

# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_sender = "madariaga492@gmail.com"
email_password = "lkyc rhar hzyz xwiq"
email_receiver = email_list

# Crear el mensaje
msg = MIMEMultipart()
msg["From"] = email_sender
msg["To"] = ",".join(email_receiver)
msg["Subject"] = "Materiales para experimento: construcción de vehículo a prepulsión con aire"

# Cuerpo del correo
body = """"Junto con saludar y esperando que se encuentren bien, adjunto imagen con los materiales que
 necesitan los estudiantes para el experimento.
 Sin otro particular me despido atentamente.
 Profesor de tecnología.
    """
msg.attach(MIMEText(body, "plain"))

# Adjuntar imagen
filename = "materiales.jpeg"  # Cambia por el nombre de tu archivo
filepath = "materiales.jpeg"  # Ruta completa del archivo

with open(filepath, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Codificar el archivo adjunto en base64
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(part)

# Conectar al servidor SMTP y enviar el correo
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, msg.as_string())

print("Correo enviado con éxito")
