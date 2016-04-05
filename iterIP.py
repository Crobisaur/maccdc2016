__author__='Christo Robison'
import sys
import os
from subprocess import call

""" A script hastily written during MACCDC 2016 to reflash the firmware of 
	the badges via OTA in an attempt to overcome Red Team's attack.  Unfortunately,
	Red's tactic involved broadcasting updates to all badges via udp packets so any 
	update attempts were moot unless UDP traffic is filtered via firmware."""

for i in range(8):
	#replace this with the first badge IP of team
	baseIP = 178
	ip = "10.13.37." + str(baseIP + i)
	out = ' '.join(["platformio", "run", "-t", "uploadfs", "--upload-port", ip])
	call(out)