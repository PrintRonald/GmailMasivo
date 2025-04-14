import pandas as pd

# Cargar el archivo Excel
file_path = "8BB.xlsx"  # Cambia esto por la ruta de tu archivo
df = pd.read_excel(file_path)

# Suponiendo que la columna con los correos se llama "Email"
email_list = df["Email"].dropna().tolist()  # Elimina valores vacíos y convierte en lista

print(email_list)  # Ver la lista de correos

"""
CAROLINADIAZ22@HOTMAIL.COM, giovi_noemi@hotmail.com, karinasofia15@outlook.com, vane.silvaparra@gmail.com,
  Cherieleclerc@gmail.com, mgch84@gmail.com, danitzacarvajal@gmail.com, andrus.olivarez@gmail.com, stephanibb@gmail.com, 
  lci_tj@hotmail.com, lorevera28@gmail.com, danielasotozamora@gmail.com, africacortez@icloud.com, mbaezamontoya@gmail.com,
  MESTAYTOLEDO@HOTMAIL.COM, fdelcei1985@gmail.com, carolina.valdes.villegas@gmail.com, sicher.eirl@gmail.com,
  karol.velastegui.kv@gmail.com, A.ARDILESE@GMAIL.COM, rodolfo.quezada.s@gmail.com, camilatobar661@gmail.com, 
  camipinedav@gmail.com, j.barriossaavedra@gmail.com, ppeiranogatica@gmail.com, fsaconstrucciones@gmail.com, 
  nicoledesidelguerra14@outlook.com, MSMARY624@GMAIL.COM, ibaniapablaza87@gmail.com, gonzalo16744@yahoo.es, 
  alvarado.susana@hotmail.com, MARIA_ELENA_VERA@HOTMAIL.COM, micavifi@gmail.com,
  olgasilva1523@gmail.com, lorenaavilapizarro@gmail.com, alejandro.terapiasistemica@gmail.com, ruthgon@gmail.com

"""


