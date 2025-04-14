import pandas as pd

# Cargar el archivo Excel
file_path = "5BB.xlsx"  # Cambia esto por la ruta de tu archivo
df = pd.read_excel(file_path)

# Suponiendo que la columna con los correos se llama "Email"
email_list = df["Email"].dropna().tolist()  # Elimina valores vacíos y convierte en lista

print(email_list)  # Ver la lista de correos
