import os
sudoPass = '04636331'
command = 'cp -r output/* output_site/'
os.system('echo %s|sudo -S %s' % (sudoPass, 'rm -rf output/'))
os.system('echo %s|sudo -S %s' % (sudoPass, 'rm -rf output_site/*'))
os.system('make publish')
os.system('echo %s|sudo -S %s' % (sudoPass, command))
os.system('cd output_site && git add -A && git commit -a -m "new" && git push')
