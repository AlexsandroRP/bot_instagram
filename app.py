from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select # para interagir com dropdown
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # para waits explicitos
from selenium.common.exceptions import * # para usar excecoes no wait explicito
from selenium.webdriver.support import expected_conditions

usuario = input("Digite o seu usuário: ")
senha = input("Digite sua senha: ")
pagina = input("Digite o nome da página a automatizar: ")

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument) # passar os argumentos pro chrome options


    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    # inicializando o webdriver e atualizando automaticamente de acordo com a versão do chrome do pc
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1, # clica de 1 em 1 segundo
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ] # lista de excecoes ignoradas
    )

    return driver, wait

# Navegar até o instagram
driver, wait = iniciar_driver()
driver.get('https://www.instagram.com/')

# Clicar e digitar usuário
campo_usuario = wait.until(expected_conditions.element_to_be_clickable((By. XPATH, "//input[@name='username']")))
campo_usuario.send_keys(usuario)
sleep(2)

# Clicar e editar senha
campo_pass = driver.find_element(By. XPATH, "//input[@name='password']")
campo_pass.send_keys(senha)
sleep(2)

# Clicar em entrar
login = wait.until(expected_conditions.element_to_be_clickable((By. XPATH, "//div[text()='Entrar']")))
sleep(2)
login.click()
sleep(3)
# Navegar até a página alvo
while True:
    driver.get(f'https://www.instagram.com/{pagina}')
    sleep(3)
    # Clicar na ultima postagem
    postagens = wait.until(expected_conditions.visibility_of_any_elements_located((By. XPATH, "//div[@class='_aagu']"))) # retorna uma lista
    sleep(3)
    postagens[0].click()

    # Verificar se postagem foi curtida, caso não, clicar em curtir, caso sim, aguardar 24h
    elementos_postagem = wait.until(expected_conditions.visibility_of_any_elements_located((By. XPATH, "//div[@class='_abm0 _abl_']")))

    if len(elementos_postagem) == 24:  # Verifica o tamanho da lista de elementos_postagem, se for 24, significa que ainda não foi curtida e clica, caso contrário, não faz nada.
        elementos_postagem[0].click()
        sleep(86400) 
    else:
        print("Postagem já foi curtida")    
        sleep(86400)


# sugestoes_voo = wait.until(expected_conditions.visibility_of_all_elements_located((By. XPATH, "//div[@class='wIuJz']"))) # espera até todos os elementos estiverem localizadas na página

# # or
# sugestoes_voo = wait.until(expected_conditions.visibility_of_any_elements_located((By. XPATH, "//div[@class='wIuJz']"))) # espera até qualquer elemento aparecer
# sugestoes_voo[0].click()

# # esperar até elemento se tornar clicavel (como paginas de login)
# xxxx = wait.until(expected_conditions.element_to_be_clickable((By. XPATH, "//xxxxxxxxxxxxx']")))




