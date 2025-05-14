import pandas as pd

# Cargar el archivo Excel
file_path = "5BB.xlsx"  # Cambia esto por la ruta de tu archivo
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

"""
cfmfilo@gmail.com, neve.jimenez.vilches@gmail.com, info.torosalinas@gmail.com, vane.silvaparra@gmail.com, inesvasquez1@gmail.com,
 sotelonicole@gmail.com, danitajaksic@gmail.com, mahuen@gmail.com, tamaruz2010@gmail.com, dilujo1076@gmail.com,
   saavedramarjorie39@gmail.com, lornapuguita@gmail.com, alemancilla2006@gmail.com, isaabemargarita@gmail.com, jovitajoyas@gmail.com,
     carolinadunstan@hotmail.com, lissette.cortes.araya@gmail.com, marielamilena1973@gmail.com, dangrafics@gmail.com,
       dangrafics@gmail.com, juliainocenciob@gmail.com, daa.vgodoy@gmail.com, sangopa1970@gmail.com, almendragr@gmail.com,
         ivo.silva.carvajal12@gmail.com, brandorita1980@gmail.com, milenka.azagra@gmail.com, sep.so.pablo@gmail.com, 
         pau.diaz.vargas@gmail.com, dponce.ag@gmail.com, leorodriguez60@gmail.com, gabrieladunstan@hotmail.com,
           cristian.daniel.salinas@gmail.com, ruthgon@gmail.com

"""

"""
'CAROLINADIAZ22@HOTMAIL.COM', 'giovi_noemi@hotmail.com', 'karinasofia15@outlook.com', 'vane.silvaparra@gmail.com', 'Cherieleclerc@gmail.com',
'mgch84@gmail.com', 'danitzacarvajal@gmail.com', 'andrus.olivarez@gmail.com', 'stephanibb@gmail.com', 'lci_tj@hotmail.com', 'lorevera28@gmail.com',
'danielasotozamora@gmail.com', 'africacortez@icloud.com', 'mbaezamontoya@gmail.com', 'MESTAYTOLEDO@HOTMAIL.COM', 'fdelcei1985@gmail.com',
'carolina.valdes.villegas@gmail.com', 'sicher.eirl@gmail.com', 'karol.velastegui.kv@gmail.com', 'A.ARDILESE@GMAIL.COM',
'rodolfo.quezada.s@gmail.com', 'camilatobar661@gmail.com', 'camipinedav@gmail.com', 'j.barriossaavedra@gmail.com',
'ppeiranogatica@gmail.com', 'fsaconstrucciones@gmail.com', 'nicoledesidelguerra14@outlook.com',
'MSMARY624@GMAIL.COM', 'ibaniapablaza87@gmail.com', 'gonzalo16744@yahoo.es', 'alvarado.susana@hotmail.com',
'MARIA_ELENA_VERA@HOTMAIL.COM', 'micavifi@gmail.com', 'olgasilva1523@gmail.com', 'lorenaavilapizarro@gmail.com',
'alejandro.terapiasistemica@gmail.com', 'ruthgon@gmail.com'
"""


