import pyautogui
import threading
import time
from datetime import date
import os
import pyperclip

dataAmerica = date.today()
dataBrasil = dataAmerica.strftime('%d/%m/%Y')

def start():
    os.system('start C:\TOTVS\PRODUÇÃO\RM.EXE')


def logTotvs():
    threading.Thread(target=start())
    time.sleep(2)
    while True:
        local_user = pyautogui.locateCenterOnScreen("user.png")
        local_pass= pyautogui.locateCenterOnScreen("pass.png")
        time.sleep(2)
        if local_pass != None or local_user != None:
            pyautogui.click(local_pass.x, local_pass.y)
            pyautogui.write("SENHA")
            pyautogui.click(local_user.x, local_user.y)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.keyDown("backspace")
            pyautogui.keyUp("backspace")
            pyautogui.write("USERNAME")
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            break
        else:
            print("ERRO")
        


def processo_Retorno():
    time.sleep(5)
    while True:
        local_inicar = pyautogui.locateCenterOnScreen("iniciar.png")
        if local_inicar != None:
            pyautogui.click(local_inicar.x, local_inicar.y, duration=1)
            local_backoffice = pyautogui.locateCenterOnScreen("backoffice.png")
            pyautogui.click(local_backoffice.x, local_backoffice.y, duration=1)
            pyautogui.moveTo(local_backoffice.x + 500, local_backoffice.y, duration=1)
            local_gestaoFinanceira = pyautogui.locateCenterOnScreen("gestaoFinanceira.png")
            pyautogui.click(local_gestaoFinanceira.x, local_gestaoFinanceira.y, duration=1)
            time.sleep(10)
            local_MovimentBancaria = pyautogui.locateCenterOnScreen("MovimentBancaria.png")
            pyautogui.click(local_MovimentBancaria.x, local_MovimentBancaria.y, duration=1)
            local_RetornoBanc = pyautogui.locateCenterOnScreen("RetornoBanc.png")
            pyautogui.click(local_RetornoBanc.x, local_RetornoBanc.y, duration=1)
            local_RetornoLote = pyautogui.locateCenterOnScreen("RetornoLote.png")
            pyautogui.moveTo(local_RetornoLote.x, local_RetornoLote.y, duration=1)
            time.sleep(1)
            local_Pagamento = pyautogui.locateCenterOnScreen("Pagamento.png")
            pyautogui.moveTo(local_RetornoLote.x + 200, local_RetornoLote.y, duration=1)
            time.sleep(1)
            pyautogui.click(local_Pagamento.x, local_Pagamento.y, duration=1)
            time.sleep(2)
            local_banco = pyautogui.locateCenterOnScreen("banco.png")
            pyautogui.click(local_banco.x, local_banco.y + 20, duration=1)
            pyautogui.write("341")
            pyautogui.hotkey("Tab")
            local_pastaLeituraArq = pyautogui.locateCenterOnScreen("pastadeleitura.png")
            pyautogui.click(local_pastaLeituraArq.x, local_pastaLeituraArq.y + 20, duration=1)
            pyautogui.write(r"ARQUIVOS")  
            local_botaoBuscar = pyautogui.locateCenterOnScreen("buscarArquivos.png")
            pyautogui.click(local_botaoBuscar.x, local_botaoBuscar.y, duration=1)
            local_RetornoPagamento = pyautogui.locateCenterOnScreen("RetornoPagamento.png")
            pyautogui.click(local_RetornoPagamento.x, local_RetornoPagamento.y, duration=1)
            local_avancar = pyautogui.locateCenterOnScreen("avancar.png")
            pyautogui.click(local_avancar.x, local_avancar.y, duration=1)
            time.sleep(10)
            pyautogui.click(local_avancar.x, local_avancar.y-200, duration=1)
            local_executar = pyautogui.locateCenterOnScreen("executar.png")
            pyautogui.click(local_executar.x, local_executar.y, duration=1) 
            break            
    

def pegarArquivos():
    os.system("start explorer.exe")
    while True:
        local_lupa = pyautogui.locateCenterOnScreen("lupa.png")
        if local_lupa != None:
            pyautogui.click(local_lupa.x - 300, local_lupa.y)
            pyautogui.write(r"LINK PARA BAIXAR ARQUIVOS")
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            time.sleep(15)
            pyautogui.click(local_lupa.x + 50, local_lupa.y)
            time.sleep(1)
            pyperclip.copy("datademodificação:" + dataBrasil)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            time.sleep(15)
            pyautogui.click(local_lupa.x - 300, local_lupa.y +200)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("ctrl", "c")
            time.sleep(1)
            pyautogui.click(local_lupa.x - 300, local_lupa.y)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("backspace")
            pyautogui.write(r"ARQUIVOS")
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.click(local_lupa.x - 300, local_lupa.y +200)
            pyautogui.hotkey("ctrl", "v")
            break
    

if __name__ == '__main__':
    processo_Retorno()
    
