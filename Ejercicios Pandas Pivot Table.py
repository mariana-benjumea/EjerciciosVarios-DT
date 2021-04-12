#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importamos las bibliotecas necesarias
import pandas as pd
import pandas as np


# In[ ]:


# Importamos y visualizamos el conjunto de datos
US_ag_exports_2011_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv'
US_ag_exports_2011 = pd.read_csv(US_ag_exports_2011_url)


# In[ ]:


US_ag_exports_2011.head()


# In[ ]:


# Creamos un dataframe a partir de los datos descargados
data = pd.DataFrame(US_ag_exports_2011)
data.head()


# In[ ]:


# Renombramos la columna 'category' a 'region'
data.rename(columns = {'category':'region'}, inplace=True)
data.head(10)


# # PRIMERA FORMA DE REALIZARLO

# In[ ]:


filtro1 = data['state'].isin(['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont'])
filtro1_2 = data[filtro1].index
data.loc[filtro1_2, 'region'] = 'New England'


# In[ ]:


filtro2 = data['state'].isin(['Delaware', 'District of Columbia', 'Maryland', 'New Jersey', 'New York', 'Pennsylvania'])
filtro2_2 = data[filtro2].index
data.loc[filtro2_2, 'region'] = 'Mideast'


# In[ ]:


filtro3 = data['state'].isin(['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin'])
filtro3_2 = data[filtro3].index
data.loc[filtro3_2, 'region'] = 'Great Lakes'

filtro4 = data['state'].isin(['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota'])
filtro4_2 = data[filtro4].index
data.loc[filtro4_2, 'region'] = 'Plains'

filtro5 = data['state'].isin(['Alabama', 'Arkansas', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Mississippi', 'North Carolina', 'South Carolina', 'Tennessee', 'Virginia', 'West Virginia'])
filtro5_2 = data[filtro5].index
data.loc[filtro5_2, 'region'] = 'Southeast'

filtro6 = data['state'].isin(['Arizona', 'New Mexico', 'Oklahoma', 'Texas'])
filtro6_2 = data[filtro6].index
data.loc[filtro6_2, 'region'] = 'Southwest'

filtro7 = data['state'].isin(['Colorado', 'Idaho', 'Montana', 'Utah', 'Wyoming'])
filtro7_2 = data[filtro7].index
data.loc[filtro7_2, 'region'] = 'Rocky Mountain'

filtro8 = data['state'].isin(['Alaska', 'California', 'Hawaii', 'Nevada', 'Oregon', 'Washington'])
filtro8_2 = data[filtro8].index
data.loc[filtro8_2, 'region'] = 'Far West'


# In[ ]:


data


# # SEGUNDA FORMA DE REALIZAR EL EJERCICIO

# Introducción a la operativa de funcionamiento

# In[ ]:


New_England = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']

filtro = data['state'].isin(New_England) # Obtenemos de los datos de los estado del dataframeque vamos a actualizar
indices_de_estados_de_la_lista = data[filtro].index # Obtenemos la lista de índices que nos interesa actualizar

for indice_estado in indices_de_estados_de_la_lista:
  data.loc[indice_estado, 'region'] = 'New England'

data[data['region'] == 'New England']


# Reaprovechando del código mediante una función

# In[ ]:


New_England = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']
Mideast = ['Delaware', 'District of Columbia', 'Maryland', 'New Jersey', 'New York', 'Pennsylvania']
Great_Lakes = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']
Plains = ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']
Southeast = ['Alabama', 'Arkansas', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Mississippi', 'North Carolina', 'South Carolina', 'Tennessee', 'Virginia', 'West Virginia']
Southwest = ['Arizona', 'New Mexico', 'Oklahoma', 'Texas']
Rocky_Mountain = ['Colorado', 'Idaho', 'Montana', 'Utah', 'Wyoming']
Far_West = ['Alaska', 'California', 'Hawaii', 'Nevada', 'Oregon', 'Washington']

def list_contains(Region_list, Region):
  filtro = data['state'].isin(Region_list) # Obtenemos de los datos de los estado del dataframeque vamos a actualizar
  indices_de_estados_de_la_lista = data[filtro].index # Obtenemos la lista de índices que nos interesa actualizar

  for indice_estado in indices_de_estados_de_la_lista:
    data.loc[indice_estado, 'region'] = Region
  #return 0

#list_contains(New_England, 'New England')
list_contains(Mideast, 'Mideast')
list_contains(Great_Lakes, 'Great Lakes')
list_contains(Plains, 'Plains')
list_contains(Southeast, 'Southeast')
list_contains(Southwest, 'Southwest')
list_contains(Rocky_Mountain, 'Rocky Mountain')
list_contains(Far_West, 'Far West')


# In[ ]:


data[data['region'] == 'New England']
#data[data['region'] == 'Mideast']
#data[data['region'] == 'Great Lakes']
#data[data['region'] == 'Plains']
#data[data['region'] == 'Southeast']
#data[data['region'] == 'Southwest']
#data[data['region'] == 'Rocky Mountain']
#data[data['region'] == 'Far West']


# In[ ]:


data

