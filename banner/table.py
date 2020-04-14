#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Set color
R = '\033[1;93m' # Red
W = '\033[1;97m' # White
G = '\033[1;92m' # Green
O = '\033[1;91m' # Orange
C = '\033[1;96m' #Blue
M = '\033[48;5;0;38;5;197m' # X
Y = '\033[1;90m'
def force_to_unicode(text): 
  "If Text is Unicode, it is Returned as is. If it's str, Convert it to Unicode Using UTF-8 Encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')

print
print (""+R+"     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (""+R+"     ┃"+M+"["+Y+"00"+M+"]"+C+"       DroidX Antivirus"+R+"       ┃")
print (""+R+"     ┃"+M+"["+W+"01"+M+"]"+G+"       Android Frozen"+R+"         ┃")
print (""+R+"     ┃"+M+"["+Y+"02"+M+"]"+C+"      Android Ransomware"+R+"      ┃")
print (""+R+"     ┃"+M+"["+W+"03"+M+"]"+G+"       Android Malware"+R+"        ┃")
print (""+R+"     ┃"+M+"["+Y+"04"+M+"]"+C+"      Android Decryptor"+R+"       ┃")
print (""+R+"     ┃"+M+"["+W+"05"+M+"]"+G+"      Android Decryptor 2"+R+"     ┃")
print (""+R+"     ┃"+M+"["+Y+"06"+M+"]"+C+"       Android SMS Thief"+R+"      ┃")
print (""+R+"     ┃"+M+"["+W+"07"+M+"]"+G+"  Android Dangerous Malware"+R+"   ┃")
print (""+R+"     ┃"+M+"["+Y+"08"+M+"]"+C+"     Android ENC Malware"+R+"      ┃")
print (""+R+"     ┃"+M+"["+W+"09"+M+"]"+G+"   Android Trojan Backdoor"+R+"    ┃")
print (""+R+"     ┃"+M+"["+Y+"10"+M+"]"+O+"            EXIT  "+R+"            ┃")
print (""+R+"     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
print
print
