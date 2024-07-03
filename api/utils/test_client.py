import requests
from pprint import pprint

base_url = 'http://localhost:8000/api/'

# Consulta por período de datas
start_date = '2020-07-23'
end_date = '2020-07-30'
url = f'{base_url}program-data/period/{start_date}/{end_date}/'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    pprint(f'Dados para o período de {start_date} a {end_date}:')
    pprint(data)
else:
    pprint(f'Erro ao consultar API: {response.status_code}')
