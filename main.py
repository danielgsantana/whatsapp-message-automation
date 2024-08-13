import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Função para validar e limpar números de telefone
def clean_phone_number(phone_number):
    # Remove todos os caracteres que não são números
    return re.sub(r'\D', '', phone_number)

# Carrega a planilha .xlsx
file_path = '/home/daniel/Documentos/Daniel/Automações/disparo_mensagens_whatsapp/telefones.xlsx'  # Substitua pelo nome do seu arquivo
df = pd.read_excel(file_path)

# Listas para armazenar os nomes e os números de telefone limpos
names = []
phone_numbers = []


# Loop para percorrer as linhas da planilha
for index, row in df.iterrows():
    name = row['Nome']  # Nome do usuário
    phone_number = clean_phone_number(str(row['Telefone']))  # Telefone do usuário (limpo)
    
    if pd.isna(name) or not name.strip():  # Verifica se o nome é NaN ou vazio
        names.append("Parceiro(a) Transportador")
    else:
        names.append(name)

    #names.append(name)
    phone_numbers.append(phone_number)


# Exemplo de loop que percorre as listas
for name, phone_number in zip(names, phone_numbers):
    print(name,phone_number)


# Configurar o driver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Acessando a URL
url = 'https://cnpj.linkana.com/'

driver.get(url)

time.sleep(10)

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="q"]').click()
driver.find_element(By.XPATH, '//*[@id="q"]').send_keys('azship')
driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div[2]/form/div/input[2]').click()