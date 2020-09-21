#!/bin/bash

python3 -m venv venv;
. venv/bin/activate;
pip3 install -r requirements.txt;

if [ -d "$HOME/.local/bin" ]; then
	EXE_PATH=$HOME/.local/bin
	SUCCESS=1
else
	if [ ! "$(whoami)" == "root" ]; then
		echo "Can't install in your home folder! Need permission to do it in /usr/, try again with sudo!"
		exit
	else
		EXE_PATH=/usr/local/bin
		SUCCESS=1
	fi
fi
sed "s|<PWD>|"${PWD}"|" ${PWD}/francais > $EXE_PATH"/francais"
chmod +x $EXE_PATH"/francais"
if [ $SUCCESS == 1 ]; then
	echo "C'est fini!"
fi
