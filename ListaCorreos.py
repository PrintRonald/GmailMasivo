import pandas as pd

# Cargar el archivo Excel
file_path = "6BA.xlsx"  # Cambia esto por la ruta de tu archivo
df = pd.read_excel(file_path)

# Suponiendo que la columna con los correos se llama "Email"
email_list = df["6A"].dropna().tolist()  # Elimina valores vacíos y convierte en lista

#print(email_list)  # Ver la lista de correos

listaFinal = ",".join(email_list)
print(listaFinal)


