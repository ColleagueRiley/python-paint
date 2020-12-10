import sys,os

if sys.platform == "win32" or sys.platform == 'cygwin':
	pip='pip'
	os.system('py -m pip install -U pygame --user')
elif sys.playform == 'linux' or sys.playform == 'linux':
	pip='pip3'
	os.syetem('sudo apt-get install python3-pygame')
else:
	os.syetem('python3 -m pip install -U pygame --user')
	pip='pip3'
deps = ['pickle','PyZenity-0.1.7.tar.gz','easygui']
for dep in deps
	os.system(f'{pip} install {dep}')