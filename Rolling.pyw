import webbrowser
import keyboard

while True:
    if keyboard.is_pressed("Ctrl") and keyboard.is_pressed("q"):
        webbrowser.open_new('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
