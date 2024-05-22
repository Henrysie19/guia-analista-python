import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(color_codes=True)
pd.set_option('display.max_columns',None)
startup_data_file_path = 'C:/DOCS/trabajo_analista/Proyectos_referencia/startup_data.csv'

df = pd.read_csv(startup_data_file_path)
df.head()

### Procesando los datos Parte 1

df.drop(columns = ['Unnamed: 0', 'id', 'Unnamed: 6', 'name'], inplace=True)
df.shape

# Verifique el número de valores únicos de todos los tipos de datos del objeto
df.select_dtypes(include='object').nunique()

# Eliminar columna con valor único superior a 100, excepto la columna de fecha y hora
df.drop(columns = ['zip_code', 'city', 'object_id'], inplace = True)
df.shape

# Extraiga solo el año de toda la columna de fecha y hora y cambie el tipo de datos a un número entero excepto el valor nulo
df['founded_at'] = df['founded_at'].apply(lambda x: int(x[-4:].lstrip('0')) if isinstance(x, str) else np.nan)
df['closed_at'] = df['closed_at'].apply(lambda x: int(x[-4:].lstrip('0')) if isinstance(x, str) else np.nan)
df['first_funding_at'] = df['first_funding_at'].apply(lambda x: int(x[-4:].lstrip('0')) if isinstance(x, str) else np.nan)
df['last_funding_at'] = df['last_funding_at'].apply(lambda x: int(x[-4:].lstrip('0')) if isinstance(x, str) else np.nan)

# Verifique el número de valores únicos de todos los tipos de datos del objeto
df.select_dtypes(include='object').nunique()

### Segmente el código de categoría en un valor único más pequeño
df.category_code.unique()

def segment_category (category):

    if category in ['music', 'games_video', 'photo_video', 'entertainment']:
        return "Entertainment"
    
    elif category in ['enterprise', 'web', 'software', 'network_hosting', 'hardware', 'tech']:
        return "Technology"
    
    elif category in ['finance', 'mobile', 'ecommerce', 'advertising', 'business']:
        return "Business"
    
    elif category in ['education', 'public_relations', 'security']:
        return "Education & PR"
    
    elif category in ['travel', 'fashion', 'hospitality', 'transportation']:
        return "Lifestyle"
    
    elif category in ['analytics', 'consulting']:
        return "Consulting & Analytics"
    
    elif category in ['biotech', 'cleantech', 'search', 'semiconductor', 'medical', 'health']:
        return "Science $ Health"
    
    else:
        return "Other"
    
# Aplicar la función de segmentación a cada código de categoría.
df['category_segment'] = df['category_code'].apply(segment_category)

plt.figure(figsize=(10,5))
df['category_segment'].value_counts().plot(kind='bar')

# Eliminar la columna category_code
df.drop(columns = 'category_code', inplace=True)

### EDA (Exploratory Data Analysis)

# Obtenga los nombres de todas las columnas con el tipo de datos 'objeto' (columnas categóricas)
cat_vars = df.select_dtypes(include='object').columns.tolist()

# Crear una figura con subplots
num_cols = len(cat_vars)
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()


# Cree un diagrama de conteo para los 5 valores principales de cada variable categórica usando Seaborn
for i, var in enumerate(cat_vars):
    top_values = df[var].value_counts().nlargest(5).index
    filtered_df = df[df[var].isin(top_values)]
    sns.countplot(x=var, data=filtered_df, ax=axs[i])
    axs[i].set_title(var)
    axs[i].tick_params (axis="x", rotation=90)

# Elimine cualquier subtrama vacía adicional si es necesario
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
    
# Ajustar el espaciado entre los graficos
fig.tight_layout()   

#_____________________________________________________________________________________________________

# Obtenga los nombres de todas las columnas con tipo de datos 'int' o 'float' 
num_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()

# Crear ua figura con subplots/(subfiugra=es un cuadro que dentro habrá una figura)
num_cols = len(num_vars)
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Crear una caja de bigotes(box_plot) para cada variable númerica usando seaborn
for i, var in enumerate(num_vars):
    sns.boxplot(x=df[var], ax=axs[i])
    axs[i].set_title(var)

# Elimina cada espacio extra subplot que no necesitas
if num_cols < len(axs):
    for i in range (num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Ajusta el espacio entre graficos (subplots)
fig.tight_layout()

#_________________________________________________________________________________________________

# Escogemos los nombre de todas las columnas con los datos 'int' "Numeros enteros"
int_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()

#Crear las figuras/espacios para los graficos
num_cols = len(int_vars)
num_rows = (num_cols + 2)// 3 # Asegurate que son los espacios suficientes para todas las graficas
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(12, 5*num_rows))
axs = axs.flatten()

#crear un box-plot para cada varibles usando seaborn con hue='attritio'

for i, var in enumerate(int_vars):
    sns.boxplot(y=var, x='status', data=df , ax=axs[i])
    axs[i].set_title(var)
    
# Eliminar cada espacio extra que o hayan llenado los graficos
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
       fig.delaxes(axs[i])
      
# Ajustar los espacios de os graficos y los titulos
fig.tight_layout()

# mostrar el grafico
plt.show()

# ____________________________________________________________________________________
#Escoger los nombres de todas las columnas que contengan datos 'int' y 'float'
int_vars = df.select_dtypes(include=['int','float']).columns.tolist()

#Crear los esopacios para las graficas
num_cols = len (int_vars)
num_rows = (num_cols + 2) //3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Crear un histograma por cada variable entero}
for i, var in enumerate(int_vars):
    df[var].plot.hist(ax=axs[i])
    axs[i].set_title(var)
    
# Elimnar los espacios extras y dejar solo los que necesitamos
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Ajustar los espacios entre las graficas
fig.tight_layout()        

# mostrar el grafico
plt.show()

#_________________________________________________________________________________

#Obtener los nombres de toidas las comlumnas de tipo 'int' (Entero)

int_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()

#Crear una fuigura con los espacios de las graficas
num_cols = len(int_vars)
num_rows = (num_cols + 2) // 3 # To make sure there are enough rows for the subplots
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

#Crear un histograma para cada variable con hue='Attrition'
for i, var in enumerate(int_vars):
    sns.histplot(data=df, x=var, hue='status', kde=True, ax=axs[i])
    axs[i].set_title(var)

# Eliminar los espacios de graficos que no se necesitan
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Ajustar los espacios entre las graficas
fig.tight_layout()

# Show plot
plt.show()

#________________________________________________________________________________________

#Especificar el número maximo de de categorías a mostrar individualmente
max_categories = 5

# Filtrar las columnas categoricas con tip 'objeto'
cat_cols = [col for col in df.columns if df[col].dtype == 'object']

# Crear los espacios de los graficos
num_cols = len(cat_cols)
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))

# Aplana la matriz axs para facilitar la indexación
axs = axs.flatten()

# Crear la torta para cada columna categorica
for i, col in enumerate(cat_cols):
    if i < len(axs): # Ensure we don't exceed the number of subplots
        #Count the number of occurrences for each category
        cat_counts = df[col].value_counts()
        
        # Categorías de grupo más allá de max_categories superiores como 'Otros'
        if len(cat_counts) > max_categories:
            cat_counts_top = cat_counts[:max_categories]
            cat_counts_other = pd.Series(cat_counts[max_categories:].sum(), index=["Other"])
            cat_counts = cat_counts_top.append(cat_counts_other)
            
            
        # Crear una torta
        axs[i].pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%', startangle=90)
        axs[i].set_title(f'{col} Distribution')
        
 #eliminar cada espacio extra 
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Ajusta el espacio entre las graficas
fig.tight_layout()

# Show plot
plt.show()        


# Revisar la cantidad de los valores perdidos
revisar_datosperdidos = df.isnull().sum()* 100 / df.shape[0] #Este codigo muestra el porcentaje de los datos perdidos
revisar_datosperdidos[revisar_datosperdidos > 0].sort_values(ascending=False)



   