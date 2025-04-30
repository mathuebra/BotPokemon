import pyautogui as pag
import time
from pynput import keyboard

# Variáveis principais
keys = ['w', 'a', 's', 'd']
reference_position = (887, 567)
reference_color = (251, 65, 73)

fight_position = (683, 539)
fight_color = (235, 56, 56)

# (position_x, position_y, priority, PP)
moveset = [[571, 532, False, 40], [796, 530, True, 25], [573, 646, False, 5], [796, 646, True, 15]]

running = True  # Controle principal do loop

def check_quit(key):
    global running
    if key == keyboard.Key.esc or str(key) == "'q'":
        print("Program terminated by user.")
        running = False
        return False  # Encerra o listener

# Retorna True se ainda existirem movimentos de dano disponíveis
def check_availability():
    flag = 0
    for current in moveset:
        if current[2] == True and current[3] == 0:
            flag += 1
    return flag != sum(1 for current in moveset if current[2] == True)

def combat():
    pag.moveTo(*fight_position)  # Clica no botão "Fight"
    pag.mouseDown()
    time.sleep(0.3)
    pag.mouseUp()
    time.sleep(0.5)

    # Se não houver movimentos disponíveis, retorna False
    # TODO: Adicionar um alerta para o usuário
    if not check_availability():
        return False

    for current in moveset:
        if current[2] == True and current[3] != 0:
            pag.moveTo(*(current[0], current[1]))
            pag.mouseDown()
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            current[3] -= 1
            break
    return True

# Alerta inicial
pag.alert("""             Pressione OK para começar! 
       Pressione 'q' a qualquer momento para parar!""", title="Pokemon Bot", button="OK")

# Inicia o listener em segundo plano
listener = keyboard.Listener(on_press=check_quit)
listener.start()

# Loop principal
while running:
    # Sugestão de TODO: Salvar a última tecla apertada para evitar que ele saia da área
    # desejada para o farming
    
    # TODO: a movimentação não está funcionando corretamente
    for key in keys:
        pag.keyDown(key)
        time.sleep(0.3)
        pag.keyUp(key)
        time.sleep(0.3)

        # se não der match com a cor de referência é porque entrou em luta
        # mas o ideal seria ficar rodando até não dar match com a cor de referência
        
        if not pag.pixelMatchesColor(*reference_position, reference_color, tolerance=5):
            while not pag.pixelMatchesColor(*fight_position, fight_color, tolerance=5):
                time.sleep(0.3)
                if not running:
                    break

            print(combat())  # Debug

        else:
            time.sleep(0.5)

        if not running:
            break
    
    print("está no while") # Debug
        
# TODO: Ele não esta retomando a movimentação normal depois de encerrar um combate

# Aguarda o listener finalizar
listener.join()