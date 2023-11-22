import mouse
import keyboard

def paste():
    mouse.click()
    keyboard.write('https://discord.gg/uSwzRvAB')
    keyboard.press_and_release('enter')

mouse.on_middle_click(paste)

keyboard.wait()
