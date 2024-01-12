from mailtm import Email
import random
import string

print("\033[0;95m",r"""
 ___              _           ___                                _         
(  _`\           ( )_        (  _`\                             ( )_       
| (_(_)_ _   ___ | ,_)______ | |_) ) _   _  _ _    _ _      __  | ,_)  ___ 
|  _)/'_` )/',__)| | (______)| ,__/'( ) ( )( '_`\ ( '_`\  /'__`\| |  /',__)
| | ( (_| |\__, \| |_        | |    | (_) || (_) )| (_) )(  ___/| |_ \__, \
(_) `\__,_)(____/`\__)       (_)    `\___/'| ,__/'| ,__/'`\____)`\__)(____/
                                           | |    | |                      
                                           (_)    (_)                      
""","\033[0;33m")  
test = Email()
test.register()

def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe


email = str(test.address)
fullname = input("Profile Name : ")
username = input("ID username : ")
password = generer_mot_de_passe()
max_len=max([len(email),len(fullname),len(username),len(password)])
char="-"*max_len
print("\033[0;31m")
print("[ACCOUNT]"+char[19:],"\033[0m")
print("Email :",email)
print("Profile Name :",fullname)
print("ID username :",username)
print("Password :",password)
print(char)

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
test.start(listener)
print("\nWaiting for new emails...")
        
                