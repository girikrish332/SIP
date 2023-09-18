#! /bin/python3
import os 

#BSNL 

bsnl = "BSNL_SIP" 
response1 = os.system("ping -c 5 " + "10.181.33.1") 
if response1 == 0: 
  print (bsnl, 'is up!^^^^^^^^^^^^^^^^^^^')
  #os.system('/usr/bin/python3 /home/administrator/SIP_A/BSNL_SIP_UP.py')
else: 
  print (bsnl, 'is down!********************')
  os.system('/usr/bin/python3 /home/administrator/SIP_A/BSNL_SIP_DOWN.py')

#TATA 
tata = "TATA_SIP"
response2 = os.system("ping -c 5 " + "10.52.15.2") 
if response2 == 0: 
  print (tata, 'is up!^^^^^^^^^^^^^^^^^^^^') 
 # os.system('/usr/bin/python3 /home/administrator/SIP_A/TATA_SIP_UP.py')
else: 
  print (tata, 'is down!*******************') 
  os.system('/usr/bin/python3 /home/administrator/SIP_A/TATA_SIP_DOWN.py')


a="asterisk -rx 'sip show peers'" 
b=os.system(a) 
c="asterisk -rx 'sip show registry'" 
d=os.system(c)
