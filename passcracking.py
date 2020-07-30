import random
import pyautogui

char = "abcdefghijklmnopqrstuvwxyz0123456789"
char_list = list(char)

# print(char_list)
password = pyautogui.password("Enter a password: ")

guess = ""

while (guess!=password):
    guess = random.choices(char_list, k=len(password))
    print("<============"+ str(guess) +"============>")
    if(guess == list(password)):
        print("Your password is: "+ "".join(guess))
        break
