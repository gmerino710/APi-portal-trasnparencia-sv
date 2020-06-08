import requests
import pandas as pd
import os

url = 'https://www.transparencia.gob.sv/api/v1/consultants.json'
url1 = 'https://jsonplaceholder.typicode.com/posts'
url2 = 'https://www.transparencia.gob.sv/api/v1/institutions.json'

Id = []
Trasnparencia = []
Nombre = []
Acronimo = []
Face =[]
Avatar = []
Email =[]
Sitio_web =[]
disponible =[]
response = requests.get(url2)


print(response.status_code)

if response.status_code == 200:

    datos = response.json()

    for i in datos:
       # print('{}:{}:{}:{}'.format(i['id'],i['name'],i['created_at'],i['acronym']))
        Id.append(i['id'])
        Nombre.append(i['name'])
        Trasnparencia.append(i['external_transparency_site_url'])
        Acronimo.append(i['acronym'])
        Face.append(i['facebook_url'])
        Avatar.append(i['avatar_file_name'])
        Email.append(i['officer_email'])
        Sitio_web.append(i['website_url'])
        disponible.append(i['enabled'])
else:
    print('error');    


df = pd.DataFrame(
            {
                'Id':Id,
                'Nombre':Nombre,
                'Acronimo':Acronimo,
                'Email':Email,
                'Portal de trasnparencia':Trasnparencia,
                'Sitio web':Sitio_web,
                'Disponible':disponible
      
            })
print(df)

#crear csv
df.to_csv('instituciones.csv',index=False)

