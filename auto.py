# Importando as bibliotecas necessárias
import pyautogui
import time
import random  # Importe a biblioteca random

# Adicionando pausa de execução pré-definida
pyautogui.PAUSE = 2

# Lista de nomes para mencionar nos comentários
nomes = ["@juliaribeiro_s", "@diegopajah_ ", "@joao.ribeiromatos ", "@jordan_caldeira ", "@f_albu21 ", "@hugodwg ", "@ispaulovitor "]

# Loop infinito para comentar várias vezes
while True:
    # Abrindo o navegador Chrome e navegando até o Instagram
    pyautogui.press("win")
    pyautogui.write("chrome")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    link = "https://www.instagram.com/"
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(2)
    
    # Pesquisando e acessando o perfil desejado
    pyautogui.click(x=122, y=276)
    pyautogui.write("buzeira")
    time.sleep(2)
    pyautogui.click(x=168, y=252)
    time.sleep(2)
    
    # Rolando para baixo até a publicação desejada
    pyautogui.scroll(-794)
    time.sleep(2)
    
    # Clicando na publicação
    pyautogui.click(x=602, y=222)
    time.sleep(2)
    
    # Clicando para comentar
    pyautogui.click(x=751, y=808)
    time.sleep(2)
    
    # Escolhendo um nome aleatório da lista e escrevendo o comentário
    nome_escolhido = random.choice(nomes)
    pyautogui.write(nome_escolhido)
    
    # Clicando para enviar o comentário
    pyautogui.click(x=1114, y=809)
    
    # Espera ndo um tempo antes de repetir o processo
    time.sleep(2)  # Espera 3 segundos antes de fechar a aba
    
    # Fechando a aba
    pyautogui.click(x=1415, y=15)
    
    # Esperando um tempo antes de repetir o processo
    time.sleep(1600)  # Espera 10 segundos antes de repetir o processo
