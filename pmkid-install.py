# -*- coding: UTF-8 -*-
#!/bin/bash
import os

print ("Começando...")
os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade && apt-get install libssl-dev && apt-get install libz-dev && apt-get install libpcap-dev && apt-get install libcurl4-openssl-dev")
os.system("clear")
print ("Baixando hcx's...") 
os.system("git clone https://github.com/ZerBea/hcxdumptool.git");
os.system("git clone https://github.com/ZerBea/hcxtools");
os.system("cd hcxdumptool && make && make install");
print("Making hcxdumptool...")
os.system("cd ..")
os.system("cd hcxtools && make && make install");
print("Making hxctools...")
os.system("clear")
print ("Concluido!")


