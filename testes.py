from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import os

def main():
    # Configuração do Selenium com o driver do navegador Firefox
    options = Options()
    options.add_argument('--headless')
    options.set_preference("javascript.enabled", False)
    driver = webdriver.Firefox(options=options)
    url = ""
    driver.get(url)

    # Obtém o conteúdo da página
    page_content = driver.page_source

    # Fecha o navegador
    driver.quit()

    # Verifica se o diretório 'static' existe
    if not os.path.exists('static'):
        os.makedirs('static')

    # Salva o conteúdo da página como arquivo HTML
    with open('static/page.html', 'w') as file:
        file.write(page_content)

    print("Arquivo page.html criado e conteúdo da página salvo")

    # Encontra o início do trecho desejado no conteúdo da página
    start_index = page_content.find('{"total"')
    # Adicione aqui o que for retirar do codigo
    end_index = page_content.find('') 
    # Extrai o conteúdo a partir do início encontrado
    json_content = page_content[start_index:end_index]

    # Salva o conteúdo em um arquivo JSON
    with open('static/data.json', 'w') as file:
        file.write(json_content)

    print("Conteúdo JSON salvo em data.json")

main()
