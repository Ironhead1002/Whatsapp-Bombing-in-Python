import pyautogui
import webbrowser as wb
import time

a = input("Enter Message : ")
n = int(input('Number of messages : '))

wb.open('https://web.whatsapp.com/')

time.sleep(30)

for i in range(n):
    for j in a:
        if j == " ":
            pyautogui.press('space')
        else:
            pyautogui.press(j)
    pyautogui.press('enter')