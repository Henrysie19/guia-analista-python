import pandas as pd
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import re
sns.set_theme(color_codes=True)     
pd.set_option('display.max_columns', None)

# Leer los archivos
## Especficar el directorio que contiene los archivos de texto

directorio = 'KIA1'

# Lista de todos los archivos con extension 'txt' en el directorio
industria_automoviles = [docs for docs in os.listdir(directorio) if docs.endswith('.txt')]

# Dataframe vacio
industria_diario = pd.DataFrame()

# Lee y combina cada archivo en el Dataframe
for docs in industria_automoviles:
    ruta_archivo = os.path.join(directorio, docs)
    datos_archivo = pd.read_csv(ruta_archivo, delimiter='|')
    industria_diario = pd.concat([industria_diario, datos_archivo], ignore_index=True)
    
# Mostrar
print(industria_diario)

#convertirlo a excel
industria_diario.to_excel('industria_diario.xlsx', index=False)

#------------------------------------------------------------------------------------------

# combinación de otra tabla 'industria_diario' con 'Acum_septiembre'

Acum_septiembre = 'Acum_septiembre.txt'

# Leer el archivo txt
df_acum_septiembre = pd.read_csv(Acum_septiembre, delimiter='|')

# Consolidar los datos con el archivo 'industria_diario'
df_consolidado = pd.concat([industria_diario, df_acum_septiembre], ignore_index=True)

# Guardar el nuevo archivo en un csv
df_consolidado.to_csv('INDUSTRIA_COMPLETO', index=False)




    