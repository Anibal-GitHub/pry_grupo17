import pandas as pd

# Cargar los datos del DataSet (archivo CSV llamado "poblacion-mundial.csv")
data = pd.read_csv("C:/Users/aniba/Downloads/poblacion-mundial.csv")

# Obtener una lista de los países únicos
lista_paises = data["Entity"].unique()

# Imprimir la lista de países
for Entity in lista_paises:
    print(Entity)

