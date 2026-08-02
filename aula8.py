#mport pyautogui
#impor
#  time
import os




#pyautogui.press("win")
#pyautogui.write("chrome")
#pyautogui.press("enter")

#ime.sleep(3)  # Espera o Chrome abrir

#yautogui.write("https://www.crunchyroll.com/pt-br/discover")
#yautogui.press("enter")
#mport pyautogui
#impor
#  time

lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}",f"arquivos/22/{arquivo}")
            print("Movimentar para a pasta 22")
        elif "23" in arquivo:
             os.rename(f"arquivos/{arquivo}",f"arquivos/23/{arquivo}")