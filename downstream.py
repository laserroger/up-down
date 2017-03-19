import os
import time
import subprocess
from wxpy import *
bot = Bot()
me = bot.friends().search(province = 'Erfurt')[0]
SudoPass = '04636331'
while True:
	a = os.popen('cd output_site/ && git pull && cd .. ').read()
	command1 = 'rm -rf /var/www/html/*'
	command2 = 'cp -r output_site/* /var/www/html/'
	os.system('echo %s|sudo -S %s' % (SudoPass, command1))
	os.system('echo %s|sudo -S %s' % (SudoPass, command2))
	me.send(a)
	time.sleep(7200)

