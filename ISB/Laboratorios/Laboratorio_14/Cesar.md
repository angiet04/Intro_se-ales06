### REPOSITORIO EDGE IMPULSE - CÉSAR AIBAR
![PERFIL](https://github.com/angiet04/Intro_se-ales06/assets/164528885/339314b9-b817-429a-94fa-a38abbe9781e)

## Código
```python
# Install requests via: pip3 install requests
import requests
import os

api_key = 'ei_45caf24c122cad2eedde0a24e975a726b0ebc1352fb581271d1393dca4261222'
# Add the files you want to upload to Edge Impulse
files = [
    'Hiperventilacion.csv',
]
# # Replace the label with your own.
label = 'Señal Hiperventilacion'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'image/png')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
```
## Señales
Sentadillas
![Sentadillas](https://github.com/angiet04/Intro_se-ales06/assets/164528885/ac04103d-98b9-4074-95c1-483061426a09)
https://studio.edgeimpulse.com/public/431138/live

Reposo
![reposo](https://github.com/angiet04/Intro_se-ales06/assets/164528885/8980ede5-fe14-4b26-bd53-11120a4e4198)
https://studio.edgeimpulse.com/public/431565/live

Hiperventilación
![hiperventilacion](https://github.com/angiet04/Intro_se-ales06/assets/164528885/3cd18aee-3ea9-4654-899c-1b6a8650176c)
https://studio.edgeimpulse.com/public/431142/live
