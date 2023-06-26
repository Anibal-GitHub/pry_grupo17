import pandas as pd

import pandas as pd

# Cargar los datos de la tabla (archivo CSV llamado "poblacion-mundial.csv")
data = pd.read_csv("poblacion-mundial.csv")

# Mostrar los primeros 5 países
primeros_paises = data.head(5)
print(primeros_paises)
