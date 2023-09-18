#! /bin/python
import os
import sys

os.system('/usr/bin/python3 /home/administrator/SIP_A/sip.py >> /home/administrator/daily_sip/SIP_$(date +"%F %T").log')
