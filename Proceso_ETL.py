#Generaremos un proceso de ETL para procesarlo mediante jenkins y git hub
#Importamos las librerias a utilizar 
import pandas as pd
import numpy as np
import matplotlib.pyplot as matplot
#Cargamos los archivos a utilizar 
df = pd.read_csv("C:/Users/51950/OneDrive/Escritorio/Data Analytis/DATAOPS/Dataops_Fabian/Base de datos.csv", delimiter = ",", index_col=0)
#Verificamos que se carguen los datos correctamente
print(df)
print("\n")
#Verificamos la información de nuestro dataframe
print(df.info())
print("\n")
#Realizaremos algunos cambios en nuestra base de datos
#Renombramos los encabezados
df = df.rename(columns={'work_year':'Año_de_Trabajo','job_title':'Titulo_Cargo','salary_currency':'Moneda_Pago'})
print(df)
print("\n")
#Realizamos el filtrado de nuestra base de datos
df1 = df[df.work_setting == 'Remote']
print(df1)
#Luego exportamos el archivo a la carpeta de destino
print("\n")
df1.to_csv("C:/Users/51950/OneDrive/Escritorio/Data Analytis/DATAOPS/Dataops_Fabian/Job_in_data1.csv", index=False)